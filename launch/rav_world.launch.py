from launch import LaunchDescription 
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
import os

from ament_index_python import get_package_share_directory
from launch_ros.actions import Node
    

def generate_launch_description():

    pkg_path = get_package_share_directory('rav_bot')

    gazebo_pkg = get_package_share_directory('gazebo_ros')

    world_path = os.path.join(pkg_path,'worlds','clearpath_playpen.world')

    gzserver_cmd = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(gazebo_pkg,'launch','gzserver.launch.py'),
        )
    )

    gzclient_cmd = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(gazebo_pkg,'launch','gzclient.launch.py')

        )
    )

    spawn_robot = Node(
        package="gazebo_ros",
        executable="spawn_entity.py",
        arguments=["-topic", "robot_description", "-entity", "rav_bot", "-x", "0.0", "-y", "0.0", "-z", "0.0"],
        output="screen")

    return LaunchDescription([
        
        spawn_robot,
        gzserver_cmd,
        gzclient_cmd,

    ])