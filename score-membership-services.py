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

Scoring methodology (each category scored 1-10; see report S4 for rubrics):
  Priority Coverage  - how many of the 45-test target panel are directly measured
  Total Coverage     - total directly-measured analytes + category breadth
  Value              - BLEND of two equally-weighted legs (50/50):
                         (1) Efficiency  = AS-IS cost-effectiveness ($/directly-measured-biomarker + draws/yr)
                         (2) Affordability = absolute annual cost (a $250 budget can't buy a $549 service)
                       Value = (Efficiency + Affordability) / 2.
  Frequency          - draws/year + trend-tracking support
  Unique Features    - meaningful differentiators (Garmin, automated EHR import, clinician, NMR, ...)
  Data Access        - data OUT (PDF/CSV/API) + data IN (automated medical-record/EHR import) + wearable
  Convenience        - turnaround, at-home option, app, lab network, state coverage

Confidence discount (§4.6): services whose individual biomarker list is NOT published are
  scored on vendor claims, not verifiable data. Their claim-dependent inputs are multiplied
  by DISCOUNT so unverifiable claims can't out-rank documented services. The discount applies to
  Priority Coverage, Total Coverage, and the Value EFFICIENCY leg (the $/biomarker denominator is
  the unpublished count). It does NOT apply to the Value AFFORDABILITY leg — the annual price is a
  hard, verified fact regardless of how many biomarkers it buys.

Tie-break (matches the report): higher Priority Coverage, then higher Value.
"""
import sys

# ---- WEIGHTS (must sum to 1.0) -------------------------------------------------
WEIGHTS = {
    "Priority Coverage": 0.05,
    "Total Coverage":    0.30,
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
    "Function Health":          ([7, 8, 9, 6, 7, 6, 5], 365),
    "Ultrahuman Blood Vision":  ([5, 7, 7, 7, 6, 8, 7], 499),
    "Hundred Health":           ([3, 5, 9, 6, 8, 8, 8], 199),
    "Superpower Base+Adv":      ([7, 7, 7, 6, 6, 7, 7], 388),
    "Mito Health Pro":          ([8, 7, 6, 4, 8, 5, 6], 549),
    "Mito Health Core":         ([6, 6, 7, 4, 6, 5, 6], 349),
    "Superpower Base Only":     ([2, 5, 7, 6, 6, 7, 8], 199),
    "WHOOP Advanced Labs":      ([4, 5, 4, 7, 6, 6, 8], 588),
    "Parsley Longevity Labs":   ([4, 7, 7, 3, 4, 4, 5], 350),
    "Geviti Plus":              ([6, 7, 3, 7, 7, 4, 7], 1529),
    "SiPhox Health U360":       ([4, 4, 5, 7, 7, 6, 6], 450),
    "Empirical Health":         ([5, 4, 5, 8, 3, 4, 6], 399),
    "InsideTracker":            ([4, 4, 3, 7, 7, 8, 8], 829),
    "Lifeforce":                ([3, 2, 3, 7, 7, 4, 7], 599),
    "Wild Health":              ([2, 3, 1, 9, 8, 3, 6], 4345),
}

IDX = {"Pri": 0, "Tot": 1, "Eff": 2, "Freq": 3, "Uniq": 4, "Data": 5, "Conv": 6}

# ---- CONFIDENCE DISCOUNT --------------------------------------------------------
UNPUBLISHED = {"Ultrahuman Blood Vision", "Geviti Plus", "Parsley Longevity Labs"}
DISCOUNT = 0.5  # default; override with --discount X (e.g., --discount 0.7) or --nodiscount

# ---- AFFORDABILITY bands (annual $ -> 1-10) ------------------------------------
# Absolute-cost leg of Value. Lower price = more people can afford it = higher band.
AFFORD_BANDS = [(200, 10), (300, 9), (400, 8), (500, 7), (650, 6), (850, 5), (1200, 4), (2000, 3), (3000, 2)]


def afford_band(price):
    for cap, band in AFFORD_BANDS:
        if price <= cap:
            return band
    return 1


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
