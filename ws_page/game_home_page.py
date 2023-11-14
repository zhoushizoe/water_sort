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
    input_fields = Template(r"../picture/home_page_picture/input_fields.png", threshold=0.8,
                            record_pos=(-0.178, -0.965), resolution=(1440, 3088))
    debug_level = Template(r"../picture/home_page_picture/debug_level.png", threshold=0.9, target_pos=6,
                           record_pos=(-0.193, -0.378), resolution=(1440, 3088))
    dubug_yes = Template(r"../picture/home_page_picture/dubug_yes.png", record_pos=(0.375, 0.827),
                         resolution=(1440, 3088))

    goto_game_button = Template(r"../picture/home_page_picture/goto_game_button.png", threshold=0.5,
                                record_pos=(-0.249, 0.429), resolution=(1440, 3088))
    # 首页展开debug按钮
    expand_debug_button = Template(r"../picture/home_page_picture/expand_debug_button.png", target_pos=5,
                                   record_pos=(-0.468, -0.975),
                                   resolution=(1440, 3088))

    def get_debug(self):
        """
        在游戏首页开启debug并回到首页
        :return:
        """
        self.sleep_time(4)
        # if exists(self.game_icon):
        #     self.image_click(self.game_icon, times=7)
        # else:
        self.image_click([722, 1253], times=7)

        self.sleep_time(1)
        self.image_click_plus(self.input_fields, [462, 167])
        self.image_click_plus(self.debug_passward, [619, 1002])
        self.image_click_plus(self.debug_close_button, [702, 1312])
        self.image_click_plus(self.debug_close_button, [702, 850])
        return self

    def get_level(self, level):
        """
        开启debug后，进入debug，得到想要的关卡
        :param level:希望的关卡
        :return:
        """
        self.image_click_plus(self.input_fields, [462, 167])
        self.sleep_time(1)
        self.image_click_plus(self.debug_level, [619, 997])
        self.sleep_time(1)
        for i in range(3):
            self.delete_word()
        self.input_word(level)
        self.sleep_time(1)
        self.image_click_plus(self.dubug_yes, [1290, 2801])
        self.sleep_time(1)
        self.image_click(self.debug_close_button)
        self.sleep_time()
        return self

    def goto_game_page(self):
        """
        从首页进入游戏页面
        :return:
        """
        self.sleep_time()
        self.image_click_plus(self.goto_game_button, [698, 2202])
        self.sleep_time(3)
        return self

    def expand_debug(self):
        """
        在首页展开debug
        :return:
        """
        self.sleep_time()
        self.image_click_plus(self.expand_debug_button, [44, 127])
        return self

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

    def get_unlock_level(self, level):
        """
        在首页展开debug后，得到想要的关卡，然后进入游戏
        :param level:
        :return:
        """
        self.expand_debug().get_level(level).goto_game_page()
        self.sleep_time()
        return self


if __name__ == "__main__":
    if not cli_setup():
        auto_setup(__file__, logdir=True, devices=[
            "android://127.0.0.1:5037/R3CW10C3D9N?cap_method=MINICAP&touch_method=MAXTOUCH&", ])
    GameHome().expand_debug()
