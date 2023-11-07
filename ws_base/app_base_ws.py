# coding = utf-8
# Author: Zoe
# File: app_base_ws.py
# Time: 2023/10/16 2:42 下午
from airtest.core.api import *
from airtest.cli.parser import cli_setup


class WaterSortApp:
    """
    一些关于倒水的前置操作
    """

    # 安装游戏
    def install_app(self):
        pass

    def poco_set(self):
        # UnityPoco()
        return self

    # 首次开启游戏
    def first_start_app(self, package):
        start_app(package)
        sleep(5)
        # self.poco_set()

        # return PolicyPage()

    # 非首次开启游戏
    def start_app(self, package):
        start_app(package)
        sleep(5)
        self.poco_set()
        # return MainPage()

    # 关闭游戏
    def stop_app(self, package):
        stop_app(package)
        sleep(2)
        return self

        pass

    # 清除游戏数据
    def clear_app(self, package):
        clear_app(package)
        return self

    def uninstall_ios(self, package):
        uninstall(package)
        sleep(4)
        return self

    def install_ios(self, package):
        install(package)
        sleep(10)
        return self

    def goback_home(self):
        keyevent("HOME")
        return self
