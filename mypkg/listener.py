import rclpy
from rclpy.node import Node
from person_msgs.msg import Person
from std_msgs.msg import Int16


rclpy.init()
node = Node("listener")


def cb(msg):
    global node
    node.get_logger().info("Listen: %s" % msg)
    node.get_logger().info("Listen: %d" % msg.data)


def main():
    pub = node.create_subscription(Person, "person", cb, 10)
    pub = node.create_subscription(Int16, "countup", cb, 10)
    rclpy.spin(node)
