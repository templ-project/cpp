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
- ✅ **Google Test** - Unit testing framework (auto-fetched)
- ✅ **CMake + XMake** - Dual build system with built-in dependency management
- ✅ **Clang-format + Clang-tidy** - Code formatting and linting
- ✅ **Taskfile** - Modern Task Runner written in Go
- ✅ **Doxygen** - API documentation generation
- ✅ **CI/CD** - GitHub Actions workflows included
- ✅ **No external package managers** - CMake FetchContent & XMake handle dependencies

## Common Commands

```bash
task build             # Build the project
task test              # Run tests
task run               # Run the application
task format            # Format code with clang-format
task lint              # Lint and auto-fix with clang-tidy
task validate          # Run all quality checks
task docs              # Generate Doxygen documentation
```

## Project Structure

```text
src/
├── main.cpp           # Main entry point
├── greeter.cpp        # Example module implementation
└── CMakeLists.txt     # CMake source configuration

include/
└── greeter.hpp        # Example module header

tests/
├── test_greeter.cpp   # Google Test unit tests
└── test_simple.cpp    # Simple fallback tests
```

## Documentation

- **[Contributing Guide](CONTRIBUTING.md)** - How to contribute
- **[Usage Guide](USAGE.md)** - Detailed usage instructions
- **[Architecture](ARCHITECTURE.md)** - Design decisions

## Requirements

- C++20 compatible compiler (Clang recommended)
- CMake 3.20+
- Python 3.11+ (for bootstrap script only)
- Task (optional, for task automation)

## Configuration

All configuration follows Google C++ Style Guide:

- **Clang-format**: `.clang-format` (Google style)
- **Clang-tidy**: `.clang-tidy` (comprehensive checks)
- **CMake**: `CMakeLists.txt` (modern CMake 3.20+)
- **Doxygen**: `Doxyfile` (API documentation)
- **Duplicate Check**: `.jscpdrc` (code duplication detection)

## Quality Checks

Pre-commit hooks automatically check:

- Code formatting (clang-format)
- Linting (clang-tidy)

Pre-push hooks verify:

- Unit tests (Google Test)
- Duplicate code detection
- Build success

## Using as a Library

```cpp
// Include the header
#include "greeter.hpp"

// Use the convenience functions
std::string msg = cpp_template::Hello("World");
std::cout << msg << std::endl;  // "Hello, World!"

// Or use the Greeter class
cpp_template::Greeter greeter;
std::string msg2 = greeter.Hello("C++");
std::cout << msg2 << std::endl;  // "Hello, C++!"
```

## License

MIT © [Templ Project](https://github.com/templ-project)

## Support

- 🐛 [Report Issues](https://github.com/templ-project/cpp/issues)
- 📖 [Read the Docs](https://github.com/templ-project/cpp#readme)
- ⭐ [Star on GitHub](https://github.com/templ-project/cpp)
