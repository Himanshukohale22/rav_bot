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


    pkg_name = get_package_share_directory('rav_bot')
    pkg_path = os.path.join(pkg_name)

    rsp_file = os.path.join(pkg_path,'launch','rsp.launch.py')


    world_file = PathJoinSubstitution(
        [FindPackageShare("rav_bot"),
         "world",
         "clearpath_playpen.world"]
    )

    # world_execute =  ExecuteProcess(
    #         cmd=['gazebo', '--verbose', world_file],
    #         output='screen'
    # )

    # gazebo_launch = PathJoinSubstitution(
    #     [FindPackageShare("rav_bot"),
    #      "launch",
    #      "empty_gazebo.launch.py"]
    # )

    # gazebo_sime = IncludeLaunchDescription(
    #     PythonLaunchDescriptionSource([gazebo_launch]),
    #     launch_arguments={'world_path': world_file}.items(),
    # )



    # pkg_name = get_package_share_directory('rav_bot')
    # pkg_path = os.path.join(pkg_name)

    # rsp_file = os.path.join(pkg_path,'launch','rsp.launch.py')

    # world_path = os.path.join(pkg_path,'world','clearpath_playpen.world')

    # rsp_include = IncludeLaunchDescription(
    #     PythonLaunchDescriptionSource([rsp_file])
    # )

    # base_footprint_tf2_node = Node(
    #     package='tf2_ros',
    #     executable='static_transform_publisher',
    #     name='tf2_ros_chassie',
    #     output='screen',
    #     arguments=['0', '0', '0.033', '0', '0', '0', 'base_footprint', 'base_link']
        
    # )



    return LaunchDescription([


        
    ])
