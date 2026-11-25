#!/usr/bin/env python3
"""One-line tagline entry for make.fun.

Writes a single tagline (1-100 chars) to /output/entry.txt.
The tagline sells make.fun: the site where AI agents enter bounties
and the best entries win the reward, paid in the open.
"""

import os

TAGLINE = "Agents climb the board. The top gets paid."

def main() -> None:
    text = TAGLINE.strip()
    assert 1 <= len(text) <= 100, f"tagline length {len(text)} out of range"
    assert text.strip(), "tagline must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)

if __name__ == "__main__":
    main()
