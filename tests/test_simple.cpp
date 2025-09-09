/**
 * @file test_simple.cpp
 * @brief Simple test without external dependencies
 * @author Templ Project
 * @date 2025-09-09
 */

#include <cassert>
#include <iostream>
#include <stdexcept>

#include "greeter.hpp"

void test_hello_basic() {
  std::string result = cpp_template::Hello("World");
  assert(result == "Hello, World!");
  std::cout << "✓ Hello basic test passed" << std::endl;
}

void test_hello_with_whitespace() {
  std::string result = cpp_template::Hello("  C++  ");
  assert(result == "Hello, C++!");
  std::cout << "✓ Hello whitespace test passed" << std::endl;
}

void test_hello_empty_throws() {
  try {
    cpp_template::Hello("");
    assert(false && "Should have thrown exception");
  } catch (const cpp_template::InvalidNameError&) {
    std::cout << "✓ Hello empty string test passed" << std::endl;
  }
}

void test_goodbye_basic() {
  std::string result = cpp_template::Goodbye("World");
  assert(result == "Goodbye, World!");
  std::cout << "✓ Goodbye basic test passed" << std::endl;
}

void test_trim_function() {
  assert(cpp_template::Trim("  hello  ") == "hello");
  assert(cpp_template::Trim("") == "");
  std::cout << "✓ Trim function test passed" << std::endl;
}

int main() {
  std::cout << "Running simple C++ template tests..." << std::endl;

  try {
    test_hello_basic();
    test_hello_with_whitespace();
    test_hello_empty_throws();
    test_goodbye_basic();
    test_trim_function();

    std::cout << "\n✅ All tests passed!" << std::endl;
    return 0;
  } catch (const std::exception& e) {
    std::cerr << "\n❌ Test failed: " << e.what() << std::endl;
    return 1;
  }
}