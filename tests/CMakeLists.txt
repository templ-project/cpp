# GTest executable with proper tests
add_executable(cpp-template-tests test_greeter.cpp)

target_link_libraries(cpp-template-tests
    PRIVATE
    GTest::gtest
    GTest::gtest_main
)

target_include_directories(cpp-template-tests PRIVATE ${CMAKE_SOURCE_DIR}/include)

# Link with greeter source (for testing)
target_sources(cpp-template-tests PRIVATE ${CMAKE_SOURCE_DIR}/src/greeter.cpp)

# Add test to CTest
add_test(NAME GreeterTests COMMAND cpp-template-tests)

# Enable testing properties
set_tests_properties(GreeterTests PROPERTIES
    TIMEOUT 30
    PASS_REGULAR_EXPRESSION ".*\\[  PASSED  \\].*"
)

# Also create a simple test executable as backup
add_executable(cpp-template-tests-simple test_simple.cpp)
target_include_directories(cpp-template-tests-simple PRIVATE ${CMAKE_SOURCE_DIR}/include)
target_sources(cpp-template-tests-simple PRIVATE ${CMAKE_SOURCE_DIR}/src/greeter.cpp)
add_test(NAME SimpleTests COMMAND cpp-template-tests-simple)
