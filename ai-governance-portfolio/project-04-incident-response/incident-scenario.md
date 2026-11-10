# Incident IR-001 — scenario and evidence register

At 09:00 the fictional monitoring team receives a signal from an invented batch of 500 lending decisions: 60 of 200 applications in cluster P were approved, compared with 150 of 300 in cluster Q. Rates are 30% and 50%; ratio 0.60. Differences in qualifications, missing data, and the relation between postcode and protected characteristics are unresolved. The signal is not a causal or legal conclusion.

An assumed deployment record shows a recent postcode-derived feature change. An assumed complaint alleges that an applicant could not obtain a useful explanation. These injects justify urgent investigation and a precautionary stop; they do not prove the model caused unlawful discrimination.

| Evidence ID | Scenario material to preserve | Purpose / limitation |
| --- | --- | --- |
| E-IR-01 | Model package, version, feature transformations and configuration | Reproduce affected scoring; actual files absent in this tabletop |
| E-IR-02 | Decision IDs, inputs, scores, reasons, timestamps and human actions | Bound affected population; sensitive data requires controlled handling |
| E-IR-03 | Deployment approvals and change history | Determine authorization and divergence from validated version |
| E-IR-04 | Monitoring queries and count outputs | Validate detection; invented aggregate counts only here |
| E-IR-05 | Complaint and communications records | Understand harm and notice; fictional narrative only |
| E-IR-06 | Access and evidence-export audit trail | Establish custody; design requirement, not implemented evidence |

Incident commander provisionally assigns internal severity 1 because decisions may affect access to credit at scale. Legal separately evaluates whether the facts meet a statutory serious-incident definition. Internal severity does not automatically establish legal reportability.

The immediate objective is to prevent additional potentially harmful automated decisions while preserving applicants' access to a staffed manual process. Do not delete adverse records or retrain over the only copy of the implicated model.
