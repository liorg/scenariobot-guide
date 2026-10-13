# 03. Connecting a phone

**How to get there:** **Top bar → Phones**. This is the screen you land on after
signing in.

**URL:** [grossman.bot/phones](https://grossman.bot/phones)

Also [grossman.bot/phones/new](https://grossman.bot/phones/new) to add one, and `grossman.bot/phones/<phone>/reconnect` to reconnect.

## The phone list

Every number you've connected, as a card showing its nickname, number, label,
colour and live status.

| Status | Meaning |
|---|---|
| **Active** | linked and working |
| **Disconnected** | the WhatsApp session dropped — nothing will run |

Each card has actions for disconnecting and reconnecting. **Clicking the card
itself opens that phone** — see [Phone Detail](#what-is-inside-a-phone) below.

There's also a **Templates** tab on this screen → [Chapter 08](08-templates.md).

## Two kinds of phone

Before adding one, the choice that shapes everything after it:

| | **Linked phone** (Baileys) | **Cloud API** |
|---|---|---|
| How it connects | you scan a QR with a real handset | official credentials from Meta |
| What you need | the handset, nearby | a WhatsApp Business Account, a phone number id and an access token |
| The handset | must stay on and online | **not needed at all** |
| Setup | minutes | Meta's business verification first |
| Templates | per phone | shared across every number on the same business account |

A linked phone is the quick way to start and the right choice for a number you
already own and keep powered on. Cloud API is Meta's official route: nothing to
keep charged, nothing to re-scan, and it is the one that scales.

The rest of the product behaves identically either way. Scenarios, contacts,
schedules and the chat view do not care which you picked.

## Adding a phone

**Phones → + Add Phone.**

### Step 1 — Choose the provider

Pick **linked phone** or **Cloud API**. The wizard asks for different things
after this, and the choice cannot be changed later — a number moves between
providers by removing it and adding it again.

### Step 2 — Phone details

Nickname, number, a label (Business, Private, Marketing, Support, Sales,
General) and a colour. Accept the terms to continue.

The label and colour are only for your own organisation — they don't change
behaviour.

**For Cloud API** you also supply the business account id, the phone number id
and an access token, all from Meta's dashboard. They are checked against Meta
before the phone is created, so a wrong value is rejected here rather than
producing a phone that never works.

### Step 3 — Connect

**Linked phone:** open WhatsApp on the handset → **Linked devices** → scan the
code shown on screen. Keep the handset nearby, because the code refreshes on a
timer. A **pairing code** is offered as an alternative if scanning isn't
practical — you type an 8-character code into WhatsApp instead.

**Cloud API:** nothing to do. There is no QR and no pairing code; the
credentials are the connection. The phone turns active once it has registered,
which takes a few seconds.

### Step 4 — Confirm

The phone joins the list and turns active.

## Reconnecting

If a phone shows **disconnected**, use **Reconnect** on its card. The same
wizard opens with the number already filled in, and you rescan.

**A Cloud API phone has no session to lose**, so it does not drop the way a
linked phone does. If one shows disconnected, the usual cause is an expired or
revoked access token rather than anything on a handset.

The session behaves like any WhatsApp Web session: it stays linked until
something ends it. See [Chapter 15](15-tips.md) for what keeps it alive.

## What is inside a phone

Clicking a phone card opens **Phone Detail**, which has three tabs:

| Tab | Contents | Chapter |
|---|---|---|
| **📞 Calls** | chat view and call history | [12](12-chat-view.md), [11](11-reading-a-call.md) |
| **👥 Contacts** | contact list and the contact wizard | [04](04-contacts.md) |
| **🤖 Scenarios** | scenario list and the designer | [05](05-scenarios.md) |

The back arrow at the top-left returns to the phone list.

---

**Next:** [Adding a contact](04-contacts.md)
