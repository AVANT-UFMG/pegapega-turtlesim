#!/usr/bin/env python  
import roslib
roslib.load_manifest('pegapega_ws')
import rospy
import math
import tf
import geometry_msgs.msg
import turtlesim.srv

if __name__ == '__main__':
    rospy.init_node('tf_listener1')

    listener = tf.TransformListener()

    turtle_vel = rospy.Publisher('turtle1/cmd_vel', geometry_msgs.msg.Twist,queue_size=1)

    rate = rospy.Rate(10.0)
    while not rospy.is_shutdown():
        
        cmd = geometry_msgs.msg.Twist()
        cmd.linear.x = 1
        cmd.angular.z = 1
        turtle_vel.publish(cmd)

        rate.sleep()