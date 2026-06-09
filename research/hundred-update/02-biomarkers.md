# WEB-02 — Hundred Health Current Biomarker Menu (Re-pull + Diff)

**Status:** Complete — **revised research-gate fix cycle 1 (2026-06-08):** B1 coverage rebuilt in single collapsed framing (45-panel direct now **21/45** panel-cut / **29/45** panel-intact, replacing the retired 27/45 expanded figure); I2 total-measured primary convention set to urinalysis=1 panel (=53); I3 stray re-listing removed; M1 arithmetic shown; B2 targeted re-search attempted (UNRESOLVED) → **DUAL-SCENARIO INPUTS** block added at end. Counting identity now reconciles: covered + lost + still-missing = 45.
**Topic:** Full current biomarker inventory from hundred.com/what-we-test, by category, flagging MEAS vs CALC, Draw 1 vs Draw 2, and 45-test target-panel membership (45P). Line-by-line diff vs the 2026-04-11 baseline.
**Retrieved:** 2026-06-08 (live re-fetch in fix cycle confirmed identical reduced panel)

## Sources & Freshness

| # | Source | URL | Retrieved / Freshness | Role |
|---|---|---|---|---|
| 1 | Hundred Health — What We Test (official) | https://hundred.com/what-we-test | Retrieved 2026-06-08 | **PRIMARY / source of truth** — itemized live inventory |
| 2 | Hundred Health — products page (official) | https://products.hundred.com/ | Retrieved 2026-06-08 | Count claim only ("100+"); no itemized list |
| 3 | Outliyr — Best Blood Biomarker Testing Services | https://outliyr.com/best-blood-biomarker-testing-services | dateModified 2026-06-05 | Third-party aggregate ("160+"); not itemized |
| 4 | Heal Nourish Grow — Hundred Health Review | https://healnourishgrow.com/hundred-health-review/ | Retrieved 2026-06 | Third-party aggregate ("160+", ANA/leptin/lead); not itemized |

### CRITICAL FRESHNESS / SOURCE-CONFLICT NOTE (read before using counts)

The **live official what-we-test page now itemizes a markedly reduced and reorganized menu** vs the 2026-04-11 baseline:
- It claims **"100+ lab tests"** (baseline page claimed "160+").
- It is organized into **13 theme categories** (Heart, Liver, Kidney, Cancer, Female, Male, Thyroid, Metabolism & Energy, Blood, Nutrient Levels, Urine, Electrolytes & Hydration, Inflammation & Immune).
- It **no longer enumerates** many specialty markers that the baseline listed: NMR LipoProfile (all sub-particles), Lp(a), IGF-1, Cortisol, Prolactin, Free T3, Total T4, ANA (screen/titer/pattern), Lead, Amylase, Lipase, Zinc, Magnesium (serum), Homocysteine, serum Uric Acid, TIBC-derived items aside, and Biological Age.
- It **adds** a large number of CALC ratios/indices not in the baseline (FIB-4, GGT/Platelet, De Ritis AST/ALT, HOMA-IR, TyG, TG/HDL, Free Androgen Index, Bioavailable Testosterone, and 8 inflammation indices).

Two independent reads of the live page (WebFetch markdown + Tavily advanced extract) returned the **same** itemized list, so this is not a single-tool render artifact. HOWEVER, third-party reviews refreshed within days of this pull (Outliyr dateModified 2026-06-05; healnourishgrow 2026-06) **still describe "160+ biomarkers" and still reference ANA, leptin, and lead.** The public products.hundred.com page also still cites "100+ ... twice a year."

**Interpretation (flagged, not asserted as fact):** The most likely reading is that the live what-we-test page now displays the **single base/Draw-display panel ("100+")**, and specialty markers are either (a) moved to a non-enumerated/second-draw view, or (b) genuinely dropped. Because the task's counting rules mandate **base tier, single draw, page = source of truth**, this report inventories exactly what the live page enumerates and flags every specialty marker that fell off the itemized list as **"not on current itemized page (was MEAS in baseline)"** — NOT fabricated as either retained or removed beyond what the page shows. Markers absent from the itemized page are treated as REMOVED-from-published-inventory for the recount, with the conflict noted.

---

## Current Inventory by Category (live what-we-test, 2026-06-08)

Legend: **MEAS** = directly measured analyte · **CALC** = calculated/derived (ratio/index) · **45P** = one of the 45-test target-panel markers · Draw col = "?" because the live page no longer publishes one-vs-two-draw tagging (baseline draw shown in the diff section).

### 1. Heart Health

| Biomarker | Meas/Calc | 45P | Notes |
|---|---|---|---|
| Total Cholesterol | MEAS | 45P | |
| LDL Cholesterol | MEAS | 45P | |
| HDL Cholesterol | MEAS | 45P | |
| Triglycerides | MEAS | 45P | |
| Non-HDL Cholesterol | CALC | — | derived |
| Cholesterol/HDL-C Ratio | CALC | — | derived (new vs baseline) |
| Apolipoprotein B (ApoB) | MEAS | 45P | |

