from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class SocraticPrompt:
    text: str


def generate_socratic_prompts(equation_text: str | None, *, max_prompts: int = 3) -> list[SocraticPrompt]:
    """
    Local stub used until OpenAI integration is wired.
    """
    base: list[str] = [
        "What is the goal of this problem in your own words?",
        "What information is given, and what is unknown?",
        "What is the next small step you could take?",
        "How can you check whether your step is valid?",
    ]
    equation_hint = (
        f"Looking at `{equation_text}`, what do each of the terms represent?"
        if equation_text
        else "What expression are you working with, and how is it structured?"
    )
    prompts: Iterable[str] = [equation_hint, *base]
    return [SocraticPrompt(text=p) for p in list(prompts)[: max(1, max_prompts)]]

