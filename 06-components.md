---
id: 06-components
title: Scenario components — EXPECT, SEND and code steps
url: /phones/<phone>/scenarios/<scenario>/design
keywords:
  - EXPECT
  - SEND
  - step
  - component
  - pattern
  - regex
  - condition
  - custom code
  - Deno
  - fetch
  - parameters
  - placeholders
  - retry
  - wrong reply
related:
  - 05-scenarios
  - 10-watching-a-call
actions:
  - id: find-expect-steps
    description: Show the EXPECT step types
    screen: screen-designer
    target: panel-expect
    type: highlight
  - id: find-send-steps
    description: Show the SEND step types
    screen: screen-designer
    target: panel-send
    type: highlight
  - id: read-scenario-canvas
    description: Show the conversation canvas
    screen: screen-designer
    target: panel-canvas
    type: highlight
---
# 06. Scenario components

**How to get there:** **Top bar → Phones → a phone → 🤖 Scenarios → open a
scenario.** The components are the two side columns of the designer.

**URL:** `grossman.bot/phones/<phone>/scenarios/<scenario>/design`

The parts in `<angle brackets>` are ids filled in as you click, so this one cannot be opened by typing it.

## EXPECT and SEND — which is which

This is the thing people get backwards, so it's worth stating plainly:

- **EXPECT** = what the **bot sends**, and then waits on. An EXPECT step
  describes a message the bot puts out *and* the reply shape it will accept
  back.
- **SEND** = what the **other side supplies** — the reply.

A conversation alternates EXPECT → SEND → EXPECT → SEND. **Two EXPECT steps in a
row means the bot sends twice and only waits once.**

## EXPECT steps

| Step | What it does | Its settings |
|---|---|---|
| **Text** | sends free text, waits for a text reply | the message, match mode |
| **Menu** | sends a WhatsApp list, waits for a selection | the message, the list items, match mode |
| **Buttons** | sends up to 3 buttons, waits for a tap | header, the buttons, match mode |
| **Code card** | runs your own code against the reply | the code, sample input, failure action, timeout |
| **📧 Receive mail** | waits for an email to the phone's address and captures a value from it | senders, subject, what to capture, timeout |

### Receive mail

**Every phone has an email address** — its number at `grossmanbot.download` —
and this card waits for a mail to arrive there and pulls a value out of it.
It is how a scenario gets a verification code that is sent by email rather
than by WhatsApp.

Narrow it with **who sends** (`noreply@bank.co.il`, or `@bank.co.il` for the
whole domain) and **which subject** — each can be *is*, *contains*, *starts
with* or *ends with*, and both ignore upper and lower case. Leave them empty
and any mail counts.

**What to capture** is one of `6 digits`, `4 digits`, `3+3 digits`, `Link`,
`Format` — `Your code is <?>` — or a regex. The subject and the body are both
searched. Only one value comes out: one `<?>`, or the regex's group 1, with
any further groups landing in `MailParam01` onwards.

The card has a **Test** box. Paste a real mail into it and it says whether
the value would be captured, and if not, which part failed.

Two things that are easy to get wrong: **the wait is counted from the last
message the scenario sent**, not from when the card is reached; and a mail
that arrives up to **ten minutes early still counts**, because services often
send the code before the scenario gets that far.

[Chapter 24](24-mail.md) covers the address, the Mail tab and what the
statuses mean.

### Match mode

On Text, Menu and Buttons:

| Mode | Matches when |
|---|---|
| **exact** | the reply is exactly this |
| **contains** | the reply contains this somewhere |
| **pattern** | the reply matches this pattern (regular expression) |
| **any** | anything counts as a reply |

**`exact` is the most common cause of "they answered but the step still
failed".** Trailing spaces, different capitalisation, or an extra word all fail
it. `contains` is usually what was meant.

### Pattern mode writes the pattern for you

Choosing **pattern** replaces the message box with an assistant. Describe the
condition in your own words — Hebrew, English, Russian or Arabic — and press
**✨ Generate**:

> *an answer that starts with yes or confirm, in any capitalisation*

