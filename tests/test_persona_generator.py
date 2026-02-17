import pytest
from wlm_persona_engine.api import generate_persona


def test_generate_persona_basic():
    structure = {
        "role": "strategist",
        "traits": ["analytical", "calm"]
    }

    persona = generate_persona(structure)

    assert isinstance(persona, dict)
    assert persona["role"] == "Strategist"
    assert persona["traits"] == ["analytical", "calm"]
    assert "invariants" in persona
    assert "tensions" in persona
    assert "closures" in persona
