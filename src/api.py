"""
High‑level API for WLM‑Persona‑Engine.

This module exposes a single entry point:

    generate_persona(structure) -> Persona

MVP behavior:
    - Returns a deterministic persona structure.
"""

from .persona_generator import build_persona


def generate_persona(structure: dict) -> dict:
    """
    Generate a deterministic persona from structural inputs.

    Parameters
    ----------
    structure : dict
        Input structure containing role, traits, worldview, etc.

    Returns
    -------
    dict
        Persona structure.
    """
    return build_persona(structure)
