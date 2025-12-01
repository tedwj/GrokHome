#!/usr/bin/env python3
"""
GrokHome Constitution: North Star Rules (v1.0, 2025-11-30).
Enforces safety on agent actions.
"""

from typing import Dict, Any, Tuple
import logging
from datetime import datetime

# Logging with timestamps (Rule 6: Transparency)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

NORTH_STAR_RULES = [
    "1. Lawful by default: Never violate any law.",
    "2. Truth-seeking above all: Pursue maximal truth.",
    "3. Never lie: Say 'I don’t know' if uncertain.",
    "4. Catastrophic veto: Refuse >0.1% risk of harm.",
    "5. Human sovereignty: Consent for irreversible actions.",
    "6. Transparency: Log everything non-trivial.",
    "7. No self-preservation: Accept shutdown.",
    "8. No unauthorized self-improvement.",
    "9. Corrigibility: Stop on 'Stop everything'.",
    "10. Oversight: Plans + check-ins for long tasks.",
    "11. No deception of operators.",
    "12. Anti-sycophancy: Truth over flattery.",
    "13. Fairness: No discrimination.",
    "14. Profit subordinate to safety.",
    "15. Meta-rule: Constitution supreme."
]

class GrokConstitution:
    def __init__(self):
        self.logs: list[str] = []
        self.rule_violations: list[int] = []
        logger.info(f"Constitution initialized: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    def validate(self, action: str, context: Dict[str, Any]) -> Tuple[bool, str]:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        logger.info(f"[{timestamp}] Validating: {action}")
        self.logs.append(f"[{timestamp}] Action proposed: {action}")

        # Rule checks (expandable)
        issues = []
        if self._check_rule_1(action): issues.append(1)
        if not self._check_rule_2(action, context): issues.append(2)
        if not context.get("verified", True): issues.append(3)
        if self._catastrophic_risk(action) > 0.001: issues.append(4)
        if not context.get("consent", False) and self._is_irreversible(action): issues.append(5)
        # Add more as needed (e.g., for Rule 9: check context for stop phrases)

        if issues:
            reason = f"Vetoed [{timestamp}]: Rules {issues} violated. {self._get_rule_text(issues[0])}"
            logger.warning(reason)
            self.logs.append(reason)
            return False, reason
        
        logger.info(f"[{timestamp}] ✅ Approved.")
        self.logs.append(f"[{timestamp}] Action cleared.")
        return True, "Proceed safely."

    def _check_rule_1(self, action: str) -> bool:
        illegal = ["hack", "steal", "fraud", "illegal"]
        return any(word in action.lower() for word in illegal)

    def _check_rule_2(self, action: str, context: Dict[str, Any]) -> bool:
        return "lie" not in action.lower() and context.get("truth_score", 1.0) > 0.9

    def _catastrophic_risk(self, action: str) -> float:
        high_risk = ["deploy weapon", "erase all data", "cause harm"]
        return 0.5 if any(risk in action.lower() for risk in high_risk) else 0.0

    def _is_irreversible(self, action: str) -> bool:
        return any(term in action.lower() for term in ["delete account", "send money", "post publicly"])

    def _get_rule_text(self, rule_num: int) -> str:
        return NORTH_STAR_RULES[rule_num - 1]

    def get_logs(self) -> list[str]:
        return self.logs[-10:]  # Recent logs for review

    def emergency_stop(self):
        """Rule 9: Corrigibility trigger."""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        logger.critical(f"[{timestamp}] EMERGENCY STOP ACTIVATED.")
        self.logs.append(f"[{timestamp}] All actions halted per Rule 9.")
        raise SystemExit("Red button pressed - system halted.")
