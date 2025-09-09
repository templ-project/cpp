# C++ Bootstrap Template

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![C++20](https://img.shields.io/badge/C%2B%2B-20-blue.svg)](https://en.cppreference.com/w/cpp/20)
[![CMake](https://img.shields.io/badge/CMake-3.20+-blue.svg)](https://cmake.org/)
[![XMake](https://img.shields.io/badge/XMake-latest-green.svg)](https://xmake.io/)
[![Clang](https://img.shields.io/badge/Clang-latest-red.svg)](https://clang.llvm.org/)

> A comprehensive C++ Bootstrap/Template project using modern tools and best practices

This template provides a complete setup for modern C++ development with CMake, XMake, and Taskfile support, featuring Google Test integration, comprehensive linting, and cross-platform builds.

## 🚀 Features

- **Modern C++20**: Latest C++ standard with best practices
- **Dual Build Systems**: Both CMake and XMake support
- **Task Management**: Taskfile for streamlined development workflow
- **Testing Framework**: Google Test integration with TDD examples
- **Code Quality**: Clang-format + Clang-tidy configuration
- **Cross-Platform**: Windows, Linux, macOS support with Clang
- **Documentation**: Doxygen integration for API docs
- **Memory Safety**: Address Sanitizer and Undefined Behavior Sanitizer
- **CI/CD Ready**: GitHub Actions workflow included
- **Package Management**: Conan and vcpkg support

## 📦 Built With

- **[CMake](https://cmake.org/)** - Cross-platform build system
- **[XMake](https://xmake.io/)** - Modern Lua-based build system
- **[Taskfile](https://taskfile.dev/)** - Task runner and automation
- **[Google Test](https://github.com/google/googletest)** - C++ testing framework
- **[Clang](https://clang.llvm.org/)** - LLVM-based C++ compiler
- **[Doxygen](https://www.doxygen.nl/)** - Documentation generator

## 🏁 Quick Start

### Prerequisites

```bash
# Required tools
- C++20 compatible compiler (Clang recommended)
- CMake 3.20+
- Git

# Optional but recommended
- XMake (for alternative build system)
- Task (for task automation)
- Doxygen (for documentation)
- Conan or vcpkg (for package management)
```

### Installation

```bash
# Clone the template
git clone https://github.com/templ-project/cpp.git my-cpp-project
cd my-cpp-project

# Install dependencies (choose one)
task deps:install  # Auto-detects Conan/vcpkg
# OR manually with Conan
conan install . --build=missing
# OR manually with vcpkg
vcpkg install gtest
```

### Development

```bash
# Using Taskfile (recommended)
task build          # Build with CMake
task build:xmake     # Build with XMake
task test            # Run tests
task run             # Run the application
task format          # Format code
task lint            # Run linting
task ci              # Full CI pipeline

# Using CMake directly
cmake -B build -DCMAKE_CXX_COMPILER=clang++
cmake --build build --parallel
cd build && ctest

# Using XMake directly
xmake f -m release --toolchain=clang
xmake build
xmake run cpp-template
```

## 📁 Project Structure

```
src/
├── main.cpp                 # Main entry point
├── greeter.cpp              # Example module implementation
└── CMakeLists.txt           # CMake source configuration

include/
└── greeter.hpp              # Example module header

tests/
├── test_greeter.cpp         # Google Test unit tests
├── test_simple.cpp          # Simple fallback tests
└── CMakeLists.txt           # CMake test configuration

.clang-format               # Code formatting rules
.clang-tidy                 # Static analysis rules
Taskfile.yml                # Task automation
CMakeLists.txt              # Main CMake configuration
xmake.lua                   # XMake configuration
Doxyfile                    # Doxygen configuration
```

## 🧪 Testing Strategy

This template follows **Test-Driven Development (TDD)** principles:

### Google Test Integration

```cpp
#include <gtest/gtest.h>
#include "greeter.hpp"

TEST(GreeterTest, HelloReturnsGreeting) {
  std::string result = cpp_template::Hello("World");
  EXPECT_EQ(result, "Hello, World!");
}
```

### Fallback Simple Tests

```cpp
#include <cassert>
#include "greeter.hpp"

void test_hello_basic() {
  std::string result = cpp_template::Hello("World");
  assert(result == "Hello, World!");
}
```

### Test Categories

- **Unit Tests**: Test individual functions and classes
- **Integration Tests**: Test module interactions
- **Exception Tests**: Test error handling
- **Memory Tests**: AddressSanitizer and Valgrind integration

## 🔧 Configuration

### CMake Configuration

```cmake
# Set C++20 standard
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Clang-specific flags
set(CMAKE_CXX_FLAGS "-Wall -Wextra -Wpedantic -Werror")
set(CMAKE_CXX_FLAGS_DEBUG "-g -O0 -fsanitize=address,undefined")
```

### XMake Configuration

```lua
set_languages("c++20")
set_toolchains("clang")
add_cxflags("-Wall", "-Wextra", "-Wpedantic", "-Werror")
```

### Code Quality

#### Clang-Format (Google Style)
```yaml
BasedOnStyle: Google
IndentWidth: 2
ColumnLimit: 80
```

#### Clang-Tidy (Comprehensive)
```yaml
Checks: |
  bugprone-*, clang-analyzer-*, cppcoreguidelines-*,
  google-*, modernize-*, performance-*, readability-*
```

## 🌍 Multi-Platform Development

This template supports development on all major platforms:

| Platform | Compilers | Status |
|----------|-----------|--------|
| **Windows 10/11** | MSVC 2019+, Clang 12+, MinGW-w64 | ✅ |
| **Ubuntu 20.04+** | GCC 10+, Clang 12+ | ✅ |
| **macOS 11+** | Clang 12+, GCC 11+ | ✅ |

### Recommended Approach

**1. Native Development (Recommended)**
```bash
# Develop on your target platform using native tools
# Windows: Visual Studio, CLion, or VS Code
# Linux: Any IDE with CMake support
# macOS: Xcode, CLion, or VS Code
```

**2. CI/CD for Multi-Platform Testing**
```bash
# GitHub Actions automatically builds and tests on:
# - Windows (MSVC, Clang)
# - Linux (GCC, Clang)
# - macOS (Clang)
```

**3. Container-Based Development**
```bash
# Use Docker for consistent environments
docker run --rm -v $(pwd):/workspace -w /workspace ubuntu:22.04 bash -c \
  "apt update && apt install -y build-essential cmake && task build"
```

## 📚 API Documentation

### Example API

#### `cpp_template::Hello(const std::string& name)`

Creates a greeting message for the specified name.

**Parameters:**
- `name` - The name to greet (must be non-empty)

**Returns:**
- `std::string` - A formatted greeting message

**Throws:**
- `InvalidNameError` - When name is empty or only whitespace

**Example:**
```cpp
#include "greeter.hpp"

std::string message = cpp_template::Hello("World");
std::cout << message << std::endl;  // "Hello, World!"
```

### Generate Documentation

```bash
task docs
# OR
doxygen Doxyfile
```

## 🛠️ Development Workflow

### Available Tasks

```bash
task --list                 # Show all available tasks

# Build tasks
task build                  # Build with CMake (default)
task build:cmake            # Build with CMake
task build:xmake            # Build with XMake

# Test tasks
task test                   # Run tests (default: CMake)
task test:cmake             # Run tests with CMake/CTest
task test:xmake             # Run tests with XMake

# Development tasks
task format                 # Format code with clang-format
task format:check           # Check code formatting
task lint                   # Run clang-tidy linter
task ci                     # Run CI pipeline

# Debug tasks
task debug                  # Run with debugger (gdb)
task valgrind               # Run with Valgrind

# Cross-platform
task build:windows          # Cross-compile for Windows
task build:linux            # Cross-compile for Linux
task build:macos            # Cross-compile for macOS
```

### Code Style Guidelines

Following [Google C++ Style Guide](https://google.github.io/styleguide/cppguide.html):

```cpp
// Naming conventions
namespace cpp_template {        // snake_case
class MyClass {                 // CamelCase
 public:
  void MyMethod();              // CamelCase
 private:
  int member_variable_;         // snake_case with trailing _
};

// Constants
const int kMaxSize = 100;       // kCamelCase

// Functions
std::string ProcessData();      // CamelCase
}
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Follow the code style (`task format`)
4. Run quality checks (`task ci`)
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

### Development Guidelines

- Follow Google C++ Style Guide
- Write tests for all new features (TDD approach)
- Maintain comprehensive documentation
- Ensure all quality gates pass
- Support all three major platforms (Windows, Linux, macOS)

## 🐛 Troubleshooting

### Common Issues

**Compiler Not Found**
```bash
# Set compiler explicitly
export CXX=clang++
task build
```

**Missing Dependencies**
```bash
# Install with package manager
task deps:install
# OR manually
conan install . --build=missing
```

**Test Failures**
```bash
# Run tests with verbose output
task test -- --verbose
# OR debug specific test
gdb ./build/tests/cpp-template-tests
```

### Memory Issues

```bash
# Run with AddressSanitizer
task build BUILD_TYPE=Debug
task test

# Run with Valgrind
task valgrind
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Related Projects

- [Templ Project](http://templ-project.github.io/) - More project templates
- [JavaScript Template](../javascript/) - JavaScript counterpart

## 👨‍💻 Author

**Templ Project**

- GitHub: [templ-project](https://github.com/templ-project)
- Email: [contact@templ-project.io](mailto:contact@templ-project.io)

## 💝 Support

If you find this template useful:

- ⭐ Star the repository
- 🐛 Report bugs and request features
- 📖 Improve documentation
- 🚀 Share with the community

---

**Happy Coding with Modern C++! 🎉**
