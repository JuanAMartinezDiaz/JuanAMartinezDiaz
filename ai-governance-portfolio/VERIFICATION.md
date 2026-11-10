# Verification record

Date: 10 November 2026. Environment: managed Linux workspace, Python standard library.

## Observed results

- `python3 -m unittest discover -s tests -v`: **14 tests passed**.
- `python3 tools/evaluate.py`: completed successfully; [recorded output](verification-output.json).
- Inventory: 10 unique system IDs; 3 high-risk, 1 prohibited on stated facts, 4 with no high-risk category identified within scope, 2 requiring review.
- Recruitment calculation: 60% and 36% selection rates; ratio 0.60; difference −24 percentage points.
- Incident calculation: reference cluster Q 50%, cluster P 30%; P/Q ratio 0.60; difference −20 percentage points.
- Risk calculations: one critical, six high, one moderate; current residual scores receive no credit for untested controls.

Tests address unknown inputs, purpose changes, a claimed emotion-recognition exception, human-review classification, invalid numeric inputs, zero denominators and score boundaries. They establish behavior of the small demonstration program only.

## Review limits

No vendor model, recruitment system, credit model, access-control gateway, immutable logging service, or live monitoring service was tested. No human tabletop participants were convened. No legal opinion, certification or conformity assessment was obtained. No employer or customer information was used. No signatures or approvals were fabricated.

The documents contain completed analysis of fictional facts and proposed control designs. Planned operational tests remain explicitly marked not run. Juan's personal review and interview defense remain pending. Repository publication makes the work inspectable; it does not change these evidence limits.

## Reproduction

Run the two commands from the portfolio root with Python 3.10 or newer. No external dependencies or network access are required. The checked-in output is deterministic; compare regenerated JSON with the recorded output. Git commit history identifies the exact artifact revision.
