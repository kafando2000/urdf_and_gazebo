from launch import LaunchDescription
import os 
from ament_index_python.packages import get_package_share_path
from launch_ros.parameter_descriptions import ParameterValue
from launch_ros.actions import Node
from launch.substitutions import Command


def generate_launch_description():
    
    urdf_path = os.path.join(get_package_share_path('rb_description'),'urdf','mobilrobot.urdf.xacro')
    rviz_config = os.path.join(get_package_share_path('rb_description'),'rviz','rviz_config.rviz')
    robot_description = ParameterValue(Command(['xacro ',urdf_path]),value_type=str)
    robot_state_publisher = Node(
        package="robot_state_publisher",
        executable= "robot_state_publisher",
        parameters=[{"robot_description":robot_description}]
    )
    joint_state_publisher_gui = Node(
        package="joint_state_publisher_gui",
        executable= "joint_state_publisher_gui",
    )
    rviz2_node = Node(
        package="rviz2",
        executable="rviz2",
        arguments=['-d',rviz_config]
        
    )
    
    return LaunchDescription([
        robot_state_publisher,
        joint_state_publisher_gui,
        rviz2_node,
        
    ])