# 06 — Performance and monitoring plan

**Synthetic plan; no model evaluation or live monitoring has occurred.** Article 15 addresses accuracy, robustness and cybersecurity. Article 72 addresses provider post-market monitoring; Article 17 concerns quality management. The deployer's local monitoring must connect to vendor processes without assuming the vendor sees all local harms.

| Indicator | Proposed frequency / owner | Trigger and response |
| --- | --- | --- |
| Invalid or unsupported inputs | Per request / platform | Route to human clarification; never infer missing facts |
| Unsupported decision criteria | Each sampled review / HR quality | Any confirmed invented criterion triggers immediate investigation and affected-case review |
| Unauthorized action or disclosure | Continuous / security | Any confirmed event triggers suspension and incident triage |
| Selection and error disparities | Weekly, where lawful and sample adequate / validation | Material unexplained disparity triggers hold and investigation; no single ratio proves fairness |
| Override and complaint patterns | Weekly / HR operations | Sudden change or repeated harm triggers case review |
| Model or integration version | Each request and release / platform | Unapproved version blocked |
| Availability and manual capacity | Daily / operations | Inability to maintain fair service triggers suspension of automated intake |

Before launch, validation must set job-specific accuracy, robustness, uncertainty and subgroup thresholds against a documented manual baseline. Acceptance criteria must be selected before testing; do not tune the test until it passes. The Project 2 ratio is an illustrative alert, not a production acceptance standard.

Provider evidence to obtain: evaluation methods, limitations, supported populations, cybersecurity testing, monitoring plan, incident contact and update process. Local evidence to create: representative evaluation, reviewer exercises, operational monitoring, rollback and customer/applicant redress pathways.

A material change or unexplained deterioration invalidates the relevant prior approval. Re-entry requires a new version-bound decision. Release remains blocked until that process and its controls are demonstrated.