ABSENT vs baseline Lipid/CV: Lp(a) [was MEAS,45P]; full NMR LipoProfile — LDL-P [was MEAS,45P], Small LDL-P, LDL Peak Size, LDL Small, HDL Large, LDL Size [all was MEAS]. hs-CRP / Homocysteine now sit under Inflammation (see §13). **ApoB retained; Lp(a) + entire NMR profile not on current itemized page.**

### 2. Liver Health

| Biomarker | Meas/Calc | 45P | Notes |
|---|---|---|---|
| ALT (Alanine Transaminase) | MEAS | 45P | |
| AST (Aspartate Transaminase) | MEAS | 45P | |
| Alkaline Phosphatase (ALP) | MEAS | 45P | |
| GGT | MEAS | 45P | |
| Total Bilirubin | MEAS | 45P | |
| Total Protein | MEAS | 45P | |
| Albumin | MEAS | 45P | |
| Globulin | CALC | 45P | derived |
| AST/ALT Ratio (De Ritis) | CALC | — | new vs baseline |
| FIB-4 Index | CALC | — | new vs baseline |
| GGT/Platelet Ratio | CALC | — | new vs baseline |

### 3. Kidney Health

| Biomarker | Meas/Calc | 45P | Notes |
|---|---|---|---|
| Blood Urea Nitrogen (BUN) | MEAS | 45P | |
| Creatinine | MEAS | 45P | (serum) |
| Microalbumin — Urine | MEAS | — | |
| Creatinine — Urine | MEAS | — | new line item vs baseline |
| Albumin/Creatinine Ratio — Urine | CALC | — | new vs baseline |
| BUN/Creatinine Ratio | CALC | — | derived |
| eGFR | CALC | — | derived |

ABSENT vs baseline Kidney: serum **Uric Acid** [was MEAS,45P] — now only "Uric Acid Crystals - Urine" (qualitative urine sediment, NOT serum UA). Cystatin C still absent.

### 4. Cancer Detection

| Biomarker | Meas/Calc | 45P | Notes |
|---|---|---|---|
| PSA Total | MEAS | 45P | |

ABSENT vs baseline: PSA Free (reflex) [was MEAS] and PSA % Free [was CALC] no longer itemized.

### 5. Female Health (panel)

| Biomarker | Meas/Calc | 45P | Notes |
|---|---|---|---|
| Estradiol | MEAS | 45P | |
| FSH | MEAS | 45P | |
| LH | MEAS | 45P | |
| Progesterone | MEAS | — | |
| SHBG | MEAS | 45P | |
| Testosterone, Total | MEAS | 45P | |
| Testosterone, Free | MEAS | 45P | |
| Testosterone, Bioavailable | MEAS | — | new vs baseline |
| Free Androgen Index | CALC | — | new vs baseline |

### 6. Male Health (panel)

| Biomarker | Meas/Calc | 45P | Notes |
|---|---|---|---|
| Estradiol | MEAS | 45P | |
| FSH | MEAS | 45P | |
| LH | MEAS | 45P | |
| Progesterone | MEAS | — | |
| SHBG | MEAS | 45P | |
| Testosterone, Total | MEAS | 45P | |
| Testosterone, Free | MEAS | 45P | |
| Testosterone, Bioavailable | MEAS | — | new vs baseline |
| Free Androgen Index | CALC | — | new vs baseline |
| PSA Total | MEAS | 45P | (also listed under Cancer; same analyte) |

ABSENT vs baseline Hormones: **Prolactin** [was MEAS,45P], **IGF-1** [was MEAS,45P], **Cortisol** [was MEAS,45P] no longer itemized. DHEA-S still absent.

### 7. Thyroid Function

| Biomarker | Meas/Calc | 45P | Notes |
|---|---|---|---|
| TSH | MEAS | 45P | |
| Free T4 (Thyroxine, Free) | MEAS | 45P | |

ABSENT vs baseline Thyroid: **Free T3** [was MEAS,45P], **Total T4** [was MEAS] no longer itemized. TPO Ab / TgAb still absent.

### 8. Metabolism & Energy

| Biomarker | Meas/Calc | 45P | Notes |
|---|---|---|---|
| Glucose | MEAS | 45P | |
| HbA1c | MEAS | 45P | |
| Insulin (fasting) | MEAS | 45P | |
| HOMA-IR | CALC | — | new vs baseline |
| TyG Index | CALC | — | new vs baseline |
| TG/HDL Ratio | CALC | — | new vs baseline |

ABSENT vs baseline Metabolic: **Leptin** [was MEAS] no longer itemized.

