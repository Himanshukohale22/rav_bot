
from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration, Command
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node
import os


def generate_launch_description():

    # Check if we're told to use sim time
    use_sim_time = LaunchConfiguration('use_sim_time')
    use_ros2_control = LaunchConfiguration('use_ros2_control')

    # Process the URDF file
    pkg_path = os.path.join(get_package_share_directory('rav_bot'))
    xacro_file = os.path.join(pkg_path,'urdf','robot.urdf.xacro')
    # robot_description_config = xacro.process_file(xacro_file).toxml()
    robot_description_config = Command(['xacro ', xacro_file, ' use_ros2_control:=', use_ros2_control, ' sim_mode:=', use_sim_time])
    
    # Create a robot_state_publisher node
    params = {'robot_description': robot_description_config, 'use_sim_time': use_sim_time}

    # left_wheel_tf2_node = Node(
    #     package='tf2_ros',
    #     executable='static_transform_publisher',
    #     name='tf2_ros_left_wheel',
    #     output='screen',
    #     arguments=['0', '0.1485', '0', '0', '0', '-1.570795', 'base_link', 'left_wheel']
    # )

    # right_wheel_tf2_node = Node(
    #     package='tf2_ros',
    #     executable='static_transform_publisher',
    #     name='tf2_ros_right_wheel',
    #     output='screen',
    #     arguments=['0', '-0.1485', '0', '0', '0', '-1.570795', 'base_link', 'right_wheel']
        
    # )

    # chassie_tf2_node = Node(
    #     package='tf2_ros',
    #     executable='static_transform_publisher',
    #     name='tf2_ros_chassie',
    #     output='screen',
    #     arguments=['-0.226', '0', '-0.01', '0', '0', '0', 'base_link', 'chassis']
        
    # )

    # base_footprint_tf2_node = Node(
    #     package='tf2_ros',
    #     executable='static_transform_publisher',
    #     name='tf2_ros_chassie',
    #     output='screen',
    #     arguments=['0', '0', '0.033', '0', '0', '0', 'base_footprint', 'base_link']
        
    # )

    # caster_wheel_tf2_node = Node(
    #     package='tf2_ros',
    #     executable='static_transform_publisher',
    #     name='tf2_ros_chassie',
    #     output='screen',
    #     arguments=['0.075', '0', '-0.013', '0', '0', '0', 'chassis', 'caster_wheel']
        
    # )

    node_robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[params]
    )
    
    joint_state_publisher_gui_node = Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui',
        name='joint_state_publisher_gui',
        output='screen'
    )

    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen'
    )


    # Launch!
    return LaunchDescription([
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='false',
            description='Use sim time if true'),
        DeclareLaunchArgument(
            'use_ros2_control',
            default_value='true',
            description='Use ros2_control if true'),

        node_robot_state_publisher,
        rviz_node,
        # left_wheel_tf2_node,
        # right_wheel_tf2_node
        # caster_wheel_tf2_node,
        # chassie_tf2_node,
        # base_footprint_tf2_node
        joint_state_publisher_gui_node
    ])