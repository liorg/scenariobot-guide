# 04. Adding a contact

**How to get there:** **Top bar → Phones → click a phone → 👥 Contacts tab**.

## Why this isn't just a form

Adding a contact is a **handshake**, not a text field. ScenarioBot has to be
certain that the number you typed is the same WhatsApp identity that actually
replies — WhatsApp numbers and WhatsApp identities are not the same thing, and
guessing wrong means messages go to the wrong person.

**Nothing in the product works against an unlinked contact.** Finishing this
properly is the single most important setup step.

## The wizard, step by step

### 1. Name and number

You enter both. The number is checked immediately and you get one of three
answers:

| Answer | Meaning | What to do |
|---|---|---|
| **new** | no contact for this number | continue |
| **override** | a contact exists and can be reset | restart the handshake and continue |
| **blocked** | already linked to a real WhatsApp identity | cancel — edit it from the table instead |

The check also reports how far any half-finished handshake got: **pending** (the
PING hasn't gone yet) or **waiting_reply** (it has, and nothing has come back).

### 2. PING

ScenarioBot sends a message from your phone to that number. Nothing for you to
do here.

The message it sends is a **template**, because the person has not written to
you yet and WhatsApp only allows templates for first contact. It picks
`check_contact` — a one-line "Are you a bot?" created with every phone — and
falls back to `hello_world` or any other approved, published template without
placeholders if that one is missing.

**If the phone has no approved, published template at all, the handshake cannot
start.** A new phone gets `check_contact` automatically, so this only comes up
if it was deleted. See [Chapter 08](08-templates.md).

### 3. They reply — and you pick the reply

The wizard polls for incoming replies and lists them as they arrive. **You pick
the one that came from the person you meant.**

Each candidate has a **Chat** button so you can read the full conversation
before choosing.

If the list is empty, the person hasn't replied yet. Press **Refresh**.

Replies are only offered **from the last 24 hours**. A handshake left open for
days will show an empty list even though the person did answer — start it again
rather than waiting.

### 4. PONG

Picking the reply links the contact to the real WhatsApp identity behind it —
its **LID** — and tags the contact **active**. This is the step that makes the
contact usable.

### 5. Summary

Confirm, and the contact is ready.

## The contact table

Once linked, contacts appear in a table on the same tab. From there you can edit
a contact, and open its calls.

**Clicking a contact opens that contact's calls** →
[Chapter 10](10-watching-a-call.md) for a running call,
[Chapter 11](11-reading-a-call.md) for finished ones.

## Common problem

**"I added a contact but nothing works."** The handshake almost certainly wasn't
finished — step 3 was left open without picking a reply. Reopen the wizard for
that number; you'll get the **Override** answer, and you can complete it.

---

**Next:** [Building a scenario](05-scenarios.md)