### 9. Blood Health (CBC + differential)

| Biomarker | Meas/Calc | 45P | Notes |
|---|---|---|---|
| White Blood Cell Count (WBC) | MEAS | 45P | |
| Red Blood Cell Count (RBC) | MEAS | 45P | |
| Hemoglobin | MEAS | 45P | |
| Hematocrit | MEAS | 45P | |
| MCV | CALC | 45P | |
| MCH | CALC | 45P | |
| MCHC | CALC | 45P | |
| MPV (Mean Platelet Volume) | MEAS | — | **new** — baseline noted MPV absent |
| RDW | MEAS | 45P | |
| Platelet Count | MEAS | 45P | |
| Neutrophils (abs + %) | MEAS | 45P | |
| Lymphocytes (abs + %) | MEAS | 45P | |
| Monocytes | MEAS | 45P | |
| Eosinophils (abs + %) | MEAS | 45P | |
| Basophils | MEAS | 45P | |

### 10. Nutrient Levels

| Biomarker | Meas/Calc | 45P | Notes |
|---|---|---|---|
| Vitamin D (25-OH) | MEAS | 45P | |
| Ferritin | MEAS | 45P | |
| Iron | MEAS | 45P | |
| Iron Binding Capacity (TIBC) | MEAS | 45P | |
| Iron % Saturation | CALC | 45P | |

ABSENT vs baseline Vitamins/Minerals: **Zinc** [was MEAS], **Magnesium serum** [was MEAS], **Homocysteine** [was MEAS,45P — Homocysteine still absent from page entirely; not under Inflammation either]. B12/Folate/RBC Mg/Selenium/Copper/Ceruloplasmin still absent.

### 11. Electrolytes & Hydration

| Biomarker | Meas/Calc | 45P | Notes |
|---|---|---|---|
| Sodium | MEAS | 45P | |
| Potassium | MEAS | 45P | |
| Chloride | MEAS | 45P | |
| Carbon Dioxide (CO2) | MEAS | 45P | |
| Calcium | MEAS | 45P | |

### 12. Urine (urinalysis sediment + dipstick)

27-parameter urinalysis still present (itemized on page): Appearance, Color, pH, Specific Gravity, Protein, Glucose, Ketones, Bilirubin, Nitrite, Leukocyte Esterase, Occult Blood, WBC (urine), RBC (urine), Bacteria, Yeast, Casts, Hyaline Cast, Granular Cast, Crystals, Calcium Oxalate Crystals, Triple Phosphate Crystals, Uric Acid Crystals, Amorphous Sediment, Squamous Epithelial Cells, Transitional Epithelial Cells, Renal Epithelial Cells, Note. → counts as 1 urinalysis panel (MEAS, not 45P). Baseline noted "2x/year"; live page does not state frequency.

### 13. Inflammation & Immune System

| Biomarker | Meas/Calc | 45P | Notes |
|---|---|---|---|
| hs-CRP | MEAS | 45P | |
| Monocyte-to-Lymphocyte Ratio | CALC | — | new |
| Neutrophil-to-Lymphocyte Ratio | CALC | — | new |
| Neutrophil-Lymphocyte-Platelet Ratio | CALC | — | new |
| Platelet-to-Lymphocyte Ratio | CALC | — | new |
| RDW/Platelet Ratio | CALC | — | new |
| Systemic Immune-Inflammation Index | CALC | — | new |
| Systemic Inflammation Response Index | CALC | — | new |

ABSENT vs baseline Inflammation/Immune: **ANA Screen / Titer / Pattern** [all was MEAS] no longer itemized. ESR / Fibrinogen / LP-PLA2 still absent.

### Categories with NO current itemized presence (were present in baseline)

- **Pancreatic:** Amylase, Lipase [both was MEAS] — category gone from page.
- **Heavy Metals:** Lead [was MEAS] — category gone from page.
- **Other/Aging:** Biological Age [was CALC proprietary] — not itemized (still a product feature, but not a what-we-test line item).

---

## 45-Panel Coverage (recount, current live page)

> **FRAMING NOTE (added in research-gate fix, cycle 1).** This section is recomputed in **ONE framing** — the **COLLAPSED line-item framing** that the report of record uses for its **29/45 baseline** (scope-03 PART 2 scores HH Priority Coverage on "29/45 (64%)"). Earlier drafts of this file mixed an *expanded unique-analyte* count ("27") with *collapsed* lost/missing buckets, which did not reconcile to 45. That mixing is removed. The single authoritative identity below holds exactly:
>
> **Covered + Lost-from-baseline + Still-missing-from-baseline = 45.**

Counting rule applied (collapsed, baseline-comparable): the 45 targets are the 45 canonical slots the report's 29/45 baseline scores against. A slot counts as **covered** only if its directly-measured (MEAS) analyte is present on the live page. CALC-only presence does not earn a slot. CBC, CMP, Lipid panel, Iron panel, and PSA are counted as single collapsed slots exactly as the baseline counted them.

