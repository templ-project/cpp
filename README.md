# C++ Bootstrap Template

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![C++20](https://img.shields.io/badge/C%2B%2B-20-blue.svg)](https://en.cppreference.com/w/cpp/20)
[![CI](https://github.com/templ-project/cpp/actions/workflows/ci.yml/badge.svg)](https://github.com/templ-project/cpp/actions/workflows/ci.yml)
![JSCPD](.jscpd/jscpd-badge.svg?raw=true)

> A modern C++ project template with three build systems (Bazel, CMake, XMake), mise tooling, Jinja2 templates, and comprehensive quality automation.

- [C++ Bootstrap Template](#c-bootstrap-template)
  - [✨ What Makes This Template Special](#-what-makes-this-template-special)
  - [Quick Start](#quick-start)
  - [What's Included](#whats-included)
    - [Build Systems (Choose Your Favorite!)](#build-systems-choose-your-favorite)
    - [Tooling \& Automation](#tooling--automation)
    - [Code Quality](#code-quality)
    - [Testing \& Coverage](#testing--coverage)
    - [CI/CD](#cicd)
  - [Project Structure](#project-structure)
  - [Common Commands](#common-commands)
    - [Mise Tasks (Recommended)](#mise-tasks-recommended)
    - [Taskfile (Alternative)](#taskfile-alternative)
  - [Key Features](#key-features)
    - [1. Template-Driven Configuration](#1-template-driven-configuration)
    - [2. Mise Tool Management](#2-mise-tool-management)
    - [3. Hedron Compile Commands for Bazel](#3-hedron-compile-commands-for-bazel)

    - [4. GitHub Actions Integration](#4-github-actions-integration)
  - [Requirements](#requirements)
    - [Auto-Installed by Mise](#auto-installed-by-mise)
    - [Manual Installation](#manual-installation)
    - [Optional](#optional)
  - [Configuration](#configuration)
    - [Build System Selection](#build-system-selection)
    - [Coverage Tools](#coverage-tools)
  - [Code Characteristics](#code-characteristics)
    - [Performance Optimizations](#performance-optimizations)
    - [Safety Features](#safety-features)
    - [Modern C++20 Features](#modern-c20-features)
  - [License](#license)
  - [Support](#support)

## ✨ What Makes This Template Special

- 🎯 **Three Build Systems**: Bazel 8, CMake 4.1.2, and XMake 3.0.3 - all with full feature parity
- 🔧 **Mise-Powered Build Isolation**: Complete environment isolation - no local tool installation needed
- 🔗 **Task Integration**: Task runner works via `mise exec -- task` for isolated execution
- 📋 **Jinja2 Templates**: Build configurations auto-generated from templates - consistent across all systems
- 🚀 **Zero Manual Setup**: One command gets you building, testing, and linting
- 🎨 **Hedron Compile Commands**: Bazel now supports full clang-tidy integration via compile_commands.json
- 🤖 **GitHub Actions**: Reusable composite actions for CI/CD with caching

## Quick Start

```bash
# Clone or bootstrap the template
git clone https://github.com/templ-project/cpp.git my-project
```

or

```bash
# Use our proprietary script to scaffold the template
uvx --from git+https://github.com/templ-project/cpp.git bootstrap ./my-project
```

then

```bash
cd my-project
rm -rf .git # if you used git clone

# Install mise (if not already installed)
curl https://mise.run | sh

# Everything auto-installs on first run
mise trust               # Trust the setup
mise run build           # Builds with CMake by default
mise run test            # Runs tests with coverage
mise run lint            # Lints with clang-tidy

# Try other build systems
mise run build --build-system bazel
mise run test --build-system xmake
```

## What's Included

### Build Systems (Choose Your Favorite!)

- ✅ **Bazel 8** - Google's build system with Hedron compile commands for linting
- ✅ **CMake 4.1.2** (latest) - Industry standard with FetchContent for dependencies
- ✅ **XMake 3.0.3** - Modern Lua-based build system with package management

### Tooling & Automation

- ✅ **Mise** - Build isolation manager (no local tools required - everything auto-installed)
- ✅ **Task** - Modern task runner (run via `mise exec -- task` for isolation)
- ✅ **Jinja2 Templates** - Build configs generated from `templates/` directory
- ✅ **Python Scripts** - Format/lint automation with staged file support
- ✅ **Complete Isolation** - All tools (Clang, CMake, Bazel, XMake, Python, Node) managed by mise

### Code Quality

- ✅ **Clang/LLVM 20.1.8** - Latest compiler with libc++ on Linux/macOS
- ✅ **Clang-format** - Auto-formatting (Google style, 80-column)
- ✅ **Clang-tidy** - Comprehensive linting (bugprone, modernize, performance)

- ✅ **JSCPD** - Duplicate code detection with badge generation

### Testing & Coverage

- ✅ **Google Test** - Unit testing (auto-fetched by all build systems)
- ✅ **Coverage Reports** - gcovr/lcov support (CMake & XMake)
- ✅ **Address Sanitizer** - Memory safety in debug builds
- ✅ **Integration Tests** - Simple no-dependency test suite

### CI/CD

- ✅ **GitHub Actions** - Composite action for setup-tools (Task + mise)
- ✅ **Multi-Build Testing** - All three build systems tested in CI
- ✅ **Caching** - mise tools cached per OS for fast CI runs
- ✅ **Sequential Matrix** - Prevents rate limits and resource exhaustion

## Project Structure

```
.
├── .github/
│   ├── actions/
│   │   └── setup-tools/        # Composite action (Task + mise + caching)
│   └── workflows/
│       └── ci.build.yml        # Main CI pipeline
├── .mise.toml                  # Tool versions and task definitions
├── Taskfile.yml                # Alternative task runner config
├── templates/                  # Jinja2 templates for build configs
│   ├── BUILD.bazel.j2          # Bazel main build
│   ├── tests_BUILD.bazel.j2    # Bazel tests
│   ├── MODULE.bazel.j2         # Bazel modules (includes Hedron)
│   ├── WORKSPACE.j2            # Bazel workspace
│   ├── .bazelrc.j2             # Bazel config
│   ├── CMakeLists.txt.j2       # CMake main build
│   ├── src_CMakeLists.txt.j2   # CMake src (auto-scans *.cpp)
│   └── xmake.lua.j2            # XMake build
├── scripts/
│   ├── compile_templates.py    # Template compiler
│   ├── format.py               # Formatting automation
│   ├── lint.py                 # Linting automation
│   └── which.py                # Tool detection
├── src/
│   ├── main.cpp                # Entry point
│   └── greeter.cpp             # Example module
├── include/
│   └── greeter.hpp             # Example header (string_view optimized)
└── tests/
    ├── unit/
    │   └── test_greeter.cpp    # Google Test unit tests
    └── integration/
        └── test_simple.cpp     # Simple integration tests
```

## Common Commands

### Mise Tasks (Recommended)

```bash
# Building
mise run build                  # CMake (default)
mise run build --build-system bazel
mise run build --build-system xmake

# Testing
mise run test                   # Runs tests with coverage
mise run test --build-system bazel

# Code Quality
mise run format --staged        # Format staged files
mise run lint --fix             # Lint with auto-fix
mise run duplicate-check        # Check duplicates, update badge

# Cleanup
mise run clean                  # Remove all build artifacts

# Full Validation
mise run validate               # Format + lint + test + build (all systems)
```

### Taskfile (Alternative)

```bash
# If not used with mise, it will rely on OS installed tools

mise exec -- task build                         # Build with CMake
mise exec -- task build CPP_BUILD_SYSTEM=bazel  # Build with Bazel
mise exec -- task test CPP_BUILD_SYSTEM=xmake   # Test with XMake
mise exec -- task lint                          # Lint code
mise exec -- task validate                      # Full CI pipeline
```

## Key Features

### 1. Template-Driven Configuration

All build configs are generated from Jinja2 templates:

```bash
# Happens automatically during build, but you can also run manually:
python scripts/compile_templates.py --build-system cmake --compiler clang++
```

Variables like `{{ project_name }}`, `{{ compiler }}`, `{{ build_type }}` are injected automatically.

### 2. Mise Tool Management

`.mise.toml` manages all tools:

- Clang/LLVM 20.1.8 (via HTTP backend)
- Bazel 8 (via GitHub backend)
- CMake latest (via GitHub backend)
- XMake 3.0.3 (via GitHub backend)
- Python 3.11+, Node.js, UV package manager

**No manual installation needed!** Just run `mise install`.

### 3. Hedron Compile Commands for Bazel

Bazel now generates `compile_commands.json` using [Hedron's Compile Commands Extractor](https://github.com/hedronvision/bazel-compile-commands-extractor):

```bash
# Automatically runs during build
bazel run @hedron_compile_commands//:refresh_all
```

This enables full clang-tidy support for Bazel builds!

### 4. GitHub Actions Integration

Custom composite action in `.github/actions/setup-tools/`:

```yaml
- uses: actions/checkout@v4
- uses: ./.github/actions/setup-tools  # Sets up Task, mise, caching
```

Handles:

- Task installation
- Mise installation (cross-platform)
- Tool caching (`~/.local/share/mise`, `~/.local/state/mise`)
- Python venv setup with UV

## Requirements

### Auto-Installed by Mise

- **Clang/LLVM 20.1.8** - Compiler and tools
- **Bazel 8** - Build system
- **CMake 4.1.2** (latest) - Build system
- **XMake 3.0.3** - Build system
- **Python 3.11+** - Scripting
- **Node.js** - For JSCPD
- **UV** - Python package manager

### Manual Installation

- **Mise** - Build isolation manager ([mise.jdx.dev](https://mise.jdx.dev))

  ```bash
  curl https://mise.run | sh
  ```

  **Note**: Mise provides complete build isolation. All other tools (Clang, CMake, Bazel, XMake, Python, Node) are auto-installed in isolated environments. No local installation needed!

- **Task** (Optional) - Task runner ([taskfile.dev](https://taskfile.dev))

  ```bash
  brew install go-task  # macOS
  # Or download from releases
  ```

  **Note**: Task must be run via `mise exec -- task` for isolated execution. Direct `task` commands require all tools installed locally (not recommended).

  ```bash
  brew install go-task  # macOS
  # Or download from releases
  ```

### Optional

- **GDB** - Debugging (`mise run debug`)
- **Valgrind** - Memory profiling (Linux/macOS)

## Configuration

### Build System Selection

Set default in `.mise.toml`:

```toml
[env]
CPP_BUILD_SYSTEM = "cmake"  # or "bazel" or "xmake"
CPP_BUILD_TYPE = "Release"  # or "Debug"
CPP_COMPILER = "clang++"
```

### Coverage Tools

Choose in `.mise.toml`:

```bash
mise run test --cov-tool gcovr  # Default, generates HTML
mise run test --cov-tool lcov   # Alternative

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

## Code Characteristics

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
