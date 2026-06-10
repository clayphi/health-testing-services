# Membership Health Testing Services — Comprehensive Comparison

An independent, reproducible ranking of **15 membership blood-testing services** for comprehensive longevity-oriented health monitoring. Every service is scored on a transparent 7-category weighted rubric, and every number in the report is produced by a published scoring engine you can re-weight and re-run.

**📄 Read the report:**
- **Web (recommended):** https://clayphi.github.io/health-testing-services/
- **PDF:** [`report.pdf`](report.pdf)
- **Markdown:** [`report.md`](report.md)

---

## The verdict

| # | Service | $/yr | Score |
|---|---------|------|-------|
| 1 | **Function Health** | $365 | **7.45** |
| 2 | **Hundred Health** | $199 | **7.10** |
| 3 | Superpower Base+Adv | $388 | 6.95 |
| 4 | Superpower Base Only | $199 | 6.45 |
| 5 | Mito Health Pro | $549 | 6.30 |
| … | *(11 more in the report)* | | |

- **Best Overall — Function Health:** the broadest directly-measured panel (~92 markers), 2 draws/yr, strong value.
- **Best Value — Hundred Health:** the field's top Value score (lowest cost per biomarker at the lowest price), and the cheapest service with confirmed Garmin sync.
- No single service covers the full 45-test reference panel — completing it takes some à-la-carte gap-fill regardless of choice.

## Scoring methodology

Each service is scored 1–10 across seven categories, then weighted:

| Category | Weight |
|---|---|
| Priority Coverage (of a 45-test reference panel) | 5% |
| Total Coverage (directly-measured breadth) | 30% |
| **Value** (50/50 blend: cost-efficiency + absolute affordability) | 30% |
| Frequency (draws/yr + trend tracking) | 10% |
| Unique Features | 10% |
| Data Access (export + wearable + EHR import) | 10% |
| Convenience | 5% |

A **confidence discount** (×0.5 on the claim-dependent inputs) is applied to services that do not publish their individual biomarker list, so unverifiable vendor claims can't outrank services that disclose their panels.

These weights and the reference panel are **declared editorial choices**, not universal truths — the scoring engine lets anyone change them and get a different order.

## Reproduce the scores

The entire ranking comes from one script:

```bash
python3 score-membership-services.py            # ranked table
python3 score-membership-services.py --check     # per-category breakdown
python3 score-membership-services.py --value     # Value-leg (efficiency / affordability) breakdown
python3 score-membership-services.py --md        # markdown table used in the report
```

Edit the `WEIGHTS` or per-service `RAW` scores at the top of the script and re-run to see how the ranking changes.

## Rebuild the report

The web and PDF versions are generated from `report.md` with [pandoc](https://pandoc.org) + [WeasyPrint](https://weasyprint.org):

```bash
# Web page (self-contained, styled)
pandoc -f gfm-tex_math_dollars-tex_math_gfm \
  --metadata title="Membership Health Testing Services — Comparison" \
  --template build/report-template.html report.md -o index.html

# PDF (wide tables auto-rotated to landscape)
pandoc -f gfm-tex_math_dollars-tex_math_gfm --css build/report.css \
  --lua-filter build/wide-tables.lua report.md \
  -o report.pdf --pdf-engine=weasyprint
```

## Repository contents

| Path | What it is |
|---|---|
| `index.html` | The report as a styled, self-contained web page (GitHub Pages serves this) |
| `report.md` | The full report in Markdown (renders on GitHub) |
| `report.pdf` | Print/download version |
| `score-membership-services.py` | The scoring engine — single source of truth for every number |
| `research/` | Research backbone — per-service company profiles, the Hundred Health re-research, and community / third-party-comparison / biomarker-verification notes |
| `build/` | Pandoc template, print stylesheet, and Lua filter used to generate the report |

## License

Report content (report + research) is **CC BY 4.0**; the scoring engine and build tooling are **MIT**. See [LICENSE.md](LICENSE.md).

## Notes & disclaimer

This is an independent comparison for informational purposes only; it is **not medical advice** and is **not affiliated with or sponsored by** any service listed. Pricing, panels, and features change frequently — verify current details with each provider before purchasing. Figures reflect public information as of mid-2026; see the report's *Open Questions* and *Sources* sections for confidence levels and citations.