You get back a working pattern, which you can edit by hand afterwards if you
want. **Ctrl/Cmd + Enter** generates without reaching for the button.

**Test it before you rely on it.** Below the pattern there's a box for sample
messages, one per line. Each gets a ✅ or ❌ as you type — no need to run the
scenario to find out.

The **+ name** and **+ answer** buttons insert a placeholder into your
description, so you can ask for things like *a reply containing
`"{{payload.target_contact.name}}"`*. A pattern that uses one shows which
placeholders it depends on underneath.

The **📋** button copies the pattern, which is useful when you want the same
condition on another step.

Two things worth knowing:

- **Generation is instant the second time.** An identical description comes
  back from cache, marked as such.
- **A sample test is a shape test.** Placeholders are treated as "any word"
  while testing, because their real values only exist while a call is running.
  A ✅ means the pattern fits that kind of message, not that this exact text
  will match at run time.

### Per-step timeout

The **code card** is the only step with its own timeout. Left alone it inherits
the scenario's interval; switched on, you set minutes and seconds, with quick
presets.

## SEND steps

| Step | What it does | Its settings |
|---|---|---|
| **Button select** | supplies a button tap | button id, display text |
| **Menu select** | supplies a list-row selection | row id, display text |
| **Input** | supplies free text, or a template | the text, or a template + its values |
| **Code card** | generates the reply with your own code | the code, failure action |
| **✉️ Send mail code** | sends on the value the mail card captured | the value, by default the last capture |

**Button select and menu select carry both an id and a text** because WhatsApp
actually receives the text, while the scenario matches on the id.

### Input has two modes

- **Text** — free text, with `{{ }}` placeholders (below).
- **Template** — a pre-approved WhatsApp template, chosen from the ones
  published for this phone, with each slot filled in and a live preview.

Switching from template back to text clears the template selection, so pick your
mode before filling values in. Templates are the only way to open a conversation
outside WhatsApp's 24-hour window → [Chapter 08](08-templates.md).

## When the reply is wrong

By default a mismatch stops the call and it's recorded as failed. Each step can
instead be given a failure behaviour:

| Behaviour | Effect |
|---|---|
| **Retry** | wait again for a reply, up to a number of attempts |
| **Skip** | ignore non-matching messages and keep waiting until one matches |
| **Skip next** | jump past the following step |
| **Stop** | end the call here — the default |

Retry and skip are mutually exclusive on the same step; the editor won't let you
set both.

On the **SEND code card** the same idea uses different words: **continue** (=
skip), **stop**, **retry**. They mean the same things.

## Custom code steps

Both code cards hold **TypeScript**, edited in a proper code editor inside the
card and run in a Deno sandbox.

Every card is one default-exported async function, and its argument is always
typed **`ScenarioPayload`**:

```ts
export default async function (payload: ScenarioPayload) {
  // …
}
```

`ScenarioPayload` is available without an import — it is the type of everything
the step is given, so the editor can complete `payload.` for you and catch a
misspelt field before you save. Every example below uses it.

### A SEND code card generates a reply

```ts
export default async function (payload: ScenarioPayload) {
  const customer = payload.target_contact;

  return {
    success: true,
    selectedValue: customer.name,
  };
}
```

`selectedValue` becomes the reply. **The next step receives it as
`payload.lastMessage.Value`.**

### An EXPECT code card judges a reply

```ts
export default async function (payload: ScenarioPayload) {
  const received = payload.lastMessage.Value;

  if (!received?.trim()) {
    return { expected: "EMPTY", proceed: false };   // empty → stop
  }

  return {
    expected: received.trim(),
    proceed: true,
  };
}
```

Two keys matter: **`expected`** is the value written out, **`proceed`** decides
whether the scenario carries on.

**The key must be named `expected`.** Returning a differently-named key produces
a step that runs successfully and stores nothing — with no error anywhere.

### What your code can read

The editor knows the whole shape — type `payload.` and it lists it — but these
are the fields you will actually use:

