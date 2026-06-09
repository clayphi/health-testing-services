# Web Re-Search: Hundred Health Panel Scope Gap-Fill

**Gap:** B2 / G-BIO — Did Hundred Health's CURRENT serviced blood panel (post-$199 price drop) genuinely REMOVE specialty markers (NMR LipoProfile, Lp(a), IGF-1, Cortisol, Prolactin, Free T3, ANA, Lead, Amylase, Lipase, Homocysteine, Zinc, etc.) OR merely de-itemize them on the marketing page?
**Date:** 2026-06-08
**Status:** In Progress

## Context
- Live hundred.com/what-we-test now shows a reduced "100+" itemized list.
- Same-week third-party reviews still cite the fuller "160+ across two draws" panel.
- Central blocker for the rescore (determines Priority + Total Coverage + whether rank flips).
- PRIOR re-search FAILED on: live what-we-test page (x3), web.archive.org Wayback (unreachable), hundred.com FAQ (JS-collapsed), generic review search.
- Garmin-confirmed override stands unless POSITIVE removal evidence found.

## New Angles Tried

### Angle 1 — Hundred's OWN current properties (NEW; prior attempt only hit what-we-test x3 + JS-collapsed FAQ)
Extracted the live pages via Tavily advanced extract (renders more than WebFetch's JS-collapsed view). ALL Hundred-owned pages now uniformly tie the $199 price to a **"100+"** figure:
- **hundred.com/join** — "Hundred membership. What's Included: **100+ lab tests**" (the $199 tier; gift link = `hundred_tier_1_membership`).
- **hundred.com/faq** — "The average physical checks for ~20 basic biomarkers... Hundred measures **over 100+ biomarkers** that are specifically selected by clinicians... across numerous biological systems: heart, hormones, metabolic, stress, aging, immune function, and more." Footer banner: "Hundred tests **100+**... **$0.55/day**."
- **products.hundred.com** (Shopify marketplace, "Ready to become a member" block) — "What's included: **100+ lab tests**... **$16 / month · Billed annually at $199**." Marketplace FAQ: "**Precision Testing — 100+ biomarkers analyzed twice a year**" and lists "**Advanced Diagnostics — Access to specialty tests like full-body MRIs, cancer screening, gut health analysis, and other specialty tests**" as a SEPARATE add-on category (i.e., specialty = add-on, not core 100+).
- hundred.com homepage is the lone outlier still showing **"160+ ... $1.37/day"** (and "+12 more"/"+more" collapsed category headers e.g. "Heart Health 19 markers", "Metabolic Health 15 markers") — i.e. STALE marketing not yet updated to match the $199/"100+" repricing.

### Angle 2 — Full itemized live what-we-test list (NEW: Tavily advanced extract pulled the COMPLETE itemized list, not the JS-collapsed view the prior attempt got)
Live `hundred.com/what-we-test` itemizes ONLY these (complete list, ends at footer CTA):
- Cholesterol: HDL, LDL, Non-HDL, Total, Triglycerides — **NO ApoB, NO Lp(a), NO LDL-P/NMR**
- Liver (11), Kidney (incl. urine microalbumin), Cancer (**PSA only**), Female/Male hormones (T total/free/bioavail, E2, FSH, LH, SHBG, Progesterone, Free Androgen Index — **NO prolactin, NO IGF-1**), Thyroid (**TSH + Free T4 ONLY — NO Free T3, NO Total T4**), Metabolism (Glucose, HbA1c, Insulin, HOMA-IR, TyG, TG/HDL — **NO leptin**), Blood Health (full CBC), Nutrients (Ferritin, Iron, Iron%Sat, TIBC, Vitamin D — **NO zinc, NO magnesium, NO homocysteine**), Urine (~30 markers), Electrolytes (Ca, CO2, Cl, K, Na), Inflammation (hs-CRP + computed ratios — **NO ANA**).
- **NONE of the target specialty markers appear on the live page:** NMR/LDL-P, Lp(a), ApoB, IGF-1, Cortisol, Prolactin, Free T3, ANA, Lead, Amylase/Lipase (pancreas), Homocysteine, Zinc, Magnesium, Uric acid, Leptin — ALL absent from the itemized live list. The itemized count is ~100, consistent with "100+".

### Angle 3 — Third-party reviews enumerating the full 160+ panel (freshness check, NEW: pinned the draw date)
- **healnourishgrow.com/hundred-health-review** (title now reads "Worth the new **$199** Price?") explicitly lists ALL specialty markers as PRESENT in the standard panel: Lp(a), IGF-1, cortisol (x2), Free T3, Total T4, prolactin, full ANA screen, lead, zinc, magnesium, homocysteine, pancreas enzymes, leptin, uric acid, "160+ across two draws." BUT: the author's draw was **March 16, 2026**, her app showed **"48 of 107 biomarkers"** (a 107-marker single draw, NOT 160), and the review BODY still evaluates "$499"/"$449" — she did NOT re-verify the panel after the $199 repricing. The "160+" + full specialty list describes the panel as marketed/tested in mid-March 2026, pre/at-repricing, NOT a post-$199 re-verification.
- **outliyr.com** and **worth.com**: worth.com is actually a **Superpower** review ($199 competitor) — this is the likely source of the $199/Hundred conflation in the ecosystem. outliyr cites "160+ / $1.37/day / $499" (stale, matches Hundred homepage), reviewer had not yet tested.

### Angle 4 — Blog / press / changelog for a panel-change announcement (NEW)
- No Hundred blog/press post announces a panel cut OR a "we only simplified the page" statement. Launch press (prnewswire, finance.yahoo, hlth.com, nutritioninsight, chaindrugreview — all Dec 2025) uniformly says "160+ advanced lab tests annually." No changelog reconciling 160+ → 100+.

### Angle 5 — Reddit / community (NEW)
- Tavily community search returned NO member posts enumerating the post-$199 serviced panel. r/Function_Health thread surfaced but not Hundred-specific. No screenshots/YouTube walkthrough dated after the price change found enumerating markers. (Hundred has a YouTube @MyHundredHealth but no dated post-$199 panel walkthrough surfaced.)

### Angles NOT productively reachable
- Google/Bing `cache:` — not exposed via available tools; Tavily advanced extract of the LIVE page was the effective substitute and DID retrieve the full itemized list (better than cache for this purpose).
- app.hundred.com panel pages — auth-gated (sign-in), not publicly fetchable.

---

## Analysis

**The de-itemization-vs-removal question now has a sharper shape.** The data is no longer "live page reduced vs reviews say 160+." It is:
1. **Every Hundred-owned property has been repriced and re-described to "100+" / $199** (join, faq, marketplace) — uniform, not a single stale page. Only the homepage hero retains "160+/$1.37/day" (clearly the un-updated asset).
2. **The live itemized what-we-test list is now ~100 markers and omits ALL target specialty markers** — this is a genuine, consistent reduction in what is publicly itemized, matching the "100+" count, NOT merely a collapsed/"+more" UI on a still-160 panel.
3. **The "160+ with full specialty markers" now exists ONLY in third-party reviews describing March-2026 draws** that were not re-verified after the repricing.
4. The marketplace FAQ reframes specialty diagnostics (MRI, cancer screen, gut) as **add-ons**, consistent with a leaner core membership.

This tilts toward **Scenario B (panel cut/reduced)** for the publicly-serviced $199 membership: the itemized core dropped from ~160 to ~100 and the specialty markers (Lp(a), IGF-1, ANA, cortisol, Free T3, prolactin, lead, pancreas enzymes, homocysteine, zinc, magnesium, NMR/LDL-P, ApoB) are no longer in the itemized core.

**BUT positive-removal proof is still absent.** No Hundred statement says "we removed marker X." It remains *possible* (less likely now) that the markers are still drawn but de-itemized to a generic "100+" while specialty results still populate in-app (cf. the March reviewer's app showing ANA/IGF-1/cortisol from a draw at the transition). Because the override rule requires POSITIVE removal evidence to flip the Garmin-confirmed baseline, and what we have is strong-but-circumstantial (count drop + itemization drop + uniform repricing) rather than an explicit "removed" statement or a post-$199 member screenshot showing the specialty markers GONE, this does not meet the "positive removal" bar to override.

## RESOLUTION

**RESOLUTION: UNRESOLVED — dual-scenario stands, with evidence now tilted toward Scenario B (cut/reduced).**

Evidence tilt (NEW this pass, did not exist in prior attempt): All Hundred-owned properties (join, faq, products.hundred.com marketplace) uniformly state **"100+" tied to $199**, the live what-we-test itemizes only ~100 markers with EVERY target specialty marker absent, and the "160+/full-specialty" description now survives only in third-party reviews of pre-repricing March-2026 draws. The homepage "160+" is a stale un-updated asset. This is strong circumstantial evidence of a real reduction — but no source explicitly states "marker X removed" and no post-$199 member screenshot confirms the specialty markers are gone from the serviced draw, so it does not meet the POSITIVE-removal bar.

**Garmin-confirmed override PRESERVED** — circumstantial tilt toward B is NOT positive removal evidence and does not override.

New angles genuinely tried this pass: (1) Tavily advanced-extract of hundred.com/join + /faq + products.hundred.com [NEW, productive — uniform "100+/$199"]; (2) Tavily advanced-extract of full itemized live what-we-test list [NEW vs prior JS-collapsed fetch — productive, ~100 markers, all specialty absent]; (3) freshness/date-pinning of healnourishgrow review [NEW — draw was March 16 2026, 107 markers, body still says $499, not re-verified post-$199]; (4) blog/press/changelog scan [NEW — no panel-change announcement, no "only simplified page" statement]; (5) Reddit/community + YouTube walkthrough [NEW — no member enumeration of post-$199 panel found]. Google/Bing `cache:` and app.hundred.com were not reachable via available tools; Tavily live-page advanced extract substituted effectively for cache.

**Status:** Complete

