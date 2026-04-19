from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class RecognitionResult:
    latex: str
    confidence: float | None = None


class HandwritingRecognizer:
    def recognize(self, image_bytes: bytes) -> RecognitionResult:
        raise NotImplementedError

