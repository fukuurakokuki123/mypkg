import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class Talker(Node):
    def __init__(self):
        super().__init__("talker")
        self.pub = self.create_publisher(String, "question", 10)
        self.create_timer(1.0, self.publish_question)

    def publish_question(self):
        msg = String()
        msg.data = "今日の筋トレは何をやるんだ？"
        self.get_logger().info(f"Talker: {msg.data}")
        self.pub.publish(msg)


def main():
    rclpy.init()
    node = Talker()
    rclpy.spin(node)a
