import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import datetime
import random


class Talker(Node):
    def __init__(self):
        super().__init__("talker")
        self.pub = self.create_publisher(String, "question", 10)
        self.create_timer(1.0, self.publish_question)

    def publish_question(self):
        muscle_groups = [
            "大胸筋", "僧帽筋", "上腕三頭筋", "広背筋", "大臀筋",
            "大腿二頭筋", "下腿三頭筋", "三角筋", "上腕二頭筋",
            "腹直筋", "大腿四頭筋"
        ]
        selected_muscle = random.choice(muscle_groups)
        today = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        msg = String()
        msg.data = f"日時: {today} | 今日の筋トレ部位: {selected_muscle}"
        self.get_logger().info(f"Talker: {msg.data}")
        self.pub.publish(msg)


def main():
    rclpy.init()
    node = Talker()
    rclpy.spin(node)