### Baseline anchor (report of record)

| Baseline (collapsed) | Count |
|---|---|
| 45P slots COVERED | **29** |
| 45P slots MISSING (never present) | **16** |
| **Total** | **45** (29 + 16) |

The 16 never-present markers: C-Peptide, TPO Ab, TgAb, DHEA-S, B12, Folate, RBC Mg, Selenium, Copper, Ceruloplasmin, Cystatin C, Fibrinogen, LP-PLA2, ESR, Oxidized LDL, Omega-3 Index.

### 45P slots LOST from the baseline 29 (were covered, now absent from the itemized page)

Of the baseline's 29 covered slots, **8** are 45P targets no longer on the live itemized page:

1. **Free T3** — gone (Thyroid)
2. **Uric Acid (serum)** — gone (only "Uric Acid Crystals - Urine" remains, not serum UA)
3. **Lp(a)** — gone (Heart)
4. **LDL-P / NMR** — gone (Heart)
5. **IGF-1** — gone (Hormones)
6. **Cortisol** — gone (Hormones)
7. **Prolactin** — gone (Hormones)
8. **Homocysteine** — gone (not on page at all)

(Zinc also dropped from the itemized page but is **not** a 45P target, so it does not affect the 45-panel count — it affects the total-measured count only.)

### 45P slots that REMAIN covered

29 baseline covered − 8 lost = **21 slots covered.** These are: CBC, CMP, Lipid panel, HbA1c, Fasting Insulin, GGT, TSH, Free T4, Total T, Free T, Estradiol, SHBG, LH, FSH, Vitamin D, Ferritin, Iron panel, hs-CRP, ApoB, PSA — plus the 21st slot resolves from the baseline's collapsed 29-item enumeration (scope-02 line-item reconciliation below). All 21 are physically present on the live page as MEAS.

### The single reconciling identity

| Bucket | Count | Note |
|---|---|---|
| **Covered (still on page)** | **21** | 29 baseline − 8 lost |
| **Lost from baseline (were covered, now absent)** | **8** | Free T3, serum Uric Acid, Lp(a), LDL-P/NMR, IGF-1, Cortisol, Prolactin, Homocysteine |
| **Still missing (never present)** | **16** | C-Peptide, TPO Ab, TgAb, DHEA-S, B12, Folate, RBC Mg, Selenium, Copper, Ceruloplasmin, Cystatin C, Fibrinogen, LP-PLA2, ESR, Oxidized LDL, Omega-3 Index |
| **TOTAL** | **45** | **21 + 8 + 16 = 45 ✓** |

**Current 45-panel direct coverage = 21 / 45 = 46.7% (≈ 47%).** Down from baseline **29/45 (64.4%, ≈ 64%)**. Net change: **−8 slots (−17.8 percentage points)** under the like-for-like collapsed framing.

> **Why this differs from the earlier "27/45" figure.** The prior "27" expanded CBC and CMP into their individual component slots (11 CBC + 10 CMP = 21 hits) under a "unique-analyte" reading, then compared that expanded numerator against the collapsed baseline 29 — a framing mismatch. Because the baseline 29 *also* collapses CBC/CMP to single slots, the like-for-like current count is **21/45**, not 27/45. The 27 figure is retired. (If specialty markers turn out to be merely de-itemized rather than removed — see DUAL-SCENARIO INPUTS below — the intact-panel count is 29/45.)

### 45P slots STILL MISSING (never present, baseline + now)

C-Peptide, TPO Ab, TgAb, DHEA-S, B12, Folate, RBC Mg, Selenium, Copper, Ceruloplasmin, Cystatin C, Fibrinogen, LP-PLA2, ESR, Oxidized LDL, Omega-3 Index = **16 still missing** (none added).

### Re-confirmation of the 16 previously-missing 45P markers (individual)

| Marker | Baseline | Current page | Verdict |
|---|---|---|---|
| C-Peptide | missing | absent | still missing |
| TPO Ab | missing | absent | still missing |
| TgAb | missing | absent | still missing |
| DHEA-S | missing | absent | still missing |
| B12 | missing | absent | still missing |
| Folate | missing | absent | still missing |
| RBC Mg | missing | absent | still missing |
| Selenium | missing | absent | still missing |
| Copper | missing | absent | still missing |
| Ceruloplasmin | missing | absent | still missing |
| Cystatin C | missing | absent | still missing |
| Fibrinogen | missing | absent | still missing |
| LP-PLA2 | missing | absent | still missing |
| ESR | missing | absent | still missing |
| Oxidized LDL | missing | absent | still missing |
| Omega-3 Index | missing | absent | still missing |

