# Classification rationale

**Synthetic facts; baseline checked 10 November 2026.** All ten cases assume EU use. Proposed classification does not establish compliance or permission to operate. [Sources](../SOURCES.md) identify the legal baseline.

| ID | System | Conclusion | Rationale and next decision |
| --- | --- | --- | --- |
| HB-001 | CreditGuide | High-risk | Natural-person creditworthiness; Annex III 5(b). Require enhanced review, including applicable rights-impact assessment and lending obligations. |
| HB-002 | FraudWatch | No high-risk category identified in stated scope | Financial-fraud detection only; explicit 5(b) exclusion. Any reuse for eligibility or credit scoring requires new assessment. Internal risk remains high. |
| HB-003 | CandidateRank | High-risk | Candidate ranking materially influences recruitment; Annex III 4(a). Human final selection does not remove the category. Project 2 recommends hold. |
| HB-004 | ServiceDesk Chat | No high-risk category identified in stated scope | FAQs only, with no eligibility decisions or account actions. Evaluate Article 50 disclosure separately; security and accuracy review still required. |
| HB-005 | PolicySearch | No high-risk category identified in stated scope | Internal source-linked retrieval, no personnel evaluation or decision execution. Access-control and hallucination risks remain. |
| HB-006 | LifeQuote | High-risk | Risk assessment and pricing of life insurance for natural persons; Annex III 5(c). Enhanced review required. |
| HB-007 | EmotionHire | Prohibited on stated facts | Biometric emotion inference during workplace interviews, without medical or safety purpose; Article 5(1)(f). Reject procurement. |
| HB-008 | PaymentDraft | No high-risk category identified in stated scope | Draft payment instructions only; no signing or submission. Internal risk high; any proposed execution capability triggers fresh authority review. |
| HB-009 | CandidateExtract | Review required | Proposed narrow CV extraction could be preparatory, but material influence and profiling facts are unknown. Do not assume Article 6(3) applies. |
| HB-010 | NetworkOptimizer | Review required | Unclear whether it is a safety component in critical digital infrastructure. Obtain architecture and failure-impact analysis before classification. |

## Decision sequence and limitations

First establish whether the system and territorial scope fall within the Act; then screen prohibitions, Annex I and Annex III, specific exceptions, and additional duties. The executable demonstration assumes the first scope assessment and models only these ten categories. It is not an exhaustive legal engine. It does not determine transition treatment or reporting duties.

An unknown value yields review. Evidence supporting an exception must be documented by the responsible party and reviewed; a vendor's “low risk” label is not evidence. A narrow task that becomes profiling or materially influences recruitment must be reassessed. Separately record transparency, data protection and sectoral controls.

Decision owner: business executive. Legal supplies interpretation; second-line AI risk challenges completeness and consistency. Neither the vendor nor the automated classifier can self-approve deployment. Reassess at every material purpose, data, geography, authority or model change.
