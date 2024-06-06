# Omnicar robot

- You need `robot_localization` installed in your workspace
```
git clone -b noetic-devel https://github.com/cra-ros-pkg/robot_localization.git
```

- You need `orb_slam2_ros` installed in your workspace
```
git clone https://github.com/appliedAI-Initiative/orb_slam_2_ros.git
```

- You need `aruco_detect` installed in your workspace
```
git clone https://github.com/UbiquityRobotics/fiducials.git
```

- You can Install all required dependencies. Run it from your catkin folder
```
sh src/omnicar/install_dependencies.sh
```

- don't forget to build it
```
catkin build
```

## Prepare lidar
Currently we are using DTOF LIDAR LD19
...

## Prepare depth camera for robot

- Install drivers and basic staff for realsence d435 camera.
```
sudo apt-get install ros-$ROS_DISTRO-realsense2-camera
```
- Test depth camera with
```
roslaunch realsense2_camera rs_camera.launch filters:=pointcloud
```
