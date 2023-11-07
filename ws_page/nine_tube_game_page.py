# coding = utf-8
# Author: Zoe
# File: nine_tube_game_page.py
# Time: 2023/10/20 2:38 下午
from ws_base.base_ws import BaseElement
from airtest.core.api import *
from airtest.cli.parser import cli_setup

from ws_page.seven_tube_game_page import SevenTubeGamePage


class NineTubeGamePage(BaseElement):
    def nine_first_tube(self):
        return [185, 1087]

    def nine_second_tube(self):
        return [456, 1220]

    def nine_third_tube(self):
        return [728, 1110]

    def nine_fourth_tube(self):
        return [948, 1093]

    def nine_fifth_tube(self):
        return [1214, 994]

    def nine_sixth_tube(self):
        return [329, 1844]

    def nine_seventh_tube(self):
        return [613, 1989]

    def nine_eighth_tube(self):
        return [844, 1839]

    def nine_ninth_tube(self):
        return [1133, 1839]

    def tube_position(self, position):
        self.image_click(position)
        sleep(1.5)
        return self

    def tube_position_first(self):
        self.image_click(self.nine_first_tube())
        sleep(1.5)
        return self

    def tube_position_secend(self):
        self.image_click(self.nine_second_tube())
        sleep(1.5)
        return self

    def tube_position_third(self):
        self.image_click(self.nine_third_tube())
        sleep(1.5)
        return self

    def tube_position_seventh(self):
        self.image_click(self.nine_seventh_tube())
        sleep(1.5)
        return self

    def tube_position_fourth(self):
        self.image_click(self.nine_fourth_tube())
        sleep(1.5)
        return self

    def tube_position_sixth(self):
        self.image_click(self.nine_sixth_tube())
        sleep(1.5)
        return self

    def tube_position_ninth(self):
        self.image_click(self.nine_ninth_tube())
        sleep(1.5)
        return self

    def twentieth_level(self):
        self.tube_position_sixth().tube_position_secend().\
            tube_position_first().tube_position_third().\
            tube_position_sixth().tube_position_third()
        return SevenTubeGamePage
