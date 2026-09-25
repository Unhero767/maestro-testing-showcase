import pytest
from src.main.core.manifest import HarmonicScar
from src.main.core.dag import AshArchiveBlock

def test_ash_archive_block_hashing():
    scar = HarmonicScar(
        identifier="scar-dag-test",
        spectral_frequency="Teal-Curiosity",
        contradiction_vector={"flux": 100},
        intensity=0.88
    )
    block_a = AshArchiveBlock(index=1, parent_hash="0" * 64, scars=[scar], nonce=42)
    block_b = AshArchiveBlock(index=1, parent_hash="0" * 64, scars=[scar], nonce=42)
    
    assert block_a.block_hash == block_b.block_hash
    assert len(block_a.block_hash) == 64
    assert block_a.validate_hash_chain("0" * 64) is True

def test_ash_archive_block_chain_failure():
    block = AshArchiveBlock(index=1, parent_hash="0" * 64, scars=[], nonce=0)
    assert block.validate_hash_chain("f" * 64) is False
