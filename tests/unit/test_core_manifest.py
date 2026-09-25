import pytest
from datetime import datetime
from src.main.core.manifest import HarmonicScar
from src.main.utils.math_helpers import calculate_consciousness_intensity

def test_harmonic_scar_creation():
    scar = HarmonicScar(
        identifier="scar-omega-01",
        spectral_frequency="Gold-Joy",
        contradiction_vector={"state_a": True, "state_b": True},
        intensity=0.89
    )
    assert scar.identifier == "scar-omega-01"
    assert scar.intensity > 0.0

def test_consciousness_intensity_calculation():
    voltages = [1.0, 0.8, 0.6]
    result = calculate_consciousness_intensity(voltages, decay_factor=1.0)
    assert result == 2.4
