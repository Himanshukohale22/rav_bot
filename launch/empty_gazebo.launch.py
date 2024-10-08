#!/usr/bin/python3
import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch_ros.actions import Node
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():

    pkg_path = os.path.join('rav_bot')
    
    urdf_file = os.path.join(get_package_share_directory(pkg_path),'urdf','robot.urdf.xacro')

    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        arguments=[urdf_file]
    )
    
    gazebo_node = Node(
            package='gazebo_ros',
            executable='gazebo',
            name='gazebo',
            output='screen',
            arguments=['--verbose', '-s', 'libgazebo_ros_factory.so']  # Factory plugin allows model spawning
        ),

    spawn_robot = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        name='spwan_entity',
        output='screen',
        arguments=[
            '-topic', '/robot_description',
            '-entity', 'my_robot',  # Using formatted string for entity name
            '-z', '0.28',
            '-x', '0',
            '-y', '0',
            '-Y', '0'
        ]
    )


    return LaunchDescription([

        # rsp,
        # rviz_launch,
        robot_state_publisher_node,
        gazebo_node,
        spawn_robot
        
    ])
