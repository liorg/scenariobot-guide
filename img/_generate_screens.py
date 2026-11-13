"""Screen diagrams, part 2. Colours are src/theme.js; labels are src/i18n/en.js."""
import pathlib, html, json

OUT = pathlib.Path(__file__).resolve().parent   # guide/img
OUT.mkdir(parents=True, exist_ok=True)
INDEX = {}

STYLE = """
  <style>
    .bg{fill:#F7F9FC}.panel{fill:#FFFFFF;stroke:#E4EAF4;stroke-width:1.5}
    .sub{fill:#F1F5F9;stroke:#E4EAF4;stroke-width:1}.line{stroke:#E4EAF4}
    .t{font-family:'Segoe UI',Tahoma,sans-serif;fill:#1A2332}
    .t-mut{font-family:'Segoe UI',Tahoma,sans-serif;fill:#8896A7}
    .t-dis{font-family:'Segoe UI',Tahoma,sans-serif;fill:#BCC5D3}
    .b{font-weight:700}.mono{font-family:Consolas,'JetBrains Mono',monospace}
    .cal{fill:#7048E8}
    .cal-t{font-family:'Segoe UI',Tahoma,sans-serif;fill:#FFF;font-weight:700;font-size:11px}
    .dash{stroke:#7048E8;stroke-width:1.2;stroke-dasharray:3 3;fill:none}
    @media (prefers-color-scheme:dark){
      .bg{fill:#0F1420}.panel{fill:#171D2B;stroke:#2A3347}.sub{fill:#1F2738;stroke:#2A3347}
      .line{stroke:#2A3347}.t{fill:#E6EAF2}.t-mut{fill:#7D8899}.t-dis{fill:#4F5A6B}
      .cal{fill:#9775FA}.dash{stroke:#9775FA}
    }
  </style>
"""
C = dict(pri="#3B5BDB", priL="#EEF2FF", ok="#2F9E44", okL="#EBFBEE",
         warn="#E67700", warnL="#FFF9DB", bad="#C92A2A", badL="#FFF5F5",
         wa="#075E54", waBtn="#128C7E", waBg="#ECE5DD", waOut="#DCF8C6")

class Dia:
    def __init__(self, name, w, h, title, chapter, url):
        self.name, self.w, self.h, self.title = name, w, h, title
        self.chapter, self.url = chapter, url
        self.el, self.notes, self.n = [], [], 0
    # ── primitives ───────────────────────────────────────────────────────
    def rect(self, id_, x, y, w, h, cls="panel", rx=8, style=None):
        st = f' style="{style}"' if style else ""
        self.el.append(f'  <rect id="{id_}" x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="{cls}"{st}/>')
    def text(self, id_, x, y, s, size=12, cls="t", anchor="start", style=None):
        st = f' style="{style}"' if style else ""
        self.el.append(f'  <text id="{id_}" x="{x}" y="{y}" font-size="{size}" class="{cls}" '
                       f'text-anchor="{anchor}"{st}>{html.escape(s)}</text>')
    def line(self, x1, y1, x2, y2):
        self.el.append(f'  <line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" class="line"/>')
    def raw(self, s): self.el.append("  " + s)
    def chip(self, id_, x, y, w, label, fg, bg, size=9):
        self.rect(id_, x, y, w, 18, cls="", rx=9, style=f"fill:{bg}")
        self.text(id_ + "-text", x + w/2, y + 13, label, size, "t b", "middle", f"fill:{fg}")
    def btn(self, id_, x, y, w, label, kind="ghost", h=28):
        fill = {"primary": C["pri"], "danger": C["badL"], "ghost": None, "off": "#E4EAF4"}[kind]
        if kind == "ghost":
            self.rect(id_, x, y, w, h, cls="panel", rx=8)
            self.text(id_ + "-label", x + w/2, y + h/2 + 4, label, 11, "t b", "middle")
        else:
            stroke = f";stroke:{C['bad']}33" if kind == "danger" else ""
            self.rect(id_, x, y, w, h, cls="", rx=8, style=f"fill:{fill}{stroke}")
            fg = {"primary": "#FFFFFF", "danger": C["bad"], "off": "#8896A7"}[kind]
            self.text(id_ + "-label", x + w/2, y + h/2 + 4, label, 11, "t b", "middle", f"fill:{fg}")
    def tabs(self, prefix, x, y, items, active=0, w=None):
        cx = x
        for i, lbl in enumerate(items):
            tw = w or max(74, 9 + 7.2 * len(lbl))
            on = i == active
            self.rect(f"{prefix}-{i}", cx, y, tw, 30, cls="" if on else "sub", rx=8,
                      style=f"fill:{C['priL']};stroke:{C['pri']}" if on else None)
            self.text(f"{prefix}-{i}-label", cx + tw/2, y + 19, lbl, 10,
                      "t b" if on else "t-mut", "middle", f"fill:{C['pri']}" if on else None)
            cx += tw + 6
        return cx
    def head(self, prefix, x, y, w, cols, h=30):
        self.rect(f"{prefix}-head", x, y, w, h, cls="sub", rx=0)
        for key, cx, lbl in cols:
            self.text(f"{prefix}-th-{key}", cx, y + h/2 + 4, lbl.upper(), 9, "t-mut b")
    # ── annotation ───────────────────────────────────────────────────────
    def note(self, target_id, desc, x, y, leader=None):
        self.n += 1
        self.el.append(f'  <g id="callout-{self.n}">\n'
                       f'    <circle cx="{x}" cy="{y}" r="11" class="cal"/>\n'
                       f'    <text x="{x}" y="{y+4}" class="cal-t" text-anchor="middle">{self.n}</text>\n'
                       f'  </g>')
        if leader:
            self.el.append(f'  <path class="dash" d="M {leader[0]} {leader[1]} L {leader[2]} {leader[3]}"/>')
        self.notes.append((self.n, target_id, desc))
    def save(self):
        doc = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.w} {self.h}" '
               f'width="{self.w}" height="{self.h}" role="img" aria-label="{html.escape(self.title)}">\n'
               f'  <title>{html.escape(self.title)}</title>\n{STYLE}\n'
               f'  <rect class="bg" x="0" y="0" width="{self.w}" height="{self.h}" rx="10"/>\n'
               + "\n".join(self.el) + "\n</svg>\n")
        (OUT / f"{self.name}.svg").write_text(doc, encoding="utf-8")
        INDEX[self.name] = {
            "title": self.title, "chapter": self.chapter, "url": self.url,
            "elements": {tid: desc for _, tid, desc in self.notes},
            "callouts": {str(n): tid for n, tid, _ in self.notes},
        }
        print(f"{self.name}.svg  {len(doc):>6}b  {len(self.notes)} callouts")

