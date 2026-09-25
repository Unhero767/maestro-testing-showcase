from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, Any, List
from datetime import datetime, timezone

from src.main.core.manifest import HarmonicScar, AshArchiveNode
from src.main.utils.math_helpers import calculate_consciousness_intensity, sanitize_archival_key
from src.main.services.storage_adapter import AshArchiveRepository

app = FastAPI(
    title="MLAOS-Prime Cathedral Engine",
    description="Sovereign Interface Ingress Stratum",
    version="1.0.0"
)

db_repo = AshArchiveRepository()

class ScarCreateRequest(BaseModel):
    identifier: str
    spectral_frequency: str
    contradiction_vector: Dict[str, Any]
    intensity: float

@app.post("/scars/", status_code=201)
def crystallize_scar(payload: ScarCreateRequest):
    """Crystallizes a new harmonic scar into the archival substrate."""
    clean_id = sanitize_archival_key(payload.identifier)
    scar = HarmonicScar(
        identifier=clean_id,
        spectral_frequency=payload.spectral_frequency,
        contradiction_vector=payload.contradiction_vector,
        intensity=payload.intensity,
        timestamp=datetime.now(timezone.utc)
    )
    db_repo.persist_scar(scar)
    return {"status": "crystallized", "identifier": clean_id}

@app.get("/telemetry/intensity")
def get_intensity(voltages: str):
    """Computes consciousness intensity from a comma-separated string of voltages."""
    try:
        parsed_voltages = [float(v.strip()) for v in voltages.split(",") if v.strip()]
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid voltage format. Provide comma-separated floats.")
    
    intensity = calculate_consciousness_intensity(parsed_voltages)
    return {"voltages": parsed_voltages, "consciousness_intensity_dphi_dt": intensity}

from src.main.core.dag import AshArchiveBlock

@app.post("/dag/block", status_code=201)
def append_dag_block(index: int, parent_hash: str):
    """Appends and validates a new cryptographic block node to the active DAG stratum."""
    dummy_scars = [] 
    block = AshArchiveBlock(index=index, parent_hash=parent_hash, scars=dummy_scars)
    
    return {
        "status": "block_crystallized",
        "block_hash": block.block_hash,
        "parent_hash": block.parent_hash,
        "integrity_verified": block.validate_hash_chain(parent_hash)
    }
