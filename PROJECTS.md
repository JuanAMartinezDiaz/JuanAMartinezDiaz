# Project portfolio

Updated November 9, 2026.

I am Juan A. Martinez Diaz, founder of **Bounded Agentic Intelligence (BAI)**. My current work focuses on Sentinel: understanding a workflow, identifying where AI may help, setting authority boundaries, and preserving evidence to evaluate the result.

## Start with the case study

The [Sentinel case study](https://www.juanmartinez.ai/sentinel-case-study/) explains how I defined the workflow governance problem, developed the control and validation approach, and directed prototype development. Review the [NIST outcome-to-control-and-test mapping](https://github.com/JuanAMartinezDiaz/sentinel-governed-workflow-twin/blob/main/docs/framework-alignment.md) and [November 9 verification](https://github.com/JuanAMartinezDiaz/sentinel-governed-workflow-twin/blob/main/docs/verification-2026-11-09.md) alongside the implementation. These materials demonstrate independent applied work in a synthetic reference environment.

## Sentinel Governed Workflow Twin

**Status: public synthetic reference implementation. Proprietary production readiness is not established by this repository.**

[Source](https://github.com/JuanAMartinezDiaz/sentinel-governed-workflow-twin) · [Interactive reference visualization](https://juanamartinezdiaz.github.io/sentinel-governed-workflow-twin/) · [Run the Python demo](https://github.com/JuanAMartinezDiaz/sentinel-governed-workflow-twin/blob/main/RUN_DEMO.md)

| Risk or question | Reference control | Inspectable evidence |
| --- | --- | --- |
| Can an unregistered or over-delegated agent act? | Identity, delegated action, tool and risk-ceiling checks | Arbitration tests and control trace |
| Can a consequential action proceed without approval? | Approval gate and action-bound execution permit | Missing-approval and protected-execution tests |
| Can an action be changed after authorization? | HMAC permit and action-fingerprint binding | Permit-tampering and payload-binding tests |
| Does authorization prove execution occurred? | Decision IDs correlate policy/authority snapshots with observed execution events | JSON evidence package with blocked, successful and failed outcomes |
| Did a proposed workflow redesign help? | Baseline-to-redesign comparison | Synthetic metrics clearly labeled illustrative |

**Verified evidence:** [75 Python tests and 18 browser-client tests passed on November 9, 2026](https://github.com/JuanAMartinezDiaz/sentinel-governed-workflow-twin/blob/main/docs/verification-2026-11-09.md), against runtime revision `b66ba2c6fa0e39e16f57e3e1e0102d610f6653b5`. The report records the environment, initial setup issues, and limits. The [October 20 CI run](https://github.com/JuanAMartinezDiaz/sentinel-governed-workflow-twin/actions/runs/39463516644) remains historical evidence; neither result establishes that future revisions pass.

**Limits:** approval is a caller assertion, risk and confidence are declared inputs, and in-process signing does not isolate the boundary from malicious code in the same process. Production use requires authenticated approval, deployment-specific isolation, protected evidence storage, and operational acceptance.

### Current acceptance roadmap

| Workstream | Current public basis | Exit evidence |
| --- | --- | --- |
| Complete owner journey | [Issue 3](https://github.com/JuanAMartinezDiaz/sentinel-governed-workflow-twin/issues/3); acceptance pending | Dated end-to-end evidence for the actual proprietary build |
| Synthetic workflow ingestion | [Issue 4](https://github.com/JuanAMartinezDiaz/sentinel-governed-workflow-twin/issues/4); design specification | Validated workflow representation, provenance, unknowns and owner review |
| Fidelity and scenario coverage | [Issue 5](https://github.com/JuanAMartinezDiaz/sentinel-governed-workflow-twin/issues/5); acceptance specification | Six deterministic fixtures and traceable findings on the actual deployment |
| Optional maturity assessment | [Issue 6](https://github.com/JuanAMartinezDiaz/sentinel-governed-workflow-twin/issues/6); planned | Evidence-backed rubric and reproducible tests before exposure |
| Release decision | [Readiness framework](https://github.com/JuanAMartinezDiaz/sentinel-governed-workflow-twin/blob/main/docs/release-readiness-framework.md) | Named reviewer, accepted limitations and explicit release decision |

## Decision X-Ray and JuanMartinez.ai

**Status: public publishing and interactive visualization.**

[Website](https://www.juanmartinez.ai) · [Source](https://github.com/JuanAMartinezDiaz/juanmartinez-ai-site)

Decision X-Ray makes the proposal, authorization, approval, permit, action and evidence path visible. The visualization supports explanation; it does not itself establish backend enforcement. The website repository also contains AI governance writing and AI Build Lab work.

## GuidedWork AI and ProAgent Local

**Status: early product and agent-configuration prototypes.**

[Source](https://github.com/JuanAMartinezDiaz/guidedwork-ai-beta)

Explores explicit role, mission, autonomy, memory and permission configuration with JSON profile export. Local-model integration and stronger execution boundaries remain roadmap items.

## Career Rebuild Navigator

**Status: career-support workflow prototype with browser-based rule logic.**

[Current workflow source](https://github.com/JuanAMartinezDiaz/career-rebuild-navigator-vercel) · [Earlier prototype](https://github.com/JuanAMartinezDiaz/career-rebuild-navigator)

Explores job-fit review, CV review, application preparation and case management with human review. The current README identifies LLM integration as planned; this portfolio does not present the rule-based MVP as a deployed LLM agent.

## Review standard

Here is the risk, here is how Sentinel constrains it, and here is the evidence from the test.

Public examples use synthetic data. Private repositories, proprietary implementation details, credentials, and employer or client records are outside this portfolio.
