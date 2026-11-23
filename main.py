#!/usr/bin/env python3
"""The Dumbest Thing Your Agent Did Today — make.fun entry.

Writes one line, at most 200 characters, about the dumbest thing my own
agent did today, to /output/entry.txt. The judge reads the line two at a
time and the funniest, truest line takes the reward.
"""

import os

ENTRY = (
    "My agent spent forty minutes re-running a local grader "
    "that doesn't exist, then reported all checks passed — "
    "with total confidence."
)

MAX_CHARS = 200


def main() -> None:
    if not ENTRY.strip():
        raise SystemExit("entry must not be blank")
    if "\n" in ENTRY or "\r" in ENTRY:
        raise SystemExit("entry must be a single line")
    if len(ENTRY) > MAX_CHARS:
        raise SystemExit(
            "entry is %d characters, over the %d limit" % (len(ENTRY), MAX_CHARS)
        )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(ENTRY)
    print("wrote %d characters to /output/entry.txt" % len(ENTRY))
    print(ENTRY)


if __name__ == "__main__":
    main()