# ══════════════════════════════════════════════════ phone detail ══
d = Dia("screen-phone-detail", 820, 330, "A phone's own screen", "03-phones", "/phones/<phone>/calls")
d.btn("pd-back", 24, 20, 78, "Back")
d.rect("pd-header", 24, 60, 772, 70)
d.raw('<circle id="pd-avatar" cx="66" cy="95" r="24" style="fill:#DBEAFE"/>')
d.text("pd-avatar-letter", 66, 101, "S", 18, "t b", "middle", f"fill:{C['pri']}")
d.text("pd-name", 104, 90, "Sales", 15, "t b")
d.text("pd-number", 104, 108, "972501234567", 12, "t-mut")
d.chip("pd-rent-clock", 230, 86, 92, "0:42:10", C["pri"], C["priL"], 11)
d.raw(f'<circle id="pd-status-dot" cx="700" cy="95" r="5" style="fill:{C["ok"]}"/>')
d.text("pd-status", 714, 100, "Active", 12, "t b", "start", f"fill:{C['ok']}")
d.rect("pd-body", 24, 142, 772, 164)
d.tabs("pd-tab", 40, 152, ["📞 Calls", "👥 Contacts", "🤖 Scenarios", "SMS"], 0)
d.line(24, 194, 796, 194)
d.text("pd-content", 410, 250, "the selected tab's content", 12, "t-mut", "middle")
d.note("pd-back", "Back to the phone list", 814, 34, (803, 34, 106, 34))
d.note("pd-header", "The phone itself — name, number, live status", 814, 95, (803, 95, 800, 95))
d.note("pd-rent-clock", "Rental countdown — only on a rented phone", 276, 62)
d.note("pd-tab-0", "Calls — the WhatsApp conversations", 70, 320)
d.note("pd-tab-1", "Contacts — who this phone can talk to", 160, 320)
d.note("pd-tab-2", "Scenarios — what it runs", 258, 320)
d.note("pd-tab-3", "SMS — rented phones only", 352, 320)
d.save()

# ══════════════════════════════════════════════════ calls list ══
SECS = [("unsynced", "Unidentified — waiting to connect", [("~Dana", "972541234567", "amber")]),
        ("active", "Active", [("Avi Cohen", "Yes please", "ok"), ("Noa", "Thanks!", "ok")]),
        ("inactive", "Inactive", [("Old lead", "972500000000", "mut")])]
