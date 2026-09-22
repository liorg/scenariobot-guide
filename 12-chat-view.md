# 12. The chat view

**How to get there:** **Top bar → Phones → a phone → 📞 Calls tab**, then click
a contact.

## What it is

The plain WhatsApp conversation with a contact — the same thing you'd see on
the handset.

- full conversation history, scrolling back as you go
- updates on its own as new messages arrive
- **you can type and send a message yourself**
- **you can send an approved template**

Only contacts that finished the handshake appear in the list
([Chapter 04](04-contacts.md)).

## The 24-hour window

This is the thing to understand before sending anything by hand.

WhatsApp lets a business send **free-form text only within 24 hours** of the
person's last incoming message. Outside that window, only an approved template
gets through.

The coloured strip under the contact's name tells you where you stand:

| Strip | Means | What you can send |
|---|---|---|
| 🟢 **green** — "chat window open" | they messaged you recently; it counts down the time left | anything — free text or a template |
| 🔒 **red** — "the 24-hour window closed" | more than 24 hours since their last message | **template only** |
| 📭 **amber** — "no incoming message yet" | they have never written to you | **template only** — a template is what opens the conversation |

The countdown is measured from **their** most recent message, not yours.
Replying to them does not extend it; only a new message from them does.

### The strip does not stop you

You can still press send on free text while the window is closed. **It is a
warning, not a lock.**

What happens next depends on how the phone is connected:

- On a **Cloud API** phone, WhatsApp rejects it and the error appears above the
  input box.
- On a **Baileys** phone there is no such restriction, and it goes through.

The strip shows the WhatsApp rule in both cases, so what you read is the same
wherever the phone runs.

## Sending a template

The **📋 button** beside the send arrow is always available. When the window is
closed its outline turns green — a quiet hint that it is now the way through.

Pressing it opens the picker:

1. **Choose a template.** The list holds only templates that are **approved and
   published** for this phone. Search by name. Each row shows a preview.
2. **Fill the parameters.** One field per `{{1}}`, `{{2}}`, grouped by part
   (header, then body). They come **pre-filled with the template's own
   examples**, so you can send a test with no typing at all.
3. **Check the preview.** The green box shows the finished message with your
   values substituted.
4. **Send.**

Every parameter must have a value — the send button stays disabled and a
warning appears until they all do.

If the phone has no approved, published template, the picker says so and points
you at the Templates tab ([Chapter 08](08-templates.md)).

### Simulating a button press

If the template has quick-reply buttons, the picker shows them, and below them
a **"simulate a reply after sending"** row.

Pick one and, about a second after the template goes out, the system sends that
button's label back **as if the contact had tapped it**. The scenario waiting on
that reply then carries on.

**This is for testing.** It puts a message into a real conversation with a real
person, so it is a way to walk a scenario through its next step without waiting
for someone to answer — not something to use on a live customer.

Leave it on **"none"** for an ordinary send.

## Reading the conversation

**Message types** render the way they arrive: text, images, voice notes,
button messages, and menus. Tapping a button or a menu row in the chat **sends
that choice as a message** — useful for driving a scenario forward by hand.

**Ticks and timing.** A message sent today shows the time; older ones show the
date. Day separators divide the history.

**The three dots** appear after you send, while the system waits for a reply.
They disappear on their own after ten seconds or when something arrives.

**Scrolling back.** Older messages load as you scroll up, thirty at a time, and
your position is kept. The counter in the header shows how many are loaded — a
`+` means there are more above.

## How it differs from scenario calls

This is the **human conversation**. Scenario calls are a separate view
([Chapter 11](11-reading-a-call.md)), even though both involve the same phone
and the same contact.

Messages a scenario sent do appear here — they were real WhatsApp messages. But
this screen shows them as chat, with no step structure, no statuses and no
diagram.

## When to use it

- checking what a person actually said, in context
- answering someone by hand when a scenario isn't the right tool
- **reopening a conversation that has gone quiet**, with a template
- pushing a stuck scenario along by tapping a button or simulating a reply
- reading the history before picking a reply during the contact handshake
  ([Chapter 04](04-contacts.md))

---

**Next:** [Parallel executions](13-executions.md)
