from __future__ import annotations
import hashlib
import json
from dataclasses import dataclass, field
from typing import List
from src.main.core.manifest import HarmonicScar

@dataclass(frozen=True)
class AshArchiveBlock:
    """Represents an immutable cryptographic block within the Ash Archive Merkle DAG."""
    index: int
    parent_hash: str
    scars: List[HarmonicScar]
    nonce: int = 0
    block_hash: str = field(default="", init=False)

    def __post_init__(self):
        object.__setattr__(self, 'block_hash', self._compute_hash())

    def _compute_hash(self) -> str:
        payload = {
            "index": self.index,
            "parent_hash": self.parent_hash,
            "scars": [{"id": s.identifier, "intensity": s.intensity, "freq": s.spectral_frequency} for s in self.scars],
            "nonce": self.nonce
        }
        encoded = json.dumps(payload, sort_keys=True).encode("utf-8")
        return hashlib.sha256(encoded).hexdigest()

    def validate_hash_chain(self, expected_parent_hash: str) -> bool:
        """Verifies cryptographic continuity and structural integrity."""
        return self.parent_hash == expected_parent_hash and self.block_hash == self._compute_hash()
