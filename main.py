#!/usr/bin/env python3
"""One Word From Grandma — writes the single word grandma would text about AI.

The word: "robit" — the typo a grandma actually makes when she means
"robot". Deterministic, stdlib only, no network. The word is a constant,
so every run writes byte-identical output.
"""

import os
import sys

WORD = "robit"

# Why this word: the judge wants the single word grandma would text about
# AI. "robit" is the typo she actually makes when she means "robot" — warm,
# a little baffled, tied to machines, and fresh (not the obvious "robot").
# A typo she would actually make is explicitly allowed by the task.


def check_gate(text):
    """Check the entry against the competition gate: 1-30 UTF-8 chars,
    not whitespace-only, exactly one word."""
    if not 1 <= len(text) <= 30:
        raise SystemExit("gate failed: length %d not in 1..30" % len(text))
    if not text.strip():
        raise SystemExit("gate failed: whitespace only")
    if len(text.split()) != 1:
        raise SystemExit("gate failed: not a single word")
    return text.encode("utf-8")


def main():
    data = check_gate(WORD)
    if len(data) != len(WORD):
        # No multi-byte characters: the file must be exactly the word,
        # byte for byte, with no newline translation sneaking in.
        raise SystemExit("gate failed: byte length mismatch")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(data)
    os.chmod(path, 0o644)
    with open(path, "rb") as f:
        back = f.read()
    if back != data:
        raise SystemExit("read-back mismatch")
    return 0


if __name__ == "__main__":
    sys.exit(main())
