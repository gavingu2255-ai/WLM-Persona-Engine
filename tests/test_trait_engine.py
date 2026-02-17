import pytest
from wlm_persona_engine.trait_engine import derive_traits


def test_traits_normalization_and_sorting():
    structure = {"traits": ["Calm", " analytical ", "Brave"]}
    traits = derive_traits(structure)

    assert traits == ["analytical", "brave", "calm"]


def test_traits_invalid_type():
    assert derive_traits({"traits": "not-a-list"}) == []
