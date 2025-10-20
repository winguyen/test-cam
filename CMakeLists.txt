cmake_minimum_required(VERSION 3.16 FATAL_ERROR)

project(test-cam HOMEPAGE_URL https://github.com/winguyen/test-cam)

message(STATUS "CMAKE_MODULE_PATH: ${CMAKE_MODULE_PATH}")

find_package(OpenCV REQUIRED)

add_subdirectory(src)
