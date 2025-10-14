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

-- Compiler configuration
set_toolchains("clang")
-- Disable -Werror for better third-party compatibility
add_cxflags("-Wall", "-Wextra", "-Wpedantic")

-- Include directories
add_includedirs("include")

-- Add packages
add_requires("gtest")

-- Target: main executable
target("cpp-template")
    set_kind("binary")
    add_files("src/*.cpp")
    add_headerfiles("include/**.hpp")

-- Target: Google Test tests
target("cpp-template-tests")
    set_kind("binary")
    set_default(false)
    add_files("tests/test_greeter.cpp", "src/greeter.cpp")
    add_packages("gtest")

    -- Windows: Ensure consistent runtime library
    if is_plat("windows") then
        set_runtimes("MD")
    end

    after_build(function (target)
        os.exec(target:targetfile())
    end)
