# spawn_robot

This package launches gazebo and spawns a robot from its URDF.

Contains the /launch/gazebo.launch.py launch file
Contains the /urdf/robot.urdf URDF

## How to recreate
- Follow the instructions in the minimal_talker package, but naming the package as spawn_robot instead
- Update gazebo.launch.py to spawn a robot based on urdf/robot.urdf.xacro
```
from launch_ros.actions import Node
import xacro

...

  # Specify the name of this package and path to xacro file within the package
  pkg_name = 'spawn_robot'
  file_subpath = 'urdf/robot.urdf.xacro'

  # Use xacro to get raw xml contents
  xacro_file = os.path.join(get_package_share_directory(pkg_name),file_subpath)
  robot_description_raw = xacro.process_file(xacro_file).toxml()

  # Pass in raw urdf to the robot state publisher node as command line arguments.
  # the robot details is published onto the topic "robot_description"
  node_robot_state_publisher = Node(
    package='robot_state_publisher',
    executable='robot_state_publisher',
    output='screen',
    parameters=[{'robot_description': robot_description_raw,
    'use_sim_time': True}]
  )

  # Spawn the robot by listening to the topic "robot_description"
  spawn_entity = Node(package='gazebo_ros', executable='spawn_entity.py',
    arguments=['-topic', 'robot_description', '-entity', 'my_bot'],
    output='screen')

  return LaunchDescription([
      gazebo,
      node_robot_state_publisher,
      spawn_entity,
  ])
```
- Add the URDF for the robot (Edit with your text editor or copyand paste the file
```
mkdir urdf
touch urdf/robot.urdf.xacro
```
- Update CMakeLists.txt to install the URDF directory by adding the following lines
```
...
if(BUILD_TESTING)
  ...
endif()

install(
  DIRECTORY launch urdf
  DESTINATION share/${PROJECT_NAME}
)

ament_package()
```
