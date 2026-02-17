"""
tension_engine.py — Generate persona tensions.

MVP behavior:
    - Provide simple role-based tensions.
"""

ROLE_TENSIONS = {
    "Healer": ["harm_detected → protect"],
    "Strategist": ["uncertainty → analyze"],
    "Guardian": ["threat → defend"],
}


def derive_tensions(role: str, traits: list, structure: dict):
    """
    Determine persona tensions.

    MVP:
        - Simple lookup table.
    """
    return ROLE_TENSIONS.get(role, [])
