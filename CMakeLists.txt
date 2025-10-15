cmake_minimum_required(VERSION 3.20)

project(
    cpp-template
    VERSION 1.0.0
    DESCRIPTION "A C++ Bootstrap/Template project using modern tools and best practices"
    LANGUAGES CXX
)

# Set C++ standard
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

# Set default build type
if(NOT CMAKE_BUILD_TYPE)
    set(CMAKE_BUILD_TYPE Release)
endif()

# Force Clang - this project requires Clang/LLVM
if(NOT CMAKE_CXX_COMPILER_ID MATCHES "Clang")
    # Try to find Clang if not already set
    find_program(CLANG_CXX_EXECUTABLE
        NAMES clang++ clang++-20 clang++-19 clang++-18 clang++-17 clang++-16
        DOC "Clang C++ compiler"
    )

    if(CLANG_CXX_EXECUTABLE)
        set(CMAKE_CXX_COMPILER ${CLANG_CXX_EXECUTABLE})
        message(STATUS "Using Clang: ${CMAKE_CXX_COMPILER}")
    else()
        message(FATAL_ERROR
            "Clang/LLVM is required for this project but was not found.\n"
            "Please install Clang and set CMAKE_CXX_COMPILER to clang++.\n"
            "Ubuntu/Debian: sudo apt install clang\n"
            "macOS: brew install llvm\n"
            "Windows: Download from https://releases.llvm.org/"
        )
    endif()
endif()

# Verify we're actually using Clang after configuration
if(NOT CMAKE_CXX_COMPILER_ID MATCHES "Clang")
    message(FATAL_ERROR
        "CMAKE_CXX_COMPILER_ID is '${CMAKE_CXX_COMPILER_ID}' but this project requires Clang.\n"
        "Set CMAKE_CXX_COMPILER to clang++ or use: cmake -DCMAKE_CXX_COMPILER=clang++ ..."
    )
endif()

# Compiler-specific options
if(CMAKE_CXX_COMPILER_ID MATCHES "Clang")
    # Base flags for Clang (warnings but not errors for third-party code compatibility)
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -Wextra -Wpedantic")

    # Use libc++ on macOS (built-in), libstdc++ on Linux (for gtest compatibility)
    if(APPLE)
        set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -stdlib=libc++")
        set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} -stdlib=libc++ -lc++abi")
    endif()

    # Debug flags with sanitizers (works on all platforms with Clang)
    set(CMAKE_CXX_FLAGS_DEBUG "-g -O0")
    if(WIN32)
        # Windows requires different sanitizer syntax
        set(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} -fsanitize=address")
    else()
        # Linux/macOS: enable both address and undefined behavior sanitizers
        set(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} -fsanitize=address,undefined")
    endif()

    set(CMAKE_CXX_FLAGS_RELEASE "-O3 -DNDEBUG")
elseif(CMAKE_CXX_COMPILER_ID STREQUAL "GNU")
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -Wextra -Wpedantic")
    set(CMAKE_CXX_FLAGS_DEBUG "-g -O0")
    set(CMAKE_CXX_FLAGS_RELEASE "-O3 -DNDEBUG")
elseif(CMAKE_CXX_COMPILER_ID STREQUAL "MSVC")
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} /W4")
    set(CMAKE_CXX_FLAGS_DEBUG "/Od /Zi")
    set(CMAKE_CXX_FLAGS_RELEASE "/O2 /DNDEBUG")
endif()

# Enable testing
enable_testing()

# Fetch dependencies using FetchContent
include(FetchContent)

# Google Test
FetchContent_Declare(
    googletest
    GIT_REPOSITORY https://github.com/google/googletest.git
    GIT_TAG v1.14.0
    GIT_SHALLOW TRUE
)

# For Windows: Prevent overriding the parent project's compiler/linker settings
set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)

# Disable warnings in GTest to avoid build errors from third-party code
set(CMAKE_CXX_FLAGS_BACKUP "${CMAKE_CXX_FLAGS}")
if(CMAKE_CXX_COMPILER_ID MATCHES "Clang" OR CMAKE_CXX_COMPILER_ID STREQUAL "GNU")
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -w")  # Disable all warnings for GTest
endif()

# Make GTest available
FetchContent_MakeAvailable(googletest)

# Restore original flags for our project code
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS_BACKUP}")

# Include directories
include_directories(include)

# Add subdirectories
add_subdirectory(src)
add_subdirectory(tests)

# Install configuration
include(GNUInstallDirs)
install(TARGETS cpp-template
    RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
)

install(DIRECTORY include/
    DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}
    FILES_MATCHING PATTERN "*.h" PATTERN "*.hpp"
)
