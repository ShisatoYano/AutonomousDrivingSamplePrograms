"""
Vehicle chassis drawing program

Author: Shisato Yano
"""

import numpy as np
import matplotlib.pyplot as plt
import sys
import os

# 他のディレクトリにあるモジュールを読み込むためのパス設定
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../common")
from transformation import rotate_translate_2d

# グラフの出力有無を切り替えるフラグ
show_plot = True


class Chassis:
    """
    車両のシャーシを描画するクラス
    """

    def __init__(self, axes, front_length_m, rear_length_m, color):
        """
        コンストラクタ
        axes: 描画オブジェクト
        front_length_m: 車両位置から前方への長さ[m]
        rear_length_m: 車両位置から後方への長さ[m]
        color: ラインの色
        """

        # パラメータのセット
        self.front_length = front_length_m
        self.rear_length = rear_length_m
        self.color = color
        
        # シャーシの形を形成するための点群
        self.points = np.array([
            [front_length_m, -rear_length_m],
            [0.0, 0.0]
        ])

        # 描画オブジェクトの初期化
        self.plot, = axes.plot(self.points[0, :], self.points[1, :], lw=1, color=self.color)
    
    def draw(self, x_m, y_m, yaw_angle_deg):
        """
        シャーシの形を描画する関数
        指定した分だけ回転 + 並進移動させて描画する
        x_m: X軸方向の並進移動量
        y_m: Y軸方向の並進移動量
        yaw_angle_deg: 車両の方位角度[deg]
        """
        
        # 車両の方位角度分だけ回転
        # 車両の移動量分だけ並進移動
        transformed_points = rotate_translate_2d(self.points, x_m, y_m, np.deg2rad(yaw_angle_deg))
        
        # 描画
        self.plot.set_data(transformed_points[0, :], transformed_points[1, :])


def main():
    """
    このファイルを単体で実行したときの処理を実装したメイン関数
    車両のシャーシの絵を描画する
    """

    print(__file__ + "start!!")

    # 描画の設定
    ax = plt.subplot(1, 1, 1)
    ax.set_xlabel("X[m]")
    ax.set_ylabel("Y[m]")
    ax.set_xlim([-10, 10])
    ax.set_ylim([-10, 10])
    ax.set_aspect("equal")
    ax.grid(True)

    # 描画クラスのインスタンス生成
    chassis = Chassis(ax, 6.35, 0.0, 'k')

    # 描画
    chassis.draw(0.0, 0.0, 0.0)

    # ユニットテスト時はこのフラグをFlaseにする
    # グラフが表示されるとテストが進まなくなる
    if show_plot: plt.show()

    return True


# メイン関数の実行
if __name__ == "__main__":
    main()
