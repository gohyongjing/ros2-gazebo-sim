# additional_nodes

This package contains a launch file that launches gazebo and runs the ros2 tutorial talker.py. Use this to add custom nodes into your project.

Contains the launch/gazebo.launch.py launch file
Contains the src/talker.py file

## How to recreate
- Follow the instructions in the minimal_talker package, but naming the package as additonal_nodes instead 
- Follow the ros2 instructions to make a simple publisher package in the same workspace. Your workspace should look like this now
```
ros2_ws
|-src
  |-additional_nodes
  |-py_pubsub
```
- Add the following lines in additional_node/launch/gazebo.launch.py to run a talker node with the gazebo simulator
```
from launch_ros.actions import Node

...

  talker = Node(
    package='py_pubsub',
    executable='talker',
    output='screen',
  )

  return LaunchDescription([
      gazebo,
      talker,
  ])

```
