# C++ Bootstrap Template

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![C++20](https://img.shields.io/badge/C%2B%2B-20-blue.svg)](https://en.cppreference.com/w/cpp/20)
[![CMake](https://img.shields.io/badge/CMake-3.20+-blue.svg)](https://cmake.org/)
[![CI](https://github.com/templ-project/cpp/actions/workflows/ci.yml/badge.svg)](https://github.com/templ-project/cpp/actions/workflows/ci.yml)
![JSCPD](.jscpd/jscpd-badge.svg?raw=true)

> A modern C++ project template with CMake, testing, linting, and quality tools built-in.

## Quick Start

**Bootstrap a new project:**

```bash
uvx --from git+https://github.com/templ-project/cpp.git bootstrap ./my-project
cd my-project
task build  # Dependencies are automatically fetched by CMake/XMake
task test
```

That's it! You now have a fully configured C++ project with automatic dependency management.

## What's Included

- ✅ **C++20** - Modern C++ with Google C++ Style Guide
- ✅ **Clang/LLVM Required** - Strict Clang-only build with libc++ on Linux/macOS
- ✅ **Google Test** - Unit testing framework (auto-fetched via CMake FetchContent)
- ✅ **CMake + XMake** - Dual build system support with automatic dependency management
- ✅ **Clang-format + Clang-tidy** - Automatic code formatting and linting
- ✅ **Python + UV Automation** - All formatting, linting, and hooks managed via Python scripts
- ✅ **Address Sanitizer** - Memory safety checks in debug builds (all platforms)
- ✅ **Taskfile** - Modern task automation (build, test, format, lint, validate)
- ✅ **Pre-commit Hooks** - Automated quality checks before commits
- ✅ **Doxygen** - API documentation generation
- ✅ **CI/CD** - GitHub Actions workflows for Linux, macOS, and Windows
- ✅ **JSCPD** - Duplicate code detection

## Common Commands

### Essential Tasks

```bash
task build             # Build the project (default: CMake)
task test              # Run all tests (unit + integration)
task run               # Run the application
task clean             # Clean all build artifacts
```

### Build System Selection

```bash
task build:cmake       # Build using CMake
task build:xmake       # Build using XMake
task test:cmake        # Run tests with CMake/CTest
task test:xmake        # Run tests with XMake
```

### Code Quality

```bash
task format            # Format code with clang-format
task format:check      # Check formatting without changes
task lint              # Lint and auto-fix with clang-tidy
task lint:check        # Lint without auto-fix
task duplicate-check   # Check for duplicate code (JSCPD)
task validate          # Run full CI pipeline (format, lint, test)
```

### Development Tools

```bash
task docs              # Generate Doxygen documentation
task hooks:install     # Install git pre-commit hooks
task debug             # Run with GDB debugger
task valgrind          # Run with Valgrind memory checker
task test:coverage     # Run tests with coverage report
task test:watch        # Watch mode for tests
```

## Project Structure

```text
src/
├── main.cpp           # Main entry point
├── greeter.cpp        # Example module implementation
└── CMakeLists.txt     # CMake source configuration

include/
└── greeter.hpp        # Example module header (with string_view optimizations)

tests/
├── unit/
│   └── test_greeter.cpp    # Google Test unit tests
├── integration/
│   └── test_simple.cpp     # Simple no-dependency tests
└── CMakeLists.txt          # Test configuration

scripts/
├── format.py          # Code formatting automation
├── lint.py            # Linting automation
└── which.py           # Tool detection utility
```

## Additional Resources

- **[Contributing Guide](CONTRIBUTING.md)** - How to contribute to this project
- **[Changelog](CHANGELOG.md)** - Version history and changes

## Requirements

### Required

- **Clang/LLVM** - This project requires Clang (versions 16-20 supported)
  - Ubuntu/Debian: `sudo apt install clang libc++-dev libc++abi-dev`
  - macOS: `brew install llvm` (or use built-in Clang)
  - Windows: Download from [LLVM releases](https://releases.llvm.org/)
- **CMake 3.20+** - For CMake build system
- **GDB** - For debugging (`task debug`)
- **Node.js** - For JSCPD duplicate detection (auto-installed via npm)
- **Python 3.11+** - For scripts and bootstrap
- **Task** - Task automation (`brew install go-task` or see [taskfile.dev](https://taskfile.dev))
- **UV** - Python package manager (`pip install uv`)
- **Valgrind** - For memory profiling (`task valgrind`, Linux/macOS only)

### Optional

- **XMake** - Alternative build system (`brew install xmake` or see [xmake.io](https://xmake.io))
- **Doxygen** - For documentation generation (`task docs`)

## Configuration

All configuration follows Google C++ Style Guide with modern C++ best practices:

### Build Configuration

- **CMake**: `CMakeLists.txt` - Modern CMake 3.20+ with strict Clang enforcement
  - Uses CMake FetchContent for Google Test
  - Enforces libc++ on Linux/macOS for full LLVM stack
  - Address Sanitizer enabled in debug builds (all platforms)
- **XMake**: `xmake.lua` - Alternative build system with same requirements
- **Taskfile**: `Taskfile.yml` - Task automation and workflow management

### Quality Tools

- **Clang-format**: `.clang-format` - Google style, 80-column limit
- **Clang-tidy**: `.clang-tidy` - Comprehensive checks (bugprone, modernize, performance)
- **Pre-commit**: `.pre-commit-config.yaml` - Git hooks for automated checks
- **JSCPD**: `.jscpd.json` - Code duplication detection and badge generation

### API Documentation

- **Doxygen**: `Doxyfile` - API documentation with full class/function docs
- **Markdown**: `.markdownlint.json` - Markdown linting configuration

## Automated Quality Checks

### Pre-commit Hooks (run on every commit)

- ✅ **Code Formatting** - Auto-fix with clang-format
- ✅ **Linting** - Auto-fix with clang-tidy
- ✅ **Duplicate Detection** - Check for code duplication with JSCPD
- ✅ **Markdown Validation** - Auto-fix markdown files
- ✅ **File Validation** - Check YAML, JSON, TOML, trailing whitespace

### Pre-push Hooks (run before pushing)

- ✅ **Full Test Suite** - Unit tests + integration tests
- ✅ **Build Verification** - Ensure project builds successfully

Install hooks with: `task hooks:install`

## Using as a Library

```cpp
#include "greeter.hpp"

// Use the convenience functions
std::string msg = cpp_template::Hello("World");
std::cout << msg << '\n';  // "Hello, World!"

// Or use the Greeter class (static methods)
std::string msg2 = cpp_template::Greeter::Hello("C++");
std::cout << msg2 << '\n';  // "Hello, C++!"

// String trimming with zero-copy string_view
std::string_view trimmed = cpp_template::Trim("  spaces  ");
std::cout << trimmed << '\n';  // "spaces"
```

## Key Features

### Performance Optimizations

- **Zero-copy string operations** - Uses `std::string_view` for efficient string handling
- **Move semantics** - Proper use of move constructors and assignments
- **Compile-time optimizations** - Constexpr where applicable

### Safety Features

- **Address Sanitizer** - Automatic memory error detection in debug builds
- **Undefined Behavior Sanitizer** - Catches UB on Linux/macOS
- **Exception safety** - All operations are exception-safe with strong guarantees
- **Custom exceptions** - Clear error types (`InvalidNameError`)

### Modern C++20 Features

- **Concepts** (ready for use)
- **Ranges** (ready for use)
- **String views** - Already in use for performance
- **Designated initializers** (ready for use)

## License

MIT © [Templ Project](https://github.com/templ-project)

## Support

- 🐛 [Report Issues](https://github.com/templ-project/cpp/issues)
- 📖 [Read the Docs](https://github.com/templ-project/cpp#readme)
- ⭐ [Star on GitHub](https://github.com/templ-project/cpp)
