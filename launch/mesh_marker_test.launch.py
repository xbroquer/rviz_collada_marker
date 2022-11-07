from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import Command
from ament_index_python import get_package_share_directory
import os

def generate_launch_description():

    rviz_config_path = os.path.join(get_package_share_directory('rviz_collada_marker'), 'config/mesh_marker_test.rviz')


    rviz2_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        respawn=True,
        output='screen',
        arguments=['-d', rviz_config_path],
    )

    rviz_collada_marker = Node(
        package='rviz_collada_marker',
        executable='rviz_collada_marker',
        name='rviz_collada_marker',
        respawn=True,
        output='screen'
    )

    # tf2_ros_node = Node(
    #     package='tf2_ros',
    #     executable='static_transform_publisher',
    #     name='nil_link_base2_M1K',
    #     arguments=['1', '0', '0', '0', '0', '0', 'nil_link', 'base2_M1K'],
    #     respawn=True,
    #     output='screen',
    # )


    return LaunchDescription([
      #tf2_ros_node,
      rviz2_node,
      rviz_collada_marker,
    ])


