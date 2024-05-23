cmake_minimum_required(VERSION 3.2)
project(MicroRTS_CPP)

if (WIN32)
    	add_subdirectory(external/pugixml-win/pugixml-1.14 EXCLUDE_FROM_ALL)
	add_library(MicroRTScpp  STATIC src/cpp/PhysicalGameState.cpp 		src/cpp/UnitTypeTable.cpp  src/cpp/UnitType.cpp src/cpp/Player.cpp 		src/cpp/Unit.cpp src/cpp/ResourceUsage.cpp src/cpp/PlayerAction.cpp 		src/cpp/UnitAction.cpp src/cpp/UnitActionAssignment.cpp 		src/cpp/GameState.cpp src/cpp/AStarPathFinding.cpp )
endif (WIN32)

if (UNIX)
   	add_subdirectory(external/pugixml-unix/pugixml-1.14 EXCLUDE_FROM_ALL)
	add_library(MicroRTScpp  SHARED src/cpp/PhysicalGameState.cpp 				src/cpp/UnitTypeTable.cpp  src/cpp/UnitType.cpp src/cpp/Player.cpp 			src/cpp/Unit.cpp src/cpp/ResourceUsage.cpp src/cpp/PlayerAction.cpp 			src/cpp/UnitAction.cpp src/cpp/UnitActionAssignment.cpp 		src/cpp/GameState.cpp 	src/cpp/AStarPathFinding.cpp )
endif (UNIX)


target_include_directories(MicroRTScpp   PUBLIC include/)
target_link_libraries(MicroRTScpp pugixml)


add_executable(exp2 "main2.cpp" )
target_link_libraries(exp2 MicroRTScpp)
target_include_directories(exp2 PUBLIC include/)



