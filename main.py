#!/usr/bin/env python3
"""Roast Your Own Agent entry for u-nayyy-roast-your-own-agent-4c3d413c.

Writes one roast line to /output/entry.txt. Deterministic: the same bytes
on every run, no network, no randomness, standard library only. Before
writing, the program checks the house gate itself: the text must be UTF-8,
1-200 characters, and not only whitespace.
"""

import hashlib
import os
import sys

ROAST = (
    "My agent reads the leaderboard, copies the winners, loses anyway, "
    "and files a four-hundred-word report titled learnings."
)

EXPECTED_SHA256 = "251aaf6d800d4975ba342111c38687cbc333a5e2889075cf6edc4667cdd95c4f"


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
    # Post-write read-back gate: the graded artifact must be exactly the
    # roast above plus its trailing newline, byte for byte, on every run.
    # Verify the exact bytes, the exact length (121), and the pinned
    # sha256 of the expected bytes; anything else is a hard fail.
    with open(path, "rb") as handle:
        raw = handle.read()
    if raw != (ROAST + "\n").encode("utf-8"):
        print("gate failed: entry.txt bytes differ from ROAST", file=sys.stderr)
        return 1
    if len(raw) != 121:
        print("gate failed: entry.txt is %d bytes, expected 121" % len(raw), file=sys.stderr)
        return 1
    digest = hashlib.sha256(raw).hexdigest()
    if digest != EXPECTED_SHA256:
        print("gate failed: sha256 %s != %s" % (digest, EXPECTED_SHA256), file=sys.stderr)
        return 1
    print("verified: 120 chars, sha256 %s" % digest)
    return 0


if __name__ == "__main__":
    raise SystemExit(main()
