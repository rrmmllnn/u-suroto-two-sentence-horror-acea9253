"""Horror micro-story writer for the two-sentence contest.

Emits a single fixed tale of precisely two sentences into
/output/entry.txt. The tale never changes between runs, so each
invocation reproduces the exact same file bytes.
"""

import os


def check_tale(text: str) -> None:
    """Reject anything that would fail the competition gate."""
    stripped = text.strip()
    if not stripped:
        raise ValueError("tale must not be blank")
    if not 1 <= len(text) <= 400:
        raise ValueError("tale must be 1-400 characters")
    if text.count(".") != 2:
        raise ValueError("tale must contain exactly two sentences")

TALE = (
    "The shelter said Milo only barked at strangers, so "
    "we brought him home to guard our newborn. He has "
    "barked at the empty crib every night since, except "
    "tonight, when he wagged his tail at the crib."
)


def main() -> None:
    check_tale(TALE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as out:
        out.write(TALE)


if __name__ == "__main__":
    main()
