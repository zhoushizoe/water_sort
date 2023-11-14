# coding = utf-8
# Author: Zoe
# File: guidance_page.py
# Time: 2023/10/16 3:13 下午
from ws_base.base_ws import BaseElement
from airtest.core.api import *
from airtest.cli.parser import cli_setup
from ws_base.app_base_ws import WaterSortApp
from ws_page.four_tube_game_page import FourTubeGamePage
from ws_page.game_page import GamePage


class NewGuidance(BaseElement):
    guidance_tube = Template(r"../picture/guidance_page_picture/first_tube.png",
                             record_pos=(-0.192, -0.05),
                             resolution=(1440, 3088))

    def first_guidance_step1(self):
        """
        点击第一个管
        :return:
        """
        self.image_click_plus(self.guidance_tube, [408, 1445])
        self.sleep_time(2)
        return self

    def first_guidance_step2(self):
        """
        点击第二个管
        :return:
        游戏页面的胜利页面
        """
        self.image_click([1027, 1499])
        # self.image_click_plus(self.guidance_tube, [1027, 1499])
        self.sleep_time(6)
        return GamePage

    def second_guidance_step1(self):
        """
        第二关点击第一个管
        :return:
        """
        self.image_click([312, 1478])
        self.sleep_time()
        return self

    def second_guidance_step2(self):
        """
        第二关点击第二个管
        :return:
        """
        self.image_click([725, 1446])
        self.sleep_time()
        return self

    def second_guidance_step3(self):
        """
        第二关点击第三个管
        :return:
        """
        self.image_click([1097, 1510])
        self.sleep_time()
        return self

    def completed_level2(self):
        """
        第二关完成
        :return:
        """
        self.sleep_time()
        self.second_guidance_step1().second_guidance_step2().second_guidance_step1().second_guidance_step3()
        self.sleep_time()
        return GamePage


if __name__ == "__main__":
    if not cli_setup():
        auto_setup(__file__, logdir=True, devices=[
            "android://127.0.0.1:5037/R3CW10C3D9N?cap_method=MINICAP&touch_method=MAXTOUCH&", ])
    NewGuidance().completed_level2()

    # NewGuidance().first_guidance_step2()
