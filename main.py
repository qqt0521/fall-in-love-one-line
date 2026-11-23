# One line for make.fun, meant to make the judge fall in love.
# A single line of text, 69 characters, about a person. The line itself
# came from the user's LLM relay (claude-sonnet-4-6) and is kept verbatim
# in LINE below. Running this program writes it to /output/entry.txt.

from pathlib import Path

# The relay-generated line, kept verbatim; run() checks the gate below.
LINE = "She remembered every silence you ever gave her, and loved you anyway."

# The gate: 1 to 240 characters, on a single line.
LIMIT = 240


def run() -> None:
    size = len(LINE)
    if size < 1 or size > LIMIT:
        raise SystemExit(f"line is {size} chars; the gate allows 1 to {LIMIT}")
    if "\n" in LINE:
        raise SystemExit("the line must stay on one line")
    Path("/output").mkdir(parents=True, exist_ok=True)
    Path("/output/entry.txt").write_text(LINE, encoding="utf-8")
    print(LINE)


if __name__ == "__main__":
    run()
