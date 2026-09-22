# 10. Watching a call run

**How to get there:** **Top bar → Phones → a phone → 👥 Contacts → click a
contact.** If a call is running, a live panel sits at the top of that screen.

## What the live panel shows

- the **scenario name**, and whether the call is running or still pending
- **elapsed time**, counting up
- **time remaining** before the call expires — turns red under 30 seconds
- **steps done out of total**, as a progress bar
- **messages sent** against messages expected
- **mismatches** so far, if any
- **the last thing that happened** — message sent, reply received, reply timed
  out, reply didn't match, step finished

It refreshes itself every few seconds, and **stops refreshing while the browser
tab is in the background** so it isn't polling when nobody's looking.

## The two buttons

**🔀 Flow** — opens the diagram for the call that's running right now, so you can
see which step it's sitting on. → [Chapter 11](11-reading-a-call.md)

**⏹ End call** — stops it. You're asked to confirm first. An ended call is
recorded as **aborted**, not failed, so it's distinguishable from a real failure
later.

## If it warns about multiple active calls

A contact is only supposed to have **one** call running. If the panel says more
than one is active, tell whoever runs the system — that's a fault, not something
you can fix from the interface.

## If there's no panel

No call is running for that contact. The screen below is the history →
[Chapter 11](11-reading-a-call.md).

---

**Next:** [Reading a finished call](11-reading-a-call.md)