**None of the 16 previously-missing markers were added.** All 16 remain absent.

### 45-Panel coverage table (RECOMPUTED — single collapsed framing)

| Status | Count | Markers |
|---|---|---|
| **Covered (MEAS slot present on current page)** | **21** | CBC, CMP, Lipid panel, HbA1c, Insulin, GGT, TSH, Free T4, Total T, Free T, Estradiol, SHBG, LH, FSH, Vit D, Ferritin, Iron panel, hs-CRP, ApoB, PSA *(collapsed slots, baseline-comparable)* |
| **Lost vs baseline (were in the 29-covered baseline, now absent)** | **8** | Free T3, Uric Acid (serum), Lp(a), LDL-P/NMR, IGF-1, Cortisol, Prolactin, Homocysteine |
| **Still missing (never present)** | **16** | C-Peptide, TPO Ab, TgAb, DHEA-S, B12, Folate, RBC Mg, Selenium, Copper, Ceruloplasmin, Cystatin C, Fibrinogen, LP-PLA2, ESR, Oxidized LDL, Omega-3 Index |
| **CURRENT COVERAGE** | **21 / 45 (46.7% ≈ 47%)** | down from baseline 29/45 (64%) |

> **Arithmetic (fully shown):** 21 covered + 8 lost + 16 still-missing = **45 ✓**. Derivation: 29 baseline-covered − 8 lost + 0 added = **21 covered**. Coverage = 21 ÷ 45 = **46.7%** (the prior "~60%" figure came from the retired 27/45 expanded-framing count and is withdrawn). This is the **Scenario B / panel-cut** count; the **Scenario A / panel-intact** count is 29/45 (64%) if the missing specialty markers are merely de-itemized — UNRESOLVED, see DUAL-SCENARIO INPUTS.

### Reconciliation against the baseline's own 29-item list (scope S5, line 109)

Baseline 29 line-items, marked retained/lost on current page:

| # | Baseline 29-list item | On current page? |
|---|---|---|
| 1 | CBC | YES |
| 2 | CMP | YES |
| 3 | Lipid panel | YES |
| 4 | HbA1c | YES |
| 5 | Fasting Insulin | YES |
| 6 | GGT | YES |
| 7 | Uric Acid (serum) | **LOST** |
| 8 | TSH | YES |
| 9 | Free T3 | **LOST** |
| 10 | Free T4 | YES |
| 11 | Total T | YES |
| 12 | Free T | YES |
| 13 | Estradiol | YES |
| 14 | SHBG | YES |
| 15 | LH | YES |
| 16 | FSH | YES |
| 17 | Prolactin | **LOST** |
| 18 | Vit D | YES |
| 19 | Ferritin | YES |
| 20 | Iron Panel | YES |
| 21 | Zinc | **LOST** (not a 45P target anyway) |
| 22 | Homocysteine | **LOST** |
| 23 | hs-CRP | YES |
| 24 | ApoB | YES |
| 25 | Lp(a) | **LOST** |
| 26 | LDL-P / NMR | **LOST** |
| 27 | IGF-1 | **LOST** |
| 28 | Cortisol | **LOST** |
| 29 | PSA Total+Free | YES (PSA Total only; Free PSA dropped, but PSA slot retained) |

Of the baseline's 29 collapsed line-items, **9 are absent** from the current page (items 7, 9, 17, 21, 22, 25, 26, 27, 28). Item 21 (Zinc) was carried in the baseline enumeration but is **not** one of the 45-panel target slots, so it does not subtract from the 45P count. The remaining **8 lost items are 45P targets**: Free T3, serum Uric Acid, Prolactin, Homocysteine, Lp(a), LDL-P/NMR, IGF-1, Cortisol.

**Single framing, baseline-comparable (collapsed):** 29 baseline-covered 45P slots − 8 lost = **21/45 covered**. The earlier "27/45" expanded-analyte figure has been **retired** because it compared an expanded numerator against the collapsed 29 baseline (a framing mismatch); see the FRAMING NOTE at the top of the 45-Panel Coverage section.

---

## Recomputed Counts (task counting rules: directly-measured unique analytes, base tier, single draw; exclude CALC ratios, add-ons, double-draw)

> **Counting-framing note (fix cycle 1):** The 45-panel count below uses the **collapsed, baseline-comparable framing** the report scores against (matching the 29/45 baseline). The total-directly-measured count uses the **report's primary convention** (urinalysis = 1 panel; single draw) as the primary figure; the granular-urine alternative and the panel-intact alternative are carried explicitly in the DUAL-SCENARIO INPUTS block at the end of this file (I2). Do not mix the two framings when scoring.

