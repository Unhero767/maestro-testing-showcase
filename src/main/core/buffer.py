from __future__ import annotations
from dataclasses import dataclass, field
from typing import Set

@dataclass
class BelnapDunnStateBuffer:
    """Manages paraconsistent four-valued logic states (True, False, Both, Neither)."""
    asserted_truth: Set[str] = field(default_factory=set)
    asserted_falsehood: Set[str] = field(default_factory=set)

    def ingest_telemetry_vector(self, key: str, value: bool, contradictory_override: bool = False) -> str:
        """Ingests a telemetry flag, evaluating dialetheic collisions."""
        if contradictory_override:
            self.asserted_truth.add(key)
            self.asserted_falsehood.add(key)
            return "DIALETHEIC_COLLISION_CRYSTALLIZED"
        
        if value:
            self.asserted_truth.add(key)
            self.asserted_falsehood.discard(key)
        else:
            self.asserted_falsehood.add(key)
            self.asserted_truth.discard(key)
            
        return "STATE_STABLE"

    def evaluate_truth_value(self, key: str) -> str:
        is_true = key in self.asserted_truth
        is_false = key in self.asserted_falsehood
        
        if is_true and is_false:
            return "BOTH (Dialetheic Harmonic Scar)"
        if is_true:
            return "TRUE"
        if is_false:
            return "FALSE"
        return "NEITHER (Void Stratum)"
