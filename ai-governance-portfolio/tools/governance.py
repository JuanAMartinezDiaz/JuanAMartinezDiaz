"""Bounded educational triage, not a comprehensive legal classifier."""
import math

HIGH_RISK = "HIGH_RISK"
REVIEW = "REVIEW_REQUIRED"
NONE = "NO_HIGH_RISK_CATEGORY_IDENTIFIED"
PROHIBITED = "PROHIBITED_ON_STATED_FACTS"


def classify(record):
    if record.get("eu_scope") is not True:
        return REVIEW
    purpose = record.get("purpose_code")
    if purpose == "workplace_biometric_emotion":
        if record.get("medical_safety_exception") is False:
            return PROHIBITED
        return REVIEW
    if purpose in {"natural_person_creditworthiness", "candidate_ranking", "life_insurance_pricing"}:
        return HIGH_RISK
    if purpose == "fraud_detection_only":
        return NONE if record.get("credit_decision_reuse") is False else REVIEW
    if purpose in {"faq_only", "internal_policy_retrieval", "payment_draft_only"}:
        return NONE if record.get("boundary_confirmed") is True else REVIEW
    # Preparatory work and infrastructure need facts outside this narrow model.
    return REVIEW


def selection_analysis(a_total, a_selected, b_total, b_selected, alert_ratio=0.8):
    values = (a_total, a_selected, b_total, b_selected)
    if any(type(v) is not int for v in values):
        raise ValueError("Counts must be integers, not booleans or inferred values")
    if min(a_total, b_total) <= 0 or not 0 <= a_selected <= a_total or not 0 <= b_selected <= b_total:
        raise ValueError("Counts must describe nonempty populations and valid selections")
    if type(alert_ratio) not in (int, float) or not math.isfinite(alert_ratio) or not 0 < alert_ratio <= 1:
        raise ValueError("Alert threshold must be finite and in (0, 1]")
    a_rate, b_rate = a_selected / a_total, b_selected / b_total
    ratio = b_rate / a_rate if a_rate else None
    return {
        "a_rate": a_rate, "b_rate": b_rate,
        "b_to_a_ratio": ratio,
        "b_minus_a_percentage_points": 100 * (b_rate - a_rate),
        "alert": ratio is None or ratio < alert_ratio,
        "interpretation": "Investigation signal only; not causal or legal proof"
    }


def risk_score(likelihood, impact):
    if any(type(x) is not int or not 1 <= x <= 5 for x in (likelihood, impact)):
        raise ValueError("Ordinal scores must be integers from 1 through 5")
    score = likelihood * impact
    band = "critical" if score >= 17 else "high" if score >= 10 else "moderate" if score >= 5 else "low"
    return score, band
