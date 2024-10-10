#!/usr/bin/python3
import os
from launch import LaunchDescription
from ament_index_python.packages import get_package_share_directory
from launch_ros.actions import Node
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.actions import DeclareLaunchArgument, ExecuteProcess, IncludeLaunchDescription
from launch_ros.substitutions import FindPackageShare
from launch.substitutions import PathJoinSubstitution


def generate_launch_description():

    world_file = PathJoinSubstitution(
        [FindPackageShare("rav_bot"),
         "world",
         "obstacles.world"]
    )

    gazebo_launch = PathJoinSubstitution(
        [FindPackageShare("rav_bot"),
         "launch",
         "empty_gazebo.launch.py"]
    )

    gazebo_sime = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([gazebo_launch]),
        launch_arguments={'world_path': world_file}.items(),
    )

    return LaunchDescription([
        gazebo_sime
        
    ])
