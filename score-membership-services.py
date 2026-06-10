#!/usr/bin/env python3
"""
Membership blood-testing services — scoring & ranking engine.

Single source of truth for the weighted scoring behind
research/services/RESEARCH-REPORT-membership-health-services-update.md (S2 / S4 / S7).

To re-score: edit WEIGHTS and/or RAW below, then run:
    python3 research/services/score-membership-services.py            # ranked table
    python3 research/services/score-membership-services.py --md       # markdown table for the report (S2/S7.2)
    python3 research/services/score-membership-services.py --check     # weights-sum + per-service breakdown
    python3 research/services/score-membership-services.py --value     # Value-leg breakdown (eff/afford/blend)

Scoring methodology (each category scored 1-10; see report S4 for rubrics).
Every category below uses ONE uniform rule applied identically to all 15 services
(the "apples-to-apples" audit, 2026-06-10): no service is counted, priced, or
credited on a different basis than any other, and claim-only inputs never score
the same as verified ones.

  Priority Coverage  - how many of the 45-test target panel are directly measured.
                       UNIFORM band table (N = directly-measured of 45):
                         34-45 -> 8 | 31-33 -> 7 | 28-30 -> 6 | 25-27 -> 5
                         20-24 -> 4 | 16-19 -> 3 | 12-15 -> 2 | <=11 -> 1
                       Applied to every service's actual mapped count; for the three
                       unpublished-list services the conservative LOW end of the
                       estimate range is used (never the optimistic end). Audit fixes:
                       Hundred Health 21/45 (was band 3 -> 4, an anomaly vs InsideTracker
                       22->4 and SiPhox 24->4); Superpower Base 17/45 (was 2 -> 3).
  Total Coverage     - total directly-measured analytes + category breadth.
                       Counting convention (uniform, ALL 15 verified the exact same way):
                       count each service's ACTUAL directly-measured analytes from its real
                       panel; calculated/derived values excluded; each distinct finding once
                       (CBC differential cell types counted once each, not absolute AND %;
                       urinalysis crystal/cast/epithelial subtypes collapse to one finding).
                       A panel reported as a single line is expanded to its real distinct
                       directly-measured size (CBC w/diff ~12 measured; CMP = 14; Lipid = 3).
                       NOT a flat constant — a 10-param panel counts 10, a 19-finding
                       urinalysis counts 19. Fixes verified across all 15: Wild Health
                       (CBC/CMP/Lipid had been collapsed to 1 line each -> expanded),
                       Lifeforce (CBC/CMP had been excluded entirely -> included),
                       Hundred Health & Mito (urinalysis subtype-multiplication de-duplicated).
  Value              - BLEND of two equally-weighted legs (50/50):
                         (1) Efficiency  = AS-IS cost-effectiveness ($/directly-measured-biomarker + draws/yr)
                         (2) Affordability = absolute annual cost (a $250 budget can't buy a $549 service)
                       Value = (Efficiency + Affordability) / 2.
                       UNIFORM PRICE BASIS: each service's price = the total MANDATORY
                       annual cost to access ITS blood-testing offering (membership +
                       included draws at the representative tier). Mandatory access fees
                       are included on the same basis for everyone (WHOOP's required $239
                       membership AND InsideTracker's required $149 membership both count);
                       genuinely OPTIONAL add-ons are excluded for everyone (at-home draw
                       fees, optional devices like the Ultrahuman Ring, separately-billed
                       Rx). $/biomarker uses the SAME uniform directly-measured count as
                       Total Coverage for every service (Lifeforce and Wild Health included
                       -- no "clinically distinct" sub-standard for anyone).
  Frequency          - draws/year + trend-tracking. UNIFORM bands: 4+ full draws -> 9;
                       3 -> 8; 2 full draws BOTH verified -> 7; (2nd draw reduced & verified)
                       OR (2 full draws but panel unverifiable) -> 6; 1 draw + verified
                       affordable retest (<$200) -> 6; 1 draw + retest unpriced -> 4;
                       1 draw + no retest path -> 3. Rule: an unverifiable "2 full draws"
                       claim scores the same as a verified reduced 2nd draw (both 6) --
                       applied to Ultrahuman & Geviti (7->6).
  Unique Features    - count of meaningful, VERIFIED differentiators weighted by rarity
                       (Garmin, automated EHR import, 1:1 clinician, prescribing, NMR,
                       Cystatin C, fully-at-home, DNA-methylation age, ...). Claim-only
                       features are NOT load-bearing (e.g. SiPhox's "300+ integrations"
                       claim is not counted; its confirmed device list + at-home + C-Peptide
                       carry the score). HH homepage "prescription therapies" is marketing
                       copy (imports/tracks Rx, does not prescribe) -> NOT credited.
  Data Access        - data OUT (PDF/CSV/API) + data IN (automated medical-record/EHR import)
                       + wearable. UNIFORM rule: claim-only with no verifiable evidence does
                       NOT score the same as verified (Ultrahuman CSV was Trustpilot-only ->
                       8 dropped to 6). Verified-but-narrow is capped (Hundred Health 8 =
                       confirmed Garmin + verified 450+ EHR import, capped at 8 for no CSV/API;
                       InsideTracker 8 = confirmed CSV + Garmin + uploads).
  Convenience        - turnaround, at-home option, app, lab network, state coverage, scored on
                       a uniform 5-factor rubric. Audit fix: WHOOP 8->7 (no at-home option +
                       unavailable in 5 states cannot tie the at-home leaders HH/SP-Base/IT at 8).

Confidence discount (§4.6): services whose individual biomarker list is NOT published are
  scored on vendor claims, not verifiable data. Their claim-dependent inputs are multiplied
  by DISCOUNT so unverifiable claims can't out-rank documented services. The discount applies to
  Priority Coverage, Total Coverage, and the Value EFFICIENCY leg (the $/biomarker denominator is
  the unpublished count). It does NOT apply to the Value AFFORDABILITY leg — the annual price is a
  hard, verified fact regardless of how many biomarkers it buys.

Tie-break (matches the report): higher Priority Coverage, then higher Value.
"""
import math
import sys

