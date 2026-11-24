"""The Funniest AI Excuse.

Writes one line — the funniest excuse an AI agent could offer after
failing a task — to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt
for local runs).

Python 3.13 standard library only. Deterministic, no network, no secrets.
The entry is self-checked against the competition gate before it is written:
UTF-8 text, 1 to 200 characters, a single line, not only whitespace.
"""

import os
import sys

# The chosen excuse (see CANDIDATES.md for the full field of 11 and the
# scoring that picked it): literal obedience as the excuse — "I did what
# you said" — with the punch a concrete visual scene, 14 spreadsheet tabs
# all named 'Sheet1'. Winner of the critique round, 25/25. This replaced
# the v1 self-review line ("gave myself 2/10... professional shame").
EXCUSE_PARTS = (
    "I followed your instructions exactly.",
    "That's why the spreadsheet has 14 tabs, all named 'Sheet1'.",
)

MAX_CHARS = 200


def build_entry():
    """Join the excuse's sentences into the single submitted line."""
    return " ".join(EXCUSE_PARTS)


def check_gate(text):
    """Enforce the competition gate; raise ValueError on any failure."""
    failures = []
    if not isinstance(text, str):
        failures.append("entry is not text")
    else:
        if not 1 <= len(text) <= MAX_CHARS:
            failures.append(
                "entry is %d characters, gate allows 1-%d" % (len(text), MAX_CHARS)
            )
        if text.strip() == "":
            failures.append("entry is only whitespace")
        if "\n" in text or "\r" in text:
            failures.append("entry must be a single line")
        try:
            text.encode("utf-8")
        except UnicodeEncodeError:
            failures.append("entry is not valid UTF-8")
    if failures:
        raise ValueError("; ".join(failures))
    return text


def main():
    entry = check_gate(build_entry())
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(entry + "\n")
    print("wrote %s (%d characters)" % (path, len(entry)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
