import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import random

MUSCLE_GROUPS = [
    "大胸筋", "僧帽筋", "上腕三頭筋", "広背筋", "大臀筋",
    "大腿二頭筋", "下腿三頭筋", "三角筋", "上腕二頭筋", "腹直筋", "大腿四頭筋"
]

class Talker(Node):
    def __init__(self):
        super().__init__('talker')
        self.publisher = self.create_publisher(String, 'workout', 10)
        self.timer = self.create_timer(0.5, self.publish_workout)

    def publish_workout(self):
        # ランダムに筋トレ部位を選択
        workout = random.choice(MUSCLE_GROUPS)
        msg = String()
        msg.data = workout
        self.publisher.publish(msg)
        self.get_logger().info(f'Published: {workout}')

def main():
    rclpy.init()
    node = Talker()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()