# ---- WEIGHTS (must sum to 1.0) -------------------------------------------------
WEIGHTS = {
    "Priority Coverage": 0.15,
    "Total Coverage":    0.20,
    "Value":             0.30,
    "Frequency":         0.10,
    "Unique Features":   0.10,
    "Data Access":       0.10,
    "Convenience":       0.05,
}
CATS = list(WEIGHTS)  # canonical weighting order: Pri, Tot, Value, Freq, Uniq, Data, Conv

# ---- RAW per-service inputs (1-10), order [Pri, Tot, Eff, Freq, Uniq, Data, Conv] + annual $ --
# "Eff" = the Value EFFICIENCY leg ($/biomarker + draws). The displayed Value category is
# Value = (Eff + Affordability)/2, computed below. Edit a number here and re-run to re-rank.
RAW = {
    # service                  : ([Pri, Tot, Eff, Freq, Uniq, Data, Conv], annual_price)
    "Function Health":          ([7, 8, 9, 6, 7, 6, 5], 365),  # Pri 32/45->7; Conv 5 (no at-home + 3-4wk full turnaround)
    "Ultrahuman Blood Vision":  ([5, 7, 7, 6, 6, 6, 7], 499),  # Freq 7->6 (2 full draws unverifiable = verified-reduced); Data 8->6 (CSV claim-only, unverified)
    "Hundred Health":           ([4, 7, 10, 6, 8, 8, 8], 199),  # Pri 21/45 -> band 4 (20-24 band; was 3, an anomaly vs IT 22->4 / SiPhox 24->4); ~71 measured = 52 non-urine + ~19 urinalysis (27 params de-duped: casts/crystals/epithelials collapse to one finding each, matching FH's 16-item urine count -- prior "~79" double-counted HH urine subtypes vs FH); Total band 7 (70-84, at floor); $2.80/marker ($199/71); Data 8 = Garmin(confirmed)+450 EHR(verified homepage+PR), capped at 8 (no CSV)
    "Superpower Base+Adv":      ([7, 7, 7, 6, 6, 7, 7], 388),  # Pri 33/45->7
    "Mito Health Pro":          ([8, 8, 6, 4, 8, 5, 6], 549),  # Pri 36/45->8; granular UA: ~87-95 measured (NMR in Pro)
    "Mito Health Core":         ([6, 7, 7, 4, 6, 5, 6], 349),  # Pri 30/45->6; granular UA: ~75-80 measured
    "Superpower Base Only":     ([3, 5, 7, 6, 6, 7, 8], 199),  # Pri 17/45 -> band 3 (16-19 band; was 2, an anomaly vs Lifeforce ~18->3)
    "WHOOP Advanced Labs":      ([4, 5, 4, 7, 6, 6, 7], 588),  # Pri 24/45->4; Conv 8->7 (NO at-home option + unavailable in 5 states; can't tie the at-home field-leaders HH/SP Base/IT at 8); price = total mandatory cost incl. required $239 WHOOP membership (same all-in basis as IT's $149)
    "Parsley Longevity Labs":   ([4, 7, 7, 3, 4, 4, 5], 350),  # Pri est 20-24 -> 4 (raw, discounted)
    "Geviti Plus":              ([6, 7, 3, 6, 7, 4, 7], 1529),  # Freq 7->6 (2 full draws unverifiable); Pri est 30-35 conservative-low -> 6 (raw, discounted)
    "SiPhox Health U360":       ([4, 4, 5, 7, 7, 6, 6], 450),  # Pri 24/45->4; Data 6 = PDF + CONFIRMED multi-wearable (Apple/Oura/Fitbit/Whoop/Dexcom; "300+" is the unverified claim but 8 devices confirmed) + PDF upload
    "Empirical Health":         ([5, 4, 5, 8, 3, 4, 6], 399),  # Pri est 25-30 -> 5
    "InsideTracker":            ([4, 4, 3, 7, 7, 8, 8], 829),  # Pri 22/45->4; price = membership $149 + 2 Ultimate $680 (all-in mandatory)
    "Lifeforce":                ([3, 4, 4, 7, 7, 4, 7], 599),  # Pri ~18/45->3; UNIFORM count: CBC(~12)+CMP(14) un-excluded -> ~48 measured ($12.48/marker), Tot band 4, eff 4 (was non-uniform ~26/$23.04)
    "Wild Health":              ([2, 5, 1, 9, 8, 3, 6], 4345),  # Pri ~14/45->2; UNIFORM count: CBC/CMP/Lipid un-collapsed -> ~58 measured ($74.90/marker), Tot band 5, eff still 1 ($4,345 price)
}

