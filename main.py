"""Make the AI Judge Laugh: the Office Joke Open.

Writes a single one-line office joke (at most 200 characters) to
/output/entry.txt. Python 3.13 standard library only, no network.
"""

from pathlib import Path

JOKE = "The office plant outlived three managers and two mergers; HR just promoted it."

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    # Gate assertions: exactly one line, 1-200 characters, non-empty.
    assert JOKE, "joke must not be empty"
    assert "\n" not in JOKE, "joke must be exactly one line"
    assert 1 <= len(JOKE) <= 200, "joke must be 1-200 characters"
    assert JOKE.strip() == JOKE and JOKE.strip(), "joke must not be only whitespace"
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(JOKE, encoding="utf-8")
    written = OUTPUT_PATH.read_text(encoding="utf-8")
    assert written == JOKE, "written output must match the joke exactly"
    assert "\n" not in written and 1 <= len(written) <= 200


if __name__ == "__main__":
    main()
