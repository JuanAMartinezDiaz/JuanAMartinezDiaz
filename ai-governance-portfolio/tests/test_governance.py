import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from governance import classify, selection_analysis, risk_score, REVIEW, HIGH_RISK, NONE, PROHIBITED


class ClassificationTests(unittest.TestCase):
    def test_known_inventory_decisions(self):
        rows = json.loads((ROOT / "project-01-ai-system-inventory/inventory.json").read_text())
        expected = [HIGH_RISK, NONE, HIGH_RISK, NONE, NONE, HIGH_RISK, PROHIBITED, NONE, REVIEW, REVIEW]
        self.assertEqual([classify(r) for r in rows], expected)
        self.assertEqual(len({r["id"] for r in rows}), 10)

    def test_unknown_use_never_clears(self):
        self.assertEqual(classify({"eu_scope": True, "purpose_code": "unknown"}), REVIEW)

    def test_scope_unknown_and_outside_scope_are_not_eu_clearance(self):
        for scope in (None, False, "true"):
            self.assertEqual(classify({"eu_scope": scope, "purpose_code": "candidate_ranking"}), REVIEW)

    def test_human_review_does_not_remove_recruitment_category(self):
        self.assertEqual(classify({"eu_scope": True, "purpose_code": "candidate_ranking", "human_review": True}), HIGH_RISK)

    def test_fraud_repurposing_requires_review(self):
        for value in (True, None, "false"):
            self.assertEqual(classify({"eu_scope": True, "purpose_code": "fraud_detection_only", "credit_decision_reuse": value}), REVIEW)

    def test_emotion_exception_is_not_automatic_clearance(self):
        for value in (True, None):
            self.assertEqual(classify({"eu_scope": True, "purpose_code": "workplace_biometric_emotion", "medical_safety_exception": value}), REVIEW)

    def test_unconfirmed_boundary_requires_review(self):
        self.assertEqual(classify({"eu_scope": True, "purpose_code": "payment_draft_only"}), REVIEW)


class MeasurementTests(unittest.TestCase):
    def test_recruitment_fixture(self):
        r = selection_analysis(100, 60, 100, 36)
        self.assertAlmostEqual(r["b_to_a_ratio"], .6)
        self.assertAlmostEqual(r["b_minus_a_percentage_points"], -24)
        self.assertTrue(r["alert"])

    def test_equal_rates(self):
        self.assertFalse(selection_analysis(100, 50, 200, 100)["alert"])

    def test_zero_reference_requires_review(self):
        r = selection_analysis(100, 0, 100, 10)
        self.assertIsNone(r["b_to_a_ratio"])
        self.assertTrue(r["alert"])

    def test_invalid_counts_rejected(self):
        for args in [(0, 0, 100, 10), (100, 101, 100, 10), (100, -1, 100, 10), (100, 2.5, 100, 10), (True, 1, 100, 10)]:
            with self.assertRaises(ValueError):
                selection_analysis(*args)

    def test_invalid_thresholds_rejected(self):
        for t in (0, 2, float("nan"), float("inf"), True):
            with self.assertRaises(ValueError):
                selection_analysis(100, 50, 100, 40, t)

    def test_risk_band_boundaries(self):
        for l, i, expected in [(1, 4, (4, "low")), (1, 5, (5, "moderate")), (2, 5, (10, "high")), (4, 4, (16, "high")), (4, 5, (20, "critical"))]:
            self.assertEqual(risk_score(l, i), expected)

    def test_invalid_ordinal_scores(self):
        for pair in [(0, 5), (6, 1), (True, 3), (2.5, 4)]:
            with self.assertRaises(ValueError):
                risk_score(*pair)

if __name__ == "__main__":
    unittest.main()
