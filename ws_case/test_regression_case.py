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
from ws_page.adjust_time_android import AdjustTime


class TestRegressionCase(BaseElement):
    water_sort_android = "water.sort.puzzle.android.inner"

    def setup_class(self):
        auto_setup(__file__, logdir=True,
                   devices=["android://127.0.0.1:5037/R3CW10C3D9N?cap_method=ADBCAP&touch_method=MAXTOUCH&", ])

    def get_class(self):
        self.PolicyPage = PolicyPage()
        self.NewGuidance = NewGuidance()
        self.GamePage = GamePage()
        self.GameHome = GameHome()
        self.CollectPage = CollectPage()
        self.AdjustTime = AdjustTime()

    def get_class2(self):
        self.poco = BasePoco()

    def test1_first_open_policy(self):
        """
        首次进入游戏，弹出隐私弹窗
        :return:
        """
        element = "Button"
        self.get_class()
        self.PolicyPage.first_start_android()
        self.PolicyPage.close_information_page()
        self.PolicyPage.close_log()
        self.sleep_time(4)
        self.get_class2()
        self.poco.poco_assert(element)

    def test2_click_terms_service(self):
        self.get_class()
        self.PolicyPage.goto_tos()
        self.sleep_time(4)
        self.exists_assert(self.PolicyPage.terms_of_service_picture)

    def test3_click_privacy_policy(self):
        self.get_class()
        self.PolicyPage.privicy_close()
        self.sleep_time()
        self.PolicyPage.goto_pp()
        self.sleep_time(4)
        self.exists_assert(self.PolicyPage.privacy_policy_picture)

    def test4_stop_app_policy(self):
        """
        stop游戏，再次进入，仍然为隐私弹窗
        :return:
        """
        element = "Button"
        self.stop_app(self.water_sort_android)
        self.start_app(self.water_sort_android)
        self.sleep_time(4)
        self.get_class2()
        self.poco.poco_assert(element)

    def test5_accept_guidance(self):
        """
        点击accept，进入新手引导
        :return:
        """
        element = "BottleMask"
        self.get_class()
        self.PolicyPage.close_log().goto_guidance()
        self.sleep_time()
        self.get_class2()
        self.poco.poco_assert(element)

    def test6_new_guidance_step1(self):
        """
        判断新手引导是否正确
        :return:
        """
        self.get_class()
        self.exists_assert(self.NewGuidance.first_step)
        return self

    def test7_second_step_guidance(self):
        """
        判断第二步的新手引导文案
        :return:
        """
        self.get_class()
        self.NewGuidance.first_guidance_step1()
        self.exists_assert(self.NewGuidance.second_step)
        return self

    def test8_second_guidance_step(self):
        """
        第二步新手引导的yes和no
        :return:
        """
        self.get_class()
        self.NewGuidance.first_guidance_step2()
        self.GamePage.game_victory()
        self.NewGuidance.second_guidance_step1()
        self.exists_assert(self.NewGuidance.yes_and_no)

    def test9_pass_first_guidance(self):
        """
        通关到第三关
        :return:
        """
        element = "Button_Setting"
        self.get_class()
        self.NewGuidance.second_guidance_step1()
        self.NewGuidance.completed_level2()
        self.GamePage.game_victory()
        self.get_class2()
        self.poco.poco_assert(element)
        return self

    def test10_get_guide_page(self):
        """
        第三关弹出
        :return:
        """
        element = "Button_NoUse"
        self.get_class()
        self.PolicyPage.first_start_android()
        self.PolicyPage.close_information_page()
        self.PolicyPage.close_log().goto_guidance()
        self.NewGuidance.first_guidance_step1().first_guidance_step2()
        self.GamePage.game_victory()
        self.NewGuidance.completed_level2()
        self.GamePage.game_victory().game_back_home()
        self.GameHome.get_debug().goto_game_page()
        self.GamePage.debug_win()
        self.sleep_time()
        self.GamePage.debug_doone()
        self.sleep_time()
        self.GamePage.debug_doone()
        self.sleep_time(3)
        self.get_class2()
        self.poco.poco_assert(element)
        self.exists_assert(self.GamePage.fourth_star_Face)
        return self

    def test11_click_differend_star(self):
        """
        评分引导里点击不同的星星出现不同的断言
        :return:
        """
        self.get_class()
        first_star = [315, 1474]
        second_star = [513, 1484]
        third_star = [730, 1484]
        fourth_star = [933, 1503]
        fifth_star = [1116, 1484]
        self.image_click(first_star)
        self.exists_assert(self.GamePage.first_star_face)
        self.image_click(second_star)
        self.exists_assert(self.GamePage.second_star_face)
        self.image_click(third_star)
        self.exists_assert(self.GamePage.third_star_face)
        self.image_click(fourth_star)
        self.exists_assert(self.GamePage.fourth_star_Face)
        self.image_click(fifth_star)
        self.exists_assert(self.GamePage.fifth_star_face)
        return self

    def test12_third_star_click(self):
        """
        获得三颗星星后点击跳转到邮件反馈
        :return:
        """
        element = "Button_CanUse"
        self.get_class()
        self.get_class2()
        third_star = [730, 1484]
        self.image_click(third_star)
        self.poco.unity_poco_click(element)
        self.system_keyevent("BACK")
        self.exists_assert(self.GamePage.please_dont_delete)
        return self

    def test13_fifth_click(self):
        """
        获得五颗星之后点击跳转到gp页面
        :return:
        """
        fifth_star = [1116, 1484]
        element = "Button_OK"
        self.get_class()
        self.PolicyPage.first_start_android()
        self.PolicyPage.close_information_page()
        self.PolicyPage.close_log().goto_guidance()
        self.NewGuidance.first_guidance_step1().first_guidance_step2()
        self.GamePage.game_victory()
        self.NewGuidance.completed_level2()
        self.GamePage.game_victory().game_back_home()
        self.GameHome.get_debug().goto_game_page()
        self.GamePage.debug_win()
        self.sleep_time()
        self.GamePage.debug_doone()
        self.sleep_time()
        self.GamePage.debug_doone()
        self.sleep_time(3)
        self.image_click(fifth_star)
        self.get_class2()
        self.poco.unity_poco_click(element)
        self.exists_assert(self.GamePage.water_sort_icon)
        return self

    def test14_home_setting_page(self):
        """
        从首页进入setting页面
        :return:
        """
        element = "Button_Close"
        self.get_class()
        self.stop_app(self.water_sort_android)
        self.start_app(self.water_sort_android)
        self.PolicyPage.close_log()
        self.sleep_time(3)
        self.GamePage.goto_setting_page()
        self.get_class2()
        self.poco.poco_assert(element)

    def test15_setting_page_go_home(self):
        """
        从设置页面回到游戏首页
        :return:
        """
        element1 = "Button_Close"
        element2 = "Button_I"
        self.get_class2()
        self.poco.unity_poco_click(element1)
        self.poco.poco_assert(element2)
        return self

    def test16_home_setting_tops(self):
        """
        关闭瓶盖
        :return:
        """
        self.get_class()
        self.GamePage.close_debug()
        self.GamePage.goto_setting_page()
        self.GamePage.click_tops()
        self.GamePage.setting_close()
        self.GameHome.get_debug().goto_game_page()
        self.GamePage.debug_win()
        self.GamePage.debug_doone()
        self.sleep_time()
        self.GamePage.debug_doone()
        self.sleep_time(4)
        self.GamePage.setting_close()
        self.sleep_time(4)
        self.GamePage.game_victory().debug_win(10)
        self.not_exists_assert(self.GamePage.tube_tops)
        self.GamePage.goto_setting_page()
        self.exists_assert(self.GamePage.tops_close)
        return self

    # def test17_home_setting_tops_open(self):
    #     """
    #     打开瓶盖
    #     :return:
    #     """
    #     self.get_class()
    #     self.sleep_time(3)
    #     self.PolicyPage.close_log()
    #     self.GamePage.goto_setting_page().click_tops().setting_close()
    #     self.GameHome.goto_game_page()
    #     self.exists_assert(self.GamePage.tube_tops)
    #     self.GamePage.goto_setting_page()
    #     self.exists_assert(self.GamePage.tops_open)
