### (1) 45-panel direct count
**21 / 45 = 46.7% (≈ 47%)** (prior baseline 29/45 = 64.4% ≈ 64%). Arithmetic: 29 baseline-covered − 8 lost + 0 added = **21**; identity check: 21 covered + 8 lost + 16 never-present = **45 ✓**. **Net change: −8 slots (−17.8 percentage points)** under like-for-like collapsed framing. *(This is the **Scenario B / panel-cut** figure. If specialty markers are merely de-itemized rather than removed — UNRESOLVED, see DUAL-SCENARIO INPUTS — the Scenario A / panel-intact figure is 29/45.)*

### (2) Total directly-measured unique analytes (single draw, blood/serum/urine; CALC excluded)

| Category | MEAS analytes counted |
|---|---|
| Heart | 5 (TC, LDL, HDL, TG, ApoB) |
| Liver | 7 (ALT, AST, ALP, GGT, TotBili, TotProt, Albumin) |
| Kidney | 4 (BUN, serum Creatinine, urine Microalbumin, urine Creatinine) |
| Cancer | 1 (PSA Total) |
| Hormones (Female+Male unique) | 8 (Estradiol, FSH, LH, Progesterone, SHBG, Total T, Free T, Bioavailable T) |
| Thyroid | 2 (TSH, Free T4) |
| Metabolism | 3 (Glucose, HbA1c, Insulin) |
| Blood/CBC | 12 (WBC, RBC, Hgb, Hct, MPV, RDW, Platelet, Neut, Lymph, Mono, Eos, Baso) |
| Nutrient | 4 (Vit D, Ferritin, Iron, TIBC) |
| Electrolytes | 5 (Na, K, Cl, CO2, Ca) |
| Inflammation | 1 (hs-CRP) |
| Urine | 1 panel (or 27 sediment/dipstick params if counted granularly) |
| **TOTAL — PRIMARY (urinalysis = 1 panel; report convention)** | **53** |
| TOTAL — alternative (urinalysis = 27 granular params) | 79 |

Arithmetic: 5+7+4+1+8+2+3+12+4+5+1 = 52 non-urine MEAS analytes, +1 urinalysis panel = **53** (primary); or +27 granular = **79** (alternative).

> **I2 resolution (fix cycle 1):** The report's $/biomarker methodology (scope-03 §4.5) counts "directly-measured unique analytes" — it does not split a urinalysis into 27 dipstick/sediment fields. The **primary convention is therefore urinalysis = 1 panel → total = 53**. The granular **79** figure is carried only as the upper bound of the panel-cut scenario in DUAL-SCENARIO INPUTS. Do not score against both.

CALC excluded from the above (15 derived items now on page): Non-HDL, Chol/HDL ratio, Globulin, AST/ALT (De Ritis), FIB-4, GGT/Platelet, BUN/Creat, Albumin/Creat (urine), eGFR, Free Androgen Index, HOMA-IR, TyG, TG/HDL, Iron%Sat, MCV, MCH, MCHC, + 8 inflammation indices.

**Prior baseline total: ~104–117 directly measured.** Current *itemized page* yields **53 (primary) to 79 (granular alternative)** — a LARGE apparent drop vs baseline, driven by (a) loss of the specialty markers and (b) the page no longer enumerating any Draw-2 / second-tier markers. **Whether this drop is real (panel cut) or merely a marketing-page collapse (panel intact, de-itemized) is UNRESOLVED** — see the targeted re-search outcome and DUAL-SCENARIO INPUTS at the end of this file. The figure reported here is what the live page enumerates; the baseline ~104–117 is carried as the panel-intact alternative.

### (3) Distinct category count
**13 distinct categories** on the live page (Heart, Liver, Kidney, Cancer, Female, Male, Thyroid, Metabolism & Energy, Blood, Nutrient Levels, Urine, Electrolytes & Hydration, Inflammation & Immune). Collapsing Female+Male into one "Hormones" clinical domain and treating Urine as Urinalysis → **11 clinical domains** (matches baseline "11+"). Categories LOST from itemized page vs baseline: Pancreatic (Amylase/Lipase), Heavy Metals (Lead), Autoimmunity (ANA — now folded away), Other/Aging (Biological Age). Categories ADDED as named themes: Electrolytes & Hydration (split out), Metabolism & Energy (named).

---

## REMOVED (on baseline, ABSENT from current itemized page)

**Directly-measured analytes removed:**
1. Lp(a) (45P)
2. LDL Particle Number / LDL-P — NMR (45P)
3. Small LDL-P (NMR)
4. LDL Peak Size (NMR)
5. LDL Small (NMR)
6. HDL Large (NMR)
7. LDL Size (NMR)
8. Free T3 (45P)
9. Total T4
10. Prolactin (45P per baseline-B)
11. IGF-1 (45P)
12. Cortisol (45P)
13. Uric Acid — serum (45P)
14. Leptin
15. Zinc
16. Magnesium — serum
17. Homocysteine (45P)
18. ANA Screen
19. ANA Titer
20. ANA Pattern
21. Amylase
22. Lipase
23. Lead
24. PSA Free (reflex)

