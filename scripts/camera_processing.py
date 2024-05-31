#!/usr/bin/env python3
import os
import rospy, cv2
import numpy as np
from cv_bridge import CvBridge

from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist


from sensor_msgs.msg import Image
from sensor_msgs.msg import Range

import tf
# import tf_conversions
from random import randint
import time

class Example(object):

    def __init__(self):
        rospy.init_node("camera_processing_node")
        self.camera_subscriber = rospy.Subscriber('/usb_cam/image_raw', Image, self.camera_cb)
        self.image_preprocessed_publisher = rospy.Publisher('/image_preprocessed', Image, queue_size=3)
        self.bridge = CvBridge()

    def camera_cb(self, msg):
        frame = self.bridge.imgmsg_to_cv2(msg)
        frame = cv2.flip(frame, -1)
        self.image_preprocessed_publisher.publish(self.bridge.cv2_to_imgmsg(frame, 'bgr8'))

def main(args=None):
    Example()
    rospy.spin()

if __name__ == "__main__":
    main()
