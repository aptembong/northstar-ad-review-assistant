# Report template

Use this structure exactly. A loan officer should understand it in under a minute; a compliance reviewer should be able to check every finding against its rule.

---

## Verdict: [PASS | FLAG | HOLD]

**Ad:** [one-line description, such as "Instagram post, FHA purchase, LO: Dana Reyes"]
**Channel:** [channel] · **Product:** [product or "not stated, assumed ___"]
**In one sentence:** [why this verdict, in plain words]

### Scorecard
| Area | Result | Why |
|---|---|---|
| Rates & APR · Reg Z 1026.24(c) | PASS / FLAG / HOLD | [short reason, quoting the ad] |
| Triggering Terms & Disclosures · 1026.24(d), (f) | | |
| Prohibited Practices · 1026.24(i) | | |
| House Standards · Northstar checklist | | |
| Clarity & Placement · 1026.24(b) | | |

The overall verdict is the strictest result in the table.

### What's working
- [1 to 3 specific things the ad does well, such as "Clear call to action and NMLS ID present". Always include at least one if anything is genuinely good.]

### What the scan found
| Exact words | What it is | Status |
|---|---|---|
| "5.99%" | Rate | Needs APR |
| "low down payment" | Not a triggering term | OK |

### Action plan
List in priority order: HOLD items first, then FLAG items.

**1. [HOLD] [short title]**
- **Found:** "[exact words]"
- **Rule:** [rule name and citation]
- **Fix:** [replacement wording with placeholders such as [APR]]
- **Where:** [placement, such as "same line as the rate, same size"]

**2. [FLAG] ...**

If there are no action items, write: "No changes needed."

### For the reviewer
[One or two sentences on anything needing human judgment.]

### Your approval
[If a tappable multi-select question is available, ask it instead of this text: "Which fixes should I apply?" with one option per action item plus "All fixes".]
Which action items do you approve? Reply with "all", the item numbers (for example "1, 2, 4"), or "none". I'll make only the changes you approve, then review the revised version again.

> This is an automated pre-screen, not an approval. A licensed compliance reviewer must sign off before this ad is published.

---

## After approval: revision report

## Marked-up changes
[The ad with ~~removed words~~ struck through and **new words** in bold, each tagged with its item number like [1]]

## Clean revised version
```
[Full revised text, ready to copy. For images: corrected wording plus placement notes, and a mockup if possible]
```

### Changes made
| # | Before | After |
|---|---|---|

### New scorecard
[Same scorecard table, re-scored]

**Verdict: [old] → [new]**

[List any action items that were not approved and are still open.]

> This is an automated pre-screen, not an approval. A licensed compliance reviewer must sign off before this ad is published.

---

## Submission packet (downloadable file)

Page 1, cover:
- Title: "Ad Review Submission Packet", the Northstar Harbor Mortgage name, and the line "Northstar Harbor Mortgage is a fictional company created for portfolio purposes."
- Table: Submission ID · Loan officer and NMLS ID · Channel · Product · Planned publish date · Version number · Pre-screen verdict (original → revised) · Date submitted

Then, in order:
1. **Final ad:** the clean revised text, and the image or mockup if there is one
2. **Scorecard:** the latest scorecard table
3. **Changes made:** the before and after table
4. **Open items:** any unapproved action items or FLAG notes for the reviewer, or "None"
5. **Loan officer attestation:** "I reviewed the pre-screen results and the changes above. I understand this ad cannot be published until Compliance approves it." with a name and date line
6. **Compliance decision (for the reviewer):** checkboxes for Approved / Changes requested, plus reviewer name, date and comments lines

## Review queue item (SharePoint "Ad Review Queue" list)

| Field | Value |
|---|---|
| Submission ID | [ID] |
| Title | [one-line description of the ad] |
| Loan officer | [name], NMLS #[number] |
| Channel | [channel] |
| Product | [product] |
| Pre-screen verdict | [original] → [revised] |
| Version | [n] |
| Planned publish date | [YYYY-MM-DD] |
| Open items for reviewer | [list or "None"] |
| Publisher | Marketing (company channels and email) or Loan officer (own social accounts) |
| Status | Submitted |
| Attachment | [Submission ID]_submission-packet |

Status values used by the workflow: Submitted → Changes Requested → (resubmitted as the next version) → Approved → Published. The skill only ever sets "Submitted". Reviewers and Marketing set the others.
