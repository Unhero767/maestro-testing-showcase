from typing import Sequence

def calculate_consciousness_intensity(voltages: Sequence[float], decay_factor: float = 0.95) -> float:
    """Computes the continuous consciousness intensity metric (dΦ/dt) deterministically."""
    if not voltages:
        return 0.0
    
    accumulated = sum(v * (decay_factor ** i) for i, v in enumerate(voltages))
    return round(float(accumulated), 6)

def sanitize_archival_key(raw_key: str) -> str:
    """Normalizes string keys for ingestion into storage strata."""
    return "".join(c for c in raw_key.lower() if c.isalnum() or c in ("_", "-"))
