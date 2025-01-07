# SPDX-FileCopyrightText: 2024 Kouki Fukuura
# SPDX-License-Identifier: BSD-3-Clause

import os
import sys
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import random
from datetime import datetime, timedelta

class WorkoutPublisher(Node):
    def __init__(self):
        super().__init__("workout_publisher")
        
        sys.stdout = open(os.devnull, 'w')
        sys.stderr = open(os.devnull, 'w')

        self.publisher_ = self.create_publisher(String, "workout_plan", 10)

        self.current_date = datetime(2024, 12, 30)

        self.timer = self.create_timer(2.0, self.publish_workout_plan)

    def publish_workout_plan(self):

        workouts = {
            "大胸筋": "ベンチプレス: 3セット × 10回",
            "僧帽筋": "シュラッグ: 3セット × 15回",
            "上腕三頭筋": "トライセプスエクステンション: 3セット × 12回",
            "広背筋": "ラットプルダウン: 3セット × 10回",
            "大臀筋": "ヒップスラスト: 4セット × 12回",
            "大腿二頭筋": "レッグカール: 3セット × 15回",
            "下腿三頭筋": "カーフレイズ: 3セット × 20回",
            "三角筋": "ショルダープレス: 3セット × 10回",
            "上腕二頭筋": "バーベルカール: 3セット × 12回",
            "腹直筋": "クランチ: 3セット × 20回",
            "大腿四頭筋": "スクワット: 4セット × 10回",
        }

        muscle, exercise = random.choice(list(workouts.items()))

        date_str = self.current_date.strftime("%Y-%m-%d")

        workout_message = String()
        workout_message.data = f"日付: {date_str} | 筋トレ部位: {muscle} | トレーニング: {exercise}"

        self.publisher_.publish(workout_message)

        self.current_date += timedelta(days=1)

def main():
    rclpy.init()
    node = WorkoutPublisher()
    rclpy.spin(node)
