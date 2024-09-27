from launch import LaunchDescription 
from launch.actions import IncludeLaunchDescription, ExecuteProcess
from launch.launch_description_sources import PythonLaunchDescriptionSource
import os

from ament_index_python import get_package_share_directory
from launch_ros.actions import Node
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():

    pkg_path = os.path.join(get_package_share_directory('rav_bot'))

    rav_bot_rviz = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(get_package_share_directory('rav_bot'),
                         'launch/robot.launch.py')
        )
    )

    world_file = PathJoinSubstitution(
        [FindPackageShare(pkg_path),
        "worlds",
        "clearpath_playpen.world"],
    )

    gzserver = ExecuteProcess(
        cmd=['gzserver',
             '-s', 'libgazebo_ros_init.so',
             '-s', 'libgazebo_ros_factory.so',
             world_file],
        output='screen',
    )

    # Gazebo client
    gzclient = ExecuteProcess(
        cmd=['gzclient'],
        output='screen',
        # condition=IfCondition(LaunchConfiguration('gui')),
    )


    spawn_robot = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        name='spawn_husky',
        arguments=['-entity',
                   'rav',
                   '-topic',
                   'rav_bot'],
        output='screen',
    )

    

    return LaunchDescription([

        spawn_robot,

    ])
    