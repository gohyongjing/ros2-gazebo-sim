# ros2-gazebo-sim

This repository contains some skeletal packages to get started with ros2 and gazebo

This repo can be directly cloned into a source folder of a ros2 workspace and built with `colcon build --packages-select <name-of-pakage>`

For example, to use the minimal_gazebo package in this repository:
- Change into ur ros2 workspace and clone the repository under the `src` folder (assuming you have git and github ssh set up).
```
cd ~/ros2_ws/src
git clone git@github.com:gohyongjing/ros2-gazebo-sim.git
```
- Source the ros2 installation and build the minimal_gazebo package (assuming you are using ros2 foxy-fitzroy).
```
cd ~/ros2_ws
source /opt/ros/foxy/setup.bash
colcon build --packages-select minimal_gazebo
```
- Open a new terminal and install the package
```
cd ~/ros2_ws
source /opt/ros/foxy/setup.bash
source install/setup.bash
```
- Run the launch file using `ros2 launch minimal_gazebo gazebo.launch.py`

## minimal_gazebo

This package contains a launch file that is a simple wrapper around the gazebo launch file. Use this to check that ros2 and gazebo is installed correctly.

Contains the gazebo.launch.py launch file
