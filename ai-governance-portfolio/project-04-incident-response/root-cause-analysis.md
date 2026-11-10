# Root-cause analysis and corrective actions

**IR-001 tabletop. Root cause unproven.** A credible RCA records competing explanations and tests before assigning cause.

| Hypothesis | Discriminating test | Evidence needed | Current conclusion |
| --- | --- | --- | --- |
| Postcode feature acts as an unjustified proxy | Compare preserved model with feature ablation; match relevant credit factors | Versioned inputs, feature lineage, independent analysis | Plausible; not established |
| Input pipeline changed missing-value handling | Replay identical records through old/new transforms | Transformation versions and data-quality reports | Open |
| Population mix changed | Compare appropriately stratified cohorts and uncertainty | Representative sample and lawful subgroup data | Open |
| Monitoring query is wrong | Independent reconstruction from decision events | Query, timestamps, joins and deduplication checks | Open |
| Human overrides introduced disparity | Compare model outputs with final decisions | Reviewer action and reason records | Open |

Five-why working chain: adverse disparity → changed scoring or decisions → possible feature/pipeline/reviewer change → change controls may have omitted subgroup impact → release gates may have relied on aggregate accuracy. Each link remains a hypothesis until supported. A plausible story is not a finding.

| Action | Owner / proposed due | Closure evidence | Status |
| --- | --- | --- | --- |
| A1 Independently reconcile detection | Validation / day 1 | Matched counts and documented exclusions | Proposed |
| A2 Review affected adverse decisions | Lending / day 5 initial batch | Review outcomes and completed remedies | Proposed |
| A3 Isolate and test implicated change | Engineering and validation / day 5 | Reproducible comparative results | Proposed |
| A4 Add version-specific subgroup review to gate | Governance office / day 10 | Updated standard and release drill | Proposed |
| A5 Verify preservation and retrieval | Evidence custodian / day 2 | Hash verification, custody and access audit | Proposed |
| A6 Test restart and rollback | Operations / before restart | Independent acceptance and rollback evidence | Proposed |

Restart requires a supported cause or sufficiently bounded failure mechanism, validated correction, customer remediation plan, approved monitoring, and accountable acceptance of remaining uncertainty. A new model version alone does not close the incident. If evidence cannot reconstruct affected decisions, extend remediation scope conservatively and record the limitation.

## Tabletop assessment

Written design strengths: early containment, manual continuity, preserved versions, separate reporting clocks and explicit uncertainty. Unverified aspects: actual on-call availability, stop permissions, vendor response, evidence immutability, regulator routing and manual capacity. Next exercise should test those operational dependencies with participants; this written case does not claim that exercise occurred.
