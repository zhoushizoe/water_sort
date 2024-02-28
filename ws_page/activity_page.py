from ws_base.base_ws import BaseElement
from ws_base.base_ws import IosBaseElement
from airtest.core.api import *
from ws_page.game_page import GamePage
from airtest.cli.parser import cli_setup


class ActivityPage(BaseElement, IosBaseElement):
    level_1 = [278, 1512]
    level_2 = [735, 1507]
    level_3 = [1201, 1503]
    level_4 = [306, 2068]
    level_5 = [706, 2073]
    level_6 = [1154, 2068]
    level_7 = [259, 2643]
    level_8 = [758, 2648]
    level_9 = [1182, 2643]
    level_10 = [268, 2474]
    level_11 = [772, 2474]
    level_12 = [1178, 2469]
    pad_level_1 = [225, 1323]
    continue_button = Template(r"../picture/activity_page_picture/continue_button.png", record_pos=(-0.001, 0.582),
                               resolution=(1440, 3088))
    # 活动页面的hard按钮
    hard_button = Template(r"../picture/activity_page_picture/hard_button.png", record_pos=(0.01, -0.405),
                           resolution=(1440, 3088))
    # 活动页面的normal按钮
    normal_button = Template(r"../picture/activity_page_picture/normal_button.png", record_pos=(-0.322, -0.415),
                             resolution=(1440, 3088))

    def __init__(self):
        self.GamePage = GamePage()

    def unlock_level(self, level):
        """
        点击活动模式关卡
        :return:
        """
        self.image_click(level)
        return self

    def activity_over_continue(self):
        """
        活动模式胜利之后的continue
        :return:
        """
        self.image_click_plus(self.continue_button, [711, 2393])
        return self

    def activity_victory(self, level):
        """
        活动模式从开启关卡到关卡胜利全流程
        :param level:
        :return:
        """
        self.unlock_level(level).unlock_level(level)
        self.GamePage.debug_win().debug_doone().debug_doone().ad_close()
        self.activity_over_continue()
        self.sleep_time()
        return self

    def pad_fail_back_level(self):
        """
        挑战模式游戏失败之后点击返回首页
        :return:
        """
        self.image_click([814, 1500])
        return self

    def goto_hard_page(self):
        """
        点击进入hard页面
        :return:
        """
        self.image_click_plus(self.hard_button, [735, 966])
        return self

    def goto_normal_page(self):
        """
        点击进入normal页面
        :return:
        """
        self.image_click_plus(self.normal_button, [235, 956])
        return self

    def challenge_swipe(self):
        self.image_swipe([956, 2780], [933, 1993])
        return self

    def pad_activity_victory_continue(self):
        """
        点击活动模式的胜利继续按钮
        :return:
        """
        self.sleep_time()
        self.image_click([841, 1741]).image_click([841, 1741])
        return self

    def pad_goto_hard(self):
        """
        在pad中点击困难模式
        :return:
        """
        self.image_click([624, 714])
        return self

