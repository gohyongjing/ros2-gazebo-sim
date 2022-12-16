import os
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():

  pkg_gazebo_ros = FindPackageShare(package='gazebo_ros').find('gazebo_ros')
  pkg_share = FindPackageShare(package='spawn_world').find('spawn_world')
  world_path = os.path.join(pkg_share, 'worlds', 'empty.world')

  # Start Gazebo server
  gazebo_server = IncludeLaunchDescription(
    PythonLaunchDescriptionSource(os.path.join(pkg_gazebo_ros, 'launch', 'gzserver.launch.py')),
    launch_arguments={'world': world_path}.items())
 
  # Start Gazebo client    
  gazebo_client = IncludeLaunchDescription(
    PythonLaunchDescriptionSource(os.path.join(pkg_gazebo_ros, 'launch', 'gzclient.launch.py'))
  )

  return LaunchDescription([
      gazebo_server,
      gazebo_client,
  ])

