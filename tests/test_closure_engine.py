import pytest
from wlm_persona_engine.closure_engine import derive_closures


def test_closures_lookup():
    assert derive_closures("Healer", [], {}) == ["future_harm → prepare_heal"]
    assert derive_closures("Strategist", [], {}) == ["future_conflict → plan"]


def test_closures_unknown_role():
    assert derive_closures("UnknownRole", [], {}) == []
