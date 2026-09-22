# 19. API reference

**How to get there:** **Top bar → API** to try any of these live
([Chapter 18](18-api-explorer.md)), or read the document at
`https://api.grossman.bot/openapi.json`.

Spec version **2.0.0.9**. Every summary, description and field note below comes
from that document.

## Before anything else

**Authentication.** Nearly every operation declares an `authorization` header.
The spec marks it *optional* — an artefact of how it's generated — but in
practice you need `Authorization: Bearer <token>`. The API Explorer fills it in
from your login, which is why there's no field for it there.

**The groups:** auth, phones, contacts, messages, notifications, scenarios,
schedules, templates, plus a small `phone-contacts` group with one endpoint.

**422 means your input.** FastAPI returns a `detail` array naming the field, its
location and what was wrong. Some endpoints also use 422 deliberately to report
validation *issues* — publishing a scenario or a template does this.

**Some endpoints are internal.** A few are wrapped in `internal_route` and are
hidden from the published spec depending on the deployment mode. They are
listed here where they are useful for diagnosis, marked *internal*.

---

## Auth

All under `/api/auth/`.

**The browser does not use these.** It signs in through supabase-js directly.
These exist for service clients, for scripts and for Postman, and they return
**the same Supabase access token** the browser holds — so a token obtained here
authenticates identically everywhere else in the API.

That is the single most important thing about this router, and it is stated at
the top of the file: it **does not mint its own JWT**.

| Endpoint | Does |
|---|---|
| `POST /google` | exchange a Google **ID token** for a Supabase session |
| `POST /login` | email and password |
| `POST /signup` | register; sends the verification email |
| `POST /forgot-password` | send reset instructions |
| `GET /settings` | your profile |
| `PUT /settings` | update name, mobile or language |
| `POST /avatar` | upload an avatar image |
| `GET /me` | what the bearer token resolves to |
| `GET /health` | liveness; no auth |

### Login

```json
{ "email": "you@example.com", "password": "…" }     // password: min 6 chars
```

Returns `access_token`, `refresh_token`, `expires_in` and a small `user`
object. **Send it as `Authorization: Bearer <access_token>`.**

An account whose email is not verified is refused with **403**, distinct from
the **401** for wrong credentials.

### Google

Takes the Google **OIDC ID token** — the `id_token`, not an OAuth access token;
Supabase verifies its signature. `nonce` is required only if the ID token was
requested with one.

On first sign-in the user row is created and the Google profile picture is
copied into storage. A picture that fails to download is not fatal: the
original Google URL is kept, so a storage outage never blocks a login.

### Signup

```json
{ "email": "…", "password": "…", "name": "Dana", "lang": "he" }
```

Returns a message, not a token — the address has to be confirmed first. An
address that already exists comes back as 400.

### Forgot password

**Always returns the same message**, whether or not the address exists. That is
deliberate: the endpoint cannot be used to find out who has an account.

### Settings

`PUT /settings` accepts exactly three fields — `full_name`, `mobile`, `lang` —
and only those. Two are **deliberately missing**:

- **`package_type`** is a billing field. Accepting it would let any caller
  upgrade their own plan with a PUT.
- **`avatar`** is writable only through `POST /auth/avatar`, so the stored URL
  is always one this backend uploaded, never an arbitrary URL from a client.

Sending them anyway does nothing — the update is built from the model, not from
the raw body.

`GET /settings` returns both `name` and `full_name` with the same value; the
second is kept for the existing UI.

### Avatar

Multipart upload. JPG, PNG, GIF or WebP, **5 MB maximum**. Returns the public
URL, which is also written to the user row.

An avatar you uploaded always wins: it is never overwritten by a Google picture
on a later sign-in.

### `GET /me`

Returns `uid`, `email` and `role` **as resolved from the token**, which makes it
the right call when you want to know what a token actually is rather than what
you think it is. `uid` here is the Supabase user id — a UUID. If you ever see
an email address in that field, the token is not a Supabase token.

---

## Phones

