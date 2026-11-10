# 01 — Intended purpose and system boundary

**Synthetic deployer specification; provider confirmation required.** HB-011 v1.0 supports trained HR reviewers assessing applications for a defined set of EU analyst roles. Inputs are applicant-provided qualifications and job criteria. Outputs are source-linked relevance assessments and an ordered candidate list. The HR executive owns the purpose; the supplier must confirm the actual supported capability and limitations.

Proposed deployment: EU-hosted vendor API connected to a segregated recruitment workspace. A gateway retrieves only the assigned requisition's candidate records. The reviewer sees original documents, output, limitations, and omitted candidates. An applicant-tracking connector may store a draft assessment; it cannot reject, contact, or make an offer to an applicant. Human approval is required before any downstream decision.

Excluded purposes: biometric emotion inference, personality prediction from social media, inferred sensitive traits, autonomous rejection, cross-customer training on CVs, and reuse for credit or employee performance scoring. These are design restrictions; actual enforcement remains untested.

Provider dependencies to obtain: model family and version, component versions, supported languages and input formats, interface contract, operational requirements, intended-user instructions, cybersecurity dependencies, deployment architecture and known failure modes. Those facts are absent and must not be guessed.

The vendor supplies the intended-purpose and technical description relevant to Article 11 and Annex IV. HarborBridge documents its local integration and permitted use. A change in role, country, job family, ranking method, data source or action capability requires renewed assessment. Success is defined as assisting consistent, explainable review without reducing applicants' ability to receive a fair human assessment; no measured improvement is claimed.