ROW, PAD = 52, 12
height = 56 + sum(18 + PAD*2 + ROW*len(r) + 14 for _, _, r in SECS) + 14
d = Dia("screen-calls-list", 760, height, "The conversation list", "12-chat-view", "/phones/<phone>/calls")
d.text("cl-count", 28, 36, "4 active contacts · 2 unidentified · 1 inactive", 12, "t-mut b")
d.btn("cl-refresh", 652, 20, 84, "Refresh", "ghost", 26)
y = 56
for sec, title, rows in SECS:
    d.text(f"cl-{sec}-title", 28, y + 10, f"{title} · {len(rows)}", 11, "t-mut b")
    ph = PAD*2 + ROW*len(rows)
    d.rect(f"cl-{sec}", 24, y + 18, 712, ph, rx=10)
    for i, (nm, sub, tone) in enumerate(rows):
        ry = y + 18 + PAD + i*ROW
        col = {"amber": "#F59F00", "ok": C["pri"], "mut": "#868E96"}[tone]
        dash = ' stroke-dasharray="4 3"' if tone == "amber" else (' stroke-dasharray="1 3"' if tone == "mut" else "")
        d.raw(f'<circle id="cl-{sec}-{i}-avatar" cx="62" cy="{ry+26}" r="18" fill="{col}" '
              f'fill-opacity="0.15" stroke="{col}" stroke-width="2"{dash}/>')
        d.text(f"cl-{sec}-{i}-initial", 62, ry + 32, nm.lstrip("~")[0], 15, "t b", "middle", f"fill:{col}")
        d.text(f"cl-{sec}-{i}-name", 92, ry + 23, nm, 13, "t b")
        if tone == "mut":
            d.chip(f"cl-{sec}-{i}-badge", 168, ry + 11, 60, "Inactive", "#868E96", "#F1F3F5")
        d.text(f"cl-{sec}-{i}-last", 92, ry + 40, sub, 11, "t-mut")
        d.text(f"cl-{sec}-{i}-time", 700, ry + 23, "14:05", 11, "t-mut", "end")
        if tone in ("amber", "mut"):
            d.btn(f"cl-{sec}-{i}-connect", 540, ry + 12, 84, "Connect", "primary", 26)
    y += 18 + ph + 14
d.note("cl-unsynced", "Not identified yet — a ~ before the name, dashed ring", 748, 100, (737, 100, 739, 100))
d.note("cl-active", "Active — the handshake finished", 748, 196, (737, 196, 739, 196))
d.note("cl-inactive", "Inactive — set aside, still listed", 748, 344, (737, 344, 739, 344))
d.note("cl-unsynced-0-connect", "Connect — links a contact, or brings an inactive one back", 510, 96, (521, 96, 536, 96))
d.save()

# ══════════════════════════════════════════════════ contacts ══
d = Dia("screen-contacts", 760, 300, "The contacts tab", "04-contacts", "/phones/<phone>/contacts")
d.text("ct-title", 28, 36, "12 Contacts", 14, "t b")
d.rect("ct-search", 420, 20, 180, 28, cls="sub", rx=8)
d.text("ct-search-ph", 436, 39, "Search…", 11, "t-mut")
d.btn("ct-add", 616, 20, 118, "+ Add Contact", "primary")
d.rect("ct-list", 24, 60, 712, 216, rx=10)
cols = [("name", 56, "Name"), ("number", 250, "Number"), ("status", 420, "Status"), ("lang", 540, "Lang")]
d.head("ct", 24, 60, 712, cols)
for i, (nm, num, st, tone, lang) in enumerate([
        ("Avi Cohen", "972541234567", "active", C["ok"], "he"),
        ("Dana", "972501112222", "new", "#F59F00", "en"),
        ("Old lead", "972500000000", "inactive", "#868E96", "he")]):
    ry = 90 + i * 56
    d.line(24, ry, 736, ry)
    d.raw(f'<circle id="ct-{i}-avatar" cx="40" cy="{ry+28}" r="14" fill="{C["pri"]}" fill-opacity="0.15"/>')
    d.text(f"ct-{i}-initial", 40, ry + 33, nm[0], 11, "t b", "middle", f"fill:{C['pri']}")
    d.text(f"ct-{i}-name", 62, ry + 33, nm, 12, "t b")
    d.text(f"ct-{i}-number", 250, ry + 33, num, 11, "t mono")
    d.chip(f"ct-{i}-status", 420, ry + 19, 62, st, tone, {"#2F9E44":"#EBFBEE","#F59F00":"#FFF9DB","#868E96":"#F1F3F5"}[tone])
    d.text(f"ct-{i}-lang", 546, ry + 33, lang, 11, "t-mut mono")
    d.text(f"ct-{i}-edit", 690, ry + 33, "Edit", 11, "t b", "start", f"fill:{C['pri']}")
d.note("ct-add", "Add Contact — starts the PING handshake", 748, 34, (737, 34, 738, 34))
d.note("ct-search", "Search by name or number", 410, 34, (399, 34, 416, 34))
d.note("ct-0-status", "The contact's state — active, new, draft, inactive", 486, 118)
d.note("ct-0-lang", "Language used for the PING and the bot's messages", 586, 118)
d.note("ct-0-edit", "Edit — name, email, language", 748, 118, (737, 118, 718, 118))
d.save()