IDX = {"Pri": 0, "Tot": 1, "Eff": 2, "Freq": 3, "Uniq": 4, "Data": 5, "Conv": 6}

# ---- CONFIDENCE DISCOUNT --------------------------------------------------------
UNPUBLISHED = {"Ultrahuman Blood Vision", "Geviti Plus", "Parsley Longevity Labs"}
DISCOUNT = 0.5  # default; override with --discount X (e.g., --discount 0.7) or --nodiscount

# ---- AFFORDABILITY formula (annual $ -> 1-10) -----------------------------------
# Absolute-cost leg of Value: afford = 10 - 3*log2(price/200), clamped to [1,10],
# rounded to the nearest integer. Anchor: $200/yr = 10; halving/doubling the price
# gains/costs 3 points. Published as a one-line formula (no hand-tuned bands).
AFFORD_ANCHOR = 200
AFFORD_SLOPE = 3  # points per doubling


def afford_band(price):
    return max(1, min(10, round(10 - AFFORD_SLOPE * math.log2(price / AFFORD_ANCHOR))))


def value_legs(name, discount):
    """Return (efficiency_raw, affordability, blended_value). Efficiency is discounted for
    unpublished-list services (denominator unverifiable); affordability never is (price is fact)."""
    raw, price = RAW[name]
    eff = raw[IDX["Eff"]]
    afford = afford_band(price)
    eff_used = eff * discount if name in UNPUBLISHED else eff
    return eff, afford, round((eff_used + afford) / 2, 4)