| Endpoint | Does |
|---|---|
| `GET /api/phones/` | your phones — **session credentials are never included** |
| `POST /api/phones/provision` | connect a number |
| `GET /api/phones/{id}/qrcode` | current QR, pairing code and connection status |
| `POST /api/phones/{id}/pairing-code/refresh` | ask the agent for a new pairing code |
| `POST /api/phones/{id}/pause` · `/resume` | pause and resume on the agent host |
| `POST /api/phones/{id}/logout` | log the phone out of WhatsApp |
| `POST /api/phones/{id}/send/text` | send a message by hand |
| `PATCH /api/phones/{id}` | `label`, `color`, `lang` — **nothing else can be changed** |
| `DELETE /api/phones/{id}` | delete the phone |
| `GET /api/phones/agents/health` | *internal* — health-checks every active agent host |
| `POST /api/phones/{id}/templates/test` | *internal* — dry-run the seed templates, writing nothing |
| `POST /api/phones/{id}/templates/check-contact` | *internal* — create `check_contact` if it is missing |

`GET /api/phones/` never includes session credentials. The column list is fixed
precisely so that `creds_base64` cannot leak to a browser.

The two internal template routes are the ones to reach for when a phone's
handshake will not start: the first validates each seed template locally **and**
against the agent without writing anything, and the second creates
`check_contact` if provisioning failed to.

### Provision

```json
{
  "phone_number": "972500000000",   // required, ≥7 digits, non-digits stripped
  "nickname": "Support line",
  "tag": "Support",
  "use_pairing_code": false
}
```

It **creates a phone, or reuses the one with the same number**, places it on a
healthy agent host, seeds `check_contact`, and returns the QR or pairing code.
Re-provisioning an existing number is safe.

"Reuses" is scoped to you: the lookup matches the number **for the current
user**, with and without a leading `+`.

Host selection tries the phone's existing host first, then searches for a
healthy one, retrying three times before giving up with 503. The agent call
itself retries three times with a growing delay.

