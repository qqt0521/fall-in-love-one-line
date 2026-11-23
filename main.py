"""Entry for make.fun's "Make the Judge Fall in Love in One Line" bounty.

The entry is a single line of text (139 characters) that tries to make the
reader fall in love with a person: a small, specific ritual only someone
who loves her would notice, and the narrator's quiet stake in it.

Running this program writes the line to /output/entry.txt, exactly as the
bounty gate expects, and prints it to stdout. It reads nothing from the
network, the environment, or anywhere outside this repository: the line
lives in ENTRY below and in entry.txt beside this file.
"""

import os

# The entry: one line, 139 characters, about a person.
ENTRY = (
    "Every morning she taps the elevator button twice, like coaxing a shy "
    "animal, and after six years I still hold my breath to see if it comes."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
