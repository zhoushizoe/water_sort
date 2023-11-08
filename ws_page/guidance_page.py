# coding = utf-8
# Author: Zoe
# File: guidance_page.py
# Time: 2023/10/16 3:13 下午
from ws_base.base_ws import BaseElement
from airtest.core.api import *
from airtest.cli.parser import cli_setup
from ws_base.app_base_ws import WaterSortApp
from ws_page.four_tube_game_page import FourTubeGamePage


class NewGuidance(BaseElement):

    def first_guidance_step1(self):
        """
        点击第一个管
        :return:
        """
        self.image_click([371, 1478])
        return self

    def first_guidance_step2(self):
        """
        点击第二个管
        :return:
        游戏页面的胜利页面
        """
        self.image_click([1024, 1524])
        sleep(6)
        return self

    def second_guidance_step1(self):
        """
        点击第一个管
        :return:
        """
        self.image_click([312, 1478])
        sleep(1)
        return self

    def second_guidance_step2(self):
        """
        点击第二个管
        :return:
        """
        self.image_click([725, 1446])
        sleep(1)
        return self

    def guidance_victory(self):
        """
        引导胜利页面点击
        :return:
        """
        sleep(5)
        self.image_click([635, 2152])
        sleep(2)
        return self

    def second_guidance_step3(self):
        self.image_click([1097, 1510])
        sleep(1)
        return self


if __name__ == "__main__":
    if not cli_setup():
        auto_setup(__file__, logdir=True, devices=[
            "android://127.0.0.1:5037/QV710QR43F?cap_method=MINICAP&&ori_method=MINICAPORI&&touch_method=MAXTOUCH", ])
    NewGuidance().second_guidance_step1().second_guidance_step2()
    sleep(2)
    NewGuidance().second_guidance_step1().second_guidance_step3()
