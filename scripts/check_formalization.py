"""Fail if Lean formalization files contain unverified placeholders."""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FORMAL = ROOT / "formal"
FORBIDDEN = re.compile(r"\b(sorry|admit|axiom)\b")


def main() -> None:
    hits = []
    for path in sorted(FORMAL.rglob("*.lean")):
        for lineno, line in enumerate(path.read_text().splitlines(), start=1):
            if FORBIDDEN.search(line):
                hits.append(f"{path.relative_to(ROOT)}:{lineno}: {line.strip()}")
    if hits:
        raise SystemExit("unverified Lean placeholder found:\n" + "\n".join(hits))
    print("Lean formalization guard: no sorry/admit/axiom placeholders")


if __name__ == "__main__":
    main()
