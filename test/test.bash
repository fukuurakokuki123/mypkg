#!/bin/bash
# SPDX-FileCopyrightText: 2024 Kouki Fukuura
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
source /opt/ros/humble/setup.bash

timeout 10 ros2 run mypkg workout_publisher &

sleep 3

topic_name="workout_plan"
log_file="/tmp/workout_plan.log"
timeout 7 ros2 topic echo /$topic_name > $log_file

if grep -q "筋トレ部位" $log_file && grep -q "トレーニング" $log_file; then
  echo "トピック $topic_name に正しいデータが発信されています。成功です。"
else
  echo "トピック $topic_name に正しいデータが発信されていません。エラーです。"
fi

rm -f $log_file