| Field | Holds |
|---|---|
| `payload.target_contact` | the bot (agent): `.id`, `.name`, `.phone` |
| `payload.lastMessage.Value` | the previous step's reply or output |
| `payload.lastMessage.num` | which step that was |
| `payload.source_phone.phone` | the bot's own number, as `972…` — not an id |
| `payload.variables` | values earlier steps stored, e.g. `payload.variables.expected` |
| `payload.scenarioId` / `payload.stepId` | the ids of this run and this step |

`payload.variables` is the one people miss: it is how a value survives more than
one step, where `lastMessage.Value` only ever holds the step immediately before.

Plus anything you can reach over the network — see below.

### Calling an external service

The sandbox is **Deno**, so the standard web `fetch` is already there. Nothing
to install, nothing to import — no `axios`, no `require`, no `node-fetch`.

```ts
export default async function (payload: ScenarioPayload) {
  const customer = payload.target_contact;

  const r = await fetch("https://jsonplaceholder.typicode.com/todos/1");
  const todo = await r.json();

  return {
    success: true,
    selectedValue: `${customer.name} — ${todo.title}`,
  };
}
```

That is the whole pattern: fetch, read the response, put something into
`selectedValue`. The next step receives it as `payload.lastMessage.Value`, so a
value fetched here can be sent in the following message.

### The domain has to be approved first

**A code step can only call domains on your trusted list.** The check runs when
you **save** the scenario, not when it runs — so an unapproved URL is a save
error, with the step and the URL named:

> `https://api.example.com — domain 'api.example.com' is not in trusted domains`

