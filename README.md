# ScenarioBot User Guide

**ScenarioBot** is the product; **Grossman.bot** is the company and brand behind
it. [Chapter 01](01-what-it-does.md) sets out the distinction.

Written for end users, and structured so a chat assistant can answer from a
single chapter without needing the rest.

**Every chapter opens with a "How to get there" line** giving the exact click
path from the top bar. If someone asks "where do I do X", that line is the
answer.

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

## Navigation map

Everything in the product hangs off one top bar with three buttons.

```
Sign in
  │
  └── Top bar:  [ Phones ]  [ Schedules ]  [ Executions ]     🔔  ⚙️  Logout
        │
        ├── Phones  ........................... the default screen
        │     ├── + Add Phone → phone wizard (3 steps)
        │     └── click a phone card → Phone Detail
        │           ├── 📞 Calls tab ......... chat view + call history
        │           │     └── click a contact → that contact's calls
        │           │           └── click a call → flow diagram + events
        │           ├── 👥 Contacts tab ...... contact list + contact wizard
        │           └── 🤖 Scenarios tab ..... scenario list
        │                 ├── open a scenario → Designer (full screen)
        │                 └── playback → Playback chat (full screen)
        │
        ├── Schedules ......................... schedule list + per-schedule log
        ├── Executions ........................ parallel runs
        └── API ............................... built-in API console

  🔔  notifications        ⚙️  settings (full page)
  footer → privacy policy
```

Two things are **full-screen overlays**, not tabs: the **Designer** and
**Playback**. They cover the whole window and return you exactly where you were
when you close them.

The back arrow (top-left of any inner screen) always goes up one level. There
are no browser-style URLs to bookmark for inner screens.

## Conventions in this guide

- **Bold** with arrows is a click path: **Phones → a phone → 👥 Contacts**.
- Tab names include their icon, because that's how they appear on screen.
- Where a term has a precise meaning, it's in [the glossary](17-glossary.md).
