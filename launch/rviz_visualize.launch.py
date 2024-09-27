import os
from launch import LaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory
from launch_ros.actions import Node
from launch.substitutions import Command

from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():

    pkg_name = 'rav_bot'

    # pkg_path = os.path.join(get_package_share_directory('rav_bot'))
    pkg_path = FindPackageShare('rav_bot')

    # urdf_path = os.path.join(pkg_path,'robot.urdf.xacro')
    urdf_path = PathJoinSubstitution(['/home/himanshu/ros2_ws/src/rav_bot/urdf','robot.urdf.xacro'])

    # rviz_path = os.path.join(pkg_path,'rav.rviz')
    rviz_path = PathJoinSubstitution([pkg_path,'rviz','rav.rviz'])

    # urdf_tutorial_path = FindPackageShare('urdf_tutorial')
    # default_model_path = PathJoinSubstitution(['urdf', '01-myfirst.urdf'])
    # default_rviz_config_path = PathJoinSubstitution([urdf_tutorial_path, 'rviz', 'urdf.rviz'])


    robot_satate_publisher_node = Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            arguments=[urdf_path]
          
    )

    joint_state_publisher_node_gui = Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui',
        name='joint_state_publisher_gui',
        output='screen'
    )

    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen',
        arguments=['-d',rviz_path]
    )

    return LaunchDescription([

        robot_satate_publisher_node,
        # joint_state_broadcaster_node,
        rviz_node,
        joint_state_publisher_node_gui

    ])


