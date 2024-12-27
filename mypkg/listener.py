import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import random


class Listener(Node):
    def __init__(self):
        super().__init__("listener")
        self.sub = self.create_subscription(String, "question", self.respond, 10)

    def respond(self, msg):
        self.get_logger().info(f"Listener: 質問を受信しました -> {msg.data}")

        # 筋トレ部位のリスト
        muscle_groups = [
            "大胸筋", "僧帽筋", "上腕三頭筋", "広背筋", "大臀筋",
            "大腿二頭筋", "下腿三頭筋", "三角筋", "上腕二頭筋", 
            "腹直筋", "大腿四頭筋"
        ]

        # ランダムに部位を選択して応答
        selected_muscle = random.choice(muscle_groups)
        self.get_logger().info(f"Listener: 今日の筋トレ部位は「{selected_muscle}」です！")


def main():
    rclpy.init()
    node = Listener()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
