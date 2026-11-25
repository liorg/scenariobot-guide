---
id: 16-troubleshooting
title: Troubleshooting — symptoms and fixes
keywords:
  - bot (agent)
  - agent not working
  - troubleshooting
  - not working
  - error
  - stuck
  - blocked
  - greyed out
  - no message
  - failed
  - fix
  - why
related:
  - 10-watching-a-call
  - 11-reading-a-call
  - 17-glossary
actions:
  - id: diagnose-phone-offline
    description: Show the phone's status on its card
    screen: screen-phone-card
    target: status-badge
    type: navigate-highlight
  - id: diagnose-contact-handshake
    description: Show the bot (agent)'s state
    screen: screen-contacts
    target: ct-0-status
    type: highlight
  - id: diagnose-blocked-publish
    description: Show what is blocking publishing
    screen: screen-designer
    target: errors-panel
    type: highlight
  - id: diagnose-schedule-never-fires
    description: Show when a schedule fires next
    screen: screen-schedules
    target: sh-0-next
    type: navigate-highlight
  - id: diagnose-two-step-required
    description: Open two-step verification
    screen: screen-settings
    target: settings-tab-two-step
    type: navigate-highlight
---
# 16. Troubleshooting

**How to get there:** each entry says where to go.

## A bot (agent) was added but nothing works

**Cause:** the PING/PONG handshake wasn't finished — the reply was never picked.

**Fix:** **Phones → a phone → 👥 Bots (Agents)** → reopen the wizard for that number.
You'll get the **Override** answer; complete step 3 by picking the reply.

→ [Chapter 04](04-contacts.md)

## A call won't start for a bot (agent)

**Cause:** a bot (agent) can only run **one call at a time**, and one is probably
still open.

**Fix:** **Phones → a phone → 👥 Bots (Agents) → the bot (agent).** If the live panel
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

## The pattern assistant won't generate

**Cause:** either the description could not be turned into a pattern, or the AI
service is unavailable. They are different problems.

**Fix:** reword the description more concretely first — say what the message
looks like rather than what it means. If that changes nothing, the service is
likely down and nothing you write will help; the ✨ button works again once it
is back.

Meanwhile you can type a pattern into the field by hand — it is an ordinary
text box, and the sample tests still run.

