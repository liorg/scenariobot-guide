# 06. Scenario components

**How to get there:** **Top bar → Phones → a phone → 🤖 Scenarios → open a
scenario.** The components are the two side columns of the designer.

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

Both code cards hold JavaScript, edited in a proper code editor inside the card
and run in a sandbox.

### A SEND code card generates a reply

```js
export default async function(payload) {
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

```js
export default async function(payload) {
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

Two things:

- **`payload.target_contact`** — the contact, including `.name`
- **`payload.lastMessage.Value`** — the previous step's reply or output

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
