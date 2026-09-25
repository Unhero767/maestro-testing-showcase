import sqlite3
from typing import List, Optional
from src.main.core.manifest import HarmonicScar

class AshArchiveRepository:
    """Manages SQLite persistence layers with Write-Ahead Logging (WAL) constraints."""

    def __init__(self, db_path: str = "mlaos_archive.db"):
        self.db_path = db_path
        self._initialize_schema()

    def _initialize_schema(self) -> None:
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("PRAGMA journal_mode=WAL;")
            conn.execute("""
                CREATE TABLE IF NOT EXISTS harmonic_scars (
                    identifier TEXT PRIMARY KEY,
                    spectral_frequency TEXT NOT NULL,
                    intensity REAL NOT NULL,
                    timestamp TEXT NOT NULL
                )
            """)
            conn.commit()

    def persist_scar(self, scar: HarmonicScar) -> None:
        """Persists a harmonic scar into the local archival substrate."""
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                "INSERT OR REPLACE INTO harmonic_scars (identifier, spectral_frequency, intensity, timestamp) VALUES (?, ?, ?, ?)",
                (scar.identifier, scar.spectral_frequency, scar.intensity, scar.timestamp.isoformat())
            )
            conn.commit()
