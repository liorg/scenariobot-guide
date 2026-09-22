# 05. Building a scenario

**How to get there:** **Top bar → Phones → click a phone → 🤖 Scenarios tab**.
Create a new one, or click an existing one to open the designer.

The designer opens **full screen** and covers everything. Closing it returns you
to the scenarios tab.

## The three columns

```
EXPECT  |  CANVAS  |  SEND
```

- **CANVAS** in the middle is the conversation, top to bottom.
- **EXPECT** is what the **bot sends and then waits on**.
- **SEND** is what the **reply side supplies**.

That naming reads backwards to most people the first time. The full explanation
and every step type is in [Chapter 06](06-components.md).

A conversation alternates **EXPECT → SEND → EXPECT → SEND** down the canvas.

Drag components onto the canvas and connect them. Works with a mouse and with
touch on a tablet.

## While you work

| Action | How |
|---|---|
| Save | **Ctrl/Cmd + S**, or the save button |
| Undo | **Ctrl/Cmd + Z** — up to 50 steps |
| Redo | **Ctrl/Cmd + Y** or **Ctrl/Cmd + Shift + Z** |
| Duplicate a step | the duplicate action on the step |
| Reorder | drag, or the up/down arrows |
| Export / import | buttons on the ribbon — raw JSON |

An **errors panel** flags problems as you go and pops open by itself whenever
new issues are found.

The two side columns can be **resized, pinned and collapsed**, and your layout
choice is remembered between sessions.

## Scenario settings

The **⚙️ settings** button on the ribbon holds everything that applies to the
whole scenario rather than one step:

- description
- **bot contact** — which contact identity the bot presents as
- interval between messages
- estimated duration — set by hand, or calculated automatically
- event type — **scheduler** (started by a schedule) or **trigger** (starts on
  an incoming message)
- priority (default 15) — which scenario wins when several could match

## Saving vs publishing

**Save** keeps it as a draft. A draft can be edited freely and will not run.

**Publish** makes it runnable. Publishing runs three checks first, and is
blocked until all pass:

1. components and their required fields
2. the templates used by scheduler steps
3. custom code compiles — the scenario is compiled on the Worker

When a check fails you get the **list of issues back**, not just a refusal, and
the errors panel shows them. Only after all three pass does the scenario become
active.

Once published, **the save button is disabled** and shows "published". To edit
again, unpublish first.

## Testing before it goes out

- **Playback** reads the scenario back as a chat window →
  [Chapter 07](07-playback.md)
- **Check code** validates a custom-code step against a sandbox →
  [Chapter 06](06-components.md#custom-code-steps)

A real send still needs a real linked contact.

---

**Next:** [Scenario components](06-components.md)
