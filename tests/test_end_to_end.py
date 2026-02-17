import pytest
from wlm_persona_engine.api import generate_persona


def test_end_to_end_persona_generation():
    structure = {
        "role": "guardian",
        "traits": ["brave", "loyal"]
    }

    persona = generate_persona(structure)

    assert persona["role"] == "Guardian"
    assert persona["traits"] == ["brave", "loyal"]
    assert persona["invariants"] == ["protect-others"]
    assert persona["tensions"] == ["threat → defend"]
    assert persona["closures"] == ["future_threat → fortify"]
