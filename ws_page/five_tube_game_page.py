# coding = utf-8
# Author: Zoe
# File: five_tube_game_page.py
# Time: 2023/10/18 2:30 下午
from ws_base.base_ws import BaseElement
from airtest.core.api import *
from airtest.cli.parser import cli_setup


class FiveTubeGamePage(BaseElement):
    first_tube = [83, 1211]
    second_tube = [326, 1123]
    third_tube = [541, 1312]
    fourth_tube = [801, 1251]
    fifth_tube = [973, 1110]
    next_level_button = Template(r"../picture/game_page_picture/victory_next_button.png", target_pos=6,
                                 record_pos=(-0.247, 0.397),
                                 resolution=(1096, 2560))

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
