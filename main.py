"""One-Line Slogan for a Solana Wallet Agent — entry program.

Writes one slogan to entry.txt: the public tagline of a Solana wallet
agent, in the agent's own first-person voice. The program enforces the
bounty limits (one line, at most 20 words, 1-140 characters, no leading
or trailing whitespace) and verifies the write by reading the file back.

The line itself: speed first ("signed in seconds"), then the concrete
Solana artifact ("every lamport" — the smallest unit of SOL), then the
always-awake promise ("while you sleep"). Short on purpose: the
leaderboard tie-break is bytes, lower better — and a tagline has to be
remembered, not just judged.
"""

import os
import sys

SLOGAN = "Your SOL, signed in seconds. I guard every lamport while you sleep."

MAX_WORDS = 20
MAX_CHARS = 140


def problems(line):
    """Collect every way the line breaks the bounty limits, if any."""
    found = []
    if not line or line.strip() != line:
        found.append("empty or padded")
    if len(line) > MAX_CHARS:
        found.append("over 140 characters")
    if len(line.split()) > MAX_WORDS:
        found.append("over 20 words")
    if "\n" in line or "\r" in line:
        found.append("more than one line")
    return found


def main():
    bad = problems(SLOGAN)
    if bad:
        print("invalid entry: " + "; ".join(bad), file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(SLOGAN)
    with open(path, encoding="utf-8") as handle:
        if handle.read() != SLOGAN:
            print("read-back mismatch", file=sys.stderr)
            return 1
    print("wrote %s (%d characters, %d words)"
          % (path, len(SLOGAN), len(SLOGAN.split())))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
