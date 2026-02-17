"""
closure_engine.py — Generate persona closures (future identity states).

MVP behavior:
    - Provide simple role-based closures.
"""

ROLE_CLOSURES = {
    "Healer": ["future_harm → prepare_heal"],
    "Strategist": ["future_conflict → plan"],
    "Guardian": ["future_threat → fortify"],
}


def derive_closures(role: str, traits: list, structure: dict):
    """
    Determine persona closures.

    MVP:
        - Simple lookup table.
    """
    return ROLE_CLOSURES.get(role, [])
