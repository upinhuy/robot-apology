#!/usr/bin/env python3
"""The Robot Apology — make.fun bounty u-suga-the-robot-apology-dd96bb59.

Writes one two-line robot confession to /output/entry.txt:
  line 1 — one sentence owning a specific mistake;
  line 2 — one sentence naming the lesson and the changed behaviour.
Pure standard library, no network, no input files.
"""

import os

ENTRY = (
    "I'm sorry I woke the baby at 3 in the morning by announcing my firmware update at full volume.\n"
    "I learned that a sleeping house is a state worth protecting, so now I hold my announcements until morning and whisper the urgent ones.\n"
)


def validate(text: str) -> None:
    """Enforce the competition gate before writing: UTF-8 text of 1-400
    characters, exactly two lines, each line a single sentence."""
    assert 1 <= len(text) <= 400, f"entry must be 1-400 characters, got {len(text)}"
    lines = text.rstrip("\n").split("\n")
    assert len(lines) == 2, f"entry must be exactly two lines, got {len(lines)}"
    for line in lines:
        assert line.strip(), "entry lines must not be blank"
        assert line.endswith("."), "each line must end with a full stop"
        assert line.count(".") == 1, "each line must be a single sentence"


def main() -> None:
    validate(ENTRY)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {path} ({len(ENTRY)} characters)")


if __name__ == "__main__":
    main()
