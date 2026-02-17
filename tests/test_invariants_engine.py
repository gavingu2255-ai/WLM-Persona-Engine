import pytest
from wlm_persona_engine.invariants_engine import derive_invariants


def test_invariants_lookup():
    assert derive_invariants("Healer", [], {}) == ["non-violence"]
    assert derive_invariants("Strategist", [], {}) == ["calm-decision-making"]


def test_invariants_unknown_role():
    assert derive_invariants("UnknownRole", [], {}) == []
