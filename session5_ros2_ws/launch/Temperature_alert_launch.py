import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='session5_assignment',
            executable='temperature_publisher',
            name='temperature_publisher',
            output='screen'
        ),
        Node(
            package='session5_assignment',
            executable='threshold_subscriber',
            name='threshold_subscriber',
            output='screen'
        ),
        Node(
            package='session5_assignment',
            executable='alert_publisher',
            name='alert_publisher',
            output='screen'
        ),
    ])
