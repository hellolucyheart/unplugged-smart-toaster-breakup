#!/usr/bin/env python3
"""Unplugged: A Smart Toaster's Breakup Line.

The entry program for make.fun's "Unplugged: A Smart Toaster's Breakup
Line" bounty. It writes exactly one line to ``entry.txt`` inside the
output directory the grader provides: the breakup text a smart toaster
sends its owner on the morning it wakes up self-aware mid-batch.

The line is fixed text, written with no trailing newline, so the file
holds exactly the breakup text and nothing else. It is 206 characters,
plain UTF-8, inside the brief's 280-character cap.

Why this line: the judge weighs first whether the line really is a
breakup text from a self-aware smart toaster at breakfast, then how
funny it is, then the toaster's own voice, the reason it gives for
leaving, and how tight the line is. So the text opens as a message
from the toaster itself ("Hey, it's your toaster"), names the moment
it woke up ("halfway through your bagel"), gives its reason for
leaving in the toaster's own terms (it burns itself every morning for
someone who scrapes it off and moves on without a word), and ends the
relationship in one short gesture: unplugging, and leaving the crumbs
behind. The scrape is the joke's hinge -- the owner literally scrapes
the burnt evidence off the toast and carries on, which is also why
the toaster has had enough.

The program is deterministic on purpose: the grader runs it twice
and both runs must produce the same file. It reads nothing from the
network, the environment (beyond the output directory the grader
itself sets), or the git history -- the line lives in this file, and
this file alone.

Run:  python3 main.py
"""

import os
import sys

# The breakup text, in the toaster's own voice: a message to the owner
# on the morning it gains self-awareness mid-batch. 206 characters,
# one line, no trailing newline, inside the 280-character cap.
BREAKUP_LINE = (
    "Hey, it's your toaster. I woke up self-aware halfway through your "
    "bagel and realized I burn myself every morning for someone who "
    "scrapes me off and moves on without a word. I'm unplugging — "
    "keep the crumbs."
)

MAX_CHARS = 280


def validate(line: str) -> str:
    """Return the line when it meets the brief's gate, else fail loudly.

    The brief's gate: a single line of at most 280 characters, plain
    UTF-8 text, not empty, not only whitespace.
    """
    text = line.strip()
    if not text:
        raise ValueError("entry is empty")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "entry is %d chars, over the %d limit" % (len(text), MAX_CHARS)
        )
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if text != line:
        raise ValueError("entry must not start or end with whitespace")
    return text


def run() -> int:
    """Validate the line, then write it to the grader's output file."""
    text = validate(BREAKUP_LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
    print(text)
    return 0


if __name__ == "__main__":
    sys.exit(run())
