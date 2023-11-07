from ws_page.policy_page import PolicyPage
from ws_base.base_ws import BaseElement
from ws_base.app_base_ws import WaterSortApp
from ws_page.adjust_time import AdjustTime
from airtest.cli.parser import cli_setup
from airtest.core.api import *
from ws_page.guidance_page import NewGuidance
from ws_page.four_tube_game_page import FourTubeGamePage
from ws_page.game_home_page import GameHome

ST.SAVE_IMAGE = False
# 暂时关闭截图
# 设置全局的截图精度为90
ST.SNAPSHOT_QUALITY = 90
monday = [333, 1589]
tuesday = [486, 1594]
wednesday = [653, 1594]
thursday = [801, 1603]
friday = [963, 1589]
saturday = [1130, 1567]
sunday = [153, 1747]
three_Day = [788, 1923]
language = "意大利语"
monday_push = "周一推送"
tuesday_push = "周二推送"
Wednesday_push = "周三推送"
thursday_push = "周四推送"
friday_push = "周五推送"
saturday_push = "周六推送"
sunday_push = "周日推送"


class PushLanguage:

    def __init__(self):
        self.PolicyPage = PolicyPage()
        self.BaseElement = BaseElement()
        self.WaterSortApp = WaterSortApp()
        self.AdjustTime = AdjustTime()
        self.NewGuidance = NewGuidance()
        self.FourTubeGamePage = FourTubeGamePage()
        self.GameHome = GameHome()

    def first_open(self):
        # 安装iOS包
        self.PolicyPage.first_start_ws().goto_guidance()
        # 游戏后台
        keyevent("home")
        return self

    def adjust_time_start(self):
        """
        在开始用例之前将日期恢复到前置条件
        :return:
        """
        self.AdjustTime.ios_setting().ios_generic().date_time().adjust_start_time()
        return self

    def get_push(self, date):
        """
        得到push推送
        :param date:
        :return:
        """
        self.AdjustTime.ios_setting().ios_generic().date_time()
        self.BaseElement.sleep_time()
        self.AdjustTime.ios_push_adjust_time(date)
        return self

    def snapshot_push(self, push, push_language):
        self.BaseElement.sleep_time(1)
        self.BaseElement.get_snapshot(push, push_language)
        self.BaseElement.sleep_time()
        return self

    def goback_game(self):
        self.AdjustTime.ios_goback_home()
        return self

    def adjust_three_day(self, three_days):
        """
        调整三天，获得回归弹窗
        :param three_days:
        :return:
        """
        stop_app("ios.water.sort.puzzle.inner")
        self.AdjustTime.ios_setting().ios_generic().date_time()
        self.BaseElement.sleep_time()
        self.AdjustTime.ios_push_adjust_time(three_days)
        return self

    def get_back_snapshot(self, filename, language):
        self.BaseElement.sleep_time()
        self.AdjustTime.goto_game()
        self.BaseElement.sleep_time(5)
        self.BaseElement.get_snapshot(filename, language)
        return self


if __name__ == "__main__":
    if not cli_setup():
        auto_setup(__file__, logdir=True, devices=[
            "ios:///http://127.0.0.1:8300", ])
    # PushLanguage().adjust_time_start()
    # PushLanguage().first_open().get_push(monday).snapshot_push(monday_push, language).goback_game()
    PushLanguage().adjust_three_day(three_Day).goback_game()
