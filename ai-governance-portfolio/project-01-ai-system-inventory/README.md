# Project 1 — AI inventory and classification

**Worked synthetic example.** HarborBridge has discovered ten AI use cases through assumed procurement records, architecture reviews, and business-owner attestations. No discovery scan was actually performed. The objective is to route each use case to the right review without treating every system as the same risk.

## Artifacts

- [Structured inventory](inventory.json): machine-readable scenario facts, owners, purposes, authority, data, and decision inputs.
- [Classification rationale](eu-ai-act-classification.md): conclusions and boundaries for every system.
- [NIST gap map](nist-rmf-mapping.md): gaps, owners, evidence and closure targets.
- [Executable triage](../tools/governance.py): deliberately bounded rule logic; legal review remains required.

## Inventory management decision

Procurement must obtain an inventory ID before contracting for AI use. Architecture must record model and integration versions before pilot access. Each owner attests quarterly and after material change; the governance office reconciles procurement, approved applications, and exception records monthly. An unregistered use case receives no live-data access until triage is complete.

The ten records contain three high-risk cases, one prohibited scenario, four cases with no high-risk category identified within their stated scope, and two cases requiring further review. These are scenario classifications, not deployment approvals. The financial-fraud example is internally high risk even though the stated use is excluded from the creditworthiness category.

## Acceptance

Every record needs a unique ID, accountable role, intended purpose, geographic scope, data description, authority boundary, vendor/version and review trigger. The automated evaluator must preserve uncertainty and reject unsupported inputs. The source exercise uses CSV; this project uses JSON so nested decision facts can be checked without losing meaning.
