from __future__ import annotations
import asyncio
from typing import Dict, Any, List

class AsynchronousTelemetryWorkerPool:
    """Manages an asynchronous queue to process high-frequency telemetry without blocking ingress routes."""
    
    def __init__(self, queue_capacity: int = 1000):
        self.queue: asyncio.Queue[Dict[str, Any]] = asyncio.Queue(maxsize=queue_capacity)
        self._is_running = False
        self._worker_task: asyncio.Task | None = None

    async def enqueue_telemetry(self, payload: Dict[str, Any]) -> bool:
        """Pushes telemetry payloads into the non-blocking queue."""
        if self.queue.full():
            return False
        await self.queue.put(payload)
        return True

    async def _process_stream(self) -> None:
        """Consumes telemetry items asynchronously in the background."""
        while self._is_running:
            try:
                payload = await asyncio.wait_for(self.queue.get(), timeout=0.1)
                # Process or persist telemetry payload
                await asyncio.sleep(0.01) # Simulated async I/O persistence
                self.queue.task_done()
            except asyncio.TimeoutError:
                continue
            except asyncio.CancelledError:
                break

    def start_worker(self) -> None:
        """Initializes the background worker loop."""
        if not self._is_running:
            self._is_running = True
            self._worker_task = asyncio.create_task(self._process_stream())

    async def stop_worker(self) -> None:
        """Gracefully halts the asynchronous worker pool."""
        self._is_running = False
        if self._worker_task:
            self._worker_task.cancel()
            try:
                await self._worker_task
            except asyncio.CancelledError:
                pass
