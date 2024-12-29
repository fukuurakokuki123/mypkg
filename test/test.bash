#!/bin/bash

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws

colcon build
source $dir/.bashrc
source /opt/ros/humble/setup.bash

timeout 10 ros2 run mypkg talker > /tmp/mypkg_talker.log

tail -n 20 /tmp/mypkg_talker.log

if grep -q "今日の筋トレ部位" /tmp/mypkg_talker.log; then
  echo "Talkerノードが有用なデータを発信しています。成功です。"
else
  echo "Talkerノードが有用なデータを発信していません。エラーです。"
fi
