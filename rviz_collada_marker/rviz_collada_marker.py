#!/usr/bin/env python
# license removed for brevity
import rclpy
from rclpy.node import Node

from visualization_msgs.msg import Marker

class Talker(Node):

    def __init__(self):
        super().__init__('mesh_marker_test')

        self.marker_pub = self.create_publisher(Marker, 'mesh_markers',  200)

        self.rgba = [0.0, 0.0, 0.0, 0.0]
        self.id = 0
        self.x = 0.0
        self.y = 0.0

        timer_period = 1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def publishText(self, x, y, text):
        text_marker = Marker()
        text_marker.header.frame_id = "base_link"
        text_marker.header.stamp = self.get_clock().now().to_msg() 
        text_marker.ns = "mesh"
        text_marker.type = Marker.TEXT_VIEW_FACING
        text_marker.action = Marker.ADD
        text_marker.pose.orientation.x = 0.0
        text_marker.pose.orientation.y = 0.0
        text_marker.pose.orientation.z = 0.0
        text_marker.pose.orientation.w = 1.0
        text_marker.color.r = 1.0
        text_marker.color.g = 1.0
        text_marker.color.b = 1.0
        text_marker.color.a = 1.0
        text_marker.scale.z = 0.2
        text_marker.text = text
        text_marker.id = self.id
        text_marker.pose.position.x = x
        text_marker.pose.position.y = y
        self.id = self.id + 1

        self.marker_pub.publish(text_marker)
    

    def publishMesh(self, x, y, r, g, b, a, use_embedded_materials, mesh):
        marker = Marker()
        marker.header.frame_id = "base_link"
        marker.header.stamp = self.get_clock().now().to_msg() 
        marker.ns = "mesh"
        match mesh:
            case 0:
                marker.type = Marker.MESH_RESOURCE
                marker.mesh_resource = "package://rviz_collada_marker/data/base.dae"
                marker.mesh_use_embedded_materials = use_embedded_materials
            case 1:
                marker.type = Marker.MESH_RESOURCE
                marker.mesh_resource = "package://rviz_collada_marker/data/frame.dae"
                marker.mesh_use_embedded_materials = use_embedded_materials
            case 2:
                marker.type = Marker.SPHERE
            case 3:
                marker.type = Marker.MESH_RESOURCE
                marker.mesh_resource = "package://rviz_collada_marker/data/moonwalk.dae"
                marker.mesh_use_embedded_materials = use_embedded_materials

            
        marker.action = Marker.ADD
        marker.pose.orientation.x = 0.0
        marker.pose.orientation.y = 0.0
        marker.pose.orientation.z = 0.0995
        marker.pose.orientation.w = 0.995
        marker.scale.x = 1.0
        marker.scale.y = 1.0
        marker.scale.z = 1.0
        marker.color.r = r
        marker.color.g = g
        marker.color.b = b
        marker.color.a = a
        marker.frame_locked = True
        marker.id = self.id
        marker.pose.position.x = x
        marker.pose.position.y = y
        self.id = self.id + 1
        self.marker_pub.publish(marker)


    def publishMeshes(self, x, r, g, b, a):
        y = -5.0
        buffer = "rbg:%.1f,%.1f,%.1f,a:%.1f" % (r, g, b, a)

        self.publishText(x, y - 1, buffer)

        self.publishMesh(x, y, r, g, b, a, True, 0)
        y = y + 1

        self.publishMesh(x, y, r, g, b, a, False, 0)

        y = y + 1
        self.publishMesh(x, y, r, g, b, a, True, 1)

        y = y + 1
        self.publishMesh(x, y, r, g, b, a, False, 1)

        y = y + 1
        self.publishMesh(x, y, r, g, b, a, True, 2)

        y = y + 1
        self.publishMesh(x, y, r, g, b, a, False, 2)

        y = y + 1
        self.publishMesh(x, y, r, g, b, a, False, 3)
        y = y + 1
        self.publishMesh(x, y, r, g, b, a, True, 3)


    def publishAllMeshes(self):
        #ROS_INFO("Publishing")
        self.id = 0
        self.x = -7.0
        self.y = -5.0

        # column headers
        self.publishText(self.x, self.y, "mesh1,use_embedded_materials=true")
        self.y = self.y + 1
        self.publishText(self.x, self.y, "mesh1,use_embedded_materials=false")
        self.y = self.y + 1
        self.publishText(self.x, self.y, "mesh2,use_embedded_materials=true")
        self.y = self.y + 1
        self.publishText(self.x, self.y, "mesh2,use_embedded_materials=false")
        self.y = self.y + 1
        self.publishText(self.x, self.y, "sphere,use_embedded_materials=true")
        self.y = self.y + 1
        self.publishText(self.x, self.y, "sphere,use_embedded_materials=false")
        self.y = self.y + 1
        self.publishText(self.x, self.y, "moonwalk,use_embedded_materials=false")
        self.y = self.y + 1
        self.publishText(self.x, self.y, "moonwalk,use_embedded_materials=true")
        self.y = self.y + 1

        self.x = -6.0

        self.publishMeshes(self.x, 0.0, 0.0, 0.0, 0.0)
        self.x = self.x + 1

        self.publishMeshes(self.x, 1.0, 1.0, 1.0, 1.0)
        self.x = self.x + 1
        self.publishMeshes(self.x, 1.0, 1.0, 1.0, 0.5)
        self.x = self.x + 1
        self.publishMeshes(self.x, 1.0, 1.0, 1.0, 0.0)
        self.x = self.x + 1

        self.publishMeshes(self.x, 1.0, 0.0, 0.0, 1.0)
        self.x = self.x + 1
        self.publishMeshes(self.x, 1.0, 0.0, 0.0, 0.5)
        self.x = self.x + 1
        self.publishMeshes(self.x, 1.0, 0.0, 0.0, 0.0)
        self.x = self.x + 1

        self.publishMeshes(self.x, 1.0, .5, .5, 1.0)
        self.x = self.x + 1
        self.publishMeshes(self.x, 1.0, .5, .5, 0.5)
        self.x = self.x + 1
        self.publishMeshes(self.x, 1.0, .5, .5, 0.0)
        self.x = self.x + 1
        
        self.publishMeshes(self.x, self.rgba[0], self.rgba[1], self.rgba[2], self.rgba[3])
        
        # evolve colors over time
        index = 3

        #self.get_logger().info("id %d" % (self.id))
        while (index >= 0):
        
            self.rgba[index] += 0.2
            if (self.rgba[index] > 1.01):
                self.rgba[index] = 0.0
                index = index - 1
            else:
                break


    def timer_callback(self):
        self.publishAllMeshes()


def main(args=None):
    rclpy.init(args=args)

    talker = Talker()

    rclpy.spin(talker)

    talker.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