→ [Chapter 06](06-components.md#pattern-mode-writes-the-pattern-for-you)

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
was disconnected, the bot (agent) already had a call running, or the scenario was
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

## My message was rejected, or never arrived

**Cause:** the 24-hour window is closed. WhatsApp only allows free text within
24 hours of the bot (agent)'s last incoming message.

**Fix:** send an approved template instead — the **📋** button beside the send
arrow. The coloured strip at the top of the chat tells you which state you are
in.

→ [Chapter 12](12-chat-view.md#the-24-hour-window)

## The chat says "no incoming message yet" but they have written to me

**Cause:** the window is judged from the messages currently on screen. If a long
run of outgoing messages follows their last reply, it may not be loaded yet.

**Fix:** scroll up in the conversation. The strip corrects itself once the
inbound message loads.

→ [Chapter 12](12-chat-view.md#the-24-hour-window)

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

## The bot (agent) handshake won't start at all

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
custom code steps. A real send still needs a real linked bot (agent).

→ [Chapter 07](07-playback.md)

## The panel warns that multiple calls are active

Only one is supposed to be. **Report this** — it isn't fixable from the
interface.

→ [Chapter 15](15-tips.md#3-getting-help)

## A bot (agent) disappeared from the conversation list

**Cause:** it was **ignored** — ignored bots (agents) are hidden from the list and
from the counts by design. (Inactive ones stay visible, greyed out, at the
bottom.)

**Fix:** nothing was deleted. Send a new **PING** to that number and the bot (agent)
comes back, restarting the handshake.

→ [Chapter 04](04-contacts.md#ignored)

## A bot (agent) is marked ⛔ Unwanted and I can't send anything

That number replied STOP to the first message, or used the unsubscribe link
in it. The block is on the **number**, applies to every customer on the
platform, and is enforced in the database — so no screen, import or API call
can get around it, and deleting the bot (agent) and re-adding it brings back
the same ⛔.

**There is no button for this.** Only support can revoke it, with the
`UNW-…` reference or the number. [Chapter 23](23-unwanted.md).

## There is a message on my phone that I did not send

Read the recent calls for that phone ([Chapter 11](11-reading-a-call.md)) — a
scheduled scenario you had forgotten is the usual answer, and the call history
names the scenario and the step that sent it.

If nothing there accounts for it, treat it as a compromised session: disconnect
the phone, then mail **contact@grossman.bot** with the number and roughly when
it happened. Don't wait until you are certain.
[Your phone, your responsibility](03-phones.md#your-phone-your-responsibility).

## No mail is arriving on a phone

Check the address on **Phone details** against what you sent to — it is the
phone's own number at `grossmanbot.download`, so a wrong digit is easy. On a
phone added minutes ago the inbox may still be going up; the dialog says so.
[Chapter 24](24-mail.md).

## The mail is in the Mail tab but the scenario never got it

Read the status on the message. **Too old, not sent** means it took more than
ten minutes to reach us and the code would have expired anyway. **Phone has
no host** means the phone isn't running. **No status at all** means nothing
was waiting for it — the call was not sitting on a **Receive mail** card.

## The mail arrived but no code was captured

Open the **Receive mail** card and use its **Test** box with the real sender,
subject and body. It names the part that failed — the sender, the subject, or
the value itself. Remember the sender and subject filters ignore case, but a
`Format` or `Regex` capture can be set to match case.

## The mail I wanted to keep has gone

A rented phone's mail is deleted when the rental ends or the phone is rented
by someone else. The mailbox belongs to the phone, not to you — copy out
anything you need while the rental is live. [Chapter 24](24-mail.md).

## One screen is in English while the rest is translated

That string has no translation in your language yet, and a missing string
falls back to English one at a time rather than dropping the whole screen.
It is fixed centrally — report it and it arrives on its own.

If **everything** reverted to English, the language list didn't load; the
previously loaded languages are cached in the browser, so this usually means
a first visit on a new machine while the server was unreachable.
[Chapter 22](22-languages.md).

## My country isn't in the phone number field

Phone fields only offer the countries ticked in **Settings → 🌍 Language &
countries**. Tick it there. If it isn't in that table at all, the platform
hasn't enabled it yet. [Chapter 22](22-languages.md).

## How do I delete a bot (agent)?

**You don't** — there is no delete, on purpose. The messages and the handshake
history are kept.

**Fix:** use **⏸ Cancel** to set it aside (it stays under Inactive and can be
brought back with 🔗 Connect), or **🚫 Ignore** to take it off the list.

→ [Chapter 04](04-contacts.md#deactivating-ignoring-restoring)

## Importing a scenario says the name already exists

**Cause:** a scenario of that name is already on this phone. That is a question,
not an error.

**Fix:** **Override** replaces it — and **unpublishes it**, because the new
content hasn't been checked; publish again when you're ready. **New** keeps both
and suggests a free name.

→ [Chapter 05](05-scenarios.md#importing)

## An imported scenario won't publish — a template is pending

**Cause:** the import created a template the phone didn't have, and the provider
hasn't approved it yet. The import succeeded; the template is the hold-up.

**Fix:** wait and refresh, then publish. If it was rejected, the Templates tab
shows the reason.

→ [Chapter 08](08-templates.md)

## The ❓ Help button is gone from the top bar

**Cause:** it moved into the **avatar menu**, with Settings and Logout.

**Fix:** click your avatar → **❓ Help**. Same guide, in a dialog.

→ [Chapter 14](14-settings.md#the-avatar-menu)

## Saving a scenario fails with "not in trusted domains"

**Cause:** a code step calls a URL whose domain is not on your trusted list. The
message names the step and the URL. Common surprises: a **subdomain** (approving
`example.com` does not approve `api.example.com`), and a URL sitting in a
**comment**, which is checked like any other.

**Fix:** add that exact host in
[Settings → ⚙️ Advanced](https://grossman.bot/settings/advanced), or remove the
`https://` from the comment. A non-Latin domain must be written in its punycode
form in the code.

→ [Chapter 06](06-components.md#the-domain-has-to-be-approved-first)

## "dynamic host is not allowed"

**Cause:** the domain in a `fetch` is built from a variable —
`` `https://${host}/x` ``. The host has to be written out literally.

**Fix:** write the domain in the code and build only the path:
`` `https://api.example.com/orders/${id}` `` is fine.

→ [Chapter 06](06-components.md#the-domain-has-to-be-approved-first)

## A trusted domain won't save

**Cause:** it is verified, not just stored. The usual causes are a certificate
with under a week left, DNS pointing at a private address, nothing answering on
port 443, or a URL that isn't `https` on 443.

**Fix:** the error says which. Note that if you changed several domains at once,
**none** of them were saved — fix the one that failed and save again.

→ [Chapter 14](14-settings.md)

## A code step that calls a URL hangs or stores nothing

**Cause:** three usual ones, in order — no timeout on the `fetch`, so a hung
service hangs the step; no status check, so an error page is parsed as JSON; or
an object returned in `selectedValue`, which is a text field.

**Fix:** `AbortSignal.timeout(5000)`, an `if (!r.ok)` branch, a `try/catch` that
returns `success: false` with the reason, and `String(...)` around the value.
The reason then shows up in the call's events instead of nowhere.

→ [Chapter 06](06-components.md#calling-an-external-service)

## An execution is stuck on "pending"

**Cause:** the jobs are queued and the Scheduler has not picked them up. The
screen refreshes itself every five seconds, and ▶ stays disabled until it
clears.

**Fix:** a few seconds is normal. Much longer means the Scheduler isn't
running — report it.

→ [Chapter 13](13-executions.md)

## A phone can't be ticked as an execution target

**Cause:** it is a Cloud API phone. Only linked phones (Baileys) can be targets,
because the feature copies templates **per phone** and Cloud API templates
belong to the business account instead.

**Fix:** use linked phones for the run, or run the scenario on the Cloud API
phone directly.

→ [Chapter 13](13-executions.md)

## I deleted an execution and the copied scenarios are still there

**Cause:** that is by design. Deleting an execution removes the execution only —
the scenarios, templates and schedules it created live on the target phones.

**Fix:** they are all named after the run (`run_… <scenario>`,
`prefix_<template>`, `run_… JOB`), so search that name on each phone and delete
what you don't want.

→ [Chapter 13](13-executions.md)

## I got no warning before my rental ended

**Cause:** two possibilities. The warning is a **share of the rental**, not a
fixed lead time — on a very short rental it arrives seconds before the end. Or
you have **Errors only** on for email, which filters it out, because the warning
is a ⚠️ and only ❌ errors are mailed.

**Fix:** the bell always shows it. For the email, turn **Errors only** off in
[Settings → ⚙️ Advanced](https://grossman.bot/settings/advanced).

→ [Chapter 20](20-rented-phones.md#you-get-told-three-times)

## What is the striped frame around a phone card?

**Cause:** nothing is wrong — a green-and-white frame marks a **rented** phone,
and it disappears when the rental ends.

→ [Chapter 20](20-rented-phones.md#how-it-looks-in-the-phone-list)

## The battery icon on my phone is red

**Cause:** it is the rental gauge, and red means the last stretch of your time.
It turns red at the same moment the "ending soon" notification is sent.

**Fix:** export anything you want to keep now
([Chapter 05](05-scenarios.md#export-and-import)) — when the clock runs out
everything on the phone is deleted.

→ [Chapter 20](20-rented-phones.md#how-it-looks-in-the-phone-list)

## The Rented phones tab isn't there

**Cause:** like the API console, it is hidden until two-step verification is
done.

**Fix:** verify your mobile number in
[Settings → 🔐](https://grossman.bot/settings/2fa).

→ [Chapter 20](20-rented-phones.md)

## "Rent" is greyed out on a phone

**Cause:** one of three — the handset is **offline**, **WhatsApp isn't
installed** on that SIM, or another action is still running.

**Fix:** the first two are the rack's problem, not yours; pick another number.
The Device column shows which it is.

→ [Chapter 20](20-rented-phones.md)

## My rented phone disappeared

**Cause:** the rental ended — either you ended it or the clock ran out. The
phone went back to the pool and everything on it was deleted.

**Fix:** nothing to recover. Next time, export the scenario before the time is
up and import it onto a phone of your own.

→ [Chapter 20](20-rented-phones.md#ending-it)

## There's no SMS tab on my phone

**Cause:** the tab only exists on a **rented** phone. A phone you added yourself
has no SIM the platform can read.

**Fix:** rent one if you need to receive text messages.

→ [Chapter 21](21-sms.md)

## An SMS never arrived

**Cause:** usually the handset is offline, or the message went to the other SIM
in the same device — a different number from the one you rented.

**Fix:** check the Device column on the rent screen. Delivery takes a few
seconds, not a minute.

→ [Chapter 21](21-sms.md#when-a-message-doesnt-arrive)

## A phone is stuck greyed out after Disconnect

**Cause:** disconnecting is asynchronous — the card stays grey until the phone's
status actually changes.

**Fix:** it clears itself after about three minutes even if the status never
changes, which happens when the phone was already disconnected. If it is still
grey after that, reload.

→ [Chapter 03](03-phones.md)

## The API button has disappeared from the top bar

**Cause:** it is hidden until two-step verification is done. Opening `/api`
directly also bounces back to the phone list.

**Fix:** verify your mobile number in
[Settings → 🔐](https://grossman.bot/settings/2fa). The button appears
immediately afterwards.

→ [Chapter 18](18-api-explorer.md)

## A schedule is active but never fires

**Cause:** most often two-step verification. The Schedules screen stays open
without it, so the schedule looks fine — but every run is refused.

**Fix:** verify your mobile number in
[Settings → 🔐](https://grossman.bot/settings/2fa). If the banner is already
gone, check the usual causes instead: the scenario must be published and its
bot (agent) linked.

→ [Chapter 09](09-schedules.md)

## "This number is one of your bot phones"

**Cause:** you tried to verify a mobile number that is already one of your bot
phones. The reverse is refused too — your verified mobile cannot be added as a
bot phone.

**Fix:** verify a personal handset instead, and keep the bot numbers for bots.
A bot phone receiving your codes could read them itself, which is what the rule
prevents.

→ [Chapter 14](14-settings.md)

## The orange "two-step verification required" banner won't go away

**Cause:** your mobile number is not verified, and the banner is deliberately
not closable — it is a requirement, not a hint.

**Fix:** press **Verify now** on the banner, or open
[Settings → 🔐](https://grossman.bot/settings/2fa). It disappears the moment
the code is accepted.

→ [Chapter 14](14-settings.md)

## The verification code never arrived

**Cause:** usually the wrong number, or the message is a few seconds behind.
Check the masked number shown under the code boxes — it's the number the code
actually went to.

**Fix:** wait a few seconds, then **Resend** (it unlocks a minute after the
last code). If the screen said it **could not send the code over WhatsApp**,
that one is on our side — try again shortly, and report it if it persists.

→ [Chapter 14](14-settings.md)

## "Add Phone" is greyed out

**Cause:** one of two gates. Either adding phones is still limited to beta
accounts, or your mobile number is not verified. The button's own message says
which.

**Fix:** verify your number in [Settings → 🔐](https://grossman.bot/settings/2fa),
or bot (agent) **contact@grossman.bot** for beta access. Beta access is checked
first, so verifying won't help if that's what's missing.

→ [Chapter 03](03-phones.md)

## I verified my number, but it says unverified again

**Cause:** you saved a **different** mobile number. Changing the number resets
verification by design.

**Fix:** verify the new number. Reformatting the same number — `054…` versus
`+972 54…` — is not a change and resets nothing.

→ [Chapter 14](14-settings.md)

## I'm not getting notification emails

**Cause:** in order of likelihood — email notifications are off, **Errors
only** is on and the notification was a success, or the account has no email
address.

**Fix:** [Settings → ⚙️ Advanced](https://grossman.bot/settings/advanced). Note
that emails arrive as a **digest**, so a run against many phones is one email
rather than one per phone.

→ [Chapter 14](14-settings.md)

## Save is blocked and the ⚙️ tab has a dot

**Cause:** the **trusted domain** on the Advanced tab is not a valid domain.

**Fix:** enter the domain alone — `example.com` or `*.example.com`, without
`https://` or a trailing slash — or clear the field, which is also valid.

→ [Chapter 14](14-settings.md)

---

**Next:** [Glossary](17-glossary.md)
