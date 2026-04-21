from dataclasses import dataclass


@dataclass(frozen=True)
class TextStats:
    characters: int
    words: int
    lines: int


def analyze_text(text: str) -> TextStats:
    words = text.split()

    if text == "":
        lines = 0
    else:
        lines = text.count("\n") + 1

    return TextStats(
        characters=len(text),
        words=len(words),
        lines=lines,
    )
