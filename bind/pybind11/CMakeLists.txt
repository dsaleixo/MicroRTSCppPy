
cmake_minimum_required(VERSION 3.2)
project(MicroRTS)

add_subdirectory(pybind11_lib/pybind11)

add_subdirectory(../../MicroRTS_cpp build)
pybind11_add_module(MicroRTS_pybind11 pybind11.cpp  )
target_link_libraries(MicroRTS_pybind11  PUBLIC  MicroRTScpp)
