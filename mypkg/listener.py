import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class Listener(Node):
    def __init__(self):
        super().__init__("listener")
        self.sub = self.create_subscription(String, "question", self.cb, 10)

    def cb(self, msg):
        # 受信したメッセージをログに出力
        self.get_logger().info(f"Listener received: {msg.data}")


def main():
    rclpy.init()
    node = Listener()
    rclpy.spin(node)
