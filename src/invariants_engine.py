"""
invariants_engine.py — Generate persona invariants.

MVP behavior:
    - Provide simple role-based invariants.
"""

ROLE_INVARIANTS = {
    "Healer": ["non-violence"],
    "Strategist": ["calm-decision-making"],
    "Guardian": ["protect-others"],
}


def derive_invariants(role: str, traits: list, structure: dict):
    """
    Determine persona invariants based on role and traits.

    MVP:
        - Simple lookup table.
    """
    return ROLE_INVARIANTS.get(role, [])
