#!/bin/bash

# ディレクトリを設定
dir=~
[ "$1" != "" ] && dir="$1"

# ROS2 ワークスペースに移動
cd $dir/ros2_ws

# ビルド
colcon build
source $dir/.bashrc
source /opt/ros/humble/setup.bash

# ローンチファイルを実行し、ログを確認
timeout 30 ros2 launch mypkg talk_listen.launch.py | tee /tmp/mypkg.log

# ログファイルの最後の20行を表示
tail -n 20 /tmp/mypkg.log

# ログ内に「Listen: 10」があるか確認
if grep -q 'Listen: 10' /tmp/mypkg.log; then
  echo "Listen: 10 がログにあります。成功です。"
else
  echo "Listen: 10 がログに見つかりません。エラーです。"
fi