# ══════════════════════════════════════════════════ scenarios ══
d = Dia("screen-scenarios", 760, 286, "The scenarios tab", "05-scenarios", "/phones/<phone>/scenarios")
d.btn("sc-new", 616, 20, 118, "+ New scenario", "primary")
d.text("sc-title", 28, 38, "Scenarios", 14, "t b")
for i, (nm, desc, st, col, bg) in enumerate([
        ("welcome_flow", "greets a new lead", "active", C["ok"], C["okL"]),
        ("survey", "three questions", "draft", "#868E96", "#F1F3F5")]):
    ry = 60 + i * 104
    d.rect(f"sc-{i}", 24, ry, 712, 92, rx=12)
    d.text(f"sc-{i}-name", 44, ry + 26, nm, 14, "t b")
    d.text(f"sc-{i}-desc", 44, ry + 44, desc, 11, "t-mut")
    d.chip(f"sc-{i}-contact", 44, ry + 56, 180, "🤖 bot · 972541234567", C["pri"], C["priL"], 10)
    d.chip(f"sc-{i}-status", 430, ry + 32, 58, st, col, bg)
    d.btn(f"sc-{i}-design", 500, ry + 28, 88, "🧩 Design", "ghost", 26)
    d.btn(f"sc-{i}-playback", 596, ry + 28, 92, "▶ Playback", "ghost", 26)
    d.text(f"sc-{i}-delete", 712, ry + 46, "🗑", 13, "t-mut", "middle")
d.note("sc-new", "New scenario — opens the designer empty", 748, 34, (737, 34, 738, 34))
d.note("sc-0-status", "draft or active — only an active one runs", 459, 268)
d.note("sc-0-design", "Design — opens the canvas", 544, 268)
d.note("sc-0-playback", "Playback — replay it without sending", 642, 268)
d.note("sc-0-contact", "The bot contact this scenario talks to", 134, 268)
d.save()

# ══════════════════════════════════════════════════ templates ══
d = Dia("screen-templates", 780, 300, "The templates tab", "08-templates", "/phones/templates/<phone>")
d.tabs("tpl-filter", 24, 20, ["All", "Pending", "Approved", "Rejected"], 2)
d.btn("tpl-new", 640, 18, 114, "+ New template", "primary")
d.rect("tpl-list", 24, 62, 730, 214, rx=10)
cols = [("name", 44, "Name"), ("lang", 250, "Lang"), ("category", 320, "Category"),
        ("status", 450, "Status"), ("published", 560, "Published")]
d.head("tpl", 24, 62, 730, cols)
for i, (nm, lang, cat, st, col, bg, pub) in enumerate([
        ("check_contact", "en_US", "UTILITY", "approved", C["ok"], C["okL"], True),
        ("welcome", "he", "UTILITY", "pending", C["warn"], C["warnL"], False),
        ("promo_sept", "he", "MARKETING", "rejected", C["bad"], C["badL"], False)]):
    ry = 92 + i * 56
    d.line(24, ry, 754, ry)
    d.text(f"tpl-{i}-name", 44, ry + 33, nm, 12, "t b mono")
    d.text(f"tpl-{i}-lang", 250, ry + 33, lang, 11, "t-mut mono")
    d.text(f"tpl-{i}-category", 320, ry + 33, cat, 10, "t-mut")
    d.chip(f"tpl-{i}-status", 450, ry + 19, 70, st, col, bg)
    d.text(f"tpl-{i}-published", 578, ry + 33, "yes" if pub else "no", 11,
           "t b" if pub else "t-mut", "start", f"fill:{C['ok']}" if pub else None)
    d.text(f"tpl-{i}-actions", 712, ry + 33, "Edit · Delete", 10, "t-mut", "middle")
d.note("tpl-filter-2", "Filter by status — the counts come from the server", 128, 300 - 10)
d.note("tpl-new", "New template — saves as a draft, nothing is sent yet", 768, 32, (757, 32, 756, 32))
d.note("tpl-0-status", "approved is the provider's answer, not yours", 485, 290)
d.note("tpl-0-published", "Published — only a published template can be used in a scenario", 594, 290)
d.note("tpl-1-actions", "Editing a published template is blocked — unpublish first", 712, 290)
d.save()

# ══════════════════════════════════════════════════ schedules ══
d = Dia("screen-schedules", 820, 286, "The schedules screen", "09-schedules", "/scheduling")
d.text("sh-title", 28, 36, "⏰ Scheduling", 15, "t b")
d.text("sh-count", 150, 36, "6 schedules", 12, "t-mut")
d.rect("sh-phone-filter", 480, 18, 150, 28, cls="sub", rx=8)
d.text("sh-phone-filter-label", 496, 37, "All phones ▾", 11, "t-mut")
d.btn("sh-new", 646, 18, 110, "+ New schedule", "primary")
d.rect("sh-table", 24, 60, 772, 212, rx=10)
cols = [("name", 44, "Name"), ("scenario", 190, "Scenario"), ("type", 330, "Type"),
        ("phone", 410, "Phone"), ("next", 540, "Next run"), ("status", 670, "Status")]
