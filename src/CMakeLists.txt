# Automatically collect source files
file(GLOB_RECURSE SOURCES
    "${CMAKE_CURRENT_SOURCE_DIR}/*.cpp"
)

add_executable(cpp-template ${SOURCES})

target_include_directories(cpp-template PRIVATE ${CMAKE_SOURCE_DIR}/include)

# Link libraries if needed
# target_link_libraries(cpp-template PRIVATE somelib)
