"""
trait_engine.py — Determine persona traits.

MVP behavior:
    - Normalize trait list.
    - Ensure deterministic ordering.
"""

def derive_traits(structure: dict):
    traits = structure.get("traits", [])
    if not isinstance(traits, list):
        return []

    # Normalize + deterministic ordering
    normalized = [str(t).strip().lower() for t in traits]
    return sorted(normalized)
