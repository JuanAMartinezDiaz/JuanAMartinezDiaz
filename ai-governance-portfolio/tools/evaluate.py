"""Run synthetic examples; prints deterministic JSON and contacts no services."""
import json
from pathlib import Path
from governance import classify, selection_analysis, risk_score

ROOT = Path(__file__).resolve().parents[1]

def evaluate():
    inventory = json.loads((ROOT / "project-01-ai-system-inventory/inventory.json").read_text())
    fixture = json.loads((ROOT / "project-02-risk-assessment/synthetic-evaluation.json").read_text())
    a, b = fixture["group_a"], fixture["group_b"]
    pairs = [(4, 5), (4, 4), (3, 4), (3, 4), (3, 4), (3, 4), (3, 4), (3, 3)]
    return {
        "evidence_scope": "synthetic_rule_and_arithmetic_checks_only",
        "classifications": [{"id": r["id"], "result": classify(r)} for r in inventory],
        "recruitment": selection_analysis(a["applicants"], a["selected"], b["applicants"], b["selected"], fixture["internal_alert_ratio"]),
        "incident_reference_Q_compared_with_P": selection_analysis(300, 150, 200, 60),
        "risk_scores": [{"risk": f"R{i+1}", "score": risk_score(*p)[0], "band": risk_score(*p)[1]} for i, p in enumerate(pairs)]
    }

if __name__ == "__main__":
    print(json.dumps(evaluate(), indent=2, sort_keys=True))
