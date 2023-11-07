# coding = utf-8
# Author: Zoe
# File: base_ws.py
# Time: 2023/10/16 11:14 上午
from airtest.core.api import *


class BaseElement:
    # poco = UnityPoco()

    # 使用图像识别点击

    def image_click(self, image, times=1):
        touch(image, times)

        # 使用图像识别拖动

    def image_swipe(self, place, to):
        swipe(place, to)

    # 截图
    # def get_snapshot(self, filename):
    #     self.file_path()
    #     snapshot(filename=self.snop_name + filename + ".png")
    # 停止游戏
    def stop_app(self, package):
        stop_app(package)
        sleep(2)

    def start_app(self, package):
        start_app(package)
        sleep(5)

    # 删除输入的文字
    def delete_word(self):
        keyevent("KEYCODE_DEL")
        sleep(0.5)

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
