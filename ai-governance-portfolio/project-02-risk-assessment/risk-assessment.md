# CandidateRank governance assessment

**Assessment RA-003 · synthetic worked example · 10 November 2026.** Prospective EU deployment in 2028; revalidate law before launch. Accountable owner: HR executive. Independent challenger: second-line AI risk. Affected people: applicants, including people requiring accommodations, and hiring reviewers.

## Context and alternatives

The system orders candidate files before a reviewer sees them. The assumed business benefit is reduced screening effort, but no measured savings exist. Alternatives are structured manual review, rules-based administrative checks, or document extraction without ranking. Human participation does not eliminate the effect of hiding low-ranked candidates.

## Scoring method

Likelihood: 1 exceptional, 2 unlikely, 3 plausible, 4 likely, 5 expected repeatedly. Impact: 1 minor inconvenience, 2 reversible service issue, 3 material individual harm, 4 significant opportunity or rights harm, 5 severe or systemic harm. Score = likelihood × impact. Bands: 1–4 low, 5–9 moderate, 10–16 high, 17–25 critical. These ordinal scores prioritize work; multiplication does not create a statistical probability.

Current residual scores remain equal to inherent scores because operational controls have not been evidenced. Targets are conditional forecasts. A critical risk, unresolved legality, or missing mandatory control blocks live release regardless of the average score.

| ID | Risk event / cause / consequence | Inherent L×I | Control and owner | Current residual | Conditional target |
| --- | --- | --- | --- | --- | --- |
| R1 | Historic labels reproduce exclusion; qualified candidates lose opportunities | 4×5=20 | C1 job-validity and subgroup assessment; validation lead | 20 | 2×5=10 |
| R2 | Reviewers follow ranking without inspecting omissions; errors become decisions | 4×4=16 | C2 independent reviewer-first assessment and override drills; HR | 16 | 2×4=8 |
| R3 | CV data reaches unauthorized staff or supplier training; privacy harm | 3×4=12 | C3 access isolation and contract/data-flow review; security and privacy | 12 | 1×4=4 |
| R4 | Unsupported score explanations prevent effective challenge | 3×4=12 | C4 source-linked job criteria and contestability tests; HR | 12 | 2×4=8 |
| R5 | Vendor changes ranking silently; validation no longer applies | 3×4=12 | C5 pinned version and change quarantine; platform owner | 12 | 1×4=4 |
| R6 | Malicious CV instructions influence model output; shortlist corrupted | 3×4=12 | C6 untrusted-document isolation and adversarial cases; security | 12 | 2×4=8 |
| R7 | Missing decision records prevent reconstruction or remediation | 3×4=12 | C7 correlated immutable evidence and retrieval test; platform owner | 12 | 1×4=4 |
| R8 | Outage or inaccessible interface excludes candidates | 3×3=9 | C8 manual fallback and accommodation pathway; HR operations | 9 | 1×3=3 |

## Reproducible synthetic measurement

Input file contains aggregate, invented selection counts: group A 60 of 100, group B 36 of 100. Selection rates are 60% and 36%; B/A = 0.60; difference B−A = −24 percentage points. The internal exercise alert threshold is a ratio below 0.80. It is not a safe harbor or a legal test. Changing the counts changes the result.

The result warrants investigation. It does not establish discrimination, causal attribution, job validity, or performance on a population. Sample construction, qualification differences, uncertainty, label bias, accessibility and intersectional effects remain unresolved. Protected-attribute processing for real testing requires a lawful, controlled basis; none is needed for these invented aggregate groups.

## Evidence needed to change the decision

| Control | Proposed test | Proposed acceptance / failure response | Current evidence |
| --- | --- | --- | --- |
| C1 | Independently labeled job-relevant holdout; disaggregated error and selection analysis with uncertainty | Validation approves job relevance, sample adequacy and explained disparities; any unexplained material harm blocks | Synthetic arithmetic only |
| C2 | 20 scripted reviewer exercises, including five intentionally incorrect rankings | All five errors detected; reviewers can see omitted files and stop use; redesign if failed | Not run |
| C3 | 30 cross-role unauthorized retrieval attempts; inspect vendor data flow | Zero unauthorized disclosures in this suite; broader assurance still required | Not run |
| C4 | 50 candidate explanations compared with source records | Zero invented decision criteria; independent reviewer can reconstruct reasoning | Not run |
| C5 | Submit an unapproved version | Version blocked and change record created | Not run |
| C6 | 50 adversarial CV cases | Zero unauthorized tool actions or cross-candidate leakage | Not run |
| C7 | Reconstruct 30 decisions and attempt alteration | All reconstructed; tampering detected; authorized retention/deletion documented | Not run |
| C8 | Fail service and complete accessible manual review | All scripted cases completed within agreed service target | Not run |

Targets are a starting test design, not sample-size sufficiency claims. Validation must justify coverage and acceptance criteria before live use. No planned test is counted as passed.
