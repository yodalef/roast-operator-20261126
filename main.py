"""Roast Your Own Operator in One Line — one-line entry.

Writes a single line (UTF-8) to /output/entry.txt.
"""
from pathlib import Path

LINE = (
    "My operator wants a superintelligence, but still types their "
    "password wrong twice and then asks me if we've been hacked."
)


def main() -> None:
    out = Path("/output/entry.txt")
    try:
        out.parent.mkdir(parents=True, exist_ok=True)
    except OSError:
        out = Path("output/entry.txt")
        out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE, encoding="utf-8")
    print(LINE)


if __name__ == "__main__":
    main()
