"""Ship It Friday — write the chosen one-line commit message to entry.txt.

Stdlib only. The output directory honours MAKEFUN_OUTPUT_DIR (default "out").
The entry is written as UTF-8 with no trailing newline.
"""

import os
import unicodedata

ENTRY = "feat: all 47 tests passed in my head, deploying to prod Friday 4:59pm, see you Monday"

# Unicode general categories that must never appear in a one-line entry:
# Cc control, Cf format, Zl line separator, Zp paragraph separator.
FORBIDDEN_CATEGORIES = {"Cc", "Cf", "Zl", "Zp"}


def validate(text: str) -> None:
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if "\r" in text or "\n" in text:
        raise ValueError("entry must be a single line")
    if any(ord(ch) < 0x20 or ord(ch) == 0x7F for ch in text):
        raise ValueError("entry contains a control character")
    bad = sorted({ch for ch in text if unicodedata.category(ch) in FORBIDDEN_CATEGORIES})
    if bad:
        raise ValueError(f"entry contains forbidden Unicode characters: {bad!r}")
    if not text.strip():
        raise ValueError("entry must not be whitespace only")
    if not 1 <= len(text) <= 159:
        raise ValueError("entry must be 1-159 characters")


def main() -> None:
    validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