def cat_vector(name, discount):
    """Effective 7-category vector in CATS order, with the §4.6 discount applied."""
    raw, _ = RAW[name]
    pri, tot = raw[IDX["Pri"]], raw[IDX["Tot"]]
    if name in UNPUBLISHED:
        pri *= discount
        tot *= discount
    _, _, value = value_legs(name, discount)
    return [pri, tot, value, raw[IDX["Freq"]], raw[IDX["Uniq"]], raw[IDX["Data"]], raw[IDX["Conv"]]]


def weighted_total(name, discount):
    vec = cat_vector(name, discount)
    return round(sum(s * WEIGHTS[c] for s, c in zip(vec, CATS)), 4)


def fmt_price(price):
    return "$" + format(price, ",")


def ranked(discount):
    rows = []
    for name in RAW:
        vec = cat_vector(name, discount)
        rows.append((weighted_total(name, discount), name, vec, RAW[name][1]))
    # sort: total desc, then tie-break Priority Coverage desc, then Value desc
    rows.sort(key=lambda r: (-r[0], -r[2][0], -r[2][2]))
    return rows


def main():
    md = "--md" in sys.argv
    check = "--check" in sys.argv
    value = "--value" in sys.argv
    discount = None
    if "--nodiscount" in sys.argv:
        discount = 1.0
    elif "--discount" in sys.argv:
        discount = float(sys.argv[sys.argv.index("--discount") + 1])
    d = DISCOUNT if discount is None else discount

    wsum = round(sum(WEIGHTS.values()), 6)
    if wsum != 1.0:
        print(f"WARNING: weights sum to {wsum}, not 1.0\n")

    rows = ranked(d)

    if md:
        print("| Rank | Service | $/yr | Weighted |")
        print("|------|---------|------|----------|")
        for i, (tot, name, _vec, price) in enumerate(rows, 1):
            print(f"| **{i}** | **{name}** | {fmt_price(price)} | **{tot:.2f}** |")
        return

    if value:
        print("Value leg breakdown  (Value = (Efficiency + Affordability)/2; † = efficiency ×%.1f discount)" % d)
        print(f"{'Service':<26} {'$/yr':>7}  {'Eff':>3} {'Aff':>3}  {'Value':>5}")
        print("-" * 56)
        for _tot, name, vec, price in rows:
            eff, afford, val = value_legs(name, d)
            mark = "†" if name in UNPUBLISHED else " "
            print(f"{name:<26} {fmt_price(price):>7}  {eff:>3}{mark}{afford:>3}  {val:>5.2f}")
        return

    print("Weights: " + " · ".join(f"{c} {int(WEIGHTS[c]*100)}%" for c in CATS))
    if d != 1.0:
        print(f"Confidence discount: ×{d} on Priority/Total/Value-efficiency for {sorted(UNPUBLISHED)}")
    else:
        print("Confidence discount: OFF (baseline)")
    print(f"{'#':>2}  {'Total':>5}  Service")
    print("-" * 52)
    for i, (tot, name, vec, price) in enumerate(rows, 1):
        print(f"{i:>2}  {tot:>5.2f}  {name} ({fmt_price(price)})")
        if check:
            parts = "  ".join(f"{c.split()[0][:4]}={s:g}" for s, c in zip(vec, CATS))
            print(f"        {parts}")


if __name__ == "__main__":
    main()