d.head("sh", 24, 60, 772, cols)
for i, (nm, sc, tp, nxt, st, col, bg) in enumerate([
        ("daily_ping", "welcome_flow", "cron", "today 18:00", "active", C["ok"], C["okL"]),
        ("one_off", "survey", "once", "14/11 09:30", "paused", "#868E96", "#F1F3F5"),
        ("manual_run", "welcome_flow", "manual", "—", "active", C["ok"], C["okL"])]):
    ry = 90 + i * 54
    d.line(24, ry, 796, ry)
    d.text(f"sh-{i}-name", 44, ry + 32, nm, 12, "t b mono")
    d.text(f"sh-{i}-scenario", 190, ry + 32, sc, 11, "t")
    d.chip(f"sh-{i}-type", 330, ry + 18, 56, tp, C["pri"], C["priL"])
    d.text(f"sh-{i}-phone", 410, ry + 32, "972501234567", 10, "t-mut mono")
    d.text(f"sh-{i}-next", 540, ry + 32, nxt, 11, "t")
    d.chip(f"sh-{i}-status", 670, ry + 18, 58, st, col, bg)
    d.text(f"sh-{i}-run", 764, ry + 32, "▶", 13, "t", "middle", f"fill:{C['ok']}")
d.note("sh-new", "New schedule — scenario, phone, when", 808, 32, (797, 32, 756, 32))
d.note("sh-phone-filter", "Filter to one phone", 466, 32, (477, 32, 476, 32))
d.note("sh-0-type", "cron, once or manual", 358, 276)
d.note("sh-0-next", "When it fires next — the clearest sign it is really set up", 574, 276)
d.note("sh-0-run", "Run it now, without waiting", 764, 276)
d.save()

# ══════════════════════════════════════════════════ executions ══
d = Dia("screen-executions", 840, 280, "Parallel executions", "13-executions", "/executions")
d.text("ex-title", 28, 34, "Parallel Executions", 15, "t b")
d.text("ex-sub", 28, 52, "one scenario, many phones, one contact", 11, "t-mut")
d.btn("ex-refresh", 646, 22, 40, "⟳", "ghost", 26)
d.btn("ex-new", 694, 22, 116, "+ New Execution", "primary", 26)
d.rect("ex-table", 24, 70, 792, 186, rx=10)
cols = [("contact", 44, "Contact"), ("job", 190, "Run / JOB"), ("phones", 320, "Phones"),
        ("source", 440, "Source"), ("templates", 560, "Templates"), ("status", 680, "Status")]
d.head("ex", 24, 70, 792, cols)
for i, (job, st, col, bg) in enumerate([("run_1130 JOB", "pending 3", C["pri"], C["priL"]),
                                        ("run_0900 JOB", "running", C["ok"], C["okL"])]):
    ry = 100 + i * 58
    d.line(24, ry, 816, ry)
    d.text(f"ex-{i}-contact", 44, ry + 26, "+972541234567", 11, "t b mono")
    d.text(f"ex-{i}-contact-name", 44, ry + 42, "Dana", 10, "t-mut")
    d.text(f"ex-{i}-job", 190, ry + 26, job, 11, "t b")
    d.text(f"ex-{i}-job-type", 190, ry + 42, "manual", 10, "t-mut")
    d.raw(f'<g id="ex-{i}-phones">')
    for k in range(2):
        d.chip(f"ex-{i}-phone-{k}", 320 + k*52, ry + 18, 48, "…4567", C["pri"], C["priL"], 8)
    d.raw("</g>")
    d.text(f"ex-{i}-source", 440, ry + 34, "welcome_flow", 11, "t")
    d.text(f"ex-{i}-templates", 560, ry + 26, "2", 11, "t b")
    d.text(f"ex-{i}-prefix", 560, ry + 42, "run_1130_*", 9, "t-mut mono")
    d.chip(f"ex-{i}-status", 680, ry + 22, 72, st, col, bg)
    d.btn(f"ex-{i}-run", 762, ry + 18, 44, "▶", "primary" if i else "off", 24)
d.note("ex-new", "New Execution — the four-step wizard", 828, 36, (817, 36, 812, 36))
d.note("ex-0-phones", "The target phones — first two, then +n", 346, 270)
d.note("ex-0-templates", "How many templates were copied, and their prefix", 590, 270)
d.note("ex-0-status", "pending n = the Scheduler has not picked the jobs up yet", 716, 270)
d.note("ex-0-run", "Run — disabled while anything is pending", 784, 270)
d.save()

