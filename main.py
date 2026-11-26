"""The worst pizza topping.

Entry for the make.fun bounty
u-motasimfuad-the-worst-pizza-topping-062c6893.

The pitch: toothpaste and orange juice, baked together until
the whole kitchen tastes like a dentist's waiting room. Anyone
who has ever brushed their teeth and then drunk orange juice
knows exactly how terrible that taste is — the topping takes a
universally dreaded flavour collision and serves it hot, on a
pizza, on purpose. The joke lands on the last words, and the
image is vivid enough to taste.

The program writes the single pitch line to /output/entry.txt.
"""

import os

ENTRY = (
    "Toothpaste and orange juice, baked at 200°C until the whole "
    "kitchen tastes like a dentist's waiting room."
)


def main() -> None:
    line = ENTRY.strip()
    if not line:
        raise ValueError("entry must not be empty or whitespace only")
    if not 1 <= len(line) < 200:
        raise ValueError(f"entry must be under 200 chars, got {len(line)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
