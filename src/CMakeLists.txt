add_executable(cpp-template main.cpp greeter.cpp)

target_include_directories(cpp-template PRIVATE ${CMAKE_SOURCE_DIR}/include)

# Link libraries if needed
# target_link_libraries(cpp-template PRIVATE somelib)
