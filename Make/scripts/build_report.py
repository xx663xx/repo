from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "build" / "assignment-report.md"


def read_requirements(path: Path) -> list[str]:
    packages: list[str] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if stripped and not stripped.startswith("#"):
            packages.append(stripped)
    return packages


def main() -> int:
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    runtime_requirements = read_requirements(ROOT / "requirements.txt")
    development_requirements = read_requirements(ROOT / "requirements-dev.txt")

    content = "\n".join(
        [
            "# Build Report",
            "",
            f"Generated at: {datetime.now(timezone.utc).isoformat()}",
            "",
            "## Runtime dependencies",
            *[f"- {package}" for package in runtime_requirements],
            "",
            "## Development dependencies",
            *[f"- {package}" for package in development_requirements],
            "",
            "## Main targets",
            "- `make install`",
            "- `make run`",
            "- `make lint`",
            "- `make typecheck`",
            "- `make check-requirements`",
            "- `make test`",
            "- `make check`",
            "- `make docs`",
            "- `make build`",
        ]
    )
    REPORT.write_text(content + "\n", encoding="utf-8")
    print(f"Documentation artifact written to {REPORT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
