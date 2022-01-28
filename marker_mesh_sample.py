#!/usr/bin/env python

import rospy
from visualization_msgs.msg import Marker
from visualization_msgs.msg import MarkerArray

rospy.init_node("marker_mesh_sample")

pub = rospy.Publisher('marker', Marker, queue_size=1)
pub2 = rospy.Publisher('marker2', Marker, queue_size=1)
pub3 = rospy.Publisher('marker3', Marker, queue_size=1)
pub4 = rospy.Publisher('marker4', Marker, queue_size=1)
moonwalk_markers_pub = rospy.Publisher('markers', MarkerArray, queue_size=1)

r = rospy.Rate(10)

green = 0

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
    mesh_marker.pose.position.y = 4.0
    mesh_marker.color.r = 0
    mesh_marker.color.g = green
    mesh_marker.color.b = 0
    mesh_marker.color.a = 0.2
    pub3.publish(mesh_marker)   
    mesh_marker.mesh_use_embedded_materials = False
    mesh_marker.pose.position.y = 6.0
    mesh_marker.color.r = 0
    mesh_marker.color.g = green
    mesh_marker.color.b = 0
    mesh_marker.color.a = 0.2
    pub4.publish(mesh_marker)   
    moonwalk_markers = MarkerArray()    
    moonwalk1 = Marker()
    moonwalk1.header.frame_id = "/nil_link"
    moonwalk1.header.stamp = rospy.Time.now()
    moonwalk1.ns = "moonwalk"
    moonwalk1.id = 0
    moonwalk1.type = Marker.MESH_RESOURCE
    moonwalk1.mesh_resource = "package://rviz_collada_marker/moonwalk.dae"
    moonwalk1.mesh_use_embedded_materials=True  
    moonwalk1.pose.position.x = 2
    moonwalk1.pose.position.y = 2
    moonwalk1.pose.position.z = 0
    moonwalk1.pose.orientation.x = 0.0
    moonwalk1.pose.orientation.y = 0.0
    moonwalk1.pose.orientation.z = 0.0
    moonwalk1.pose.orientation.w = 1.0
    moonwalk1.scale.x = 1.0
    moonwalk1.scale.y = 1.0
    moonwalk1.scale.z = 1.0
    moonwalk1.color.r = 0
    moonwalk1.color.g = 0
    moonwalk1.color.b = 0
    moonwalk1.color.a = 0

    moonwalk_markers.markers.append(moonwalk1)  
    moonwalk2 = Marker()
    moonwalk2.header.frame_id = "/nil_link"
    moonwalk2.header.stamp = rospy.Time.now()
    moonwalk2.ns = "moonwalk"
    moonwalk2.id = 1
    moonwalk2.type = Marker.MESH_RESOURCE
    moonwalk2.mesh_resource = "package://rviz_collada_marker/moonwalk.dae"
    moonwalk2.mesh_use_embedded_materials=True

    moonwalk2.pose.position.x = 2
    moonwalk2.pose.position.y = 4
    moonwalk2.pose.position.z = 0
    moonwalk2.pose.orientation.x = 0.0
    moonwalk2.pose.orientation.y = 0.0
    moonwalk2.pose.orientation.z = 0.0
    moonwalk2.pose.orientation.w = 1.0
    moonwalk2.scale.x = 1.0
    moonwalk2.scale.y = 1.0
    moonwalk2.scale.z = 1.0
    moonwalk2.color.r = 0
    moonwalk2.color.g = green
    moonwalk2.color.b = 0
    moonwalk2.color.a = 0.2

    moonwalk_markers.markers.append(moonwalk2)  
    moonwalk3 = Marker()
    moonwalk3.header.frame_id = "/nil_link"
    moonwalk3.header.stamp = rospy.Time.now()
    moonwalk3.ns = "moonwalk"
    moonwalk3.id = 2
    moonwalk3.type = Marker.MESH_RESOURCE
    moonwalk3.mesh_resource = "package://rviz_collada_marker/moonwalk.dae"
    moonwalk3.mesh_use_embedded_materials=False
    moonwalk3.pose.position.x = 2
    moonwalk3.pose.position.y = 6
    moonwalk3.pose.position.z = 0
    moonwalk3.pose.orientation.x = 0.0
    moonwalk3.pose.orientation.y = 0.0
    moonwalk3.pose.orientation.z = 0.0
    moonwalk3.pose.orientation.w = 1.0
    moonwalk3.scale.x = 1.0
    moonwalk3.scale.y = 1.0
    moonwalk3.scale.z = 1.0
    moonwalk3.color.r = 0
    moonwalk3.color.g = green
    moonwalk3.color.b = 0
    moonwalk3.color.a = 0.2 
    moonwalk_markers.markers.append(moonwalk3)  
    moonwalk_markers_pub.publish(moonwalk_markers)  
    green += 0.1    
    if green > 1:
        green = 0

    r.sleep()
    

