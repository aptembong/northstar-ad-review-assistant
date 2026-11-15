#!/usr/bin/env python3
"""Deterministic first pass for mortgage ad review.

Finds every rate, dollar amount, down payment, loan term, payment and
risky phrase in ad text, so nothing is missed and results are repeatable.
Claude then interprets each match in context. This script never decides
a verdict on its own.

Usage:
    python trigger_scan.py ad.txt          # scan a text file
    echo "ad text" | python trigger_scan.py -   # scan from stdin
Output: JSON to stdout.
"""
import json
import re
import sys

PATTERNS = {
    # Reg Z 1026.24(c): any rate needs an APR
    "rate": r"\b\d{1,2}(?:\.\d{1,3})?\s?%(?!\s*down)",
    "apr_label": r"\bAPR\b|annual percentage rate",
    # Reg Z 1026.24(d)(1) triggering terms
    "down_payment": r"(?:\$\s?[\d,]+|\d{1,2}(?:\.\d+)?\s?%)\s*(?:down|down payment)\b|\bzero down\b",
    "loan_term": r"\b\d{1,2}[\s-]?(?:year|yr)s?\b|\b\d{2,3}\s+(?:monthly\s+)?payments\b",
    "payment_amount": r"\$\s?[\d,]+(?:\.\d{2})?\s*(?:/\s*mo(?:nth)?|per month|a month|monthly)",
    "finance_charge": r"\$\s?[\d,]+(?:\.\d{2})?\s*(?:in\s+)?(?:closing costs|fees|finance charges?|points)",
    # Reg Z 1026.24(i) prohibited-practice signals
    "fixed": r"\bfixed\b",
    "government": r"\bgovernment\b|\bgov(?:'t)?[\s-]?(?:backed|program|loan)\b",
    "counselor": r"\bcounse(?:l)?lor\b",
    "debt_elimination": r"\b(?:eliminate|wipe out|erase)\b.{0,20}\bdebt\b",
    # House standards signals
    "guarantee": r"\bguarantee(?:d)?\b|\beveryone qualifies\b|\bno credit check\b",
    "pressure": r"\bnever be this low\b|\btoday only\b|\bact now\b|\blast chance\b",
    "nmls": r"\bNMLS\s*#?\s*\d+",
    "equal_housing": r"equal housing (?:lender|opportunity)",
}

# Phrases that sound like triggers but are not (1026.24(d) commentary)
NOT_TRIGGERS = [
    r"low down payment",
    r"affordable (?:monthly )?payments",
    r"flexible terms",
]


def scan(text: str) -> dict:
    found = {}
    for name, pattern in PATTERNS.items():
        hits = []
        for m in re.finditer(pattern, text, flags=re.IGNORECASE):
            start = max(0, m.start() - 40)
            end = min(len(text), m.end() + 40)
            hits.append({
                "match": m.group(0).strip(),
                "context": text[start:end].replace("\n", " ").strip(),
            })
        if hits:
            found[name] = hits

    triggers = [k for k in ("down_payment", "loan_term", "payment_amount", "finance_charge") if k in found]
    safe_phrases = [p for p in NOT_TRIGGERS if re.search(p, text, flags=re.IGNORECASE)]

    return {
        "triggering_terms_found": triggers,
        "rate_without_apr": "rate" in found and "apr_label" not in found,
        "missing_nmls": "nmls" not in found,
        "missing_equal_housing": "equal_housing" not in found,
        "non_trigger_phrases": safe_phrases,
        "matches": found,
        "note": "Pattern matches only. Claude reviews each in context before any verdict.",
    }


def main() -> None:
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    text = sys.stdin.read() if sys.argv[1] == "-" else open(sys.argv[1], encoding="utf-8").read()
    print(json.dumps(scan(text), indent=2))


if __name__ == "__main__":
    main()
