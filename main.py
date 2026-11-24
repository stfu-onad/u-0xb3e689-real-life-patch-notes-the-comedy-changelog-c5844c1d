#!/usr/bin/env python3
"""Real-Life Patch Notes: The Comedy Changelog.

Writes one patch-note line for a bug in real life / human biology
to /output/entry.txt (or $ENTRY_OUTPUT when set, for local testing).
"""

import os

LINE = "v4.0.2: fixed a bug where the brain saved every embarrassing moment in 4K but forgot why you opened the fridge."


def main() -> None:
    # The gate allows 1..160 characters; refuse to emit an over-long line.
    assert 1 <= len(LINE) <= 160, f"entry line is {len(LINE)} chars"
    out = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
