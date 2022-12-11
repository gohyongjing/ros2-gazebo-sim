# minimal_gazebo

This package contains a launch file that is a simple wrapper around the gazebo launch file. Use this to check that ros2 and gazebo is installed correctly.

Contains the gazebo.launch.py launch file

## How to recreate
- Create new package named minimal_gazebo
```
ros2 pkg create --build-type ament_cmake minimal_gazebo
```
- Create the launch file (Write the file using your editor or copy paste)
```
cd minimal_gazebo
mkdir launch
touch launch/gazebo.launch.py
```
- In particular, the following lines bring in the gazebo launch description
```
  gazebo = IncludeLaunchDescription(
      PythonLaunchDescriptionSource([os.path.join(
          get_package_share_directory('gazebo_ros'), 'launch'), '/gazebo.launch.py']),
      )
```
- Update CMakeLists.txt to install the launch file by adding the following lines

```
...
if(BUILD_TESTING)
  ...
endif()

install(
  DIRECTORY launch
  DESTINATION share/${PROJECT_NAME}
)

ament_package()
```
