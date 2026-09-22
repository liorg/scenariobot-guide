# 15. Tips for a reliable setup

**How to get there:** nothing to open — this is advice to apply before and
during setup.

Most problems that look like software faults turn out to be one of three
things.

## 1. Use a clean phone number

Link a number that is dedicated to the bot and nothing else.

- **A number that has never been used on WhatsApp Business, or that has been
  freshly reset, behaves best.** A number carrying years of history brings its
  old chats, groups and contacts into the session, and every one of those is
  traffic the bot has to receive and discard.
- **Don't use it as a personal phone at the same time.** Messages you send by
  hand from the same number appear in the system as bot activity, because
  WhatsApp reports them on the same connection.
- **Don't link the same number to another automation tool.** WhatsApp allows a
  limited number of linked devices, and two tools sharing one number will keep
  disconnecting each other.
- **Leave it out of groups where possible.** Group traffic is received and
  processed even when no scenario cares about it.

If the number has been used heavily before, the cleanest start is to reset the
WhatsApp account on it and link it fresh.

## 2. Keep the phone powered on and online

The linked session depends on the phone staying reachable.

- **Keep it plugged in.** A phone that sleeps or runs flat takes the session
  down with it.
- **Keep it on Wi-Fi or mobile data continuously.** The session does not survive
  long periods offline.
- **Turn off battery optimisation for WhatsApp.** On Android this is the single
  most common cause of a session dropping overnight: the system suspends the
  app, and the link expires.
- **Don't log out of WhatsApp, clear its data, or uninstall it.** Any of those
  ends the session and requires a new QR scan.
- **Don't unlink the device.** Check the linked-devices screen occasionally — if
  the entry is gone, someone removed it.
- **Keep WhatsApp updated**, but expect a brief reconnection after a major
  update.

A dropped session shows as **disconnected** on the phone card. Until it's
rescanned, every scenario aimed at that phone will fail.

## 3. Getting help

If something is wrong and this guide doesn't cover it:

- **WhatsApp support: +972 54-625-2491**
- **Email: contact@grossman.bot**

When you get in touch, three details make the difference between a fast answer
and a long conversation:

1. **Which phone number** the problem is on.
2. **When it happened** — a rough time is enough.
3. **What you expected versus what happened** — for example, "the customer
   replied but the call still expired."

If it concerns a specific call, that call's screen has the flow diagram and the
events tab ([Chapter 11](11-reading-a-call.md)); saying which call it was lets
support look at exactly that run.

---

**Next:** [Troubleshooting](16-troubleshooting.md)
