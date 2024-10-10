# # from launch import LaunchDescription
# # from launch.actions import DeclareLaunchArgument
# # from launch_ros.actions import Node
# # from launch.substitutions import LaunchConfiguration
# # from launch_ros.substitutions import FindPackageShare
# # from launch.actions import ExecuteProcess, IncludeLaunchDescription
# # from launch.launch_description_sources import PythonLaunchDescriptionSource
# # from launch.substitutions import PathJoinSubstitution

# # def generate_launch_description():

# #     world_path = LaunchConfiguration('world_path')

# #     gazebo_launch = PathJoinSubstitution(
# #         [FindPackageShare("rav_bot"),
# #          "launch",
# #          "e_gazebo.launch.py"]
# #     )


# #     launch_include = IncludeLaunchDescription(
# #         PythonLaunchDescriptionSource([gazebo_launch]))


# #     return LaunchDescription([
# #         DeclareLaunchArgument(
# #             'world_path',
# #             default_value='/home/himanshu/ros2_ws/src/rav_bot/world/obstacles.world',
# #             description='Path to the world file to load'
# #         ),
        
# #         ExecuteProcess(
# #             cmd=['gazebo', '--verbose', world_path],
# #             output='screen'
# #         ),
# #         launch_include

# #     ])


# #!/usr/bin/python3
# import os
# from launch import LaunchDescription
# from ament_index_python.packages import get_package_share_directory
# from launch_ros.actions import Node
# from launch.launch_description_sources import PythonLaunchDescriptionSource
# from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
# from launch_ros.substitutions import FindPackageShare
# from launch.substitutions import PathJoinSubstitution

# def generate_launch_description():

#     # Define the path to the world file
#     world_file = PathJoinSubstitution(
#         [FindPackageShare("rav_bot"),
#          "world",
#          "obstacles.world"]
#     )

#     # Path to the empty_gazebo.launch.py
#     gazebo_launch = PathJoinSubstitution(
#         [FindPackageShare("rav_bot"),
#          "launch",
#          "e_gazebo.launch.py"]
#     )

#     # Include the empty_gazebo.launch.py launch file and pass the world_path argument
#     gazebo_sime = IncludeLaunchDescription(
#         PythonLaunchDescriptionSource(gazebo_launch),
#         launch_arguments={'world_path': world_file}.items(),
#     )

#     return LaunchDescription([
#         # Include Gazebo with the world file argument
#         gazebo_sime
#     ])


from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
from launch_ros.substitutions import FindPackageShare
from launch.actions import ExecuteProcess

def generate_launch_description():
    world_path = LaunchConfiguration('world_path')

    return LaunchDescription([
        DeclareLaunchArgument(
            'world_path',
            default_value='/home/himanshu/ros2_ws/src/rav_bot/world/obstacles.world',
            description='Path to the world file to load'
        ),
        
        ExecuteProcess(
            cmd=['gazebo', '--verbose', world_path],
            output='screen'
        )
    ])