You add a domain in [Settings → ⚙️ Advanced](https://grossman.bot/settings/advanced)
([Chapter 14](14-settings.md)), and it is **verified before it is accepted**: the
platform resolves it and completes a TLS handshake with it. A domain that does
not exist, does not answer on 443, or has a certificate expiring within a week
is refused there and then — which means by the time you write the `fetch`, the
address is known to work.

The rules the URL in your code must follow:

| Rule | Why |
|---|---|
| **`https` only** | no plain HTTP, ever |
| **port 443 only** | `https://api.example.com:8443/…` is refused |
| **no IP addresses** | write the domain |
| **no credentials in the URL** | `https://user:pass@…` is refused |
| **the host must be written literally** | see below |
| **the exact host must be on the list** | `sub.api.example.com` is not covered by `api.example.com` |

**The host must be literal — the path does not.** This is the distinction to
remember:

```ts
// ✅ fine — the host is written out, only the path is built
await fetch(`https://api.example.com/orders/${id}`);

// ❌ refused — "dynamic host is not allowed, write the domain literally"
await fetch(`https://${host}/orders`);
```

Two things that surprise people:

- **Every subdomain is its own entry.** Approving `example.com` does not approve
  `api.example.com`. Add the host you actually call.
- **URLs in comments are checked too.** A documentation link or a commented-out
  endpoint will block the save with a complaint about a domain you are not
  calling. Take the `https://` out of comments, or approve it.

If your domain is non-Latin, write the **punycode** form in the code
(`xn--6dbbec0c.co.il`, not `דוגמה.co.il`) — that is the form the list stores.

The annotation is types only — it is erased before the code runs, so it costs
nothing and buys you the editor's help. It is also the fastest way to catch the
mistake below: a misspelt `payload` field is a **type error** in the editor,
where plain JavaScript would hand you `undefined` at run time and send a message
with a blank in it.

**The conversation waits while you fetch.** This code runs between two WhatsApp
messages, with the person on the other end looking at their phone. A service
that takes eight seconds to answer is an eight-second silence in the middle of
your conversation, so keep these calls to things that answer quickly.

Four habits that make the difference between a step that works and one that
fails strangely:

**1. Set a timeout.** Without one, a hung service hangs the step.

```ts
const r = await fetch(url, { signal: AbortSignal.timeout(5000) });
```

**2. Check the status.** `fetch` does **not** throw on a 404 or a 500 — it
returns a response with `ok: false`. A missing check means `r.json()` tries to
parse an error page and the real cause disappears.

```ts
if (!r.ok) {
  return { success: false, selectedValue: `HTTP ${r.status}` };
}
```

**3. Wrap it.** A network failure throws, and an unhandled throw is a failed
step with nothing useful recorded.

```ts
try {
  const r = await fetch(url, { signal: AbortSignal.timeout(5000) });
  if (!r.ok) return { success: false, selectedValue: `HTTP ${r.status}` };
  const data = await r.json();
  return { success: true, selectedValue: String(data.title ?? "") };
} catch (e) {
  return { success: false, selectedValue: `fetch failed: ${e}` };
}
```

Returning `success: false` with a readable reason is what turns a mystery into a
line you can read in the call's events ([Chapter 11](11-reading-a-call.md)).

**4. `selectedValue` is text.** An object returned there is not a message. Pick
the field you want, or format it yourself — `String(...)`, a template string, or
`JSON.stringify` if you really do want the raw shape.

### Don't put secrets in a code card

An API key typed into a code card is **stored in the scenario** and visible to
anyone who can open that scenario — and it travels with every copy of it, which
is exactly what [parallel executions](13-executions.md) make lots of.

If a call needs authentication, put a small endpoint of your own in front of it
and let that endpoint hold the credentials. The scenario then calls something
that is safe to read — and that endpoint's own domain is the one you approve,
which is the tidier list anyway.

The same goes for what comes back: whatever you put into `selectedValue` can end
up in a WhatsApp message, so don't select a field you wouldn't want sent.

### An EXPECT card can fetch too

The same `fetch` works on an EXPECT card, which is how you validate an answer
against your own system rather than against a pattern:

```ts
export default async function (payload: ScenarioPayload) {
  const received = (payload.lastMessage.Value ?? "").trim();

  const r = await fetch(`https://your-api.example.com/orders/${encodeURIComponent(received)}`,
                        { signal: AbortSignal.timeout(5000) });

  return {
    expected: received,
    proceed: r.ok,          // the order exists → carry on
  };
}
```

Note `encodeURIComponent`. `received` is whatever the person typed, and dropping
it into a URL unescaped is how a stray `?` or `/` turns into a different
request.

### The editor

The code box is a real editor — the same one as VS Code — with TypeScript
checking as you type, autocomplete on `payload.`, and the errors listed
underneath.

| Control | Does |
|---|---|
| **⤢** | **expands the editor to fill the designer** |
| **⤡** or **Esc** | back to the small box |
| **▶ Check** | runs your code — also **Ctrl/Cmd + Enter** |
| **copy** | the whole file to the clipboard |

**Use the expand button.** The inline box is about ten lines tall — enough to
see what a card does, not enough to write one. Expanded, it covers the designer,
turns on the minimap, and keeps the error list visible beneath. Your cursor
position and undo history survive the switch, both ways.

Esc collapses it, unless the autocomplete or find box is open — then Esc closes
that first, as you would expect.

### Checking it

The **check** button runs your code against a sandbox before you save. On an
EXPECT card, the "expected text" field is used as the sample input.

Publishing checks every code card automatically.

## `{{ }}` parameters

In any text field on a **Text** (EXPECT) or **Input** (SEND) step, you can drop
in a value that gets filled at run time:

```
Hi {{payload.target_contact.name}}, we have you down for tomorrow.
```

Underneath the text box, each placeholder appears as a **yellow chip**. Pressing
the **×** on a chip removes that one occurrence — if the same placeholder
appears three times, each chip removes only its own.

Two **quick-add buttons** insert the common ones:

| Button | Inserts |
|---|---|
| **name** | `{{payload.target_contact.name}}` |
| **answer** | `{{payload.lastMessage.Value}}` |

These are the same two things custom code can read, which is not a coincidence.

Spaces inside the braces are fine: `{{ payload.target_contact.name }}` works.

**A misspelled path becomes an empty string, silently.** Nothing warns you.
`{{payload.target_contact.nmae}}` passes every check and sends a message with a
blank where the name should be. **If a sent message is missing a value, check
the spelling of the placeholder first.**

Placeholders are for text fields only. Inside a code card you read `payload`
directly instead.

---

**Next:** [Playback](07-playback.md)
