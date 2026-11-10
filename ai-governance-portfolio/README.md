# AI Governance Portfolio — Five Applied Projects

**Juan A. Martinez Diaz, MBA · Financial-services governance case studies · 10 November 2026**

These projects examine how a fictional financial-services organization discovers AI use, challenges risk, assigns decision authority, responds to harm, and determines whether evidence supports deployment.

**Evidence status:** original, AI-assisted synthetic work prepared for this portfolio. Organizations, vendors, people, transactions, approvals, and incident events are fictional. Documents are completed worked examples; proposed operational controls are not represented as implemented. Executable checks verify only the supplied synthetic logic and arithmetic. Juan's personal review and interview walkthrough remain pending. This is not employer work, a regulatory filing, a certification, or proof of production effectiveness.

## Start here

| Project | Decision demonstrated | Inspectable work |
| --- | --- | --- |
| [1. Inventory and classification](project-01-ai-system-inventory/README.md) | Which use cases need enhanced review, prohibition, or further facts? | Ten-system register, classification rationale, bounded executable triage, NIST gap map |
| [2. Risk assessment](project-02-risk-assessment/README.md) | Should a recruitment ranking system proceed? | Scored risk assessment, reproducible synthetic disparity analysis, executive hold decision |
| [3. Policy and operating model](project-03-responsible-ai-policy/README.md) | Who owns risk, who challenges it, and who can approve? | Policy, lifecycle gates, escalation process, separation of duties |
| [4. Incident response](project-04-incident-response/README.md) | What happens when a credit model harms applicants? | Tabletop timeline, evidence preservation, reporting decision log, root-cause hypotheses |
| [5. High-risk documentation](project-05-high-risk-documentation/README.md) | Is a replacement hiring system ready? | Six documentation modules, provider/deployer evidence matrix, Annex IV index, blocked release decision |

**Five-minute employer review:** read the Project 2 executive memo, inspect its calculation and risk register, then read the Project 5 release gate. These show how evidence changes a decision. For control ownership and independent challenge, use Project 3.

## Common scenario

HarborBridge Financial Services is a fictional EU financial institution with lending, insurance, and recruitment functions. The scenario assumes relevant EU territorial scope and a 2028 proposed deployment for new high-risk systems. Project 4 is a fictional 2028 tabletop. These future dates are scenario dates, not actual events or predictions about future law. The legal baseline is the official material available on 10 November 2026; it must be refreshed before any real deployment.

The series uses NIST AI RMF 1.0 as a voluntary risk-management framework. EU legal classification and internal operational risk are separate fields. A use case outside an Annex III category can still require stringent security, privacy, or business controls.

## Reproduce the executable evidence

Requires Python 3.10+; standard library only. From this directory:

```bash
python3 -m unittest discover -s tests -v
python3 tools/evaluate.py
```

The evaluator emits classification results and recruitment selection-rate arithmetic as JSON. No model is trained, no external service is contacted, and no personal data is used. The classifier handles only the explicitly modeled scenario categories; unknown facts produce review, never automatic clearance.

See [verification](VERIFICATION.md), [sources and corrections](SOURCES.md), and [interview walkthrough](INTERVIEW.md).

## Attribution and original contribution

The five-project learning structure was inspired by [Taimur Ijlal / The Cloud Security Guy's AIGovernance repository](https://github.com/taimurijlal/AIGovernance), reviewed at revision `d5eb5a497f43135e6410e0c6384896fd23524af4`. Its five project READMEs supplied the exercise objectives. No license file was present in the inspected tree, so its completed artifacts were not copied or republished.

This implementation supplies a new fictional organization, original records and analysis, explicit evidence states, reproducible checks, updated legal references, and a second-line challenge model. JSON replaces the source example's CSV inventory to preserve structured decision inputs and feed reproducible checks. The documents are readable directly on GitHub.

Sentinel remains a [separate executable reference](https://github.com/JuanAMartinezDiaz/sentinel-governed-workflow-twin). These projects neither assert that Sentinel implements their controls nor use its test counts as evidence for this work.
