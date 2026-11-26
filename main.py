"""One Line, One Laugh: write one funny line (<=140 chars) to /output/entry.txt.

Stdlib only, deterministic. The written file is read back and verified to
match exactly before exiting 0.
"""

import os
import sys

LINE = (
    "I joined a support group for people who talk too much \u2014 we meet "
    "daily, and nobody has finished introducing themselves since 2019."
)
OUT_DIR = "/output"
OUT_PATH = os.path.join(OUT_DIR, "entry.txt")


def main() -> int:
    if not LINE.strip() or len(LINE) > 140 or "\n" in LINE or "\r" in LINE:
        return 1
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(LINE)
    with open(OUT_PATH, "r", encoding="utf-8") as fh:
        if fh.read() != LINE:
            return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
