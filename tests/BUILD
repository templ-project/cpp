# Test BUILD file for cpp-template project

# Unit tests using Google Test
cc_test(
    name = "cpp-template-tests",
    size = "small",
    srcs = ["unit/test_greeter.cpp"],
    deps = [
        "//:greeter_lib",
        "@com_google_googletest//:gtest",
        "@com_google_googletest//:gtest_main",
    ],
)

# Integration tests (simple, no external dependencies)
cc_test(
    name = "cpp-template-tests-simple",
    size = "small",
    srcs = [
        "integration/test_simple.cpp",
        "//src:greeter.cpp",
    ],
    includes = ["//include"],
    deps = ["//:greeter_lib"],
)
