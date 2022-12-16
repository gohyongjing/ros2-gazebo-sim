# spawn_world

This package launches gazebo and a world based on a world file.

Contains the launch/gazebo.launch.py launch file

Contains the worlds/world file

## How to recreate
- Follow the instructions in the minimal_gazebo package, but naming the package as spawn_world instead
- Update gazebo.launch.py to spawn a world based on worlds/empty.world
- Add the URDF for the robot (Edit with your text editor or copy and paste the file
```
mkdir worlds
touch worlds/empty.world
```
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
