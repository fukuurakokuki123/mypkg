# mypkg
課題２
## Today's training select コマンド

![test](https://github.com/fukuurakokuki123/mypkg/actions/workflows/test.yml/badge.svg)

## 概要
このプログラムでは、ROS 2のパブリッシャとして「筋トレ計画」の情報をworkout_planというトピックに定期的に出力しています。

# workout_publisher.py
筋トレ計画をランダムに生成し、トピック workout_plan に定期的にパブリッシュするノード。

# トピック
## workout_plan

workout_publisher.py ノードが「workout_plan」トピックに情報を送信します。
