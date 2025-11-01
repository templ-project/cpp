#!/usr/bin/env python3
"""
Cross-platform code linter using clang-tidy.
Lints C++ source files (.cpp, .hpp, .h) in src/ and include/ directories.
"""

import sys
import time
import subprocess
from pathlib import Path
from typing import List, Tuple

# Fix Windows console encoding for Unicode symbols
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')


# ANSI color codes
class Colors:
    """ANSI color codes for terminal output."""
    RESET = '\033[0m'
    GRAY = '\033[90m'
    WHITE = '\033[97m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BOLD = '\033[1m'
    DIM = '\033[2m'

    @staticmethod
    def supports_color() -> bool:
        """Check if the terminal supports colors."""
        return (
            hasattr(sys.stdout, 'isatty') and
            sys.stdout.isatty() and
            sys.platform != 'win32'
        ) or sys.platform == 'win32'  # Windows Terminal supports ANSI colors


def find_source_files(staged_only: bool = False) -> List[Path]:
    """Find all C++ source files to lint."""
    files = []

    if staged_only:
        # Get staged files from git
        try:
            result = subprocess.run(
                ['git', 'status', '--porcelain', '--cached'],
                capture_output=True,
                text=True,
                check=True
            )
            for line in result.stdout.splitlines():
                if line and any(line.endswith(ext) for ext in ['.cpp', '.hpp', '.h']):
                    filepath = Path(line[3:].strip())
                    if filepath.exists():
                        files.append(filepath)
        except subprocess.CalledProcessError:
            print("Warning: Could not get staged files from git", file=sys.stderr)
    else:
        # Find all source files in project directories (excluding tests)
        for directory in ['src', 'include']:
            dir_path = Path(directory)
            if dir_path.exists():
                for ext in ['*.cpp', '*.hpp', '*.h']:
                    files.extend(dir_path.rglob(ext))

    return sorted(files)


def lint_single_file(file: Path, fix: bool, build_dir: str = 'build') -> Tuple[bool, float, str]:
    """
    Lint a single file with clang-tidy.

    Returns:
        Tuple of (has_issues, elapsed_time, error_message)
    """
    start_time = time.time()

    try:
        args = ['clang-tidy', '-p', build_dir, '--config-file=.clang-tidy', '--quiet']

        if fix:
            args.append('--fix')

        args.append(str(file))

        result = subprocess.run(
            args,
            capture_output=True,
            text=True
        )

        elapsed = time.time() - start_time

        # clang-tidy returns 0 if no issues, non-zero if issues found
        has_issues = result.returncode != 0 or bool(result.stdout.strip())

        if result.returncode != 0 and result.stderr:
            return has_issues, elapsed, result.stderr.strip()

        return has_issues, elapsed, result.stdout.strip() if result.stdout.strip() else ""

    except FileNotFoundError:
        elapsed = time.time() - start_time
        return False, elapsed, "clang-tidy not found"
    except Exception as e:
        elapsed = time.time() - start_time
        return False, elapsed, str(e)


def lint_files(files: List[Path], fix: bool = False, build_dir: str = 'build') -> int:
    """
    Lint files with clang-tidy.

    Args:
        files: List of files to lint
        fix: If True, apply fixes. If False, check only.
        build_dir: Build directory containing compile_commands.json

    Returns:
        0 if successful, non-zero if linting issues found
    """
    if not files:
        print("No files to lint")
        return 0

    use_color = Colors.supports_color()
    mode = 'Linting and fixing' if fix else 'Linting'

    # Header
    if use_color:
        print(f"{Colors.BOLD}{mode} {len(files)} file(s)...{Colors.RESET}")
    else:
        print(f"{mode} {len(files)} file(s)...")

    issues_count = 0
    error_count = 0
    total_time = 0.0

    for file in files:
        has_issues, elapsed, output = lint_single_file(file, fix, build_dir)
        total_time += elapsed

        # Format timing
        time_str = f"{int(elapsed * 1000)}ms"

        if output and "error:" in output.lower():
            # Critical error
            error_count += 1
            if use_color:
                print(f"{Colors.RED}✖{Colors.RESET} {file} {Colors.WHITE}{time_str}{Colors.RESET}")
                print(f"{Colors.RED}{output}{Colors.RESET}", file=sys.stderr)
            else:
                print(f"✖ {file} {time_str}")
                print(output, file=sys.stderr)
        elif has_issues:
            # Has linting issues/warnings
            issues_count += 1
            if use_color:
                symbol = "✓" if fix else "⚠"
                color = Colors.GREEN if fix else Colors.YELLOW
                print(f"{color}{symbol}{Colors.RESET} {Colors.WHITE}{file}{Colors.RESET} {Colors.WHITE}{time_str}{Colors.RESET}")
                if output and not fix:
                    # Show issues in check mode
                    print(f"{Colors.DIM}{output}{Colors.RESET}")
            else:
                symbol = "✓" if fix else "!"
                print(f"{symbol} {file} {time_str}")
                if output and not fix:
                    print(output)
        else:
            # No issues
            if use_color:
                unchanged_text = " (clean)" if fix else ""
                print(f"{Colors.GRAY}  {file}{Colors.RESET} {Colors.WHITE}{time_str}{unchanged_text}{Colors.RESET}")
            else:
                unchanged_text = " (clean)" if fix else ""
                print(f"  {file} {time_str}{unchanged_text}")

    # Summary
    print()
    if use_color:
        print(f"{Colors.BOLD}{mode} completed in {int(total_time * 1000)}ms!{Colors.RESET}")
    else:
        print(f"{mode} completed in {int(total_time * 1000)}ms!")

    if error_count > 0:
        if use_color:
            print(f"{Colors.RED}✖ {error_count} file(s) had errors{Colors.RESET}", file=sys.stderr)
        else:
            print(f"✖ {error_count} file(s) had errors", file=sys.stderr)
        return 1

    if not fix and issues_count > 0:
        if use_color:
            print(f"{Colors.YELLOW}⚠ {issues_count} file(s) have linting issues{Colors.RESET}")
            print(f"{Colors.DIM}Use '--fix' to attempt auto-fix.{Colors.RESET}")
        else:
            print(f"! {issues_count} file(s) have linting issues")
            print("Use '--fix' to attempt auto-fix.")
        return 1

    if fix and issues_count > 0:
        if use_color:
            print(f"{Colors.GREEN}✓ Fixed issues in {issues_count} file(s){Colors.RESET}")
        else:
            print(f"✓ Fixed issues in {issues_count} file(s)")

    return 0


def main():
    """Main entry point."""
    # Parse arguments
    fix = False
    staged = False
    build_dir = 'build'

    i = 1
    while i < len(sys.argv):
        arg = sys.argv[i]
        if arg in ['fix', '--fix']:
            fix = True
        elif arg == '--staged':
            staged = True
        elif arg in ['-p', '--build-dir']:
            if i + 1 < len(sys.argv):
                build_dir = sys.argv[i + 1]
                i += 1
        i += 1

    # Find and lint files
    files = find_source_files(staged_only=staged)
    return lint_files(files, fix=fix, build_dir=build_dir)


if __name__ == '__main__':
    sys.exit(main())