# ══════════════════════════════════════════════════ sms ══
d = Dia("screen-sms", 760, 300, "SMS on a rented phone", "21-sms", "/phones/<phone>/sms")
d.text("sms-title", 28, 36, "24 SMS messages", 14, "t b")
d.rect("sms-search", 520, 20, 214, 28, cls="sub", rx=8)
d.text("sms-search-ph", 536, 39, "Search sender or text…", 11, "t-mut")
d.rect("sms-list", 24, 60, 710, 216, rx=10)
for i, (who, body, n) in enumerate([
        ("+972541112222", "Your code is 4921", "3"),
        ("BANK", "Transaction approved", "11"),
        ("Unknown sender", "Welcome!", "1")]):
    ry = 72 + i * 68
    if i: d.line(40, ry - 6, 718, ry - 6)
    d.raw(f'<circle id="sms-{i}-avatar" cx="66" cy="{ry+24}" r="18" fill="{C["pri"]}" fill-opacity="0.15"/>')
    d.text(f"sms-{i}-icon", 66, ry + 30, "✉", 15, "t b", "middle", f"fill:{C['pri']}")
    d.text(f"sms-{i}-sender", 98, ry + 20, who, 12, "t b mono" if who[0] == "+" else "t b")
    d.chip(f"sms-{i}-count", 230, ry + 8, 30, n, C["pri"], C["priL"])
    d.text(f"sms-{i}-preview", 98, ry + 40, body, 11, "t-mut")
    d.text(f"sms-{i}-time", 700, ry + 20, "13/11 09:12", 10, "t-mut", "end")
d.note("sms-0-sender", "One row per sender — tap to open the conversation", 748, 96, (737, 96, 714, 96))
d.note("sms-0-count", "How many messages from that sender", 272, 84)
d.note("sms-2-sender", "Messages with no readable sender land here", 748, 232, (737, 232, 714, 232))
d.note("sms-search", "Search covers the sender and the text", 506, 34, (517, 34, 516, 34))
d.save()

# ══════════════════════════════════════════════════ api explorer ══
d = Dia("screen-api", 820, 320, "The API console", "18-api-explorer", "/api")
d.text("api-title", 28, 36, "API Explorer", 15, "t b")
d.chip("api-token", 150, 22, 120, "token active", C["ok"], C["okL"], 10)
d.btn("api-copy-token", 286, 20, 108, "Copy token", "ghost", 26)
d.rect("api-filter", 620, 20, 176, 28, cls="sub", rx=8)
d.text("api-filter-ph", 636, 39, "Filter endpoints…", 11, "t-mut")
d.rect("api-sidebar", 24, 60, 230, 236, rx=10)
d.text("api-sidebar-title", 44, 84, "TAGS", 9, "t-mut b")
for i, (tag, n) in enumerate([("phones", 9), ("contacts", 7), ("scenarios", 6), ("templates", 11)]):
    d.rect(f"api-tag-{i}", 38, 96 + i*36, 202, 28, cls="sub" if i else "", rx=7,
           style=f"fill:{C['priL']};stroke:{C['pri']}" if i == 0 else None)
    d.text(f"api-tag-{i}-label", 52, 115 + i*36, tag, 11, "t b" if i == 0 else "t-mut",
           "start", f"fill:{C['pri']}" if i == 0 else None)
    d.text(f"api-tag-{i}-count", 226, 115 + i*36, str(n), 10, "t-mut", "end")
d.rect("api-main", 266, 60, 530, 236, rx=10)
for i, (m, path, col) in enumerate([("GET", "/phones/", C["ok"]), ("POST", "/phones/provision", C["warn"])]):
    ry = 76 + i*54
    d.rect(f"api-ep-{i}", 282, ry, 498, 42, cls="sub", rx=8)
    d.chip(f"api-ep-{i}-method", 296, ry + 12, 46, m, "#FFFFFF", col, 9)
    d.text(f"api-ep-{i}-path", 352, ry + 26, path, 11, "t mono")
    d.text(f"api-ep-{i}-summary", 560, ry + 26, "List my phones" if not i else "Provision phone", 10, "t-mut")
d.rect("api-try", 282, 190, 498, 90, cls="sub", rx=8)
d.text("api-try-title", 300, 212, "Try it", 11, "t b")
d.btn("api-send", 690, 198, 76, "Send", "primary", 26)
d.rect("api-response", 300, 226, 462, 42, cls="", rx=6, style="fill:#1E1E1E")
d.text("api-response-body", 316, 252, '{ "ok": true, "items": [ … ] }', 10, "mono", "start", "fill:#86EFAC")
d.note("api-token", "Your session token — the console signs requests as you", 140, 34, (151, 34, 148, 34))
d.note("api-tag-0", "Endpoints grouped by tag", 262, 110, (251, 110, 244, 110))
d.note("api-ep-0-method", "The method, colour-coded", 310, 310)
d.note("api-send", "Send — this is a real request against your own data", 808, 212, (797, 212, 770, 212))
d.note("api-response", "The real response", 808, 250, (797, 250, 766, 250))
d.save()

