from __future__ import annotations

import argparse
import ast
import re
import sys
from pathlib import Path

COMMON_IMPORT_TO_PACKAGE = {
    "PIL": "pillow",
    "bs4": "beautifulsoup4",
    "cv2": "opencv-python",
    "yaml": "pyyaml",
}


def normalize_package_name(name: str) -> str:
    return name.strip().lower().replace("_", "-")


def package_name_for_import(module_name: str) -> str:
    return normalize_package_name(
        COMMON_IMPORT_TO_PACKAGE.get(module_name, module_name)
    )


def collect_declared_requirements(requirements_file: Path) -> set[str]:
    declared: set[str] = set()
    pattern = re.compile(r"^\s*([A-Za-z0-9_.-]+)")
    for line in requirements_file.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or stripped.startswith("-r"):
            continue
        match = pattern.match(stripped)
        if match:
            declared.add(normalize_package_name(match.group(1)))
    return declared


def collect_local_modules(source_dir: Path) -> set[str]:
    local_modules: set[str] = set()
    for path in source_dir.rglob("*.py"):
        relative_parts = path.relative_to(source_dir).parts
        if relative_parts[-1] == "__init__.py":
            local_modules.add(relative_parts[0])
            continue
        local_modules.add(relative_parts[0])
        local_modules.add(Path(relative_parts[-1]).stem)
    return local_modules


def collect_imports(source_dir: Path) -> set[str]:
    imported_modules: set[str] = set()
    for path in source_dir.rglob("*.py"):
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    imported_modules.add(alias.name.split(".")[0])
            elif isinstance(node, ast.ImportFrom):
                if node.level == 0 and node.module is not None:
                    imported_modules.add(node.module.split(".")[0])
    return imported_modules


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Validate that imported third-party modules are declared in "
            "requirements.txt."
        )
    )
    parser.add_argument("--source-dir", type=Path, required=True)
    parser.add_argument("--requirements", type=Path, required=True)
    args = parser.parse_args()

    stdlib_modules = set(sys.stdlib_module_names)
    local_modules = collect_local_modules(args.source_dir)
    imported_modules = collect_imports(args.source_dir)
    third_party_imports = {
        module
        for module in imported_modules
        if module not in stdlib_modules and module not in local_modules
    }
    imported_packages = {
        package_name_for_import(module) for module in third_party_imports
    }
    declared_packages = collect_declared_requirements(args.requirements)

    missing = sorted(imported_packages - declared_packages)
    extra = sorted(declared_packages - imported_packages)

    if missing:
        print("Missing requirements:")
        for package in missing:
            print(f"  - {package}")

    if extra:
        print("Unused declared requirements:")
        for package in extra:
            print(f"  - {package}")

    if missing or extra:
        return 1

    print("Requirements are synchronized with imported third-party modules.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
