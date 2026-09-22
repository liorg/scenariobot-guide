# 09. Schedules

**How to get there:** **Top bar → Schedules.**

## What a schedule is

A rule that fires a scenario at chosen times, so you don't have to start each
call by hand.

## Creating one

Create a schedule and choose three things:

1. **the phone** it runs from
2. **the scenario** to run — it must belong to that phone
3. **the timing** — either a one-off time, or a repeating cron expression

**You do not pick the contact.** It comes from the scenario, and is overwritten
whenever you change which scenario the schedule runs.

The scenario must be **published**
([Chapter 05](05-scenarios.md#saving-vs-publishing)) and its contact must be
**linked** ([Chapter 04](04-contacts.md)), or nothing will run.

## Running one now

**Play** on a schedule runs it immediately — or as close as the system gets. It
queues the schedule for right now and the Scheduler fires it on its next tick,
so it starts **within moments rather than instantly**. A short delay is normal
and not a fault.

If the schedule is already firing, play is refused until it finishes.

A schedule you control is either **active** or **paused**. The other states you
may see — *firing*, *completed*, *error* — are set by the Scheduler itself.

## The log

Each schedule keeps its own log of the calls it produced. That's the place to
check whether last night's run actually happened.

## What can stop a scheduled call

- The phone is **disconnected** → [Chapter 03](03-phones.md)
- The contact already has a **call running** — only one at a time per contact
- The scenario was **unpublished** after the schedule was made

All three show up in the schedule's log rather than as an alert, so it's worth
looking there when an expected message didn't go out.

---

**Next:** [Watching a call run](10-watching-a-call.md)
