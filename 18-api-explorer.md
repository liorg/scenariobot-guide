# 18. API Explorer

**How to get there:** **Top bar → API** (it may sit beside Executions
depending on your build).

## What it is

A built-in console for the ScenarioBot API — the same idea as Swagger UI, inside
the product. It lists every endpoint the backend offers, lets you fill in the
values, and sends a **real request** signed with your own login.

It's aimed at developers and at support: when something looks wrong in the
interface, this is where you check what the server actually returns.

## The screen

**Left** — every endpoint, grouped by area, with a search box at the top. The
current groups are **phones**, **contacts**, **messages**, and a small untagged
group with `/`, `/health` and `/whoami`.

Each entry shows its method as a coloured pill:

| Pill | Meaning |
|---|---|
| **GET** (blue) | read something |
| **POST** (green) | create or perform an action |
| **PATCH** (purple) | change part of something |
| **DELETE** (red) | remove something |

**Right** — the endpoint you picked, with up to four sections: path parameters,
query parameters, request body, and the response.

**Everything is documented in place.** Each endpoint shows what it does, each
parameter shows what it's for, and the fields of a request body are listed
underneath the editor with their type, whether they're required, and their
default. A red **\*** marks a required field.

The search box searches those descriptions too — typing `cron` finds the
schedule endpoints even though the word isn't in their paths.

**Top right** — a badge showing whether you're signed in. Green with a token
fragment means requests will be authorised; red means they won't.

## Sending a request

1. Pick an endpoint on the left.
2. Fill in **path parameters** — the `{phone_id}` style values. All of them are
   required; the screen won't send until each has a value.
3. Adjust **query parameters** if you want. They're pre-filled with the server's
   own defaults, and anything left blank is simply not sent.
4. For POST and PATCH, the **body** is pre-filled with a skeleton of the right
   shape. Fill in what you need and delete what you don't.
5. **Send.**

The response shows the **status code**, whether it succeeded, **how long it
took**, and the body — pretty-printed when it's JSON, raw otherwise.

## Reading the result

| What you see | Meaning |
|---|---|
| **200** | worked |
| **422** | your input didn't validate — the body says which field |
| **401 / 403** | not signed in, or not allowed |
| **404** | no such record |
| **500** | the server failed — worth reporting |
| **status 0** | the request never reached the server at all |

**Status 0 is the odd one.** It isn't an HTTP code; it means the browser
couldn't make the call — usually a network problem or a CORS restriction. The
panel adds a hint when this happens.

## Copy as curl

The **copy curl** button puts the equivalent command-line request on your
clipboard, ready to paste into a terminal.

⚠️ **The command contains your login token in full.** It has to, or it wouldn't
work — but that means a curl pasted into a ticket, an email or a group chat
hands over your session. Strip the `Authorization` line before sharing one.

## Careful

**These are real requests against real data.** There's no sandbox and no
dry-run. `DELETE /api/phones/{phone_id}` on this screen deletes the phone, with
no confirmation dialog.

Read-only exploring is safe: stick to **GET**, and to `/health` and `/whoami`
when you just want to check the connection.

## Useful first calls

| Endpoint | Tells you |
|---|---|
| `GET /health` | the backend is up |
| `GET /whoami` | your token is valid and which account it belongs to |
| `GET /api/phones/` | every phone on your account, with its real stored state |
| `GET /api/contacts?phone_id=…` | whether a contact really is linked |

That third one is the quickest way to settle "the interface says disconnected
but the phone looks fine" — it shows what the database actually holds.

---

**Next:** [API reference](19-api-reference.md) — what each endpoint does
