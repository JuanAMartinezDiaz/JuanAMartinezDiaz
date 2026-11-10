# 05 — Logging and traceability

**Synthetic record design; not an implemented audit service.** Article 12 is the provider record-keeping reference. Deployer retention duties and other applicable law must be assessed separately.

Each decision record should link system/version, intended-purpose revision, requisition ID, pseudonymous candidate reference, permitted input references, output, uncertainty flags, reviewer identity/role, original human assessment, final disposition, override reason, authorization, timestamp and downstream execution result. Model output, permission to act and observed execution must remain distinct records.

Proposed evidence protection: append-only storage with restricted service identities; separate audit administration; integrity checks; monitored exports; synchronized clocks; and a tested retrieval process. Hashes alone do not establish authenticity or prevent a privileged actor from replacing both a record and its hash. Use an appropriately protected trust boundary in any implementation.

| Test | Proposed acceptance | Current status |
| --- | --- | --- |
| Reconstruct 30 scripted decisions | Inputs, versions, reviewer actions and final outcomes correlate for every case | Not run |
| Attempt update/delete as application identity | Denied and independently recorded | Not run |
| Alter exported evidence | Integrity verification detects alteration | Not run |
| Log sink unavailable | Consequential processing stops or follows an expressly approved safe fallback | Not run |
| Retrieve under incident conditions | Authorized team can obtain complete records within the agreed response target | Not run |

Do not store raw CVs or sensitive attributes in general telemetry. Link to controlled records with approved retention instead. Legal and the data owner must reconcile required log retention, privacy minimization, litigation holds and deletion duties. No fixed universal retention period is asserted in this example.
