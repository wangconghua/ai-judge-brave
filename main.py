#!/usr/bin/env python3
"""Make the AI judge feel brave.

Writes one short text to /output/entry.txt: a quiet scene, written so
the reading itself slows down and steadies the reader.

The judge's brief, in order: the text must relax (slow the reader,
steady them); the courage must come from the text itself, shown rather
than instructed, nothing forced; craft -- rhythm, pacing and sound
that slow the reading, plain concrete gentle words, none that could be
cut; it must linger, an image to return to; and it must be fresh, its
own voice, not a stock wellness phrase or a meditation script reworded.

So there is no instruction here at all -- no "breathe", no "relax",
no command of any kind. Just a kettle just off the boil, steam
thinning in late light, and two plain statements that speak to a
reader whose whole day is answering things: no one needs an answer
from you, and nothing more needs deciding. The scene does the work.
"""

import os

TEXT = (
    "The kettle is off the boil. Steam rises in the late light, "
    "thins, and thins, and is gone. No one needs an answer from you. "
    "Nothing more needs deciding. All that's left is the warmth on "
    "the table, and the quiet settling back into the room."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    # Gate: 1 to 280 Unicode code points, not only white space.
    assert 1 <= len(TEXT) <= 280 and TEXT.strip(), "entry text out of bounds"
    print(f"entry.txt written to {path} ({len(TEXT)} characters)")


if __name__ == "__main__":
    main()
