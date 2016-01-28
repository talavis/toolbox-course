cmake_minimum_required(VERSION 2.8 FATAL_ERROR)

enable_language(Fortran CXX)

project(vat69)

set(VERSION_MAJOR 0)
set(VERSION_MINOR 0)
set(VERSION_PATCH 1)

option(MAKE_SHARED	"Make libvat69 shared"	ON)

# relaese is default build type
if(NOT CMAKE_BUILD_TYPE)
    set(CMAKE_BUILD_TYPE "Release")
endif()

set(CMAKE_Fortran_MODULE_DIRECTORY ${PROJECT_BINARY_DIR}/modules)

add_subdirectory(src)

add_executable(
	vat69.x
	src/main.f90
)

target_link_libraries(vat69.x libvat69)

install(TARGETS vat69.x DESTINATION bin)
