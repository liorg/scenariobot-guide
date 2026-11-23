# ScenarioBot User Guide

**ScenarioBot** is the product; **Grossman.bot** is the company and brand behind
it. [Chapter 01](01-what-it-does.md) sets out the distinction.

Written for end users, and structured so a chat assistant can answer from a
single chapter without needing the rest.

**Every chapter opens with a "How to get there" line and the screen's URL.** If
someone asks "where do I do X", those two lines are the answer — one to click
through, one to open directly. Where the screen doesn't depend on a particular
phone or bot (agent), the URL is a live link you can follow from here.

## Chapters

| # | Chapter | Answers |
|---|---|---|
| 01 | [What ScenarioBot does](01-what-it-does.md) | what the product is, the six things you work with |
| 02 | [Signing in](02-signing-in.md) | login, password reset, new accounts |
| 03 | [Connecting a phone](03-phones.md) | the phone list, the add-phone wizard, reconnecting |
| 04 | [Adding a bot (agent)](04-contacts.md) | the PING/PONG handshake and why it exists |
| 05 | [Building a scenario](05-scenarios.md) | the scenarios tab, the designer, saving and publishing |
| 06 | [Scenario components](06-components.md) | every step type, matching, failure handling, custom code, `{{ }}` |
| 07 | [Playback](07-playback.md) | reading a scenario as a chat before it runs |
| 08 | [Templates](08-templates.md) | WhatsApp approved templates |
| 09 | [Schedules](09-schedules.md) | running a scenario on a timer |
| 10 | [Watching a call run](10-watching-a-call.md) | the live panel |
| 11 | [Reading a finished call](11-reading-a-call.md) | history, flow diagram, events |
| 12 | [The chat view](12-chat-view.md) | plain WhatsApp conversation with a bot (agent) |
| 13 | [Parallel executions](13-executions.md) | copying one scenario onto many phones, the wizard, running them |
| 14 | [Settings and account](14-settings.md) | the three settings tabs, two-step verification, email notifications |
| 15 | [Tips for a reliable setup](15-tips.md) | clean phone, keeping it online, support contacts |
| 16 | [Troubleshooting](16-troubleshooting.md) | symptom → cause → fix |
| 17 | [Glossary](17-glossary.md) | one-line definitions |
| 18 | [API Explorer](18-api-explorer.md) | the built-in API console (developers and support) |
| 19 | [API reference](19-api-reference.md) | every endpoint the API offers, and what it's for |
| 20 | [Renting a phone](20-rented-phones.md) | the pool of real phones with SIMs — renting, the clock, what the wipe deletes |
| 21 | [SMS on a rented phone](21-sms.md) | text messages arriving on a rented SIM |
| 22 | [Languages and countries](22-languages.md) | the language menu, your four languages, dial codes, mother tongue |
| 23 | [When someone asks to stop](23-unwanted.md) | STOP, the unsubscribe link, and what ⛔ Unwanted means |
| 24 | [Mail](24-mail.md) | every phone's email address, the Mail tab, pulling a code out of an email |

## Every screen has an address

The product is a single web app, but **each screen has its own URL**. That means:

- **The back and forward buttons work** the way you expect.
- **Any screen can be bookmarked**, including a specific bot (agent), a specific
  scenario or one finished call.
- **A URL can be shared.** Sending a colleague the link to a failed call opens
  that call for them — provided they have access to that phone.
- **Refreshing keeps you where you are**, instead of dropping you back to the
  phone list.

### The map

```
/                                     landing / sign in
/phones                               the phone list — the default screen
/phones/new                           add-phone wizard
/phones/<phone>/reconnect             reconnect an existing number

/phones/<phone>/calls                 📞 Calls tab — conversation list
/phones/<phone>/calls/<contact>       one conversation
/phones/<phone>/contacts              👥 Contacts tab
/phones/<phone>/contacts/new          contact wizard — new contact
/phones/<phone>/contacts/<c>/wizard   contact wizard — finish an existing one
/phones/<phone>/contacts/<c>/edit     edit a contact
/phones/<phone>/contacts/<c>/chat     the full conversation
/phones/<phone>/contacts/<c>/calls    that contact's scenario calls
/phones/<phone>/contacts/<c>/calls/<call>   one call — flow diagram and events
/phones/<phone>/scenarios             🤖 Scenarios tab
/phones/<phone>/scenarios/<s>/design  the designer
/phones/<phone>/scenarios/<s>/playback  playback

/phones/templates                     Templates tab
/phones/templates/<phone>             one phone's templates
/phones/templates/<phone>/new         create a template
/phones/templates/<phone>/<t>/edit    edit one
/phones/templates/<phone>/<t>/test    test-send one

/scheduling                           schedules
/scheduling/new                       create a schedule
/scheduling/<schedule>                one schedule and its calls

/executions                           parallel runs
/executions/new                       create — the four-step wizard
/executions/<execution>/run           run confirmation
/api                                  the API console
/rent                                 rented phones — the pool
/phones/<phone>/sms                   SMS on a rented phone
/settings                             account settings — opens the personal tab
/settings/personal                    name, email, avatar, language
/settings/2fa                         two-step verification
/settings/advanced                    trusted domain, email notifications
/guide/<chapter>                      jumps to this guide
/privacy                              privacy policy
```

All of these sit under **https://grossman.bot** — so the phone list in full is
<https://grossman.bot/phones>.

`<phone>`, `<contact>`, `<scenario>`, `<call>`, `<t>` and `<schedule>` are the
internal ids. You never need to type one — they appear in the address bar as
you click, and that is what makes a screen linkable. An address containing one
of these can be copied out of the address bar and shared, but not typed from
scratch.

