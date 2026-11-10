# 03 — Data governance

**Synthetic data specification. No real CVs or protected-attribute records are present.** Article 10 informs the provider evidence request; privacy obligations need a separate lawful-basis assessment.

| Data stage | Required control | Owner and evidence state |
| --- | --- | --- |
| Provider training | Obtain provenance, permitted use, population coverage, labeling and known gaps | Provider; evidence absent |
| Local evaluation | Separate frozen holdout from tuning; record job relevance and language coverage | Validation; plan only |
| Production inputs | Limit to approved requisition and necessary applicant-provided fields | HR/data owner; specification only |
| Subgroup evaluation | Establish lawful, segregated access and justified metrics before processing sensitive data | Privacy and validation; unresolved |
| Output storage | Keep source references, review decisions and correction history | HR/platform; untested |
| Retention and deletion | Set jurisdiction-specific schedules, legal holds and verified deletion | Data owner with Legal; schedule pending |

Proposed quality checks: required-field completeness, valid formats, duplicates, language support, provenance, inconsistent dates, and out-of-scope attachments. Missing information triggers reviewer clarification; the system must not invent qualifications or treat an accommodation as negative evidence.

The provider must distinguish training, validation and test populations and document leakage controls. HarborBridge must not accept “representative data” without a defined target population and coverage analysis. Local evaluation must examine error burdens and uncertainty rather than only overall accuracy.

The aggregate groups in Project 2 are invented calculation fixtures. They are not training data, a representative hiring sample, or proof that a bias control works. No live dataset is authorized by this portfolio.

Release blocker: provenance, local coverage, lawful data handling and retention remain unverified. The data owner cannot close those gaps with this design document.
