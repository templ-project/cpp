add_rules("mode.debug", "mode.release")

-- Project configuration
set_project("cpp-template")
set_version("1.0.0")
set_description("A C++ Bootstrap/Template project using modern tools and best practices")

-- Set C++ standard
set_languages("c++20")

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
add_cxflags("-Wall", "-Wextra", "-Wpedantic", "-Werror")

-- Include directories
add_includedirs("include")

-- Add packages
add_requires("gtest")

-- Target: main executable
target("cpp-template")
    set_kind("binary")
    add_files("src/*.cpp")
    add_headerfiles("include/**.hpp")

-- Target: tests
target("cpp-template-tests")
    set_kind("binary")
    set_default(false)
    add_files("tests/*.cpp", "src/greeter.cpp")
    add_packages("gtest")
    after_build(function (target)
        os.exec(target:targetfile())
    end)
