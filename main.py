"""Write the internet in one word to the output file.

The entry is a single word that describes the whole internet:
"sidequest". The internet is one long side quest: you open it to do
one thing and surface hours later having done everything except that
thing. The word is funny by itself, true of the internet as a whole,
and surprising enough that it is not the first word anyone reaches for.
Every tab is another quest marker; the main quest is whatever you
meant to do before you opened the browser.

This program writes exactly that word and nothing else: no network
access, no randomness, and no dependence on the time or date, so every
run produces the same bytes. The word is 9 characters long, inside the
bounty gate of 1 to 30 characters, and it is a single word with no
spaces, hyphens, or punctuation.

The output directory is /output by default and can be overridden with
the OUTPUT_DIR environment variable (handy for local testing).
"""

import hashlib
import os
import sys

WORD = "sidequest"


def main() -> int:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    data = (WORD + "\n").encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    digest = hashlib.sha256(data).hexdigest()
    print(f"Wrote {len(data)} bytes to {path} (sha256 {digest})")
    print(f"Word: {WORD!r} ({len(WORD)} characters)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
