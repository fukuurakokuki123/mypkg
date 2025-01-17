# mypkg
課題２
## Today's training select コマンド

![test](https://github.com/fukuurakokuki123/mypkg/actions/workflows/test.yml/badge.svg)

## 概要
このパッケージは、ROS 2のパブリッシャとして「筋トレ計画」の情報をworkout_planというトピックに定期的に出力しています。

## workout_publisher
筋トレ計画をランダムに生成し、トピック workout_plan に定期的にパブリッシュするノード。

## トピック
### workout_plan

workout_publisher ノードが「workout_plan」トピックに情報を送信します。

## コマンドと実行例
#### 例
#### 端末1
     $ ros2 run mypkg workout_publisher
#### 端末2
     $ ros2 topic echo workout_plan
#### 実行結果(端末2(受信側)にて表示)
     data: '日付: 2025-01-03 | 筋トレ部位: 腹直筋 | トレーニング: クランチ: 3セット × 20回'
     ---
     data: '日付: 2025-01-04 | 筋トレ部位: 下腿三頭筋 | トレーニング: カーフレイズ: 3セット × 20回'
     ---
     data: '日付: 2025-01-05 | 筋トレ部位: 広背筋 | トレーニング: ラットプルダウン: 3セット × 10回'
     ---
     data: '日付: 2025-01-06 | 筋トレ部位: 僧帽筋 | トレーニング: シュラッグ: 3セット × 15回'
     ---
     data: '日付: 2025-01-07 | 筋トレ部位: 三角筋 | トレーニング: ショルダープレス: 3セット × 10回'
     ---
     data: '日付: 2025-01-08 | 筋トレ部位: 大胸筋 | トレーニング: ベンチプレス: 3セット × 10回'
     ---
     data: '日付: 2025-01-09 | 筋トレ部位: 三角筋 | トレーニング: ショルダープレス: 3セット × 10回'
     ---
     data: '日付: 2025-01-10 | 筋トレ部位: 腹直筋 | トレーニング: クランチ: 3セット × 20回'
     ---
     data: '日付: 2025-01-11 | 筋トレ部位: 僧帽筋 | トレーニング: シュラッグ: 3セット × 15回'
     ---
     data: '日付: 2025-01-12 | 筋トレ部位: 広背筋 | トレーニング: ラットプルダウン: 3セット × 10回'
## 必要なソフトウェア
- python

- ROS 2 humble

## テスト環境
- ubuntu-22.04
## 著作権・ライセンス
- このソフトウェアパッケージは、3条項BSDライセンスの下、再頒布および使用が許可されます。
- このパッケージのコードの一部は、下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを、本人の許可を得て自身の著作としたものです。
  - https://github.com/ryuichiueda/slides_marp/tree/master/robosys2024 
##### © 2024 Kouki Fukuura
