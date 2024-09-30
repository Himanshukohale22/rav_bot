## launching gazebo and rviz template 

import os
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

from ament_index_python.packages import get_package_share_directory



def generate_launch_description():

    gazebo_pkg = get_package_share_directory('gazebo_ros')

    # world_path = os.path.join(get_package_share_directory())

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
        gzserver,
        gzclient,
        robot_state_publisher_node,
        spawn_entity_node
    )