"""
persona_generator.py — Central persona construction pipeline.

MVP behavior:
    - Combine role, traits, invariants, tensions, closures.
"""

from .role_engine import derive_role
from .trait_engine import derive_traits
from .invariants_engine import derive_invariants
from .tension_engine import derive_tensions
from .closure_engine import derive_closures


def build_persona(structure: dict) -> dict:
    """
    Build a persona from structural inputs.

    Parameters
    ----------
    structure : dict
        Input structure with fields like:
        - role
        - traits
        - worldview
        - dimensions

    Returns
    -------
    dict
        Persona structure.
    """
    role = derive_role(structure)
    traits = derive_traits(structure)
    invariants = derive_invariants(role, traits, structure)
    tensions = derive_tensions(role, traits, structure)
    closures = derive_closures(role, traits, structure)

    return {
        "role": role,
        "traits": traits,
        "invariants": invariants,
        "tensions": tensions,
        "closures": closures,
    }
