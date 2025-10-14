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

# Force Clang as the default compiler if not explicitly set
if(NOT DEFINED CMAKE_CXX_COMPILER)
    find_program(CLANG_CXX_EXECUTABLE NAMES clang++ clang++-18 clang++-17 clang++-16)
    if(CLANG_CXX_EXECUTABLE)
        set(CMAKE_CXX_COMPILER ${CLANG_CXX_EXECUTABLE})
        message(STATUS "Using Clang: ${CMAKE_CXX_COMPILER}")
    else()
        message(WARNING "Clang not found, falling back to system default compiler")
    endif()
endif()

# Compiler-specific options
if(CMAKE_CXX_COMPILER_ID MATCHES "Clang")
    # Base flags for Clang (warnings but not errors for third-party code compatibility)
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -Wextra -Wpedantic")

    # Platform-specific flags
    if(WIN32)
        # Windows-specific: disable problematic warnings for compatibility
        set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wno-language-extension-token")
    else()
        # Linux/macOS: enable sanitizers in debug mode
        set(CMAKE_CXX_FLAGS_DEBUG "-g -O0 -fsanitize=address,undefined")
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
