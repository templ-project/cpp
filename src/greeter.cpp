/**
 * @file greeter.cpp
 * @brief Implementation of the greeter module
 * @author Templ Project
 * @date 2025-09-09
 */

#include "greeter.hpp"

#include <algorithm>
#include <cctype>

namespace cpp_template {

std::string Trim(const std::string& str) {
  const auto start =
      std::find_if_not(str.begin(), str.end(),
                       [](unsigned char ch) { return std::isspace(ch); });

  const auto end =
      std::find_if_not(str.rbegin(), str.rend(), [](unsigned char ch) {
        return std::isspace(ch);
      }).base();

  return (start < end) ? std::string(start, end) : std::string();
}

// Greeter class implementation
std::string Greeter::Hello(const std::string& name) {
  const std::string trimmed_name = Trim(name);

  if (trimmed_name.empty()) {
    throw InvalidNameError("Name must be a non-empty string");
  }

  return "Hello, " + trimmed_name + "!";
}

std::string Greeter::Goodbye(const std::string& name) {
  const std::string trimmed_name = Trim(name);

  if (trimmed_name.empty()) {
    throw InvalidNameError("Name must be a non-empty string");
  }

  return "Goodbye, " + trimmed_name + "!";
}

// Convenience functions using default Greeter instance
std::string Hello(const std::string& name) {
  return cpp_template::Greeter::Hello(name);
}

std::string Goodbye(const std::string& name) {
  return cpp_template::Greeter::Goodbye(name);
}

}  // namespace cpp_template
