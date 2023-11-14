# coding = utf-8
# Author: Zoe
# File: app_base_ws.py
# Time: 2023/10/16 2:42 下午
from airtest.core.api import *
from airtest.cli.parser import cli_setup
from poco.drivers.ios import iosPoco


class WaterSortApp:
    """
    一些关于倒水的前置操作
    """

    def install_app(self, package_path):
        """
        安装应用（安卓iOS通用）
        :param package_path:
        :return:
        """
        install(package_path)
        return self

    # 首次开启游戏
    def first_start_app(self, package):
        start_app(package)
        sleep(5)
        return self

    # 非首次开启游戏
    def start_app(self, package):
        start_app(package)
        sleep(5)
        # return MainPage()

    # 关闭游戏
    def stop_app(self, package):
        stop_app(package)
        sleep(2)
        return self

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

    def ios_open_app(self, app_name):
        """
        airtest中的[start_app]不支持iOS17
        游戏的名称永远是英文的，所以使用poco的方式打开应用
        :param app_name:app在首页显示的应用名字
        :return:
        """

        poco(app_name).click()
        return self
