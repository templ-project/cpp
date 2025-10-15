# Unit tests using Google Test framework
add_executable(cpp-template-tests)

target_sources(cpp-template-tests PRIVATE
    unit/test_greeter.cpp
    # Add more unit test files here as the project grows
)

target_link_libraries(cpp-template-tests
    PRIVATE
    GTest::gtest
    GTest::gtest_main
)

target_include_directories(cpp-template-tests PRIVATE ${CMAKE_SOURCE_DIR}/include)

# Link with greeter source (for testing)
target_sources(cpp-template-tests PRIVATE ${CMAKE_SOURCE_DIR}/src/greeter.cpp)

# Add test to CTest
add_test(NAME UnitTests COMMAND cpp-template-tests)

# Enable testing properties
set_tests_properties(UnitTests PROPERTIES
    TIMEOUT 30
    PASS_REGULAR_EXPRESSION ".*\\[  PASSED  \\].*"
)

# Integration tests (simple, no external dependencies)
add_executable(cpp-template-tests-simple integration/test_simple.cpp)
target_include_directories(cpp-template-tests-simple PRIVATE ${CMAKE_SOURCE_DIR}/include)
target_sources(cpp-template-tests-simple PRIVATE ${CMAKE_SOURCE_DIR}/src/greeter.cpp)
add_test(NAME IntegrationTests COMMAND cpp-template-tests-simple)
