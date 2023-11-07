# coding = utf-8
# Author: Zoe
# File: seven_tube_game_page.py
# Time: 2023/10/18 2:35 下午
from ws_base.base_ws import BaseElement
from airtest.core.api import *
from airtest.cli.parser import cli_setup

from ws_page.game_home_page import GameHome


class SevenTubeGamePage(BaseElement):
    first_tube = [185, 938]
    second_tube = [436, 894]
    third_tube = [687, 929]
    fourth_tube = [933, 837]
    fifth_tube = [308, 1493]
    sixth_tube = [541, 1559]
    seventh_tube = [766, 1445]
    next_level_button = Template(r"../picture/game_page_picture/victory_next_button.png", target_pos=6,
                                 record_pos=(-0.247, 0.397),
                                 resolution=(1096, 2560))

    setting_button = Template(r"../picture/game_page_picture/setting_button.png", record_pos=(-0.406, -1.097),
                              resolution=(1096, 2560))

    withdraw_tool_button = Template(r"../picture/game_page_picture/withdraw_tool_button.png", record_pos=(0.002, 0.833),
                                    resolution=(1096, 2560))
    goto_home_button = Template(r"../picture/game_page_picture/goto_home_button.png", record_pos=(-0.284, -1.094),
                                resolution=(1096, 2560))
    setting_close_button = Template(r"../picture/game_page_picture/setting_close_button.png",
                                    record_pos=(0.348, -0.611), resolution=(1096, 2560))
    goto_setting_button = Template(r"../picture/game_page_picture/goto_setting_button.png", record_pos=(-0.408, -1.078),
                                   resolution=(1096, 2560))
    close_score_button = Template(r"../picture/game_page_picture/close_score_button.png", record_pos=(0.339, -0.444),
                                  resolution=(1440, 3088))

    def close_debug(self):
        self.image_click([44, 44])
        sleep(1)
        return self

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
        sleep(1)
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
        return self

    def setting_collection(self):
        self.image_click([815, 1365])
        sleep(2)
        return self

    def setting_close(self):
        sleep(2)
        self.image_click(self.setting_close_button)
        sleep(2)
        return self

    def setting_close_site(self):
        self.image_click([926, 604])
        sleep(3)
        return self

    def setting_language(self):
        self.image_click([845, 1506])
        sleep(2)
        return self

    def setting_contact_us(self):
        self.image_click([837, 1638])
        sleep(2)
        return self

    def collect_goto_setting(self):
        self.image_click(self.goto_setting_button)
        sleep(2)
        return self

    def debug_win(self):
        self.image_click([1000, 150])
        sleep(20)
        return self

    def close_score_guidance(self):
        self.image_click(self.close_score_button)
        sleep(5)
        return self

    def twenty_fourth_level(self):
        self.tube_position(self.second_tube).tube_position(self.third_tube).\
            tube_position(self.fourth_tube).tube_position(self.third_tube).\
            tube_position(self.first_tube).tube_position(self.fourth_tube)
        return self


if __name__ == "__main__":
    if not cli_setup():
        auto_setup(__file__, logdir=True, devices=[
            "android://127.0.0.1:5037/QV710QR43F?cap_method=MINICAP&&ori_method=MINICAPORI&&touch_method=MAXTOUCH", ])
