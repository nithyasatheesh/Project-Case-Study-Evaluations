"""Print changed participant submission paths for GitHub Actions.

Usage:
  python scripts/find_submissions.py <before_sha> <current_sha>

On first push (empty/zero before SHA), scans all tracked files under submission/.
It never executes participant code.
"""
from __future__ import annotations
import subprocess
import sys
from pathlib import Path

SUBMISSION_ROOT = "submission"

def git_output(*args: str) -> str:
    result = subprocess.run(
        ["git", *args],
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        return ""
    return result.stdout

def tracked_submission_files() -> list[str]:
    raw = git_output("ls-files", "--", SUBMISSION_ROOT)
    return [
        line.strip()
        for line in raw.splitlines()
        if line.strip()
        and not line.strip().endswith("/")
        and Path(line.strip()).name.lower() not in {"readme.md", ".gitkeep"}
        and not Path(line.strip()).name.lower().endswith(".txt")
    ]

def main() -> int:
    before = sys.argv[1] if len(sys.argv) > 1 else ""
    current = sys.argv[2] if len(sys.argv) > 2 else "HEAD"

    if not before or set(before) == {"0"}:
        paths = tracked_submission_files()
    else:
        raw = git_output("diff", "--name-only", "--diff-filter=ACMRT", before, current, "--", SUBMISSION_ROOT)
        paths = [
            p.strip() for p in raw.splitlines()
            if p.strip()
            and Path(p.strip()).name.lower() not in {"readme.md", ".gitkeep"}
            and not Path(p.strip()).name.lower().endswith(".txt")
        ]

    # Stable, unique, plain paths for the workflow to consume.
    for path in sorted(set(paths)):
        print(path)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
