#!/usr/bin/env python

import rospy
from visualization_msgs.msg import Marker

rospy.init_node("marker_mesh_sample")

pub = rospy.Publisher('marker', Marker)
pub2 = rospy.Publisher('marker2', Marker)
r = rospy.Rate(10)
while not rospy.is_shutdown():
    mesh_marker = Marker()
    
    mesh_marker.header.frame_id = "nil_link"
    mesh_marker.header.stamp = rospy.Time.now()
    mesh_marker.pose.position.x = 1.0
    mesh_marker.pose.orientation.w = 1.0
    mesh_marker.scale.x = 1.0
    mesh_marker.scale.y = 1.0
    mesh_marker.scale.z = 1.0

    mesh_marker.type = Marker.MESH_RESOURCE
    #mesh_marker.mesh_resource = "package://pr2_description/meshes/base_v0/base.dae"
    mesh_marker.mesh_resource = "package://rviz_collada_marker/nil_link_mesh.dae"
    mesh_marker.mesh_use_embedded_materials = True
    pub.publish(mesh_marker)

    mesh_marker.mesh_resource = "package://rviz_collada_marker/base.dae"
    mesh_marker.pose.position.y = 2.0
    pub2.publish(mesh_marker)
    r.sleep()
