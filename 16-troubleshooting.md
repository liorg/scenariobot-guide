# 16. Troubleshooting

**How to get there:** each entry says where to go.

## A contact was added but nothing works

**Cause:** the PING/PONG handshake wasn't finished — the reply was never picked.

**Fix:** **Phones → a phone → 👥 Contacts** → reopen the wizard for that number.
You'll get the **Override** answer; complete step 3 by picking the reply.

→ [Chapter 04](04-contacts.md)

## A call won't start for a contact

**Cause:** a contact can only run **one call at a time**, and one is probably
still open.

**Fix:** **Phones → a phone → 👥 Contacts → the contact.** If the live panel
shows a running call, end it with **⏹ End call**.

→ [Chapter 10](10-watching-a-call.md)

## The phone shows disconnected

**Cause:** the WhatsApp session dropped.

**Fix:** reconnect from the phone card and rescan. If it keeps dropping, work
through [Chapter 15](15-tips.md) — battery optimisation is the usual culprit —
and if it still drops, that's an operations issue rather than something the
interface can fix.

→ [Chapter 03](03-phones.md)

## A call expired without a reply, but the person says they answered

**Cause:** usually the match mode was too strict, not a missing message.

**Fix:** open the call, check the **📡 Events** tab. If the reply is listed but
the step still failed, change the EXPECT step from **exact** to **contains**.

→ [Chapter 11](11-reading-a-call.md), [Chapter 06](06-components.md#match-mode)

## A sent message has a blank where a name should be

**Cause:** a misspelled `{{ }}` path. An unknown path becomes an empty string
silently — nothing warns you.

**Fix:** open the step and check the spelling against the quick-add buttons,
which insert the correct paths.

→ [Chapter 06](06-components.md#--parameters)

## A custom code step ran fine but stored nothing

**Cause:** an EXPECT code card must return a key named exactly **`expected`**. A
differently-named key succeeds and stores nothing.

**Fix:** check the return object in the card.

→ [Chapter 06](06-components.md#an-expect-code-card-judges-a-reply)

## Editing a scenario changed my old reports

**It didn't.** Each call stores a snapshot of the scenario as it was at run
time, and that snapshot is what the flow diagram renders.

→ [Chapter 11](11-reading-a-call.md)

## A scheduled call didn't happen

**Check the schedule's own log first.** The three usual causes are: the phone
was disconnected, the contact already had a call running, or the scenario was
unpublished after the schedule was made.

→ [Chapter 09](09-schedules.md)

## Publish is blocked

**Cause:** one of three checks failed — a required field, a code card that
doesn't compile, or the whole-scenario compile.

**Fix:** the errors panel opens by itself and lists them.

→ [Chapter 05](05-scenarios.md#saving-vs-publishing)

## The save button is greyed out

**Cause:** the scenario is **published**. Published scenarios are read-only.

**Fix:** unpublish, edit, publish again.

→ [Chapter 05](05-scenarios.md#saving-vs-publishing)

## A template has been pending for a long time

**Cause:** approval is automatic and normally takes about two minutes. If it
hasn't happened, the phone's container isn't answering — it's a connection
problem, not a slow reviewer.

**Fix:** check the phone's status on **Phones**. Reconnect if it shows
disconnected. The template will approve itself once the phone is back.

→ [Chapter 08](08-templates.md#approval-happens-by-itself)

## The Templates tab looks empty on a new phone

**Cause:** only `check_contact` is created when a phone is provisioned. The
five standard samples are imported from the provider afterwards, within about
fifteen minutes.

**Fix:** wait and refresh. Nothing is broken.

→ [Chapter 08](08-templates.md#the-templates-you-start-with)

## A duplicate template appeared

**Cause:** a template is matched to the provider's copy by **name plus
language**. Renaming one breaks that match, and the next import brings the
original back as a second row.

**Fix:** delete the one you don't want, and create a new template rather than
renaming an established one.

→ [Chapter 08](08-templates.md#rules-that-catch-people-out)

## The contact handshake won't start at all

**Cause:** the PING is sent as a template, and the phone has no approved,
published template to send. Usually `check_contact` was deleted.

**Fix:** re-provision the phone, or ask whoever runs the system to recreate
`check_contact`.

→ [Chapter 04](04-contacts.md), [Chapter 08](08-templates.md)

## A template isn't in the designer's list

**Cause:** the Input step lists only templates that are **approved AND
published**. Approved alone isn't enough.

**Fix:** **Phones → Templates**, publish it.

→ [Chapter 08](08-templates.md)

## I can't edit or delete a template

**Cause:** it's published. Published templates are locked.

**Fix:** unpublish, edit, publish again — but note that changing the text sends
it back to *pending*.

→ [Chapter 08](08-templates.md#rules-that-catch-people-out)

## Running a schedule now does nothing

**Cause:** either it's already firing — in which case the request is refused
until it finishes — or the play only queued it and the Scheduler hasn't ticked
yet.

**Fix:** wait a moment and check the schedule's log.

→ [Chapter 09](09-schedules.md)

## Can a scenario be tested without messaging a real person?

Use **Playback** to read it as a conversation, and the **check** button for
custom code steps. A real send still needs a real linked contact.

→ [Chapter 07](07-playback.md)

## The panel warns that multiple calls are active

Only one is supposed to be. **Report this** — it isn't fixable from the
interface.

→ [Chapter 15](15-tips.md#3-getting-help)

---

**Next:** [Glossary](17-glossary.md)