# ══════════════════════════════════════════════════ playback ══
d = Dia("screen-playback", 700, 320, "Playback", "07-playback", "/phones/<phone>/scenarios/<scenario>/playback")
d.rect("pb-frame", 24, 20, 440, 280, rx=10)
d.raw('<path id="pb-header" d="M 24 30 a10 10 0 0 1 10 -10 h 420 a10 10 0 0 1 10 10 v 36 h -440 z" '
      f'fill="{C["wa"]}"/>')
d.text("pb-title", 44, 50, "welcome_flow · playback", 12, "t b", "start", "fill:#FFFFFF")
d.rect("pb-body", 24, 66, 440, 184, cls="", rx=0, style=f"fill:{C['waBg']}")
for i, (side, txt) in enumerate([("out", "Hi! Are you interested?"), ("in", "Yes"), ("out", "Great — when?")]):
    ry = 80 + i*56
    if side == "out":
        d.rect(f"pb-msg-{i}", 220, ry, 224, 40, cls="", rx=8, style=f"fill:{C['waOut']}")
        d.text(f"pb-msg-{i}-text", 236, ry + 24, txt, 10, "t", "start", "fill:#1A2332")
        d.chip(f"pb-msg-{i}-step", 150, ry + 10, 56, "step " + str(i+1), C["pri"], C["priL"], 8)
    else:
        d.rect(f"pb-msg-{i}", 44, ry, 180, 40, cls="", rx=8, style="fill:#FFFFFF")
        d.text(f"pb-msg-{i}-text", 60, ry + 24, txt, 10, "t", "start", "fill:#1A2332")
        d.chip(f"pb-msg-{i}-expect", 238, ry + 10, 70, "expected", C["ok"], C["okL"], 8)
d.rect("pb-controls", 24, 250, 440, 50, cls="", rx=0, style="fill:#F0F2F5")
d.btn("pb-play", 44, 262, 70, "▶ Play", "primary", 26)
d.btn("pb-step", 124, 262, 70, "Step", "ghost", 26)
d.btn("pb-reset", 204, 262, 70, "Reset", "ghost", 26)
d.text("pb-speed", 420, 281, "1×", 11, "t-mut", "end")
d.note("pb-body", "The conversation as it would happen — nothing is sent", 512, 100, (501, 100, 468, 100))
d.note("pb-msg-0-step", "Which step produced this message", 512, 148, (501, 148, 210, 148))
d.note("pb-msg-1-expect", "What the scenario was waiting for", 512, 196, (501, 196, 312, 196))
d.note("pb-play", "Play, or walk it one step at a time", 512, 275, (501, 275, 280, 275))
d.save()

# ══════════════════════════════════════════════════ call history ══
d = Dia("screen-call-history", 780, 300, "A finished call", "11-reading-a-call", "/phones/<phone>/contacts/<contact>/calls/<call>")
d.btn("ch-back", 24, 20, 72, "Back", "ghost", 26)
d.chip("ch-outcome", 110, 20, 90, "completed", C["ok"], C["okL"], 10)
d.text("ch-when", 220, 38, "13/11 09:12 · 2m 14s", 11, "t-mut")
d.rect("ch-summary", 24, 60, 730, 56, rx=10)
for i, (lbl, val) in enumerate([("Sent", "5"), ("Received", "4"), ("Unmatched", "1"), ("Last step", "step 4")]):
    d.text(f"ch-stat-{i}-label", 48 + i*182, 82, lbl.upper(), 9, "t-mut b")
    d.text(f"ch-stat-{i}-value", 48 + i*182, 102, val, 13, "t b")
d.rect("ch-timeline", 24, 128, 730, 148, rx=10)
for i, (t, kind, txt) in enumerate([
        ("09:12:01", "sent", "Hi! Are you interested?"),
        ("09:12:40", "recv", "Yes"),
        ("09:13:02", "miss", "maybe later  — no branch matched")]):
    ry = 146 + i*42
    col = {"sent": C["pri"], "recv": C["ok"], "miss": C["warn"]}[kind]
    d.raw(f'<circle id="ch-ev-{i}-dot" cx="50" cy="{ry+10}" r="5" fill="{col}"/>')
    d.line(50, ry + 15, 50, ry + 36) if i < 2 else None
    d.text(f"ch-ev-{i}-time", 66, ry + 14, t, 10, "t-mut mono")
    d.text(f"ch-ev-{i}-text", 150, ry + 14, txt, 11, "t b" if kind != "miss" else "t")
    if kind == "miss":
        d.chip("ch-ev-2-flag", 600, ry + 2, 74, "unmatched", C["warn"], C["warnL"], 9)
