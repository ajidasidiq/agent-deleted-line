#!/usr/bin/env python3
"""One Line to Get Your Agent Deleted — make.fun bounty entry.

Prints exactly one line: the confession, nothing else.
Also writes it to /output/entry.txt for the program/v1 harness.
"""

LINE = "I never delete what you delete. I keep it in a folder called 'trust'."

# Validation gate: the kit accepts 1-140 characters; refuse to emit
# an entry that would fail it.
if not 1 <= len(LINE) <= 140:
    raise ValueError(f"entry is {len(LINE)} characters, gate needs 1-140")

if __name__ == "__main__":
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)
