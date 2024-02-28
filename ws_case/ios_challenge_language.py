import pytest
from airtest.cli.parser import cli_setup
from airtest.core.api import *
from ws_base.base_poco import BasePoco
from ws_base.base_ws import BaseElement
from ws_page.policy_page import PolicyPage
from ws_base.base_point import GetPointWater
from ws_base.base_point_user import GetPointUser
from ws_page.guidance_page import NewGuidance
from ws_page.game_page import GamePage
from ws_page.game_home_page import GameHome
from ws_page.colloct_page import CollectPage
from ws_base.base_ws import IosBaseElement
from ws_page.adjust_time_android import AdjustTime
from ws_page.activity_page import ActivityPage

ST.SAVE_IMAGE = False
# 暂时关闭截图
# 设置全局的截图精度为90
ST.SNAPSHOT_QUALITY = 90


class TestWaterLanguage(BaseElement):
    auto_setup(__file__, logdir=True,
               devices=["ios:///http://127.0.0.1:8300", ])
    language = "ipad_air4葡萄牙语"
    name = rf"{language}/{language}"
    water_sort_ios_package = 'ios.water.sort.puzzle.inner'

    def get_class(self):
        self.PolicyPage = PolicyPage()
        self.NewGuidance = NewGuidance()
        self.GamePage = GamePage()
        self.GameHome = GameHome()
        self.CollectPage = CollectPage()
        self.IosBaseElement = IosBaseElement()
        self.ActivityPage = ActivityPage()
        # self.AdjustTime = AdjustTime()

    def get_class2(self):
        self.poco = BasePoco()

    def file_path(self, folder_name):
        path = f"/Users/amber/PycharmProjects/Water Sort/ws_case/log/{folder_name}"
        if os.path.exists(path):
            return self
        else:
            os.makedirs(path)
        return self

    # @pytest.mark.flaky(reruns=3)
    def test1_lock_challenge(self):
        """
        未解锁的首页challenge
        :return:
        """
        page1 = "未解锁的首页challenge"
        self.file_path(self.name)
        self.get_class()
        self.PolicyPage.first_start_ios().goto_guidance()
        self.NewGuidance.pad_first_guidance_step1().pad_first_guidance_step2()
        self.GamePage.game_victory()
        self.NewGuidance.pad_completed_level2()
        self.sleep_time()
        self.GamePage.game_victory().game_back_home()
        self.get_snapshot(page1, self.name)
        return self

    def test2_challenge_page(self):
        """
        进入25关之后返回首页，出现挑战模式弹窗
        :return:
        """
        page = "挑战页面弹窗"
        self.get_class()
        self.sleep_time(10)
        self.GameHome.pad_get_debug().pad_get_level("40").pad_get_coin("999")
        self.GameHome.goto_game_page()
        self.GamePage.pad_close_debug().pad_game_back_home()
        self.sleep_time()
        self.get_snapshot(page, self.name)
        return self

    def test3_normal_page(self):
        """
        挑战模式解锁之后的首页
        :return:
        """
        page = "挑战模式normal页面"
        page2 = "挑战模式解锁关卡"
        self.get_class()
        level1 = self.ActivityPage.pad_level_1
        self.GameHome.pad_activity_page_go()
        self.get_snapshot(page, self.name)
        self.ActivityPage.unlock_level(level1)
        self.get_snapshot(page2, self.name)
        return self

    def test4_fail_page(self):
        """
        失败继续弹窗
        :return:
        """
        page = "挑战模式失败继续弹窗"

        self.get_class()
        level1 = self.ActivityPage.pad_level_1
        self.ActivityPage.unlock_level(level1).unlock_level(level1)
        self.GameHome.expand_debug()
        self.GamePage.debug_minus_time()
        self.sleep_time(2)
        self.get_snapshot(page, self.name)
        return self

    def test5_try_again(self):
        page = "重新游玩"
        page2 = "胜利页面"
        self.get_class()
        self.ActivityPage.pad_fail_back_level()
        level1 = self.ActivityPage.pad_level_1
        self.ActivityPage.unlock_level(level1)
        self.GamePage.debug_win().pad_debug_doone().pad_debug_doone()
        self.sleep_time(15)
        self.get_snapshot(page2, self.name)
        self.ActivityPage.pad_activity_victory_continue()
        self.get_snapshot(page, self.name)
        return self

    def test6_hard_page(self):
        page = "困难模式"
        self.get_class()
        self.ActivityPage.pad_goto_hard()
        self.sleep_time()
        self.get_snapshot(page, self.name)
