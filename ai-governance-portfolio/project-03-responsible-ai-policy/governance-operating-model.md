# Governance operating model

Synthetic design for a mid-sized regulated financial institution. Named roles below are fictional positions, not actual appointments.

| Activity | Accountable decision owner | Performs work | Independent challenge / consultation |
| --- | --- | --- | --- |
| Intended purpose and business case | Business executive | Product owner | AI risk, affected-user representatives |
| Data use and quality | Data owner | Data engineering | Privacy, Legal, validation |
| Technical controls | Technology executive | Engineering and security operations | Independent security review |
| Model evaluation | Validation head | Independent validation team | AI risk; business supplies context |
| Risk acceptance within appetite | Business executive | Governance office records | Second-line AI risk; Legal determines lawful scope |
| Enhanced release or disputed finding | Executive Risk Committee | Business presents packet | Risk presents independent opinion; Legal advises |
| Incident containment | Incident commander | Operations and engineering | Risk, Legal, privacy, business |
| Regulatory communication | Authorized legal/compliance executive | Regulatory liaison | Incident commander, vendor, relevant specialists |
| Assurance of the governance program | Audit committee | Internal audit | Risk and business provide evidence |

## Disagreement and independence

The business cannot close its own independent validation finding. Validation records whether evidence resolves the finding; second line retains its opinion and escalation right. The committee records an explicit decision, conditions and dissent. A disagreement involving law or a critical unresolved harm blocks release. Audit evaluates the process without designing or operating its controls.

## Meeting and escalation design

The governance office runs weekly case triage. The committee reviews enhanced cases monthly and urgent incidents immediately when convened. An urgent technical stop does not wait for a committee meeting. The board risk committee receives quarterly trends and material escalations, not routine configuration approvals.

Resource assumption: part-time existing Legal, security, privacy, model-validation and business roles supported by a small governance office. The design does not assume a large new ethics department. If independent validation capacity is unavailable, release remains on hold; the developer cannot replace it with self-attestation.

## Worked separation-of-duties example

HR proposes CandidateRank and owns benefits and harms. Engineering builds the isolated evaluation. Validation investigates subgroup behavior and job relevance. AI risk challenges the packet. Legal confirms the applicable rules. The committee considers DEC-003. An AI assistant can assemble evidence references, but cannot impersonate any approver or issue release authority.
