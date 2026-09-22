# 17. Glossary

**Aborted** — a call someone stopped by hand. Distinct from failed.

**Active** — a phone whose WhatsApp session is connected and working.

**Bot contact** — which contact identity the bot presents as, set in scenario
settings.

**Call** — one run of one scenario against one contact. A contact can only have
one running at a time.

**Canvas** — the middle column of the designer, holding the conversation top to
bottom.

**Code card** — a step that runs your own JavaScript. Exists in both EXPECT and
SEND forms.

**Contact** — a verified WhatsApp identity a phone can talk to. Verified through
the PING/PONG handshake.

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

**Linked** — a contact that completed the handshake and is usable.

**Match mode** — how strictly a reply must match: exact, contains, pattern, any.

**Override** — the wizard's answer when a partly-finished contact already exists
for a number.

**Parallel execution** — running one scenario against many phones at once.

**Phone** — a connected WhatsApp number. Owns its own contacts and scenarios.

**PING / PONG** — the two halves of the contact handshake: a message out, and
picking the reply that comes back.

**Placeholder** — a `{{ }}` value in a text field, filled at run time. Shown as
a yellow chip.

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

---

**Next:** [API Explorer](18-api-explorer.md)
