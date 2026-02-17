"""
role_engine.py — Determine persona role structure.

MVP behavior:
    - Normalize role name.
    - Provide deterministic fallback.
"""

def derive_role(structure: dict) -> str:
    role = structure.get("role")
    if not role:
        return "Undefined"

    # Normalize capitalization
    return str(role).strip().title()
