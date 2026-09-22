# 01. What ScenarioBot does

**How to get there:** this is background — nothing to open.

## Brand structure

Two names appear throughout the product, and they are not interchangeable.

**Grossman.bot** — the company and the main brand identity. It represents the
broader technology, the vision, and the future product ecosystem.

**ScenarioBot** — the core product built by Grossman.bot. A platform for
designing, testing, automating and monitoring WhatsApp conversational
scenarios.

So: Grossman.bot is who makes it, ScenarioBot is what you use. The web address
is `grossman.bot`, the product you are signed into is ScenarioBot, and more
products may sit under the same brand later.

> **ScenarioBot by Grossman.bot**
> Design. Test. Automate.

### The story behind the logo

The logo draws on the work of **Frank Rosenblatt**, who built the Perceptron in
the late 1950s — one of the earliest models of an artificial neural network.

The geometric shapes — **triangle, circle, square** — stand for simple inputs
and patterns. On their own they are basic forms. Together they carry the idea
underneath artificial intelligence: recognising patterns, learning from
information, and turning inputs into meaningful decisions.

That is what the platform does. ScenarioBot takes messages, scenarios, data and
user interactions, and turns them into intelligent, automated workflows.

The visual language therefore ties the origins of machine learning to a modern
AI and automation platform.

## What ScenarioBot does

ScenarioBot runs scripted WhatsApp conversations for you.

You connect a WhatsApp number, draw a conversation as a flow — what the bot
sends, what it expects back, what to do when the answer isn't what you expected
— and then either run it on demand or put it on a schedule. Every run is
recorded, so you can open any past conversation and see exactly which step sent
what, what came back, and where it went wrong.

Typical uses: appointment reminders that confirm or reschedule, recurring
check-ins, intake questionnaires, and monitoring that another WhatsApp bot still
answers correctly.

The interface is available in English, Hebrew, Russian and Arabic, and flips to
right-to-left for Hebrew and Arabic.

## The six things you work with

**Phone** — a WhatsApp number you've connected. Each one runs in isolation, has
its own contacts and its own scenarios. A phone is either active or
disconnected. → [Chapter 03](03-phones.md)

**Contact** — someone that phone can talk to. Not just a number typed into a
box; a contact has to be verified through a handshake before anything will run
against it. → [Chapter 04](04-contacts.md)

**Scenario** — the conversation script. Built visually, saved as a draft, then
published when it's ready to run. → [Chapter 05](05-scenarios.md)

**Call** — one execution of one scenario against one contact. This is the unit
you look at afterwards. **A contact can only have one call running at a time.**
→ [Chapter 11](11-reading-a-call.md)

**Schedule** — a rule that fires a scenario at chosen times.
→ [Chapter 09](09-schedules.md)

**Template** — a pre-approved WhatsApp message format with `{{1}}`-style
placeholders. Managed separately, and the only way to open a conversation
outside WhatsApp's 24-hour window. → [Chapter 08](08-templates.md)

## How they fit together

```
Phone ──┬── has many Contacts ──── has many Calls
        └── has many Scenarios ─── run against a Contact = a Call
                                    ▲
                          Schedule ─┘  (fires it on a timer)
```

A call always needs three things: **a phone, a scenario, and a contact.** If any
one of them is missing or not ready, nothing runs.
