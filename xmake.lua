add_rules("mode.debug", "mode.release")

-- Project configuration
set_project("cpp-template")
set_version("1.0.0")
set_description("A C++ Bootstrap/Template project using modern tools and best practices")

-- Set C++ standard
set_languages("c++20")

-- Windows-specific: Use dynamic runtime (MD) to match GTest
if is_plat("windows") then
    set_runtimes("MD")
end

-- Set warnings and optimizations
if is_mode("debug") then
    set_symbols("debug")
    set_optimize("none")
    if is_plat("linux", "macosx") then
        add_cxflags("-fsanitize=address,undefined")
        add_ldflags("-fsanitize=address,undefined")
    end
elseif is_mode("release") then
    set_symbols("hidden")
    set_optimize("fastest")
    add_defines("NDEBUG")
end

-- -- Compiler configuration
-- set_toolchains("clang")

-- More explicit Clang enforcement
if is_plat("windows") then
    set_toolchains("clang-cl")  -- Use clang-cl on Windows
elseif is_plat("macosx") then
    set_toolchains("clang")
    add_cxflags("-stdlib=libc++")  -- Use libc++ on macOS (built-in)
    add_ldflags("-stdlib=libc++", "-lc++abi")
elseif is_plat("linux") then
    set_toolchains("clang")
    -- On Linux, use libstdc++ to match pre-built gtest from xmake packages
    -- libc++ would require building gtest from source with matching stdlib
end

-- Validate compiler at configuration time
before_build(function (target)
    local cc = target:tool("cxx")
    if not cc or not cc:find("clang") then
        raise("This project requires Clang/LLVM. Please install Clang.")
    end
end)

-- Disable -Werror for better third-party compatibility
add_cxflags("-Wall", "-Wextra", "-Wpedantic")

-- Include directories
add_includedirs("include")

-- Add packages
-- Note: SDK flags for macOS are set via environment variables in .mise.toml
add_requires("gtest")

-- Target: main executable
target("cpp-template")
    set_kind("binary")
    add_files("src/*.cpp")
    add_headerfiles("include/**.hpp")

-- Target: Unit tests using Google Test
target("cpp-template-tests")
    set_kind("binary")
    set_default(false)
    add_files("tests/unit/test_greeter.cpp", "src/greeter.cpp")
    add_packages("gtest")

    -- Windows: Ensure consistent runtime library
    if is_plat("windows") then
        set_runtimes("MD")
    end

    after_build(function (target)
        os.exec(target:targetfile())
    end)

-- Target: Integration tests (simple, no external dependencies)
target("cpp-template-tests-simple")
    set_kind("binary")
    set_default(false)
    add_files("tests/integration/test_simple.cpp", "src/greeter.cpp")

    -- Windows: Ensure consistent runtime library
    if is_plat("windows") then
        set_runtimes("MD")
    end

    after_build(function (target)
        os.exec(target:targetfile())
    end)
