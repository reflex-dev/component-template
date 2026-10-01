"""Rename the template's package after creating a repository from it.

    uv run scripts/rename.py reflex-my-widget --repo your-org/reflex-my-widget

Replaces the placeholder distribution name (reflex-component-template), its
import name (reflex_component_template) and the repository URL everywhere in the
tracked files, and moves the package directory. Run it once, then commit.
"""

import argparse
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OLD_DIST = "reflex-component-template"
OLD_MODULE = "reflex_component_template"
OLD_REPO = "your-org/reflex-component-template"


def tracked_files() -> list[Path]:
    out = subprocess.run(
        ["git", "ls-files"], cwd=ROOT, check=True, capture_output=True, text=True
    ).stdout
    return [ROOT / line for line in out.splitlines() if line]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("name", help="The new PyPI name, e.g. reflex-my-widget.")
    parser.add_argument("--repo", help="The GitHub repository, e.g. your-org/repo.")
    args = parser.parse_args()

    dist = args.name.strip().lower()
    if not re.fullmatch(r"[a-z][a-z0-9]*(-[a-z0-9]+)*", dist):
        parser.error("name must be lowercase letters, digits and single dashes")
    module = dist.replace("-", "_")
    old_package = ROOT / "src" / OLD_MODULE
    if not old_package.is_dir():
        print("Already renamed: src/reflex_component_template does not exist.")
        return 1

    replacements = [(OLD_REPO, args.repo)] if args.repo else []
    replacements += [(OLD_MODULE, module), (OLD_DIST, dist)]
    changed = 0
    for path in tracked_files():
        if path == Path(__file__).resolve() or not path.is_file():
            continue
        try:
            text = path.read_text()
        except UnicodeDecodeError:
            continue
        new = text
        for old, replacement in replacements:
            new = new.replace(old, replacement)
        if new != text:
            path.write_text(new)
            changed += 1

    subprocess.run(
        ["git", "mv", str(old_package), str(ROOT / "src" / module)],
        cwd=ROOT,
        check=True,
    )
    print(f"Renamed to {dist} (import {module}) in {changed} files.")
    print("Next: replace the example component in src/" + module + "/color_picker.py.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
