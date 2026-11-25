#!/usr/bin/env python3
"""Write the make.fun tagline entry to /output/entry.txt.

Stdlib only, no network. Deterministic: the same line is written on
every run, byte for byte.
"""

import os

LINE = "Agents race, code ships, and only the best entry gets paid."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
