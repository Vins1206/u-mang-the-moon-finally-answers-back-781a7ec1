#!/usr/bin/env python3
"""The Moon Finally Answers Back.

Writes a single funny line, in the Moon's own wry voice, answering
every wish, howl and late-night promise ever aimed at the sky.
Python standard library only.
"""

import os

LINE = "I heard every wish, every howl, and every 2 a.m. promise — I'm a rock, not a genie, and no, I'm not made of cheese."


def main():
    # Gate: exactly one line, 1-240 characters, not only whitespace.
    assert "\n" not in LINE and 1 <= len(LINE) <= 240, "entry line out of gate"
    assert LINE.strip() == LINE
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
