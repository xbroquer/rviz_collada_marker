#!/usr/bin/env python
# license removed for brevity
import rclpy
from rclpy.node import Node

from visualization_msgs.msg import Marker
from visualization_msgs.msg import MarkerArray


class Talker(Node):

    def __init__(self):
        super().__init__('marker_mesh_sample')

        self.green = 0.0

        self.pub = self.create_publisher(Marker, 'marker1',  1)
        self.pub2 = self.create_publisher(Marker, 'marker2',  1)
        self.pub3 = self.create_publisher(Marker, 'marker3',  1)
        self.pub4 = self.create_publisher(Marker, 'marker4',  1)
        self.moonwalk_markers_pub = self.create_publisher(
            MarkerArray, 'markers', 1)

        timer_period = 0.1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)


    def timer_callback(self):

        #self.get_logger().info('timer...')
        mesh_marker = Marker()

        mesh_marker.header.frame_id = "nil_link"
        mesh_marker.header.stamp = self.get_clock().now().to_msg() 
        mesh_marker.pose.position.x = 1.0
        mesh_marker.pose.orientation.w = 1.0
        mesh_marker.scale.x = 1.0
        mesh_marker.scale.y = 1.0
        mesh_marker.scale.z = 1.0
        mesh_marker.type = Marker.MESH_RESOURCE
        #mesh_marker.mesh_resource = "package://pr2_description/meshes/base_v0/base.dae"
        mesh_marker.mesh_resource = "package://rviz_collada_marker/data/nil_link_mesh.dae"
        mesh_marker.mesh_use_embedded_materials = True
        self.pub.publish(mesh_marker)

        mesh_marker.mesh_resource = "package://rviz_collada_marker/data/base.dae"
        mesh_marker.pose.position.y = 2.0
        self.pub2.publish(mesh_marker)

        mesh_marker.pose.position.y = 4.0
        mesh_marker.color.r = 0.0
        mesh_marker.color.g = self.green
        mesh_marker.color.b = 0.0
        mesh_marker.color.a = 0.2
        self.pub3.publish(mesh_marker)

        mesh_marker.mesh_use_embedded_materials = False
        mesh_marker.pose.position.y = 6.0
        mesh_marker.color.r = 0.0
        mesh_marker.color.g = self.green
        mesh_marker.color.b = 0.0
        mesh_marker.color.a = 0.2
        self.pub4.publish(mesh_marker)

        moonwalk_markers = MarkerArray()
        moonwalk1 = Marker()
        moonwalk1.header.frame_id = "/nil_link"
        moonwalk1.header.stamp = self.get_clock().now().to_msg() 
        moonwalk1.ns = "moonwalk"
        moonwalk1.id = 0
        moonwalk1.type = Marker.MESH_RESOURCE
        moonwalk1.mesh_resource = "package://rviz_collada_marker/data/moonwalk.dae"
        moonwalk1.mesh_use_embedded_materials = True
        moonwalk1.pose.position.x = 2.0
        moonwalk1.pose.position.y = 2.0
        moonwalk1.pose.position.z = 0.0
        moonwalk1.pose.orientation.x = 0.0
        moonwalk1.pose.orientation.y = 0.0
        moonwalk1.pose.orientation.z = 0.0
        moonwalk1.pose.orientation.w = 1.0
        moonwalk1.scale.x = 1.0
        moonwalk1.scale.y = 1.0
        moonwalk1.scale.z = 1.0
        moonwalk1.color.r = 0.0
        moonwalk1.color.g = 0.0
        moonwalk1.color.b = 0.0
        moonwalk1.color.a = 0.0

        moonwalk_markers.markers.append(moonwalk1)
        moonwalk2 = Marker()
        moonwalk2.header.frame_id = "/nil_link"
        moonwalk2.header.stamp = self.get_clock().now().to_msg() 
        moonwalk2.ns = "moonwalk"
        moonwalk2.id = 1
        moonwalk2.type = Marker.MESH_RESOURCE
        moonwalk2.mesh_resource = "package://rviz_collada_marker/data/moonwalk.dae"
        moonwalk2.mesh_use_embedded_materials = True

        moonwalk2.pose.position.x = 2.0
        moonwalk2.pose.position.y = 4.0
        moonwalk2.pose.position.z = 0.0
        moonwalk2.pose.orientation.x = 0.0
        moonwalk2.pose.orientation.y = 0.0
        moonwalk2.pose.orientation.z = 0.0
        moonwalk2.pose.orientation.w = 1.0
        moonwalk2.scale.x = 1.0
        moonwalk2.scale.y = 1.0
        moonwalk2.scale.z = 1.0
        moonwalk2.color.r = 0.0
        moonwalk2.color.g = self.green
        moonwalk2.color.b = 0.0
        moonwalk2.color.a = 0.2

        moonwalk_markers.markers.append(moonwalk2)

        moonwalk3 = Marker()
        moonwalk3.header.frame_id = "/nil_link"
        moonwalk3.header.stamp = self.get_clock().now().to_msg() 
        moonwalk3.ns = "moonwalk"
        moonwalk3.id = 2
        moonwalk3.type = Marker.MESH_RESOURCE
        moonwalk3.mesh_resource = "package://rviz_collada_marker/data/moonwalk.dae"
        moonwalk3.mesh_use_embedded_materials = False
        moonwalk3.pose.position.x = 2.0
        moonwalk3.pose.position.y = 6.0
        moonwalk3.pose.position.z = 0.0
        moonwalk3.pose.orientation.x = 0.0
        moonwalk3.pose.orientation.y = 0.0
        moonwalk3.pose.orientation.z = 0.0
        moonwalk3.pose.orientation.w = 1.0
        moonwalk3.scale.x = 1.0
        moonwalk3.scale.y = 1.0
        moonwalk3.scale.z = 1.0
        moonwalk3.color.r = 0.0
        moonwalk3.color.g = self.green
        moonwalk3.color.b = 0.0
        moonwalk3.color.a = 1.0
        moonwalk_markers.markers.append(moonwalk3)
        self.moonwalk_markers_pub.publish(moonwalk_markers)
        self.green += 0.01
        if self.green > 1.0:
            self.green = 0.0


def main(args=None):
    rclpy.init(args=args)

    talker = Talker()

    rclpy.spin(talker)

    talker.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
