# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.22

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/adm.sof44944@gaia.fkie.fraunhofer.de/ros2_cs/src/motion_capture_tracking/motion_capture_tracking

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/adm.sof44944@gaia.fkie.fraunhofer.de/ros2_cs/build/motion_capture_tracking

# Utility rule file for NightlyTest.

# Include any custom commands dependencies for this target.
include deps/libmotioncapture/deps/vrpn/CMakeFiles/NightlyTest.dir/compiler_depend.make

# Include the progress variables for this target.
include deps/libmotioncapture/deps/vrpn/CMakeFiles/NightlyTest.dir/progress.make

deps/libmotioncapture/deps/vrpn/CMakeFiles/NightlyTest:
	cd /home/adm.sof44944@gaia.fkie.fraunhofer.de/ros2_cs/build/motion_capture_tracking/deps/libmotioncapture/deps/vrpn && /usr/bin/ctest -D NightlyTest

NightlyTest: deps/libmotioncapture/deps/vrpn/CMakeFiles/NightlyTest
NightlyTest: deps/libmotioncapture/deps/vrpn/CMakeFiles/NightlyTest.dir/build.make
.PHONY : NightlyTest

# Rule to build all files generated by this target.
deps/libmotioncapture/deps/vrpn/CMakeFiles/NightlyTest.dir/build: NightlyTest
.PHONY : deps/libmotioncapture/deps/vrpn/CMakeFiles/NightlyTest.dir/build

deps/libmotioncapture/deps/vrpn/CMakeFiles/NightlyTest.dir/clean:
	cd /home/adm.sof44944@gaia.fkie.fraunhofer.de/ros2_cs/build/motion_capture_tracking/deps/libmotioncapture/deps/vrpn && $(CMAKE_COMMAND) -P CMakeFiles/NightlyTest.dir/cmake_clean.cmake
.PHONY : deps/libmotioncapture/deps/vrpn/CMakeFiles/NightlyTest.dir/clean

deps/libmotioncapture/deps/vrpn/CMakeFiles/NightlyTest.dir/depend:
	cd /home/adm.sof44944@gaia.fkie.fraunhofer.de/ros2_cs/build/motion_capture_tracking && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/adm.sof44944@gaia.fkie.fraunhofer.de/ros2_cs/src/motion_capture_tracking/motion_capture_tracking /home/adm.sof44944@gaia.fkie.fraunhofer.de/ros2_cs/src/motion_capture_tracking/motion_capture_tracking/deps/libmotioncapture/deps/vrpn /home/adm.sof44944@gaia.fkie.fraunhofer.de/ros2_cs/build/motion_capture_tracking /home/adm.sof44944@gaia.fkie.fraunhofer.de/ros2_cs/build/motion_capture_tracking/deps/libmotioncapture/deps/vrpn /home/adm.sof44944@gaia.fkie.fraunhofer.de/ros2_cs/build/motion_capture_tracking/deps/libmotioncapture/deps/vrpn/CMakeFiles/NightlyTest.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : deps/libmotioncapture/deps/vrpn/CMakeFiles/NightlyTest.dir/depend

