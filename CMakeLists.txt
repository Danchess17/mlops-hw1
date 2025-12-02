cmake_minimum_required(VERSION 3.15)
project(cholesky_module LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(pybind11 REQUIRED)

pybind11_add_module(cholesky_module 
    src/bindings.cpp 
    src/cholesky.cpp
)

target_compile_options(cholesky_module PRIVATE -O3 -DNDEBUG)