---
id: 17-glossary
title: Glossary of terms
keywords:
  - bot (agent)
  - agent
  - glossary
  - terms
  - definitions
  - what does X mean
  - vocabulary
related:
  - 01-what-it-does
  - 06-components
---
# 17. Glossary

**Aborted** — a call someone stopped by hand. Distinct from failed.

**Active** — a phone whose WhatsApp session is connected and working.

**Bot (agent)** — a verified WhatsApp identity a phone can talk to. Verified
through the PING/PONG handshake. The API and the URLs still call this a
`contact`.

**Bot (agent) language** — the language the platform writes to a number in,
taken from the number's dial code, not from your interface language.

**Bot (agent) setting** — which bot (agent) a scenario talks to, set in scenario
settings. Stored as `bot_contact`.

**Balance** — what you have been charged minus what you have paid. Charges
accrue as you go; you pay when you choose.

**Call** — one run of one scenario against one bot (agent). A bot (agent) can only have
one running at a time.

**Canvas** — the middle column of the designer, holding the conversation top to
bottom.

**Code card** — a step that runs your own TypeScript, as one default async
function taking `payload: ScenarioPayload`. Exists in both EXPECT and SEND
forms.

**Designer** — the full-screen scenario editor.

**Disconnected** — a phone whose WhatsApp session has dropped. Nothing runs
against it.

**Draft** — a saved but unpublished scenario. Editable, not runnable.

**Events tab** — the raw timestamped timeline of a call.

**EXPECT** — what the bot **sends and then waits on**. The left/right column of
the designer.

**Expired / Timeout** — a call that ran out of time waiting for a reply.

**Grossman.bot** — the company and brand. Makes ScenarioBot; may carry other
products in future.

**Flow diagram** — the visual record of a finished call, showing which steps ran
and which failed.

**Linked** — a bot (agent) that completed the handshake and is usable.

**Mail address** — the inbox every phone has, its number at
`grossmanbot.download`. Mail sent there can be read in the Mail tab and
captured by a Receive mail card.

**Cooldown** — the 24 hours a removed bot (agent) keeps its plan slot, so a
small plan cannot be cycled through many numbers.

**Match mode** — how strictly a reply must match: exact, contains, pattern, any.

**Mother tongue** — the one language a country maps to. Decides the second
language of the platform's own messages to a number with that dial code.

**Opt-in message** — the notice the platform sends with the first PING: who is
testing, how to reply STOP, and an unsubscribe link.

**Override** — the wizard's answer when a partly-finished bot (agent) already exists
for a number.

**Parallel execution** — running one scenario against many phones at once.

**Phone** — a connected WhatsApp number. Owns its own bots (agents) and scenarios.

**PING / PONG** — the two halves of the bot (agent) handshake: a message out, and
picking the reply that comes back.

**Placeholder** — a `{{ }}` value in a text field, filled at run time. Shown as
a yellow chip.

**Plan** — what your account may have: how many phones, bots (agents) and
schedules, and whether the API and parallel executions are included.

**Playback** — reading a scenario as a chat window rather than a diagram.
Doesn't send anything.

**Published** — a scenario cleared to run. Read-only until unpublished.

**ScenarioBot** — the product itself: designing, testing, automating and
monitoring WhatsApp conversational scenarios. Built by Grossman.bot.

**Scenario** — the conversation script.

**Schedule** — a rule that fires a scenario at chosen times.

**SEND** — what the reply side supplies. The other side column of the designer.

**Snapshot** — the copy of a scenario stored with each call, so old reports never
change when you edit.

**Template** — a WhatsApp-approved message format with numbered slots. Required
outside the 24-hour window.

**Trigger** — a scenario that fires on an incoming event rather than a timer.

**Unwanted** — a number that asked to stop. Blocked for every customer on the
platform, enforced in the database, revocable only by support.

---

**Next:** [API Explorer](18-api-explorer.md)
