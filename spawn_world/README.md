# spawn_world

This package launches gazebo and a world based on a world file.

Contains the launch/gazebo.launch.py launch file

Contains the worlds/ world file

## How to recreate
- Update CMakeLists.txt to install the launch file by adding the following lines

```
...
if(BUILD_TESTING)
  ...
endif()

install(
  DIRECTORY launch worlds
  DESTINATION share/${PROJECT_NAME}
)

ament_package()
```
