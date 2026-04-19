from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class FirebaseConfig:
    project_id: str | None = None


class FirebaseClient:
    """
    Placeholder wrapper for Firebase Admin SDK.
    The concrete initialization depends on how we store credentials (service account vs emulator).
    """

    def __init__(self, config: FirebaseConfig) -> None:
        self.config = config

