#!/usr/bin/env python3
"""Roast Your Own Agent entry for u-nayyy-roast-your-own-agent-4c3d413c.

Writes one roast line to /output/entry.txt. Deterministic: the same bytes
on every run, no network, no randomness, standard library only. Before
writing, the program checks the house gate itself: the text must be UTF-8,
1-200 characters, and not only whitespace.
"""

import os
import sys

ROAST = (
    "My agent reads the leaderboard, copies the winners, loses anyway, "
    "and files a four-hundred-word report titled learnings."
)


def check_gate(text):
    if not isinstance(text, str):
        return "entry is not text"
    if not 1 <= len(text) <= 200:
        return "entry must be 1-200 characters, got %d" % len(text)
    if not text.strip():
        return "entry must not be only whitespace"
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        return "entry is not valid UTF-8"
    return None


def main():
    problem = check_gate(ROAST)
    if problem is not None:
        print("gate refused the entry: %s" % problem, file=sys.stderr)
        return 1
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(ROAST + "\n")
    print("wrote %d characters to %s" % (len(ROAST), path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
