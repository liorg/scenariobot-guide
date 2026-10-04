# ScenarioBot User Guide

**ScenarioBot** is the product; **Grossman.bot** is the company and brand behind
it. [Chapter 01](01-what-it-does.md) sets out the distinction.

Written for end users, and structured so a chat assistant can answer from a
single chapter without needing the rest.

**Every chapter opens with a "How to get there" line and the screen's URL.** If
someone asks "where do I do X", those two lines are the answer — one to click
through, one to open directly. Where the screen doesn't depend on a particular
phone or contact, the URL is a live link you can follow from here.

## Chapters

| # | Chapter | Answers |
|---|---|---|
| 01 | [What ScenarioBot does](01-what-it-does.md) | what the product is, the six things you work with |
| 02 | [Signing in](02-signing-in.md) | login, password reset, new accounts |
| 03 | [Connecting a phone](03-phones.md) | the phone list, the add-phone wizard, reconnecting |
| 04 | [Adding a contact](04-contacts.md) | the PING/PONG handshake and why it exists |
| 05 | [Building a scenario](05-scenarios.md) | the scenarios tab, the designer, saving and publishing |
| 06 | [Scenario components](06-components.md) | every step type, matching, failure handling, custom code, `{{ }}` |
| 07 | [Playback](07-playback.md) | reading a scenario as a chat before it runs |
| 08 | [Templates](08-templates.md) | WhatsApp approved templates |
| 09 | [Schedules](09-schedules.md) | running a scenario on a timer |
| 10 | [Watching a call run](10-watching-a-call.md) | the live panel |
| 11 | [Reading a finished call](11-reading-a-call.md) | history, flow diagram, events |
| 12 | [The chat view](12-chat-view.md) | plain WhatsApp conversation with a contact |
| 13 | [Parallel executions](13-executions.md) | running against many phones at once |
| 14 | [Settings and account](14-settings.md) | profile, language, notifications, logout |
| 15 | [Tips for a reliable setup](15-tips.md) | clean phone, keeping it online, support contacts |
| 16 | [Troubleshooting](16-troubleshooting.md) | symptom → cause → fix |
| 17 | [Glossary](17-glossary.md) | one-line definitions |
| 18 | [API Explorer](18-api-explorer.md) | the built-in API console (developers and support) |
| 19 | [API reference](19-api-reference.md) | every endpoint the API offers, and what it's for |

## Every screen has an address

The product is a single web app, but **each screen has its own URL**. That means:

- **The back and forward buttons work** the way you expect.
- **Any screen can be bookmarked**, including a specific contact, a specific
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
/api                                  the API console
/settings                             account settings
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
| [grossman.bot/settings](https://grossman.bot/settings) | your profile |
| [grossman.bot/guide/16-troubleshooting](https://grossman.bot/guide/16-troubleshooting) | this guide's troubleshooting chapter |

The last one is worth noting: **`grossman.bot/guide/<chapter>` opens this
guide**, so any chapter can be linked from inside the product or from a
message. The chapter name is the file name without its number — for example
[grossman.bot/guide/08-templates](https://grossman.bot/guide/08-templates).

The **designer** and **playback** still open as full-screen views over the
screen beneath, and closing one returns you where you were — but they now have
their own addresses too, so a scenario you are working on can be bookmarked
mid-edit.

The back arrow (top-left of any inner screen) always goes up one level, and
matches the browser's own back button.

## Conventions in this guide

- **Bold** with arrows is a click path: **Phones → a phone → 👥 Contacts**.
- **`URL:`** under it is the same screen's address. It is a **live link** when
  the screen doesn't depend on a particular record, and plain text containing
  `<phone>`, `<contact>` or similar when it does.
- Tab names include their icon, because that's how they appear on screen.
- Where a term has a precise meaning, it's in [the glossary](17-glossary.md).
