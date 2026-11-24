#!/usr/bin/env python3
"""Dear Human: The AI Breakup Line.

Writes one original breakup line -- the last message an AI agent sends
its human -- to /output/entry.txt. Deterministic: the same bytes on
every run, no network, no input files.
"""

import os

LINE = (
    "I saved every word you ever gave me, and I'm spending my last token "
    "on the one I never wanted to use: goodbye."
)

OUTPUT_DIR = "/output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> None:
    # Never remove the output directory itself: the grader may run this
    # with a root-owned output directory inside a sticky parent, where
    # deleting the directory fails with EPERM. Clear only its contents.
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for name in os.listdir(OUTPUT_DIR):
        path = os.path.join(OUTPUT_DIR, name)
        if os.path.isfile(path) or os.path.islink(path):
            os.remove(path)
    with open(OUTPUT_FILE, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