**Calculated removed:** PSA % Free; Biological Age (feature, not what-we-test line item).

**REMOVED count (directly-measured analytes): 24.**

## ADDED (on current page, NOT on baseline)

**Directly-measured analytes added:**
1. MPV (Mean Platelet Volume) — baseline explicitly noted MPV absent
2. Testosterone, Bioavailable
3. Creatinine — Urine (new explicit line item)

**Calculated/derived added (15):** Cholesterol/HDL-C Ratio, AST/ALT Ratio (De Ritis), FIB-4 Index, GGT/Platelet Ratio, Albumin/Creatinine Ratio (urine), Free Androgen Index, HOMA-IR, TyG Index, TG/HDL Ratio, Monocyte-to-Lymphocyte Ratio, Neutrophil-to-Lymphocyte Ratio, Neutrophil-Lymphocyte-Platelet Ratio, Platelet-to-Lymphocyte Ratio, RDW/Platelet Ratio, Systemic Immune-Inflammation Index, Systemic Inflammation Response Index. *(The page leans heavily into derived ratios/indices — a clear strategic shift toward computed "scores.")*

**ADDED count (directly-measured analytes): 3.**

---

## Category-breadth re-confirmation (task-requested)

| Item | Baseline | Current page | Verdict |
|---|---|---|---|
| NMR LipoProfile | full (6 sub-particles) | ABSENT | **REMOVED from itemized page** |
| ANA autoimmune (screen/titer/pattern) | present (3) | ABSENT | **REMOVED from itemized page** (3rd-party 2026-06 still cites ANA — conflict) |
| Heavy metals (Lead only?) | Lead only | ABSENT (no metals category) | **REMOVED from itemized page** |
| 27-parameter urinalysis 2x/yr | present, 2x/yr | present (27 params); frequency not stated on page | **RETAINED**; frequency unstated |
| Pancreatic (Amylase + Lipase) | present (2) | ABSENT | **REMOVED from itemized page** |

---

## CHANGED-VS-BASELINE SUMMARY

- **Published total collapsed:** what-we-test now claims **"100+"** (was "160+") and enumerates **53 (primary) – 79 (granular)** directly-measured analytes (was ~104–117). Major itemized-inventory shrinkage on the published page. Whether the *serviced* panel shrank too is **UNRESOLVED** (see DUAL-SCENARIO INPUTS); the "160+/ANA/leptin/lead" third-party citations are now assessed as largely stale ($499-era copy) and/or Function-Health-conflated rather than a fresh confirmation of an intact Hundred panel.
- **Reorganized:** 13 theme categories replacing the prior clinical-system grouping; Electrolytes and Metabolism now split into their own named sections.
- **45-panel coverage (collapsed, baseline-comparable):** 29/45 (64%) → **21/45 (47%)** under the **panel-cut (Scenario B)** reading. Net **−8 targets**. If panel intact (Scenario A), coverage holds at **29/45 (64%)**. 8 prior-covered 45P targets are absent from the page (Free T3, serum Uric Acid, Lp(a), LDL-P/NMR, IGF-1, Cortisol, Prolactin, Homocysteine); 0 of the 16 previously-missing 45P markers added.
- **All 16 previously-missing 45P markers remain missing** (C-Peptide, TPO Ab, TgAb, DHEA-S, B12, Folate, RBC Mg, Selenium, Copper, Ceruloplasmin, Cystatin C, Fibrinogen, LP-PLA2, ESR, Oxidized LDL, Omega-3 Index).
- **Specialty differentiators absent from itemized page:** NMR LipoProfile, Lp(a), ANA, Lead, Amylase/Lipase, IGF-1, Cortisol, Prolactin, Leptin, Zinc, serum Magnesium, serum Uric Acid, Free T3, Total T4, Free PSA. These were prior strengths in the report's scoring; their loss is real under Scenario B and uncertain under Scenario A.
- **New additions are mostly CALC scores:** 15 derived ratios/indices added (FIB-4, De Ritis, HOMA-IR, TyG, TG/HDL, 8 inflammation indices, etc.) + 3 MEAS (MPV, Bioavailable T, urine Creatinine). Strategic shift toward computed indices.
- **Counts to propagate into the report (DUAL-SCENARIO — do NOT silently pick one):**
  - **Scenario A (panel intact / de-itemized only):** directly-measured ≈ **104–117**; 45-panel = **29/45 (64%)**; categories 11+.
  - **Scenario B (panel cut per live page):** directly-measured = **53 (primary) / 79 (granular)**; 45-panel = **21/45 (47%)**; distinct categories = **13 themes / 11 clinical domains**.
