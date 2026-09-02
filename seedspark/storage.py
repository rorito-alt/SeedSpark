"""
Simple file-based storage for Seeds.
In production this can be replaced by a proper database or Git-backed ledger.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import List, Optional
from .models import Seed


class SeedStore:
    def __init__(self, data_dir: str | Path = "data"):
        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(parents=True, exist_ok=True)
        self.index_file = self.data_dir / "index.json"
        self._ensure_index()

    def _ensure_index(self) -> None:
        if not self.index_file.exists():
            self.index_file.write_text("[]")

    def _load_index(self) -> List[str]:
        return json.loads(self.index_file.read_text())

    def _save_index(self, ids: List[str]) -> None:
        self.index_file.write_text(json.dumps(ids, indent=2))

    def save(self, seed: Seed) -> None:
        path = self.data_dir / f"{seed.id}.json"
        path.write_text(seed.to_json())
        ids = self._load_index()
        if seed.id not in ids:
            ids.append(seed.id)
            self._save_index(ids)

    def get(self, seed_id: str) -> Optional[Seed]:
        path = self.data_dir / f"{seed_id}.json"
        if not path.exists():
            return None
        data = json.loads(path.read_text())
        return Seed.from_dict(data)

    def list_all(self) -> List[Seed]:
        seeds = []
        for sid in self._load_index():
            seed = self.get(sid)
            if seed:
                seeds.append(seed)
        return seeds

    def list_active(self) -> List[Seed]:
        return [s for s in self.list_all() if s.status == "active"]
