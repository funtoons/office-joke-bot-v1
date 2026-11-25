"""One-Line Office Joke Laugh-Off entry.

Writes a single one-line office joke to /output/entry.txt.
Deterministic, stdlib-only, offline: no randomness, no network,
no timestamps, no paths in the output.
"""

import os

JOKE = (
    "The printer finally got fixed after 6 months, and the first "
    "thing it printed was the email announcing the office is going paperless."
)
# Structure: setup (broken printer fixed after 6 months) -> reversal in the
# final beat (its first job is printing the paperless-office announcement,
# the very thing that makes the printer obsolete). Specific mechanism: 6 months.


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
