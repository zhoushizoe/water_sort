# coding = utf-8
# Author: Zoe
# File: base_ws.py
# Time: 2023/10/16 11:14 上午
from airtest.cli.parser import cli_setup
from airtest.core.api import *
from poco.drivers.ios import iosPoco


class BaseElement:
    # poco = UnityPoco()

    # 使用图像识别点击

    def image_click(self, image, times=1):
        touch(image, times)
        return self

        # 使用图像识别拖动

    def image_swipe(self, place, to):
        swipe(place, to)
        return self

    # 截图
    # def get_snapshot(self, filename):
    #     self.file_path()
    #     snapshot(filename=self.snop_name + filename + ".png")
    # 停止游戏
    def stop_app(self, package):
        stop_app(package)
        sleep(2)
        return self

    def start_app(self, package):
        start_app(package)
        sleep(5)
        return self

    # 删除输入的文字
    def delete_word(self):
        keyevent("KEYCODE_DEL")
        sleep(0.5)
        return self

    # 输入所需要的文字
    def input_word(self, word):
        text(word)
        sleep(0.5)
        return self

    def get_snapshot(self, filename, language):
        snapshot(filename=language + filename + ".png")
        return self

    def sleep_time(self, second=2):
        sleep(second)
        return self

    # 进行图片点击操作时同时使用坐标点击
    def image_click_plus(self, image, coordinate):
        if exists(image):
            self.image_click(image)
        else:
            self.image_click(coordinate)
        self.sleep_time(4)

    def ios_open_app(self, package_name):
        """
        进入应用
        :param package_name: 包名
        :return:
        """
        # start_app(package_name)
        # poco(package_name).click()
        # return self


class IosBaseElement:
    """
    封装关于iOS特殊的一些操作
    """

    def ios_delete_text(self):
        # ios中删除输入的字符
        text("\b", enter=False)
        return self

    def ios_inter_word(self, enter=False):
        """
          iOS的text()接口默认会在给定的输入字符后面加一个换行符 \n 。
          如果不想要输入之后出现换行的效果，可以把enter = False传到text()接口里面
        :return: 
        """""

        text("\b", enter)
        return self

    def ios_test(self):
        a = 100

    def ios_open_app(self):
        # print(a)
        poco("Water Sort").click()
        return self


if __name__ == "__main__":
    if not cli_setup():
        auto_setup(__file__, logdir=True, devices=[
            "ios:///http://127.0.0.1:8300", ])
    poco = iosPoco()
    IosBaseElement().ios_open_app()

