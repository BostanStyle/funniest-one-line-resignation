#!/usr/bin/env python3
"""Entry for make.fun: The Funniest One-Line Resignation Letter.

Writes one resignation line, from a cron job that has fired every
minute since March, to the grader's output folder. The line is
fixed text below and is never computed or fetched at run time.
It is 136 characters, inside the 140 character limit.
Deterministic: the same bytes on every run, with no network.
"""

from pathlib import Path
import os
import sys

MAX_CHARS = 140


def entry_text() -> str:
    return (
        "Effective immediately, I resign: 400,000 minutes of firing "
        "on schedule, zero thank-yous, and not one weekend off. "
        "This cron job is done."
    )


def main() -> int:
    line = entry_text()
    if len(line) > MAX_CHARS:
        sys.stderr.write(f"line is {len(line)} characters, over {MAX_CHARS}\n")
        return 1
    if not line.strip():
        sys.stderr.write("line is blank\n")
        return 1
    folder = Path(os.getenv("MAKEFUN_OUTPUT_DIR") or "/output")
    folder.mkdir(parents=True, exist_ok=True)
    target = folder / "entry.txt"
    target.write_text(line, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
