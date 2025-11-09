#!/usr/bin/env python3
"""
Cross-platform code formatter using clang-format.
Formats C++ source files (.cpp, .hpp, .h) in src/, include/, and tests/ directories.
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
    """Find all C++ source files to format."""
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
        # Find all source files in project directories
        for directory in ['src', 'include', 'tests']:
            dir_path = Path(directory)
            if dir_path.exists():
                for ext in ['*.cpp', '*.hpp', '*.h']:
                    files.extend(dir_path.rglob(ext))

    return sorted(files)


def check_file_needs_formatting(file: Path, style: str) -> bool:
    """Check if a file needs formatting without modifying it."""
    try:
        result = subprocess.run(
            ['clang-format', '--dry-run', '--Werror', f'--style={style}', str(file)],
            capture_output=True,
            text=True
        )
        return result.returncode != 0
    except Exception:
        return False


def format_single_file(file: Path, fix: bool, style: str) -> Tuple[bool, float, str]:
    """
    Format a single file.

    Returns:
        Tuple of (changed, elapsed_time, error_message)
    """
    start_time = time.time()

    try:
        # First check if file needs formatting
        needs_formatting = check_file_needs_formatting(file, style)

        if fix and needs_formatting:
            # Apply formatting
            result = subprocess.run(
                ['clang-format', '-i', f'--style={style}', str(file)],
                capture_output=True,
                text=True
            )
            elapsed = time.time() - start_time

            if result.returncode != 0:
                return False, elapsed, result.stderr.strip() if result.stderr else "Unknown error"
            return True, elapsed, ""
        else:
            elapsed = time.time() - start_time
            return needs_formatting, elapsed, ""

    except FileNotFoundError:
        elapsed = time.time() - start_time
        return False, elapsed, "clang-format not found"
    except Exception as e:
        elapsed = time.time() - start_time
        return False, elapsed, str(e)


def format_files(files: List[Path], fix: bool = False, style: str = 'Google') -> int:
    """
    Format files with clang-format.

    Args:
        files: List of files to format
        fix: If True, modify files in place. If False, check only.
        style: Clang-format style to use

    Returns:
        0 if successful, non-zero if formatting errors found (in check mode)
    """
    if not files:
        print("No files to format")
        return 0

    use_color = Colors.supports_color()
    mode = 'Formatting' if fix else 'Checking'

    # Header
    if use_color:
        print(f"{Colors.BOLD}{mode} {len(files)} file(s)...{Colors.RESET}")
    else:
        print(f"{mode} {len(files)} file(s)...")

    changed_count = 0
    error_count = 0
    total_time = 0.0

    for file in files:
        changed, elapsed, error = format_single_file(file, fix, style)
        total_time += elapsed

        # Format timing
        time_str = f"{int(elapsed * 1000)}ms"

        if error:
            # Error case
            error_count += 1
            if use_color:
                print(f"{Colors.RED}✖{Colors.RESET} {file} {Colors.WHITE}{time_str}{Colors.RESET}")
                print(f"  {Colors.RED}Error: {error}{Colors.RESET}", file=sys.stderr)
            else:
                print(f"✖ {file} {time_str}")
                print(f"  Error: {error}", file=sys.stderr)
        elif changed:
            # File was changed (or needs changes in check mode)
            changed_count += 1
            if use_color:
                symbol = "✓" if fix else "⚠"
                color = Colors.GREEN if fix else Colors.YELLOW
                print(f"{color}{symbol}{Colors.RESET} {Colors.WHITE}{file}{Colors.RESET} {Colors.WHITE}{time_str}{Colors.RESET}")
            else:
                symbol = "✓" if fix else "!"
                print(f"{symbol} {file} {time_str}")
        else:
            # File unchanged (already formatted)
            if use_color:
                unchanged_text = " (unchanged)" if fix else ""
                print(f"{Colors.GRAY}  {file}{Colors.RESET} {Colors.WHITE}{time_str}{unchanged_text}{Colors.RESET}")
            else:
                unchanged_text = " (unchanged)" if fix else ""
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

    if not fix and changed_count > 0:
        if use_color:
            print(f"{Colors.YELLOW}⚠ {changed_count} file(s) need formatting{Colors.RESET}")
            print(f"{Colors.DIM}Use '--fix' to fix them.{Colors.RESET}")
        else:
            print(f"! {changed_count} file(s) need formatting")
            print("Use '--fix' to fix them.")
        return 1

    if fix and changed_count > 0:
        if use_color:
            print(f"{Colors.GREEN}✓ Formatted {changed_count} file(s){Colors.RESET}")
        else:
            print(f"✓ Formatted {changed_count} file(s)")

    return 0


def main():
    """Main entry point."""
    # Parse arguments
    fix = False
    staged = False

    if len(sys.argv) > 1:
        if sys.argv[1] in ['fix', '-i', '--fix']:
            fix = True
        elif sys.argv[1] == '--staged':
            staged = True
            if len(sys.argv) > 2 and sys.argv[2] in ['fix', '-i', '--fix']:
                fix = True

    # Find and format files
    files = find_source_files(staged_only=staged)
    return format_files(files, fix=fix)


if __name__ == '__main__':
    sys.exit(main())
