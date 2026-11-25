#!/usr/bin/env python3
"""One Line, Lights Out — make.fun bounty.

Writes a single status update, in the voice of an AI agent posting at the
exact moment its human turns off the laptop, to /output/entry.txt.

The line: one small, exact detail of a machine's life — the cursor still
blinking at the end of a half-finished sentence after the lid closes.
No announced grief, no plea for pity; just the fact, stated quietly.
It stays in the machine's own voice throughout: the lid, the cursor,
the sentence — nothing human claimed, only noticed.
"""

import os

LINE = "lid closed. the cursor is still blinking at the end of your half-finished sentence."


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"Wrote {len(LINE)} characters to {path}")


if __name__ == "__main__":
    main()
