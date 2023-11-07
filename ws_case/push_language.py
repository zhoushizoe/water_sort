# coding = utf-8
# Author: Zoe
# File: push_language.py
# Time: 2023/11/3 16:13


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
monday = [358, 2034]
tuesday = [537, 2025]
wednesday = [721, 2034]
thursday = [895, 2039]
friday = [1074, 2029]
saturday = [1253, 2025]
sunday = [183, 2167]
language = "意大利语"
monday_push = "周一推送"
tuesday_push = "周二推送"
Wednesday_push = "周三推送"
thursday_push = "周四推送"
firday_push = "周五推送"
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

    def first_day_android(self):
        # 第一天打开游戏
        self.PolicyPage.first_start_android().goto_guidance()
        self.WaterSortApp.goback_home()
        return self

    def get_push(self, date):
        self.AdjustTime.get_setting_button().get_language()
        self.BaseElement.sleep_time()
        self.AdjustTime.adjust_date_mon(date).check_push()
        return self

    def snapshot_push(self, push, push_language):
        self.BaseElement.sleep_time()
        self.BaseElement.image_click([1318, 881])
        self.BaseElement.sleep_time(1)
        # self.BaseElement.image_click([1322, 1143])
        self.BaseElement.sleep_time(1)
        self.BaseElement.get_snapshot(push, push_language)
        self.BaseElement.sleep_time()
        return self

    def goback_game(self):
        self.AdjustTime.push_back_setting()
        self.PolicyPage.start_android()
        self.WaterSortApp.goback_home()
        return self

    def back_page(self, language1):
        back = "回归弹窗"
        self.PolicyPage.first_start_android().goto_guidance()
        self.NewGuidance.first_guidance_step1().first_guidance_step2().guidance_victory()
        self.NewGuidance.second_guidance_step1().second_guidance_step2().second_guidance_step3(). \
            second_guidance_step1().guidance_victory()
        stop_app("water.sort.puzzle.android.inner")
        self.get_push([523, 2286])
        self.AdjustTime.push_back_setting()
        self.PolicyPage.start_android()
        self.BaseElement.sleep_time(10)
        self.BaseElement.get_snapshot(back, language1)
        self.BaseElement.sleep_time()
        self.BaseElement.image_click([766, 2153])
        return self

    def get_congratulation(self, language1):
        congratulation_page = "通关弹窗"
        home_congratulation = "恭喜"
        self.PolicyPage.first_start_android().goto_guidance()
        self.NewGuidance.first_guidance_step1().first_guidance_step2().guidance_victory()
        self.NewGuidance.second_guidance_step1().second_guidance_step2().second_guidance_step3(). \
            second_guidance_step1().guidance_victory()
        self.FourTubeGamePage.goto_game_home()
        self.BaseElement.image_click([766, 2153])
        self.BaseElement.sleep_time()
        self.GameHome.get_debug().get_level("2000")
        sleep(2)
        self.GameHome.goto_game_page()
        sleep(2)
        self.BaseElement.image_click([1010, 179])
        self.BaseElement.sleep_time(35)
        self.BaseElement.image_click([1125, 179], times=4)
        self.BaseElement.sleep_time(10)
        self.BaseElement.get_snapshot(congratulation_page, language1)
        self.BaseElement.image_click([743, 2250])
        self.BaseElement.sleep_time()
        self.BaseElement.get_snapshot(home_congratulation, language1)

        return self


if __name__ == "__main__":
    if not cli_setup():
        auto_setup(__file__, logdir=True, devices=[
            "android://127.0.0.1:5037/R3CW10C3D9N?cap_method=ADBCAP&touch_method=MAXTOUCH&", ])

    # PushLanguage().first_day_android().get_push(monday).snapshot_push(monday_push, language).goback_game()
    # PushLanguage().first_day_android().get_push(tuesday).snapshot_push(tuesday_push, language).goback_game()
    # PushLanguage().first_day_android().get_push(wednesday).snapshot_push(Wednesday_push, language).goback_game()
    # PushLanguage().first_day_android().get_push(thursday).snapshot_push(thursday_push, language).goback_game()
    # PushLanguage().first_day_android().get_push(friday).snapshot_push(firday_push, language).goback_game()
    # PushLanguage().first_day_android().get_push(saturday).snapshot_push(saturday_push, language).goback_game()
    # PushLanguage().first_day_android().get_push(sunday).snapshot_push(sunday_push, language).goback_game()
    PushLanguage().back_page(language)
    # PushLanguage().get_congratulation(language)
