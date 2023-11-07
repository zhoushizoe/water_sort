# coding = utf-8
# Author: Zoe
# File: four_tube_game_page.py
# Time: 2023/10/16 5:21 下午
from ws_base.base_ws import BaseElement
from airtest.core.api import *
from airtest.cli.parser import cli_setup
from ws_base.app_base_ws import WaterSortApp
from ws_page.game_home_page import GameHome


class FourTubeGamePage(BaseElement):
    first_tube = [213, 1532]
    second_tube = [555, 1520]
    third_tube = [907, 1445]
    fourth_tube = [1202, 1497]
    next_level_button = Template(r"../picture/game_page_picture/victory_next_button.png", target_pos=6,
                                 record_pos=(-0.247, 0.397),
                                 resolution=(1096, 2560))
    setting_button = Template(r"../picture/game_page_picture/setting_button.png", record_pos=(-0.406, -1.097),
                              resolution=(1096, 2560))

    withdraw_tool_button = Template(r"../picture/game_page_picture/withdraw_tool_button.png", record_pos=(0.002, 0.833),
                                    resolution=(1096, 2560))
    goto_home_button = Template(r"../picture/game_page_picture/goto_home_button.png", record_pos=(-0.284, -1.094), resolution=(1096, 2560))

    def game_victory_page(self):
        """
        胜利页面的next按钮
        :return:
        """
        self.image_click(self.next_level_button)
        return self

    def tube_position(self, position):
        self.image_click(position)
        sleep(1)
        return self

    def goto_game_home(self):
        self.image_click(self.goto_home_button)
        sleep(3)
        return GameHome

    def goto_home_site(self):
        self.image_click([1097, 1510])
        sleep(3)
        return GameHome

    def goto_setting_page(self):
        self.image_click(self.setting_button)
        sleep(1)
        return self

    def replay_tool(self):
        pass

    def withdraw_tool(self):
        self.image_click(self.withdraw_tool_button)
        sleep(6)

    def add_tube_tool(self):
        pass


if __name__ == "__main__":
    if not cli_setup():
        auto_setup(__file__, logdir=True, devices=[
            "android://127.0.0.1:5037/QV710QR43F?cap_method=MINICAP&&ori_method=MINICAPORI&&touch_method=MAXTOUCH", ])
