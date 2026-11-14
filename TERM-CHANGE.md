# contact -> bot (agent) — guide + diagrams

The whole `guide/` folder, so nothing is missed. 208 replacements across 20
chapters, 13 in the diagram generator.

## What changed

- **Prose, headings, link text, chapter titles, action descriptions** — the
  entity is a **bot (agent)** now. Chapter 4 is "Adding a bot (agent)".
- **5 diagrams** carry the new labels: `screen-contacts` (title, count,
  "+ Add Bot (Agent)"), `screen-phone-detail` (the 👥 tab), `screen-calls-list`,
  `screen-executions` (subtitle + column header), `screen-scenarios` (callout).
  They were regenerated from `img/_generate_screens.py`, not hand-edited.
- **`img/index.json`** — 6 element descriptions.
- **`index.json`** — rebuilt. 207 keywords now (was 195).

## What deliberately did NOT change

- **Every file name and anchor.** `04-contacts.md` keeps its name, so the
  HelpModal slug `04-contacts` and every `](04-contacts.md)` link still work.
- **Every URL** — `/phones/<phone>/contacts`, `<contact>`.
- **Every API path, field and tag** — `/api/contacts`, `contact_id`,
  `check_contact`, `bot_contact`, `payload.target_contact`, the `contacts`
  OpenAPI group. Chapter 19 now opens its section with a note saying so.
- **Every element id in the SVGs** — `ct-add`, `sc-0-contact`, `cl-*`. The ids
  are the contract with `index.json`; renaming them would break every action.
- **Action ids** — `add-contact`, `edit-contact`, `diagnose-contact-handshake`.
- **The old keywords.** `add contact`, `contact wizard`, `activate contact`
  stay in the frontmatter *and* bot/agent terms were added, so a search for
  either word finds the chapter.
- **"first contact"** (cold outreach) and **"support contacts"** — different
  sense of the word.

## New

- Chapter 4 opens with a one-line note that these used to be called contacts
  and that the URL and API still say `contact`.
- The glossary had two entries collide on the new name; it now has
  **Bot (agent)** (the entity) and **Bot (agent) setting** (the scenario's
  `bot_contact`), in alphabetical order.

## Verified

- `_build_index.py` passes — it caught 5 action `screen:` values that a bad
  mask had rewritten to `screen-bots (agents)`; fixed.
- no broken links or images anywhere in `guide/`
- every id in `img/index.json` exists in its `.svg`
- the 5 changed diagrams render without overflow
