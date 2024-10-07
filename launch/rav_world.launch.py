from launch import LaunchDescription 
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
import os

from ament_index_python import get_package_share_directory
from launch_ros.actions import Node
    

def get_launch_description():
    
    rav_bot_rviz = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_path,'launch/robot.launch.py')
        )
    )

    world_file = PathJoinSubstitution(
        [FindPackageShare(pkg_path),
        "worlds",
        "clearpath_playpen.world"],
    )
    
    robot_world = Node(
        package='',
        executable='/* exec_name */',
        name='/* node_name */',
        output='screen'),

    return LaunchDescription([
        robot_world
    ])