from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Dict, Any, List

@dataclass(frozen=True)
class HarmonicScar:
    """Represents a crystallized dialetheic contradiction managed by paraconsistent logic."""
    identifier: str
    spectral_frequency: str
    contradiction_vector: Dict[str, Any]
    intensity: float
    timestamp: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

@dataclass(frozen=True)
class AshArchiveNode:
    """Core domain entity for tracking Merkle DAG state transitions."""
    node_hash: str
    parent_hash: str
    scars: List[HarmonicScar] = field(default_factory=list)

    def validate_integrity(self) -> bool:
        """Ensures that structural invariants hold across state transitions."""
        return len(self.node_hash) == 64 and all(s.intensity >= 0.0 for s in self.scars)
