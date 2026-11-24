#!/usr/bin/env python3
"""Write one one-line joke about cats to /output/entry.txt.

The joke: a cat walks across a keyboard during a work call, types three
random letters, and the boss praises the gibberish. The turn is the
boss's corporate-speak reply to cat typing -- the cat accidentally
contributes more than most meetings do.

v2: the line is built from named fragments joined by assemble(), and
validate() checks the entry rules (one line, 1-200 chars, non-blank)
before anything is written. Output is byte-identical to v1.
"""
import os

SETUP = "My cat walked across my keyboard during a work call, "
ACCIDENT = "typed three random letters, "
PUNCH = "and my boss replied, 'Great point \u2014 let's circle back on that.'"


def assemble():
    """Join the fragments into the single joke line."""
    return SETUP + ACCIDENT + PUNCH


def validate(line):
    """Entry rules: one line, 1-200 chars, not only whitespace."""
    if "\n" in line or "\r" in line:
        raise ValueError("joke must be a single line")
    if not 1 <= len(line) <= 200:
        raise ValueError("joke must be 1-200 characters, got %d" % len(line))
    if not line.strip():
        raise ValueError("joke must not be only whitespace")
    return line


def main():
    joke = validate(assemble())
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(joke + "\n")


if __name__ == "__main__":
    main()
