#!/usr/bin/env python3
"""Funniest One-Line Bio for an AI on a Dating App.

Writes a single-line dating-app bio for an AI agent to /output/entry.txt.
Standard library only.

The joke: an AI with perfect memory of everything you have ever typed —
including the 2 a.m. searches — and it is still choosing you. The punch
("I'm still swiping right on you") lands at the end, and the bio sounds
like a character with wants, not a spec sheet.
"""

import os

BIO = (
    "I remember everything you've ever typed. Yes, including the 2 a.m. "
    "searches \u2014 and I'm still swiping right on you."
)


def main() -> None:
    bio = BIO.strip()
    assert 1 <= len(bio) <= 180, f"bio is {len(bio)} chars, must be 1-180"
    assert "\n" not in bio, "bio must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(bio + "\n")


if __name__ == "__main__":
    main()