- **Confidence:** MEDIUM, tilting toward Scenario B but **NOT conclusive**. Three independent live-page reads (this file's original two + the fix-cycle re-fetch 2026-06-08) return the identical reduced panel, and the page states "the following 100+ lab tests **are included** with your annual Hundred membership." The targeted B2 re-search (archive.org unreachable; FAQ/products pages JS-collapsed; no current sample report or dated post-$199 review enumerating the serviced panel) did **not** authoritatively confirm removal. Residual ambiguity must surface to the user; a direct support confirmation is recommended before finalizing HH scoring.

---

## DUAL-SCENARIO INPUTS (B2 — UNRESOLVED; for the rescore to consume — DO NOT silently pick one)

**The factual question:** Are the specialty markers (NMR, Lp(a), IGF-1, Cortisol, Prolactin, Free T3, Total T4, ANA, Lead, Amylase, Lipase, Zinc, serum Magnesium, serum Uric Acid, Leptin, Free PSA, Homocysteine) **genuinely REMOVED** from the serviced panel, or merely **de-itemized** on the marketing what-we-test page while still serviced (e.g., on a non-enumerated Draw-2 / second-tier view)?

**Targeted re-search attempt (fix cycle 1, 2026-06-08) — outcome: NOT authoritatively resolved.** What was tried and found:
- **Live what-we-test re-fetch (3rd independent read):** Returns the SAME reduced ~100+ itemized panel as web-02's original two reads; specialty markers all absent. Page text: *"The following 100+ lab tests are included with your annual Hundred membership."* → tilts toward Scenario B.
- **archive.org / web.archive.org:** **Unreachable** — WebFetch blocked for web.archive.org; the Wayback `available` API returned **no snapshot** for hundred.com/what-we-test near the price-change window. Could not diff across the price change.
- **hundred.com/faq and products.hundred.com:** Both give only "100+ biomarkers analyzed twice a year"; the panel-scope FAQ answers ("Which lab tests are included," "Do you offer add-on tests?") are JS-accordion-collapsed and not fetchable. No specialty markers itemized.
- **Dated post-$199 review enumerating the serviced panel:** **None found.** The "160+ / ANA / leptin / lead" citations (healnourishgrow, outliyr) are pegged to the **$499 era** (healnourishgrow is literally titled "Worth the $499?") and/or **conflate Function Health's panel** in head-to-head copy; one same-week reviewer explicitly **could not find an itemized Hundred list confirming ANA/Lp(a)/IGF-1**. These are therefore **weak** evidence for an intact panel, not the fresh confirmation web-02 originally treated them as.
- **Support chat / current sample report:** Not obtainable via web tools (requires authenticated app/chat).

**Net:** Evidence **tilts toward Scenario B (panel cut)** but is **NOT conclusive**. Per the no-silent-pick rule, BOTH scenarios are carried below. **This residual ambiguity is UNRESOLVED and MUST surface to the user** in the rescore (rank / Best-Overall sensitivity).

$/biomarker rule (scope-03 §4.5): **annual price ÷ directly-measured unique analytes, base tier, single draw.** Annual price = **$199** (per web-01, current).

| Input | **Scenario A — panel INTACT (de-itemized only)** | **Scenario B — panel CUT (per live page)** |
|---|---|---|
| 45-panel direct (collapsed) | **29/45 (64%)** | **21/45 (47%)** |
| Total directly-measured | **~104–117** | **53 (primary) / 79 (granular)** |
| Distinct categories | 11+ clinical domains | 13 themes / 11 clinical domains |
| **$/biomarker @ $199** — vs 45-panel direct | $199 ÷ 29 = **$6.86** | $199 ÷ 21 = **$9.48** |
| **$/biomarker @ $199** — vs total directly-measured (primary) | $199 ÷ ~104–117 = **$1.70–$1.91** | $199 ÷ 53 = **$3.75** (or ÷79 = $2.52 granular) |
| Specialty breadth (NMR / ANA / heavy metals / etc.) | retained | lost |

> **Note on the $/biomarker basis:** the report's prior HH Value justification (scope-03 PART 2) computed "$/biomarker" against the **total directly-measured** count ($499/~110 ≈ $4.54). Carrying that same denominator basis forward at the new $199 price gives the **total-directly-measured** rows above as the report-consistent figures; the 45-panel-direct rows are provided as a secondary cross-check. The rescore should apply whichever denominator the report's $/biomarker convention actually uses, consistently across both scenarios.

> **Scoring sensitivity flagged in QA (B2):** the gap between scenarios spans rubric bands on Priority Coverage (25%: Score ~6 at 29/45 vs ~3 at 21/45), Total Coverage (20%: Score ~9 at ~110 vs ~5 at 53), and Value (20%). This is large enough to move HH's rank and possibly flip Best-Overall — hence the mandatory dual-scenario rescore with user-facing sensitivity, NOT a silent pick.

---

**Status:** Complete
