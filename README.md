# Northstar Harbor Ad Review Assistant

A Claude skill that pre-screens mortgage marketing (social posts, emails, flyers, images and video scripts) for Regulation Z advertising issues and house standards. It returns a **PASS**, **FLAG** or **HOLD** verdict with a scorecard, a plain-language action plan and suggested fixes, so loan officers can fix problems before an ad ever reaches Compliance.

It never approves an ad. A licensed compliance reviewer makes every final decision.

**[See the full case study ↗](https://claude.ai/artifact/3eRUWtX9zD8umwhvwBLeP2)**: the tool, enablement materials, governance, workflow, dashboard and a real-world field test.

---

## Add the skill to your Claude

This takes about 5 minutes. You need a Claude account. On a Team or Enterprise plan, your admin may need to turn on skills first.

### 1. Download the skill

1. In the file list at the top of this page, click **`mortgage-ad-review.zip`**.
2. Click the **Download raw file** button (a down-arrow icon on the right).
3. Keep the file zipped. Claude needs the .zip file itself.

### 2. Turn on code execution

The skill runs a small script that scans ad text, so Claude needs code execution turned on.

1. Go to [claude.ai](https://claude.ai) and sign in.
2. Click your name in the bottom-left corner, then **Settings**.
3. Open **Capabilities** and turn on **Code execution and file creation**.

### 3. Upload the skill

1. Go to **Customize** > **Skills**.
2. Click the **+** button, then **Create skill**.
3. Choose **Upload a skill** and select `mortgage-ad-review.zip`.
4. Make sure the **mortgage-ad-review** toggle is on.

### 4. Try it

1. Download a sample ad from the [`sample-ads`](sample-ads) folder. `ad1-simone-instagram.png` is a good first test.
2. Start a new chat in Claude and attach the ad.
3. Type: **"Review this ad before I send it to Compliance."**
4. Claude returns a verdict, a scorecard and an action plan. Approve the fixes you want, and it revises the ad and checks it again.

Compare each result with [`sample-ads/EXPECTED-RESULTS.md`](sample-ads/EXPECTED-RESULTS.md).

> **Use only fictional or public ad content.** Never paste customer names, phone numbers, emails, loan numbers or other personal information into a review.

Official help: [Use skills in Claude](https://support.claude.com/en/articles/12512180-using-skills-in-claude).

---

## What's in this repository

| Folder or file | What it is |
|---|---|
| `mortgage-ad-review.zip` | The skill, ready to upload to Claude |
| `mortgage-ad-review/` | The same skill, unzipped, so you can read the instructions and rules |
| `northstar-sample-ads.zip` | All the sample ads in one download |
| `sample-ads/` | Five fictional Northstar Harbor ads (Instagram post, email, print flyer, bilingual flyer, video frames and script) plus expected results |
| `portfolio-static/` | Downloadable backup copies of every case study page, as HTML and PDF |
| `LICENSE` | MIT license |

### How the skill works

- **`SKILL.md`**: step-by-step instructions Claude follows for each review
- **`references/reg-z-advertising-rules.md`**: the Regulation Z advertising rules it checks (12 CFR 1026.24)
- **`references/house-standards.md`**: the lender's own advertising standards (NMLS ID, Equal Housing Lender and more)
- **`references/output-template.md`**: the report format, plus the submission packet and review queue fields
- **`scripts/trigger_scan.py`**: a quick scan that finds rates, payments and other "triggering terms" in ad text

To adapt it for your own organization, replace `house-standards.md` with your own standards and have your Compliance team review every rule before use.

---

## Good to know

- **Northstar Harbor Mortgage is a fictional company** created for portfolio purposes. All names, NMLS numbers, rates and figures are illustrative.
- **This is a pre-screen, not legal advice.** It helps people catch common issues early. It does not replace a licensed compliance reviewer, and it does not cover every federal, state or investor rule.

## About

Built by **Akeyla Peele-Tembong**, AI workflow and enablement builder.
[Case study](https://claude.ai/artifact/3eRUWtX9zD8umwhvwBLeP2) · [LinkedIn](https://www.linkedin.com/in/akeylatembong)
