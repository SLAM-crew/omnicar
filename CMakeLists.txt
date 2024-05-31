cmake_minimum_required(VERSION 3.0.2)
project(omnicar)
find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  sensor_msgs
  cv_bridge
  std_msgs
  image_transport
  nav_msgs
)
catkin_package(
 INCLUDE_DIRS include
#  LIBRARIES bachelor
#  CATKIN_DEPENDS roscpp rospy
#  DEPENDS system_lib
)
include_directories(
  include/bachelor
  ${catkin_INCLUDE_DIRS}
)
install(DIRECTORY scripts/
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
  USE_SOURCE_PERMISSIONS
  PATTERN ".svn" EXCLUDE)