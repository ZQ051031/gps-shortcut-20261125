#!/usr/bin/env python3
"""The GPS Swears It Was a Shortcut.

Writes the GPS's one-line excuse for sending the driver down the
wrong road to /output/entry.txt. Standard library only.

The entry is a fixed string, so every run produces byte-identical
output: one line of plain text, no dialogue tags, no setup, no
trailing newline. The GPS blames the map, the cul-de-sac turns out
to be a wedding, and the punchline lands on the driver — smug,
defensive, and specific, exactly the voice the judge brief asks for.
"""

import os

ENTRY = (
    "The map called it a shortcut, the cul-de-sac called it a wedding, "
    "and honestly the bride looked happier to see us than you did."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY.strip()
    # Gate: UTF-8 text of 1 to 200 characters, not only whitespace,
    # and a single line — no newline characters inside the entry.
    assert 1 <= len(text) <= 200, f"entry is {len(text)} characters"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text and "\r" not in text, "entry must be one line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
