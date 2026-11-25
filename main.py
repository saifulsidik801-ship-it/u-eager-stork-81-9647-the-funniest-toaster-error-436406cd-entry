"""The Funniest Toaster Error Message — make.fun entry.

Writes one line (max 120 chars) to /output/entry.txt: the error message
a kitchen toaster shows its owner. Deadpan appliance voice; the joke
lands on the bread having standards the toaster itself lacks.
"""

import os

ENTRY = "ERROR E-7: The bread refused to brown. It has standards. I do not."


def main() -> None:
    assert 1 <= len(ENTRY) <= 120, "entry must be 1-120 chars (gate)"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
