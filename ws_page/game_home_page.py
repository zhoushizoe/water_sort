# coding = utf-8
# Author: Zoe
# File: game_home_page.py
# Time: 2023/10/18 5:20 下午
from ws_base.base_ws import BaseElement
from airtest.core.api import *
from airtest.cli.parser import cli_setup


class GameHome(BaseElement):
    game_icon = Template(r"../picture/home_page_picture/game_icon.png", record_pos=(-0.03, -0.238),
                         resolution=(1096, 2560))
    debug_passward = Template(r"../picture/home_page_picture/debug_passward.png", record_pos=(-0.08, -0.422),
                              resolution=(1096, 2560))
    debug_bingo = Template(r"../picture/home_page_picture/debug_bingo.png", record_pos=(0.423, 0.956),
                           resolution=(1096, 2560))
    debug_delete_button = Template(r"../picture/home_page_picture/delete_button.png", record_pos=(0.423, 0.803),
                                   resolution=(1096, 2560))
    debug_fugure_button = Template(r"../picture/home_page_picture/debug_fugure_button.png", record_pos=(-0.429, 0.958),
                                   resolution=(1096, 2560))
    debug_close_button = Template(r"../picture/home_page_picture/debug_close_button.png", record_pos=(-0.015, -0.509),
                                  resolution=(1096, 2560))
    home_level_button = Template(r"../picture/home_page_picture/home_level_button.png", record_pos=(-0.237, 0.403),
                                 resolution=(1096, 2560))

    def get_debug(self):
        """
        在游戏首页开启debug并回到首页
        :return:
        """
        sleep(3)
        self.image_click(self.game_icon, times=7)
        # self.image_click([577, 1013], times=6)
        sleep(1)
        self.image_click([454, 179])
        sleep(1)
        self.image_click(self.debug_passward)
        sleep(1)
        self.image_click([1239, 1630])
        sleep(1)
        self.image_click(self.debug_close_button)
        return self

    def get_level(self, level):
        self.image_click([468, 188])
        sleep(0.5)
        self.image_click([606, 1001])
        sleep(1)
        for i in range(3):
            self.delete_word()
        self.input_word(level)
        sleep(1)
        self.image_click([1290, 2801])
        sleep(1)
        self.image_click(self.debug_close_button)
        sleep(1)
        return self

    def goto_game_page(self):
        sleep(2)
        self.image_click([707, 2195])
        sleep(3)

    def open_debug(self):
        sleep(1)
        self.image_click([35, 26])
        sleep(3)
        return self

    def get_reward_page(self):
        self.image_click([954, 307])
        sleep(3)
        return self

    def reward_goto_home(self):
        self.image_click([916, 619])
        sleep(3)
        return self


if __name__ == "__main__":
    if not cli_setup():
        auto_setup(__file__, logdir=True, devices=[
            "android://127.0.0.1:5037/QV710QR43F?cap_method=MINICAP&&ori_method=MINICAPORI&&touch_method=MAXTOUCH", ])
    GameHome().get_level("7")
