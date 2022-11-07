from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import Command
from ament_index_python import get_package_share_directory
import os

def generate_launch_description():

    rviz_config_path = os.path.join(get_package_share_directory('rviz_collada_marker'), 'config/default.rviz')
    robot_description_path = os.path.join(get_package_share_directory('rviz_collada_marker'), 'data/truck.urdf')

    rviz2_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        respawn=True,
        output='screen',
        arguments=['-d', rviz_config_path],
    )

    tf2_ros_node = Node(
        package='tf2_ros',
        executable='static_transform_publisher',
        name='nil_link_base2_M1K',
        arguments=['1', '0', '0', '0', '0', '0', 'nil_link', 'base2_M1K'],
        respawn=True,
        output='screen',
    )

    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        respawn=True,
        output='screen',
        parameters=[{'robot_description': Command(['cat ', robot_description_path])}],
    )


    return LaunchDescription([
      tf2_ros_node,
      robot_state_publisher_node,
      rviz2_node,
    ])

