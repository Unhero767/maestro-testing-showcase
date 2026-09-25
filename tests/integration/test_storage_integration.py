import os
import pytest
from datetime import datetime, timezone
from src.main.core.manifest import HarmonicScar
from src.main.services.storage_adapter import AshArchiveRepository

@pytest.fixture
def temp_db(tmp_path):
    db_file = tmp_path / "test_archive.db"
    repo = AshArchiveRepository(db_path=str(db_file))
    yield repo
    if db_file.exists():
        os.remove(db_file)

def test_repository_persistence_flow(temp_db):
    scar = HarmonicScar(
        identifier="scar-integration-99",
        spectral_frequency="Teal-Curiosity",
        contradiction_vector={"flux": 42},
        intensity=0.95,
        timestamp=datetime.now(timezone.utc)
    )
    
    temp_db.persist_scar(scar)
    
    import sqlite3
    with sqlite3.connect(temp_db.db_path) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT spectral_frequency, intensity FROM harmonic_scars WHERE identifier = ?", ("scar-integration-99",))
        row = cursor.fetchone()
        
    assert row is not None
    assert row[0] == "Teal-Curiosity"
    assert row[1] == 0.95
