import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():

  gazebo = IncludeLaunchDescription(
      PythonLaunchDescriptionSource([os.path.join(
          get_package_share_directory('gazebo_ros'), 'launch'), '/gazebo.launch.py']),
      )

  talker = Node(
    package='py_pubsub',
    executable='talker',
    output='screen',
  )

  return LaunchDescription([
      gazebo,
      talker,
  ])