**Template seeding cannot fail provisioning.** It runs after the phone exists,
inside its own try/except; a failure is logged and the phone is still returned.
The other five templates are imported later — see
[Chapter 08](08-templates.md#the-templates-you-start-with).

### Send text

```json
{
  "text": "hello",                            // required
  "jid": "972501234567@s.whatsapp.net",       // preferred
  "to": "972501234567"                        // legacy alias, used only when jid is empty
}
```

`to` is explicitly documented as a **legacy alias for `jid`**, consulted only
when `jid` is empty. New code should send `jid`.

---

## Contacts

### The PING handshake

The spec numbers three steps, and the fourth endpoint is **not one of them**:

```
step 1  POST /api/contacts/create-from-ping
step 2  GET  /api/contacts/outgoing-with-replies/{phone_id}
step 3  POST /api/contacts/select-response

        POST /api/contacts/link-draft-to-parent   ← called by the agent webhook
```

**`link-draft-to-parent` is not a user action.** The agent calls it when a
message arrives, to attach a draft contact to the newest pending PING on that
phone. You will not call it from the Explorer in normal use.

**First, `GET /api/contacts/check-phone?phone_id=…&number=…`**

| `status` | Means |
|---|---|
| `new` | no contact for this number |
| `blocked` | the contact already has a real LID — it's linked, leave it alone |
| `override` | a contact exists and can be reset and re-PINGed |

It also returns `ping_step` — the state of the latest open PING, either
`pending` or `waiting_reply` — plus `contact_id`, `contact_name`,
`contact_number` and `ping_sender_id`.

Note the wizard's three outcomes in [Chapter 04](04-contacts.md) map to these:
**blocked** is the one that means "already linked, cancel."

**Step 1 — `create-from-ping`**

```json
{
  "phone_id": "…",              // required
  "target_number": "…",         // required, 7-15 digits, non-digits stripped
  "name": "Dana",               // new contacts default to the number
  "override_contact_id": "…",   // reset this contact and PING again
  "lang": "he"                  // else the contact's, else the phone owner's
}
```

Creates, reuses or overrides the contact, then **sends the PING in the contact's
language**. Any unlinked drafts that already carry a real LID are linked to this
contact at the same time.

**Step 2 — `outgoing-with-replies/{phone_id}`**

Draft contacts with a valid LID that have messages **from the last 24 hours**,
with those messages attached. That 24-hour window is why an old unfinished
handshake shows an empty list: the replies aged out.

**Step 3 — `select-response`**

```json
{
  "contact_id": "…",        // required — the DRAFT that sent the reply
  "message_id": "…",        // required — the reply whose sender LID is taken
  "parent_contact_id": "…"  // the contact to activate; defaults to contact_id
}
```

This is the step that does the linking. It takes the LID from the chosen
message, sets it on the target contact, **tags that contact `active`**, clears
the LID from the draft, links any remaining drafts, and completes the pending
PING.

Until this runs the contact is not active — which is exactly the "I added a
contact but nothing works" case in [Chapter 16](16-troubleshooting.md).

### The rest

| Endpoint | Does |
|---|---|
| `GET /api/contacts?phone_id=…` | the phone's contacts, **most recently updated first** |
| `POST /api/contacts?phone_id=…` | create one directly |
| `GET /api/contacts/{id}` | a **fresh** copy from the database |
| `PATCH /api/contacts/{id}` | `name`, `email`, `tag`, `lid`, `lang` — only what you send |
| `DELETE /api/contacts/{id}` | see below |
| `GET /api/contacts/{id}/messages` | raw stored rows, oldest first |
| `GET /api/calls/{call_id}/messages` | every message of one scenario call, oldest first |

**`DELETE` is a cascade.** It removes the contact **together with its messages
and PING records**, unlinks drafts that pointed at it, and returns the number of
deleted messages. Not a soft delete.

`POST /api/contacts` takes `phone`, `name`, `email`, `tag` (default `new`),
`lid`, `lang`. Without `lang` the phone owner's language is used. The body has
no schema, so nothing is validated — prefer the handshake, which produces a
verified contact.

### `GET /api/phones/{phone_id}/contacts/active`

Its own group. The phone's contacts tagged `active`, ordered by name, returning
just `id`, `name`, `number`, `avatar`, `is_bot`. This is the picker list — the
contacts that are actually usable.

---

## Messages

### `GET /api/messages/phone/{phone_id}/contact/{contact_id}/page`

**The one to use.** Keyset paging, three modes:

| Call it with | Returns |
|---|---|
| nothing | the newest page |
| `before_sent_at` + `before_id` | an older page — scrolling up |
| `after_sent_at` | only newer messages — polling |

`before_id` is the **tie-breaker** for messages sharing a timestamp; without it,
paging can repeat or skip a row. Returns `{ messages, has_more, next_cursor }`.
`limit` defaults to 30, max 100.

### `GET /api/messages/phone/{phone_id}/last`

The last message of **every** contact on the phone, in one call, keyed by
`contact_id`. This draws the conversation list without one request per contact.

### The simpler reads

| Endpoint | Default / max | Order |
|---|---|---|
| `GET /api/messages/contact/{id}` | 200 / 500 | oldest first |
| `GET /api/messages/phone/{p}/contact/{c}` | 200 / 500 | oldest first |
| `GET /api/messages/phone/{phone_id}` | 500 / 1000 | **newest first** |

Note the third orders the other way round.

Two details worth knowing:

- `GET /api/messages/contact/{id}` takes a **`phone_number`** parameter, used to
  tell bot messages from user messages **when `direction` is missing** on the
  stored row. Omit it and old rows may render on the wrong side.
- `GET /api/messages/phone/{p}/contact/{c}` **falls back to the contact's
  messages that have no `phone_id`**, so pre-migration rows still appear.

### `GET /api/messages/media/{phone_id}/{message_id}`

Streams the image, audio or file, **keeping the agent address hidden** from the
browser.

---

## Scenarios

All under `/api/phones/{phone_id}/scenarios/`.

| Endpoint | Does |
|---|---|
| `GET /` | the phone's scenarios, newest first, paged |
| `POST /` | create — **draft by default** |
| `GET /by-type/{event_type}` | **active** scenarios of type `trigger` or `scheduler` |
| `GET /{scenario_id}` | one scenario, **config fields expanded** |
| `PUT /{scenario_id}` | update — config is **merged**, only sent fields change |
| `DELETE /{scenario_id}` | delete |
| `POST /{scenario_id}/publish` | validate, compile, activate |

Page size comes from `bot_config` key `scenarios.paging` — it isn't a query
parameter.

### Publish

> Validates components, scheduler templates and Deno code, compiles on the
> Worker, then sets status to active. Returns **422 with issues** when a check
> fails.

That's the three-check sequence from [Chapter 05](05-scenarios.md), and note
that a failed publish comes back as a 422 carrying the issue list, not a plain
error.

### The designer fields

`ScenarioCreate` shows how the designer maps onto storage. Only `name` is
required. Everything visual lives **inside `config`**:

| Field | Stored as |
|---|---|
| `canvas` | `config.canvas` — the components |
| `arrow_data` | `config.arrow_data` — the connections |
| `interval` | delay between steps, e.g. `{ mins, secs }` |
| `estimated_time` | `config.estimated_time` |
| `use_auto_calc` | calculate the estimate automatically (default `true`) |
| `description` | `config.description` |
| `bot_contact` | `config.bot_contact` |
| `event_type` | `trigger` or `scheduler` (default `scheduler`) |
| `priority` | match priority when several scenarios match (default **15**) |

`event_type` is defined here precisely: **trigger** starts on an incoming
message, **scheduler** is started by a schedule.

---

## Schedules

| Endpoint | Does |
|---|---|
| `GET /api/schedules/paged` | **what the grid uses** — `{ schedules, total, page, page_size }` |
| `GET /api/schedules/` | legacy flat list with scenario name, last call status, running flag |
| `POST /api/schedules/` | create |
| `GET /api/schedules/{id}` | one schedule |
| `PUT /api/schedules/{id}` | update |
| `DELETE /api/schedules/{id}` | delete |
| `POST /api/schedules/{id}/run` | run now |
| `GET /api/schedules/{id}/calls` | the calls this schedule fired, paged |
| `GET /api/schedules/calls/{call_id}/events` | the Spine events of a call |

The spec labels the flat list **legacy** and points at `/paged`. Both are
registered twice — with and without the trailing slash — so `/api/schedules` and
`/api/schedules/` are the same endpoint listed twice in the Explorer.

### Create

```json
{
  "schedule_type": "cron",          // required: "once" or "cron"
  "phone_id": "…",
  "scenario_id": "…",               // must belong to phone_id
  "schedule_name": "Nightly check",
  "status": "active",               // or "paused"
  "run_at": "2026-09-20T20:30:00Z", // for "once"
  "cron_expr": "30 20 * * 0,3"      // for "cron" — Linux cron
}
```

**`contact_id` is taken from the scenario** and overwritten whenever
`scenario_id` is set — you do not choose the contact on the schedule. That's a
correction worth noting against [Chapter 09](09-schedules.md): it's three
choices, not four.

`status` accepts only `active` or `paused`. **`firing`, `completed` and `error`
are set by the Scheduler**, not by you.

On update, `next_run` is **recomputed only when the timing really changes**, so
renaming a schedule doesn't shift when it next fires.

### Run now

> Queues the schedule by setting `next_run=now` and `status=active`; the
> Scheduler fires it on its next tick. Returns **409 while the schedule is
> firing**.

This is the mechanism behind "it starts within moments rather than instantly" —
the endpoint queues, the Scheduler fires. A 409 means it's already going.

---

## Templates

All under `/api/phones/{phone_id}/templates/`.

| Endpoint | Does |
|---|---|
| `GET /` | paged, filters: `status`, `lang`, `q` (searches the name) |
| `POST /` | create |
| `GET /published` | approved **and** published, by name — feeds the scenario Input step |
| `GET /{id}` | one template with its parameter map and preview |
| `PUT /{id}` | update — **409 if published** |
| `DELETE /{id}` | delete — **409 if published** |
| `POST /{id}/validate` | returns `{ ok, issues }`, changes nothing |
| `PATCH /{id}/status` | set `pending`, `approved`, `rejected` or `pause` |
| `POST /{id}/publish` | publish an approved template that validates |
| `POST /{id}/unpublish` | mark as not published |
| `POST /{id}/approve-publish` | both at once |
| `POST /{id}/test-send` | send it to a number |

### How a template actually becomes usable

`POST /` **always inserts a draft**: `status: pending`, `is_published: false`.
It then registers the template with the Manager, which forwards it to the
phone's container. The comment in the source is explicit — *"always enters as a
draft; the Manager is what decides `status` and `provider_template_id`."*

Approval arrives **out of band**. HostAgent runs a sync pass every ~120 seconds
that reads each pending template's status from the container and, on approval,
sets `is_published: true` as well. So:

```
POST /            → pending,  unpublished
  …~2 minutes…
sync pass         → approved, published
```

Nothing you call makes that happen sooner. `POST /{id}/publish` and
`POST /{id}/approve-publish` both **require `status == "approved"` already** and
return 422 otherwise — neither one approves anything. They exist for the case
where sync has set approved but publishing was cleared afterwards.

If registration with the Manager fails, the draft stays with no
`provider_template_id`. It is **repaired automatically** by the import pass
within ~15 minutes, matched on name + lang. Creating it again is not necessary
and produces a duplicate.

### Rules that will catch you

- **A published template is locked.** `PUT` and `DELETE` both return 409.
  Unpublish first.
- **Editing content reverts approval.** Changing `content` sends an approved or
  rejected template **back to `pending`**.
- **Any status other than `approved` also unpublishes.**
- **Names are constrained**: `^[a-z0-9_]{1,120}$`. Names are lower-cased on
  write, but a name with a space or a hyphen is rejected outright.
- **Name + lang is the identity.** That pair, not the id, is what matches a
  local row to the provider's copy. Renaming a registered template breaks the
  match and the next import creates a second row.
- `category` is `UTILITY`, `MARKETING` or `AUTHENTICATION` (default `UTILITY`).
- `lang` defaults to the phone's language, then the user's.
- **`DELETE` goes through the Manager** when the template has a
  `provider_template_id`, and returns `{ ok, provider_deleted }` saying which
  path it took. A draft that never registered is deleted locally; a Manager 404
  also falls back to a local delete.

### Where a phone's templates come from

Only one template is created by the platform: **`check_contact`**, seeded when
the phone is provisioned. Everything else is **imported** from the provider's
catalog by HostAgent — five standard samples (`hello_world`,
`sample_issue_resolution`, `sample_shipping_confirmation`,
`sample_movie_ticket_confirmation`, and `sample_purchase_feedback`, which
arrives rejected).

So `GET /` on a phone provisioned a minute ago returns one row, and the same
call a quarter of an hour later returns six. Nothing was created in between.

### Content and examples

```json
{
  "name": "appointment_reminder",
  "category": "UTILITY",
  "lang": "en_US",
  "content":  { "header": …, "body": …, "footer": …, "buttons": … },
  "examples": { "header": […], "body": […], "header_media_url": "…" }
}
```

Parameters are numbered **per part** — `{{1}}`, `{{2}}` restart in the header
and in the body. `examples` supplies one example per parameter.

### Test-send

```json
{
  "to": "972500000000",                       // number or full JID
  "params": { "header": ["…"], "body": ["…"] }
}
```

It works **even before the template is published**, and **missing parameters are
filled from the template's examples** — so you can test with `params` omitted
entirely.

The template must still be `approved`; a 409 comes back otherwise. The flag
sent downstream waives the `is_published` check **and nothing else**.

`to` accepts a bare number or a full JID. A bare number is converted by length:
14 digits or more is treated as a LID (`@lid`), shorter as an ordinary number
(`@s.whatsapp.net`). Getting that wrong is the one failure worth knowing about
— **WhatsApp accepts a LID with the wrong suffix and then silently drops the
message**, with no delivery status, so the send looks fine and nothing
arrives.

---

## Notifications

| Endpoint | Does |
|---|---|
| `GET /api/notifications/` | newest first; `limit` (50), `offset`, `unread_only` |
| `GET /api/notifications/unread-count` | `{ count }` — what the bell shows |
| `POST /api/notifications/` | create an unread notification |
| `POST /api/notifications/mark-read` | mark ids read — **empty list marks everything** |
| `DELETE /api/notifications/{id}` | delete — returns `{ ok: true }` even for an unknown id |

`NotificationCreate` requires `user_id`, `title` and `message`, and takes
`phone_id`, `log_level` (`info`, `success`, `warning`, `error` — default
`info`), `is_send`, `source` and a free-form `extra` object.

The empty-`ids` behaviour on `mark-read` is the "mark all as read" button.

---

## System

| Endpoint | Tells you |
|---|---|
| `GET /` | the service answers |
| `GET /health` | the backend is up — **no token needed** |
| `GET /whoami` | your token is valid, and whose it is |

These three are **not** under `/api`.

---

## Quick diagnostics

| Question | Call |
|---|---|
| Is the backend up? | `GET /health` |
| Is my login valid? | `GET /whoami` |
| Is the phone really connected? | `GET /api/phones/{id}/qrcode` |
| Is this contact really linked? | `GET /api/phones/{id}/contacts/active` |
| Why won't this scenario publish? | `POST /…/scenarios/{id}/publish` — read the 422 issues |
| Why won't this template publish? | `POST /…/templates/{id}/validate` |
| Did the schedule fire? | `GET /api/schedules/{id}/calls` |
| Is my token what I think it is? | `GET /api/auth/me` |
| Why won't the handshake start? | `POST /api/phones/{id}/templates/test` *(internal)* |
| What happened inside that call? | `GET /api/schedules/calls/{call_id}/events` |

---

**Back to:** [chapter index](README.md)
