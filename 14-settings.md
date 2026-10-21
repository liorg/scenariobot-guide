# 14. Settings and account

**How to get there:** the **⚙️** button in the top bar, near your avatar.
Settings opens as a dialog over the screen you were on; **✕** or **Cancel**
closes it.

**URL:** [grossman.bot/settings](https://grossman.bot/settings)

Settings has **three tabs**, and each one has its own address, so you can link
straight to a tab:

| Tab | URL | What's in it |
|---|---|---|
| 👤 **Personal details** | [/settings/personal](https://grossman.bot/settings/personal) | name, email, avatar, language, package |
| 🔐 **Two-step verification** | [/settings/2fa](https://grossman.bot/settings/2fa) | your mobile number and the WhatsApp code |
| ⚙️ **Advanced** | [/settings/advanced](https://grossman.bot/settings/advanced) | trusted domain, email notifications |

A tab with an **orange dot** needs attention — 🔐 while your number is not yet
verified, ⚙️ while the trusted domain is not a valid domain.

**One Save button for all three tabs.** Changes on any tab are saved together
by the **Save** button at the bottom. The one exception is the verification code
itself, which takes effect the moment it is accepted — there is nothing to save.

---

## 👤 Personal details

| Field | Notes |
|---|---|
| **Full name** | shown in the top bar and used in the WhatsApp code message |
| **Email** | **read-only** — it is your sign-in identity, so it cannot be changed here |
| **Avatar** | click the circle to pick an image; it uploads immediately and the circle shows your initials until it finishes |
| **Language** | English, Hebrew, Russian, Arabic |
| **Package** | Basic, Pro, Business, Enterprise — **display only** |

**The language preview is live.** Pick a language and the dialog's own labels
switch at once, before you save, so you can see what you are choosing. The rest
of the app follows **after you press Save**.

Hebrew and Arabic flip the whole layout to right-to-left.

---

## 🔐 Two-step verification

**You need this.** Until your mobile number is verified you cannot
[add a phone](03-phones.md) or [create a schedule](09-schedules.md), and an
orange banner sits at the top of every screen. The banner cannot be dismissed —
it is a requirement, not a hint. Pressing **Verify now** on it brings you here.

### How to verify

1. **Type your mobile number** in the field. Israeli numbers work in the
   familiar form — `054-123-4567` becomes `+972 54 123 4567` on its own.
2. Press **Verify**.
3. **A WhatsApp message arrives** with a six-digit code. It comes from the
   platform's own WhatsApp number, not from one of your phones.
4. **Type the code** into the six boxes. You do not have to press anything —
   the code is checked as soon as the sixth digit lands. Pasting the whole code
   works too; it fills all six boxes at once.
5. The banner disappears and the tab shows **✓ Verified** with the date.

### What can go wrong

| Message | What it means |
|---|---|
| **Add a mobile number first** | the field is empty or too short |
| **Please wait Ns before requesting a new code** | codes are a minute apart — the **Resend** button counts down |
| **Too many codes. Try again in Ns** | five codes an hour is the limit |
| **Wrong code (N attempts left)** | five tries per code, then you need a new one |
| **The code has expired** | a code lasts **7 minutes**; press **Resend** |
| **Too many attempts** | press **Resend** for a fresh code |
| **The mobile number changed** | you edited the number after the code was sent — press **Verify** again |
| **Could not send the code over WhatsApp** | the sending service could not reach WhatsApp; try again shortly |

**The code may take a few seconds.** The button shows progress for up to eight
seconds and then opens the boxes anyway — if the message has not arrived yet it
usually will within a few more seconds. Only "could not send" means it is not
coming.

### It has to be your own number, not a bot's

**The number you verify cannot be one of your own bot phones.** The platform
refuses it in both directions:

| What you try | What happens |
|---|---|
| verify a number you already added as a bot phone | refused — *This number is one of your bot phones* |
| add your verified mobile as a bot phone | refused — *This number is your two-step verification mobile* |

The reason is simple: a bot phone is automated, and the code arrives as a
WhatsApp message on that phone. If the two were the same number, the automation
could read its own verification code and the check would prove nothing.

So use a real personal handset — the one in your pocket — and keep the bot
numbers for bots. One verified mobile per account.

### Changing your number un-verifies it

Saving a **different** mobile number resets verification: the banner comes back
and you verify the new number. That is the whole point — verification says *this
person can be reached on this number*, so a new number is a new claim.

Reformatting the same number is not a change. `0541234567`, `972541234567` and
`+972-54-123-4567` are the same number, and saving one over another resets
nothing.

### Where the code comes from

The code is sent as an approved WhatsApp **template message** over the
platform's Cloud API connection — the same connection used for the phone health
checks. It is not sent from any of your own phones, so verification works
before you have added a single phone.

---

## ⚙️ Advanced

### Trusted domain

The domain your own systems call the API from. Leave it empty if you are not
using the API.

- Type the domain alone — `example.com`, not `https://example.com/`. A pasted
  URL is cleaned up for you.
- A **wildcard prefix** is allowed: `*.example.com` covers every subdomain.
- An invalid value marks the tab with a dot and **blocks Save** until it is
  fixed or cleared. Clearing the field is valid and removes the setting.

### Email notifications

| Toggle | Effect |
|---|---|
| **Email notifications** | off by default. On, you get notifications by email as well as in the bell |
| **Errors only** | appears when the first toggle is on. **On by default** — only failures reach your inbox |

With **Errors only** off you get an email for every notification, including the
successful calls.

**Emails arrive as a digest.** A run against twenty phones is one email listing
them, not twenty emails. They go to your account's email address — the one shown
on the Personal tab — in your chosen language, with times in your own timezone.

If you expected an email and did not get one, the usual reasons are: email
notifications are off, **Errors only** is on and the notification was a success,
or there is no email address on the account.

---

## Light and dark mode

The **🌙 / ☀️** button in the top bar, beside the language switcher, switches
between the two themes.

- **Light** is the default.
- Your choice is **remembered on this browser** — it survives signing out and
  coming back.
- It is per browser, not per account. Switching to dark on your laptop does not
  change it on your phone.

**The page reloads when you switch.** That is expected and nothing is lost:
the address bar holds the screen you were on, so you come back to exactly the
same place. Unsaved text in a form is the one thing that does not survive, so
switch before you start typing, not during.

Scrollbars, dropdowns and date pickers follow the theme too, since the browser
is told which mode the page is in.

## Elsewhere in the top bar

| Control | Where | What it does |
|---|---|---|
| **🔔 Notifications** | top bar | the notification bell — see below |
| **🌙 / ☀️ theme** | top bar | light or dark — see above |
| **Language switcher** | top bar | English, Hebrew, Russian, Arabic — **your choice is remembered**, and the layout flips to right-to-left for Hebrew and Arabic |
| **❓ Help** | top bar, beside ⚙️ | opens this guide |
| **Your email and avatar** | top bar | shows which account you're in |
| **Logout** | far end of the top bar | signs out |
| **Version number** | far end, small grey text | useful when reporting a problem |

## Notifications

The bell collects things worth knowing about, and **every scenario that
finishes writes one** — whether it succeeded or not.

| Outcome | Shown as |
|---|---|
| finished cleanly | ✅ success |
| finished, but some replies didn't match | ⚠️ warning |
| failed | ❌ error |
| cancelled | ℹ️ info |
| expired, or timed out | ⚠️ warning |

Each one names the contact, how long the call took, how many messages were sent
and received, and how many didn't match. When something went wrong it also
names the **last step reached**, which is usually the first thing you want.

Clicking through takes you to that call ([Chapter 11](11-reading-a-call.md)).

A scenario that finishes cleanly but with mismatches is deliberately a
**warning, not a success** — it ran to the end, but not the way it was written.

**The ❌ and ⚠️ ones are what reach your inbox** if you turned email
notifications on with **Errors only** — see Advanced, above.

## Privacy policy

Linked in the footer of every page.

---

**Next:** [Tips for a reliable setup](15-tips.md)
