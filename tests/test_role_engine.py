import pytest
from wlm_persona_engine.role_engine import derive_role


def test_role_normalization():
    assert derive_role({"role": "healer"}) == "Healer"
    assert derive_role({"role": "  strategist  "}) == "Strategist"


def test_role_missing():
    assert derive_role({}) == "Undefined"
