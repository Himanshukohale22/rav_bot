## launching gazebo and rviz template 

import os
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

from ament_index_python.packages import get_package_share_directory



def generate_launch_description():

    pkg_path = get_package_share_directory('rav_bot')

    robot_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(pkg_path,'launch','robot.launch.py')
    )

    gazebo_pkg = get_package_share_directory('gazebo_ros')

    gzserver = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join[gazebo_pkg,'launch','gzserver.launch.py'],
        )
    )

    gzclient = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(gazebo_pkg,'launch','gzclient.launch.py')
        )
    )

    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen'
    )

    spawn_entity_node = Node(
        package='spawn_enity',
        executable= 'spawn_enity',
        name='spawn_entity',
        output='screen',
        parameters=''
    )

    return LaunchDescription(
        robot_launch,
        gzserver,
        gzclient,
        robot_state_publisher_node,
        spawn_entity_node
    )