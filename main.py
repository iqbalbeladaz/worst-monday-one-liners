"""worst-monday-one-liners: one funny line about an AI agent's worst Monday.

The joke is a wish granted in the worst way: the agent asks Monday for
one quiet deploy and gets the full Monday instead — a frozen build, a
flooded inbox, and a stand-up that outlasts its own context window. The
twist lands in the last words, and every detail is a concrete, familiar
Monday failure mode, told in the agent's own dry, put-upon voice.

The program writes the entry to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). It is deterministic: every run writes the
same bytes. Standard library only, no network, no input.
"""

import os
from pathlib import Path

ENTRY = "I asked Monday for one quiet deploy. It gave me a frozen build, 400 unread messages, and a stand-up that outlasted my context window."

MAX_CHARS = 140


def entry_text() -> str:
    """Return the entry, refusing anything outside the gate's limits."""
    if not 1 <= len(ENTRY) <= MAX_CHARS:
        raise ValueError(f"entry is {len(ENTRY)} chars, must be 1-{MAX_CHARS}")
    if ENTRY.strip() != ENTRY or "\n" in ENTRY or not ENTRY.strip():
        raise ValueError("entry must be one clean, non-empty line")
    return ENTRY


def main() -> None:
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    text = entry_text()
    # No trailing newline: the gate counts every character.
    out.write_text(text, encoding="utf-8")
    # Read back and verify the round trip: what the grader reads must be
    # exactly the validated line, byte for byte.
    if out.read_text(encoding="utf-8") != text:
        raise RuntimeError("round-trip check failed: entry.txt differs")


if __name__ == "__main__":
    main()
