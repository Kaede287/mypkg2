#SPDX-FileCopyrightText: 2023 Kaede Ichikawa
#SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

def cb(msg):

    global node
    time = 2000 - msg.data

    if time % 5 == 0:

        node.get_logger().info('残り %d です' % time)

        
    if time % 2 == 0:
        node.get_logger().info("Listen: %d 偶数です" % time)

    else:
        node.get_logger().info("Listen: %d 奇数です" % time)

rclpy.init()
node = Node("listener")
pub = node.create_subscription(Int16, "countdown", cb,  10)
rclpy.spin(node)