An address that doesn't exist sends you back to the phone list rather than
showing an error.

### Quick links worth keeping

| Bookmark | Goes to |
|---|---|
| [grossman.bot/phones](https://grossman.bot/phones) | the home screen |
| [grossman.bot/phones/new](https://grossman.bot/phones/new) | add a phone |
| [grossman.bot/phones/templates](https://grossman.bot/phones/templates) | templates |
| [grossman.bot/scheduling](https://grossman.bot/scheduling) | your schedules |
| [grossman.bot/executions](https://grossman.bot/executions) | parallel runs |
| [grossman.bot/api](https://grossman.bot/api) | the API console |
| [grossman.bot/rent](https://grossman.bot/rent) | rent a phone with a SIM |
| [grossman.bot/settings](https://grossman.bot/settings) | your profile |
| [grossman.bot/settings/2fa](https://grossman.bot/settings/2fa) | verify your mobile number |
| [grossman.bot/guide/16-troubleshooting](https://grossman.bot/guide/16-troubleshooting) | this guide's troubleshooting chapter |

The last one is worth noting: **`grossman.bot/guide/<chapter>` opens this
guide**, so any chapter can be linked from inside the product or from a
message — for example
[grossman.bot/guide/08-templates](https://grossman.bot/guide/08-templates).
Signed in, it opens the Help dialog on that chapter; signed out, it goes
straight to the guide site.

**The guide itself lives at
<https://liorg.github.io/scenariobot-guide>**, one page per chapter —
[.../08-templates.html](https://liorg.github.io/scenariobot-guide/08-templates.html).
That is the address to use when linking the guide from outside the product.
Inside it, **❓ Help** in the avatar menu shows the same pages in a dialog
([Chapter 14](14-settings.md)).

The **designer** and **playback** still open as full-screen views over the
screen beneath, and closing one returns you where you were — but they now have
their own addresses too, so a scenario you are working on can be bookmarked
mid-edit.

The back arrow (top-left of any inner screen) always goes up one level, and
matches the browser's own back button.

## Machine-readable index

Two JSON files carry the whole guide as data, for a chat assistant that has to
answer "where do I do X" without reading every chapter:

| File | One entry per | Holds |
|---|---|---|
| `index.json` | chapter | title, URL, screens, keywords, section headings, related chapters, 2FA gate |
| `img/index.json` | screen element | every `id` in every diagram, what it is, which chapter it belongs to |

`index.json` opens with `language: "en"` and a `language_note`. **The guide is
English; the product is not.** A reader may be looking at the interface in
Hebrew, Arabic, Russian, German or Polish, so an assistant answering from these
files should reply in the reader's language even though the source is English.

`index.json` is generated — run `python3 guide/_build_index.py` after editing
any chapter's frontmatter or headings. It fails loudly if a chapter points at a
screen that isn't filed under it, or at a `related:` chapter that doesn't exist.

### Chapter frontmatter

Every chapter opens with a YAML block:

```yaml
---
id: 09-schedules
title: Scheduling scenarios
screen: screen-schedules
url: /scheduling
two_fa: run-blocked
keywords:
  - schedule
  - cron
  - run now
related:
  - 13-executions
---
```

| Key | |
|---|---|
| `id` | the filename without `.md` — chapters reference each other by this |
| `title` | a descriptive title for search; the `#` heading in the body stays as it is |
| `screen` | the diagram in `img/`, **or a list** when the chapter has two |
| `url` | the screen's path, `<phone>`-style placeholders included; omitted where the chapter isn't one screen |
| `two_fa` | only on gated chapters — `tab-hidden` (the tab isn't there until the mobile number is verified), `run-blocked` (visible, but the run is refused), `add-phone-gated` |
| `keywords` | what someone would actually type, including words the screen doesn't use |
| `related` | chapter ids, nearest first |
| `actions` | things a user can be shown on a screen — see below |

### Actions

An action is one thing a user can be *shown*, rather than told:

```yaml
actions:
  - id: disconnect-phone
    description: Show where to disconnect a phone
    screen: screen-phone-card
    target: btn-disconnect
    type: navigate-highlight
```

| Key | |
|---|---|
| `id` | unique across the whole guide, verb first |
| `description` | what the user asked for, in their words — this is what gets matched |
| `screen` | a diagram in `img/` |
| `target` | an element `id` in that diagram, checked against `img/index.json` |
| `type` | `navigate-highlight` — open the screen's URL, then point at the element. `highlight` — the screen's URL contains ids that can't be typed, so the user has to already be on it |

`index.json` resolves every action into one flat record under `actions`, with
the URL to open, the element to highlight, that element's own description and
the chapter to read for the rest:

```json
"disconnect-phone": {
  "description": "Show where to disconnect a phone",
  "chapter": "03-phones", "screen": "screen-phone-card",
  "target": "btn-disconnect", "type": "navigate-highlight",
  "url": "/phones", "element": "Disconnect — asks first"
}
```

An action's `screen` doesn't have to be the chapter's own — Troubleshooting
points at five different screens.

If the site build doesn't strip YAML frontmatter, it will print at the top of
the page — check one rendered chapter after the first publish.

## Conventions in this guide

- **Bold** with arrows is a click path: **Phones → a phone → 👥 Bots (Agents)**.
- **`URL:`** under it is the same screen's address. It is a **live link** when
  the screen doesn't depend on a particular record, and plain text containing
  `<phone>`, `<contact>` or similar when it does.
- Tab names include their icon, because that's how they appear on screen.
- Where a term has a precise meaning, it's in [the glossary](17-glossary.md).
