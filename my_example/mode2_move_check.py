#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
目的:
  set_mode(2) (teach/manual) のときに移動指令が通るかを、
  実機でprintベースで最短確認するためのスクリプト。

注意:
  周辺環境の安全を確認してから実行してください。
  小さな相対移動を指示します。
"""

import time

from xarm.wrapper import XArmAPI


IP = "192.168.1.244"


def main():
    arm = XArmAPI(IP, is_radian=False)
    arm.motion_enable(True)
    arm.set_mode(0)
    arm.set_state(0)
    time.sleep(0.2)

    print("=== mode 2 (teach/manual) に切り替え ===")
    code = arm.set_mode(2)
    print("set_mode(2) ->", code)
    code = arm.set_state(0)
    print("set_state(0) ->", code)
    time.sleep(0.2)

    print("=== mode 2 で相対移動を指示 ===")
    print("期待: モード不一致等で拒否/無効の可能性が高い")
    code = arm.set_position(x=10, y=0, z=0, roll=0, pitch=0, yaw=0, relative=True, wait=True)
    print("set_position(relative) ->", code)

    print("=== 終了: mode 0 に戻す ===")
    code = arm.set_mode(0)
    print("set_mode(0) ->", code)
    code = arm.set_state(0)
    print("set_state(0) ->", code)
    arm.disconnect()


if __name__ == "__main__":
    main()
