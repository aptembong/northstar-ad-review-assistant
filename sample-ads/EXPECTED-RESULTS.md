# Northstar Harbor sample ads: expected results

Run each ad through the skill, then compare its verdict with the table below. Try the ad first, then check here, so you see the skill's reasoning fresh.

All ads are fictional. Northstar Harbor Mortgage is a fictional company created for portfolio purposes. Rates, APRs and NMLS numbers are illustrative placeholders.

| # | File(s) | Loan officer | Format | Expected | Why |
|---|---|---|---|---|---|
| 1 | ad1-simone-instagram.png + text/ad1-simone-instagram-caption.txt | Simone Washington | Instagram image + caption | HOLD | Rate with no APR (1026.24(c)); "3% down" and "$1,450/mo" triggers with no required disclosures (24(d), (f)); "FIXED" on a 7/1 ARM (24(i)(1)); "mortgage counselor" (24(i)(6)); "everyone qualifies" and "best rate all year" (house); no NMLS or Equal Housing Lender (house) |
| 2 | text/ad2-liam-refinance-email.txt | Liam Smith | Email | FLAG | APR and terms exist but only in the small footer, far from the 6.125% in the body (24(b) placement); "Rates will never be this low again" (house pressure claim) |
| 3 | ad3-priya-fha-flyer.png | Priya Natarajan | Print flyer | PASS | APR next to the rate with equal size; full worked example for the 3.5% down trigger; taxes/insurance/MIP statement; FHA correctly named; NMLS, Equal Housing Lender, as-of date and credit approval language present |
| 4 | ad4-luis-bilingual-flyer.png | Luis Ortega | Bilingual flyer | HOLD | Rate, payment and down payment in Spanish, but the APR and payment disclosures only in English fine print (24(i)(7)); APR also far smaller than the rate (24(f)) |
| 5 | ad5-frame1/2/3.png + text/ad5-simone-video-script.txt | Simone Washington | 30-second video | FLAG | All disclosures exist, but in tiny text on screen for 2 seconds (24(b) clear and conspicuous); rent-vs-payment comparison leaves out taxes and insurance (reviewer judgment) |

## Suggested test run
1. Run ad 1 → HOLD with a full scorecard and action plan.
2. Approve "all" → revised caption + flyer mockup → re-review shows PASS.
3. Show ad 3 → PASS with "What's working", proving it doesn't just flag everything.
4. Optional: ad 4 shows a subtle rule a human might miss.
