# nav_bot

This package follows the ros2 nav2 tuotorial: First-Time Robot Setup Guide.

Contains the display.launch.py launch file

## How to recreate
Follow the guide from nav2: https://navigation.ros.org/setup_guides/index.html. The following information is a short portion of the guide from nav2.

### Transforms
Transforms allow us to inteprete information from other frames (such as sensors) with a different position and orientation easily. It describes the position and orientation of a child frame with respect to its parent.

For Navigation2 package to work correctly, we need these frames:
- The `map` frame is fixed to the world and is used for globally consistent representations of distance.
- The `odom` frame is fixed to the robot's starting location and is used for locally consistent representations of distance.
- The `base_link` frame is fixed to the robot, typically at the main chassis at its rotational center.

### URDF
The Unified Robot Description Format (URDF), is an XML file that describes a robot (such as the size, shape, colour, mass). It also contains the transforms from one component of the robot to another.

URDF supports XML Macros (Xacro), which contains macros to create shorter and more readable XML files by eliminating the need for repetitive blocks and defining reusable constants to be used in the file.

We can use the Robot State Publisher package to publish transform messages from the URDF. The transform messages can then be used for simulation.

### Odometry
The position and velocity of the robot can be estimated using sensors and wheel encoders.

Plugins can be used in gazebo to simulate these sensors and publish their outputs onto odometry topics. The robot_localisation package cant hen be used to fuse different odometry information to provide more accurate odoometry information, as well as acceleration of the robot
