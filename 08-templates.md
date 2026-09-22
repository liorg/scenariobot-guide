# 08. Templates

**How to get there:** **Top bar → Phones → Templates tab.**

## What a template is

A **pre-approved WhatsApp message format** with numbered placeholders:

```
Hello {{1}}, your appointment is on {{2}}.
```

WhatsApp approves the wording in advance. You supply the values at send time.

## Why they exist

WhatsApp only lets a business send a free-form message within **24 hours** of
the person's last message. Outside that window, a template is the only thing
that will be delivered.

So: reminders, first contact, and anything that reaches out cold needs a
template. A reply inside an active conversation does not.

## What you can do here

| Action | Notes |
|---|---|
| **Create** | write the template with its `{{1}}`, `{{2}}` slots |
| **Validate** | check it and get back a list of issues, changing nothing |
| **Publish** | make it available to scenarios |
| **Unpublish** | take it back out of use |
| **Send test** | send it to a number, even before it's published |

A template moves through **pending → approved → published**, and can also be
**rejected** or **paused**.

## The templates you start with

A new phone does not start empty. **Six templates appear on their own**, from
two different places:

| Template | Where it comes from | When |
|---|---|---|
| `check_contact` | created when the phone is provisioned | immediately |
| `hello_world` | the provider's standard catalog | within ~15 minutes |
| `sample_issue_resolution` | the provider's catalog | ~15 minutes |
| `sample_shipping_confirmation` | the provider's catalog | ~15 minutes |
| `sample_movie_ticket_confirmation` | the provider's catalog | ~15 minutes |
| `sample_purchase_feedback` | the provider's catalog | ~15 minutes |

The first is ours — a one-line "Are you a bot?" used by the contact handshake.
The other five are the samples every new WhatsApp Business account is given,
and they are **imported**, not created here. That is why they can appear on the
Templates tab some minutes after the phone is connected rather than at once.

`sample_purchase_feedback` arrives **rejected**, with the reason
`INCORRECT_CATEGORY`. That is how it comes from the provider — nothing went
wrong, and it is a useful example of what a rejected template looks like.

If the tab looks empty just after connecting a phone, wait and refresh before
assuming something failed.

## Approval happens by itself

**You do not have to wait for anyone to approve a template you create.**

Within roughly two minutes of creating one, the system checks its status with
the provider, and a template that comes back approved is **published at the
same moment**. It then shows up in the scenario Input picker.

So the usual sequence is: write it, wait a couple of minutes, refresh, and it
is ready to use. There is no approval queue to watch and nobody to chase.

Two consequences worth knowing:

- **The publish button is often already done for you.** If a template is
  already published when you go to publish it, that is why.
- **A template that stays pending for much longer than a few minutes is a
  signal.** It usually means the phone's connection is down, not that approval
  is slow. Check the phone's status first.

This is also why the wording is worth getting right before you create the
template: nothing sits in review long enough for a second look.

### Rules that catch people out

- **A published template is locked.** You cannot edit or delete it until you
  unpublish.
- **Editing the text undoes approval.** Changing the content sends an approved
  template back to *pending*.
- **Any status other than approved also unpublishes it.**
- **Names allow lowercase letters, digits and underscores only** —
  `appointment_reminder`, not `Appointment Reminder`. A name with a capital
  letter or a space is rejected rather than corrected.
- **Renaming breaks the link to the provider's copy.** The name is how the two
  are matched, so a renamed template can come back as a second entry. Create a
  new one instead of renaming an established one.
- Each template has a category: **UTILITY**, **MARKETING** or
  **AUTHENTICATION**.
- **Deleting is safe when it half-worked before.** If a template failed to
  register the first time, the system repairs it on its own within about
  fifteen minutes — you do not need to delete and recreate it.

### Test sending

The test send works before publishing, and **any slot you leave empty is filled
from the template's own examples** — so you can fire one off without typing
anything but the recipient.

## Sending one by hand

You do not need a scenario to send a template. In the chat view
([Chapter 12](12-chat-view.md)) the **📋** button next to the send arrow opens a
picker of this phone's approved, published templates, fills the parameters from
the examples, and sends.

That is the way to **reopen a conversation** with someone who hasn't written to
you in over 24 hours.

## Using one in a scenario

In the designer, an **Input** step has a **template** mode. It lists the
templates that are **both approved and published** for that phone, and gives you
a field per slot with a live preview of the finished message.

A template that's merely approved will not appear there. If one is missing from
the list, publishing it is usually the reason — though in practice approval and
publishing happen together, so a missing template more often means it has not
been approved yet.

`check_contact` and the five samples are ordinary templates and can be used in
a scenario like any other, as long as they are approved and published.

Note the numbering restarts per part: `{{1}}` in the header and `{{1}}` in the
body are different slots.

See [Chapter 06](06-components.md#input-has-two-modes).

---

**Next:** [Schedules](09-schedules.md)
