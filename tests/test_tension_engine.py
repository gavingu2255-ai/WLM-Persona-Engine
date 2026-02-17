import pytest
from wlm_persona_engine.tension_engine import derive_tensions


def test_tensions_lookup():
    assert derive_tensions("Healer", [], {}) == ["harm_detected → protect"]
    assert derive_tensions("Guardian", [], {}) == ["threat → defend"]


def test_tensions_unknown_role():
    assert derive_tensions("UnknownRole", [], {}) == []