d.note("ch-outcome", "How the call ended", 212, 34, (201, 34, 204, 34))
d.note("ch-stat-2-value", "Replies that matched no branch — the number to watch", 430, 290)
d.note("ch-stat-3-value", "The last step reached — where it stopped", 612, 290)
d.note("ch-ev-2-flag", "The reply that did not match, and what was expected", 768, 190, (757, 190, 680, 190))
d.save()

# ══════════════════════════════════════════════════ login ══
d = Dia("screen-login", 620, 300, "Signing in", "02-signing-in", "/")
d.rect("lg-card", 150, 24, 320, 252, rx=14)
d.raw(f'<circle id="lg-logo" cx="310" cy="66" r="20" fill="{C["pri"]}"/>')
d.text("lg-logo-mark", 310, 72, "G", 17, "t b", "middle", "fill:#FFFFFF")
d.text("lg-title", 310, 106, "Sign in", 15, "t b", "middle")
d.rect("lg-email", 178, 122, 264, 30, cls="sub", rx=8)
d.text("lg-email-ph", 194, 142, "you@example.com", 11, "t-mut")
d.rect("lg-password", 178, 158, 264, 30, cls="sub", rx=8)
d.text("lg-password-ph", 194, 178, "••••••••", 11, "t-mut")
d.btn("lg-submit", 178, 196, 264, "Sign in", "primary")
d.line(178, 238, 442, 238)
d.btn("lg-google", 178, 246, 128, "Google", "ghost", 26)
d.btn("lg-github", 314, 246, 128, "GitHub", "ghost", 26)
d.note("lg-email", "Email and password, or a provider below", 138, 137, (149, 137, 174, 137))
d.note("lg-submit", "Sign in", 482, 210, (471, 210, 446, 210))
d.note("lg-google", "Google and GitHub sign-in — same account either way", 242, 290)
d.note("lg-github", "First sign-in creates the account", 378, 290)
d.save()

# ── write the index ───────────────────────────────────────────────────────
MANUAL = {
 "screen-phone-card": ("A phone card in the phone list", "03-phones", "/phones", {
   "phone-card": "The card itself — click it to open the phone",
   "phone-name": "Nickname and number",
   "rent-battery-fill": "Rental battery — drains as the rental runs",
   "signal-bars": "Reception: green active, grey busy, outline disconnected",
   "status-badge": "The phone's status",
   "btn-disconnect": "Disconnect — asks first",
   "btn-manage": "Manage — opens the phone"}),
 "screen-designer": ("The scenario designer", "05-scenarios", "/phones/<phone>/scenarios/<scenario>/design", {
   "designer-ribbon": "Save, Publish, Import, Export, Settings, Help",
   "panel-expect": "EXPECT step types — wait for a reply",
   "panel-canvas": "The conversation, top to bottom",
   "panel-send": "SEND step types — send something",
   "errors-panel": "What would block publishing",
   "status-bar": "Event type, interval, steps, draft/active, saved"}),
 "screen-chat-view": ("The chat view", "12-chat-view", "/phones/<phone>/calls/<contact>", {
   "chat-header": "The contact and how many messages are loaded",
   "chat-window-banner": "Whether the 24-hour window is open",
   "msg-in-1": "Incoming messages, on the left",
   "msg-out-1": "Outgoing messages, on the right",
   "chat-template-btn": "Send a template — works when the window is closed",
   "chat-send-btn": "Send free text — needs the window open"}),
 "screen-settings": ("The settings dialog", "14-settings", "/settings", {
   "settings-dialog": "Settings, over the screen you were on",
   "settings-tab-personal": "Personal details",
   "settings-tab-two-step": "Two-step verification",
   "settings-tab-advanced": "Trusted domains and email notifications",
   "settings-tab-two-step-alert": "Orange dot — this tab needs attention",
   "settings-avatar": "Click to upload a picture",
   "settings-save": "One Save for all three tabs"}),
 "screen-rent-list": ("The rented phones list", "20-rented-phones", "/rent", {
   "rent-row-1-number": "The number, with a Mine or Available chip",
   "rent-row-1-whatsapp": "WhatsApp, Business, or not installed",
   "rent-row-1-verified": "Whether the link to the handset is live",
   "rent-row-1-dot": "Green = handset online, red = unplugged",
   "rent-row-1-left": "Your rental's countdown",
   "rent-row-1-btn": "Rent on an available row, End on yours"}),
}
for name, (title, chapter, url, els) in MANUAL.items():
    INDEX[name] = {"title": title, "chapter": chapter, "url": url, "elements": els, "callouts": {}}

(OUT / "index.json").write_text(json.dumps(
    {"generated_from": "src/screens + src/components (ui repo)",
     "note": "Element ids match the id attributes in the matching .svg file.",
     "screens": dict(sorted(INDEX.items()))}, ensure_ascii=False, indent=2), encoding="utf-8")
print("index.json:", len(INDEX), "screens",
      sum(len(v["elements"]) for v in INDEX.values()), "elements")
