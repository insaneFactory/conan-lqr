cmake_minimum_required(VERSION 3.12)
project(lqr C)

#
# Conan
#
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

#
# Defines
#
add_compile_definitions(LQR_EXPORTS)

#
# Source
#

file(GLOB_RECURSE headers source_subfolder/lqr/*.h)
file(GLOB_RECURSE sources source_subfolder/lqr/*.c)

source_group(
	TREE ${CMAKE_CURRENT_SOURCE_DIR}
	PREFIX source_subfolder
	FILES ${headers} ${sources}
)

add_library(${PROJECT_NAME}
	${headers}
	${sources}
)

target_link_libraries(${PROJECT_NAME}
	PRIVATE CONAN_PKG::glib
)

target_include_directories(${PROJECT_NAME}
	PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/source_subfolder/lqr
	PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/source_subfolder
)
