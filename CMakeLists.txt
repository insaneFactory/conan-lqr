cmake_minimum_required(VERSION 3.12)
project(lqr C)

#
# OPTIONS
#

option(shared "ON, OFF" ON)
set(sharedOrStatic "STATIC")
if(shared)
	set(sharedOrStatic "SHARED")
endif(shared)

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

file(GLOB_RECURSE headers src/lqr/*.h)
file(GLOB_RECURSE sources src/lqr/*.c)

source_group(
	TREE ${CMAKE_CURRENT_SOURCE_DIR}
	PREFIX src
	FILES ${headers} ${sources}
)

add_library(${PROJECT_NAME} ${sharedOrStatic}
	${headers}
	${sources}
)

target_link_libraries(${PROJECT_NAME}
	PRIVATE CONAN_PKG::glib
)

target_include_directories(${PROJECT_NAME}
	PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/src/lqr
	PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/src
)

if(WIN32)
	target_link_libraries(${PROJECT_NAME}
		PRIVATE Ws2_32.lib
	)
endif(WIN32)
