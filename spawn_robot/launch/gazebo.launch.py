import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
import xacro

def generate_launch_description():
  gazebo = IncludeLaunchDescription(
      PythonLaunchDescriptionSource([os.path.join(
          get_package_share_directory('gazebo_ros'), 'launch'), '/gazebo.launch.py']),
      )

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

