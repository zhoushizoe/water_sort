import pytest
from airtest.cli.parser import cli_setup
from airtest.core.api import *
from ws_base.base_poco import BasePoco
from ws_base.base_ws import BaseElement
from ws_page.policy_page import PolicyPage
from ws_page.guidance_page import NewGuidance
from ws_page.game_page import GamePage
from ws_page.game_home_page import GameHome
from ws_page.colloct_page import CollectPage
from ws_page.adjust_time_android import AdjustTime
from new_ws_page.new_policy_page import NewPolicyPage
from new_ws_page.new_game_page import NewGamePage
from new_ws_page.new_home_page import NewHomePage
from new_ws_page.new_collection_page import NewCollectionPage
from new_ws_page.new_challenge_page import NewChallengePage


class TestRegressionCase(BaseElement):
    """
    回归测试环境为英文环境，因为涉及到一些图像识别为英语，所以在执行此脚本时将系统语言调为英文
    """
    water_sort_android = "water.sort.puzzle.android.inner"

    def setup_class(self):
        auto_setup(__file__, logdir=True,
                   devices=["android://127.0.0.1:5037/R3CW10C3D9N?cap_method=ADBCAP&touch_method=MAXTOUCH&", ])

    def get_class(self):
        self.sleep_time(3)
        self.PolicyPage = PolicyPage()
        self.NewGuidance = NewGuidance()
        self.GamePage = GamePage()
        self.GameHome = GameHome()
        self.CollectPage = CollectPage()
        self.AdjustTime = AdjustTime()
        self.NewPolicyPage = NewPolicyPage()
        self.NewGamePage = NewGamePage()
        self.NewHomePage = NewHomePage()
        self.NewCollectionPage = NewCollectionPage()
        self.NewChallengePage = NewChallengePage()

    def get_class2(self):
        self.poco = BasePoco()

    def test1_first_open_policy(self):
        """
        首次进入游戏，弹出隐私弹窗
        :return:
        """
        element = "Button_OK"
        self.get_class()
        self.NewPolicyPage.first_open_android_app()
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
        self.PolicyPage.close_log()
        self.NewPolicyPage.accept_goto_guidance()
        self.sleep_time()
        self.get_class2()
        self.poco.poco_assert(element)

    def test6_new_guidance_step1(self):
        """
        判断新手引导是否正确
        :return:
        """
        # first_guidance_content = "Click to select one bottle"
        self.get_class()
        # self.poco.poco_assert(first_guidance_content)
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

    def test_get_guide_page(self):
        """
        第三关弹出
        :return:
        """

        self.get_class()
        self.NewPolicyPage.first_open_android_app()
        self.PolicyPage.close_log()
        return self

    def test11_get_guide_page(self):
        element = "Button_NoUse"
        self.get_class()
        self.NewPolicyPage.accept_goto_guidance()
        self.NewGuidance.first_guidance_step1().first_guidance_step2()
        self.NewGamePage.new_game_victory()
        self.NewGuidance.completed_level2()
        self.NewGamePage.new_game_victory().new_game_back_home()
        self.NewHomePage.new_get_debug().new_goto_game_page()
        self.NewGamePage.new_debug_win(10)
        self.NewGamePage.new_debug_doone()
        self.sleep_time(3)
        self.get_class2()
        self.poco.poco_assert(element)
        self.exists_assert(self.GamePage.fourth_star_Face)
        return self

    def test11_click_different_star(self):
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

    def test_get_guide_page2(self):
        """
        第三关弹出
        :return:
        """

        self.get_class()
        self.NewPolicyPage.first_open_android_app()
        self.PolicyPage.close_log()
        return self

    def test13_fifth_click(self):
        """
        获得五颗星之后点击跳转到gp页面
        :return:
        """
        fifth_star = [1116, 1484]
        element = "Button_OK"
        self.get_class()
        self.NewPolicyPage.accept_goto_guidance()
        self.NewGuidance.first_guidance_step1().first_guidance_step2()
        self.NewGamePage.new_game_victory()
        self.NewGuidance.completed_level2()
        self.NewGamePage.new_game_victory().new_game_back_home()
        self.NewHomePage.new_get_debug().new_goto_game_page()
        self.NewGamePage.new_debug_win(10)
        self.sleep_time()
        self.NewGamePage.new_debug_doone()
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
        self.stop_app(self.water_sort_android)
        self.start_app(self.water_sort_android)
        self.get_class()
        self.PolicyPage.close_log()

        self.sleep_time(3)
        self.NewGamePage.new_goto_setting_page()
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

    def test_get_guide_page3(self):
        """
        第三关弹出
        :return:
        """

        self.get_class()
        self.NewPolicyPage.first_open_android_app()
        self.PolicyPage.close_log()
        return self

    def test16_home_setting_tops(self):
        """
        关闭瓶盖
        :return:
        """
        self.get_class()
        self.NewPolicyPage.accept_goto_guidance()
        self.NewGuidance.first_guidance_step1().first_guidance_step2()
        self.NewGamePage.new_game_victory()
        self.NewGuidance.completed_level2()
        self.NewGamePage.new_game_victory().new_game_back_home()
        self.NewGamePage.new_goto_setting_page().new_change_tops().new_setting_close()
        self.NewHomePage.new_get_debug().new_goto_game_page()
        self.NewGamePage.new_debug_win(10).new_goto_setting_page()
        self.NewGamePage.new_setting_close()
        self.not_exists_assert(self.GamePage.tube_tops)
        self.NewGamePage.new_goto_setting_page()
        self.exists_assert(self.GamePage.tops_close)
        return self

    def test17_home_setting_tops_open(self):
        """
        打开瓶盖
        :return:
        """
        self.get_class()
        self.NewGamePage.new_change_tops().new_setting_close()
        self.exists_assert(self.GamePage.tube_tops)
        self.NewGamePage.new_game_back_home().new_goto_setting_page()
        self.exists_assert(self.GamePage.tops_open)
        return self

    def test18_setting_goto_collection(self):
        """
        从设置页面进入收藏页面
        :return:
        """
        collection_image = "SelectGroup"
        self.stop_app(self.water_sort_android)
        self.start_app(self.water_sort_android)
        self.get_class()
        self.sleep_time()
        self.PolicyPage.close_log()
        self.sleep_time()
        self.NewGamePage.new_goto_setting_page().new_setting_goto_collection()
        self.get_class2()
        self.poco.poco_assert(collection_image)
        return self

    def test19_setting_goto_language(self):
        language = "Language"
        self.stop_app(self.water_sort_android)
        self.start_app(self.water_sort_android)
        self.get_class()
        self.PolicyPage.close_log()
        self.NewGamePage.new_goto_setting_page().new_setting_goto_language()
        self.get_class2()
        self.poco.poco_assert_text(language)
        return self

    def test20_change_language(self):
        french_language = "Langue"
        self.get_class()
        self.NewGamePage.new_change_language_french()
        self.get_class2()
        self.poco.poco_assert_text(french_language)
        return self

    def test21_contact_us(self):
        self.stop_app(self.water_sort_android)
        self.start_app(self.water_sort_android)
        self.get_class()
        self.PolicyPage.close_log()
        self.NewGamePage.new_goto_setting_page().new_goto_contact_us()
        self.exists_assert(self.GamePage.email_image)
        return self

    def test22_goto_term_of_service(self):
        self.stop_app(self.water_sort_android)
        self.start_app(self.water_sort_android)
        self.get_class()
        self.PolicyPage.close_log()
        self.NewGamePage.new_goto_setting_page().new_setting_goto_terms_service()
        self.exists_assert(self.PolicyPage.terms_of_service_picture)
        return self

    def test23_goto_privacy_policy(self):
        self.stop_app(self.water_sort_android)
        self.start_app(self.water_sort_android)
        self.get_class()
        self.PolicyPage.close_log()
        self.NewGamePage.new_goto_setting_page().new_setting_goto_privacy_policy()
        self.exists_assert(self.PolicyPage.privacy_policy_picture)
        return self

    def test24_home_ads_purchase(self):
        purchase_button = "Button_OK"
        self.stop_app(self.water_sort_android)
        self.start_app(self.water_sort_android)
        self.get_class()
        self.PolicyPage.close_log()
        self.NewHomePage.new_ads_purchase()
        self.get_class2()
        self.poco.poco_assert(purchase_button)
        return self

    def test25_home_reward_chest(self):
        """
        点击首页宝箱
        :return:
        """
        element = "Button_OK"
        self.stop_app(self.water_sort_android)
        self.start_app(self.water_sort_android)
        self.get_class()
        self.PolicyPage.close_log()
        self.NewHomePage.new_goto_level_chest_page()
        self.get_class2()
        self.poco.poco_assert(element)
        return self

    def test26_chest_page_continue(self):
        """
        在首页宝箱页面点击continue按钮回到首页
        :return:
        """
        self.get_class()
        home_level_button = self.NewHomePage.home_level_button
        self.NewHomePage.new_chest_continue()
        self.get_class2()
        self.poco.poco_assert(home_level_button)
        return self

    def test27_chest_page_close(self):
        self.stop_app(self.water_sort_android)
        self.start_app(self.water_sort_android)
        self.get_class()
        self.PolicyPage.close_log()
        home_level_button = self.NewHomePage.home_level_button
        self.NewHomePage.new_goto_level_chest_page()
        self.NewHomePage.new_chest_close()
        self.get_class2()
        self.poco.poco_assert(home_level_button)
        return self

    def test28_game_back_home(self):
        """
        从游戏页面返回首页
        :return:
        """
        self.stop_app(self.water_sort_android)
        self.start_app(self.water_sort_android)
        self.get_class()
        home_level_button = self.NewHomePage.home_level_button
        self.PolicyPage.close_log()
        self.NewHomePage.new_goto_game_page()
        self.NewGamePage.new_game_back_home()
        self.get_class2()
        self.poco.poco_assert(home_level_button)
        return self

    def test29_game_setting_page(self):
        """
        从首页进入setting页面
        :return:
        """
        element = "Button_Close"
        self.stop_app(self.water_sort_android)
        self.start_app(self.water_sort_android)
        self.get_class()
        self.PolicyPage.close_log()
        self.sleep_time(3)
        self.NewHomePage.new_goto_game_page()
        self.NewGamePage.new_goto_setting_page()
        self.get_class2()
        self.poco.poco_assert(element)

    def test30_setting_page_go_home(self):
        """
        从设置页面回到游戏首页
        :return:
        """
        element1 = "Button_Close"
        element2 = "Button_Undo"
        self.get_class2()
        self.poco.unity_poco_click(element1)
        self.poco.poco_assert(element2)
        return self

    def test_first_open(self):
        """
        首次打开游戏
        :return:
        """

        self.get_class()
        self.NewPolicyPage.first_open_android_app()
        self.PolicyPage.close_log()
        return self

    def test31_game_setting_tops(self):
        """
        关闭瓶盖
        :return:
        """
        self.get_class()
        self.NewPolicyPage.accept_goto_guidance()
        self.NewGuidance.first_guidance_step1().first_guidance_step2()
        self.NewGamePage.new_game_victory()
        self.NewGuidance.completed_level2()
        self.NewGamePage.new_game_victory()
        self.NewGamePage.new_goto_setting_page().new_change_tops().new_setting_close().new_game_back_home()
        self.NewHomePage.new_get_debug().new_goto_game_page()
        self.NewGamePage.new_debug_win(10).new_goto_setting_page()
        self.NewGamePage.new_setting_close()
        self.not_exists_assert(self.GamePage.tube_tops)
        self.NewGamePage.new_game_back_home().new_goto_setting_page()
        self.exists_assert(self.GamePage.tops_close)
        return self

    def test32_game_setting_tops_open(self):
        """
        打开瓶盖
        :return:
        """
        self.get_class()
        self.NewGamePage.new_change_tops().new_setting_close()
        self.NewHomePage.new_goto_game_page()
        self.exists_assert(self.GamePage.tube_tops)
        self.NewGamePage.new_game_back_home().new_goto_setting_page()
        self.exists_assert(self.GamePage.tops_open)
        return self

    def test33_setting_goto_collection(self):
        """
        从设置页面进入收藏页面
        :return:
        """
        collection_image = "SelectGroup"
        self.stop_app(self.water_sort_android)
        self.start_app(self.water_sort_android)
        self.get_class()
        self.PolicyPage.close_log()
        self.NewHomePage.new_goto_game_page()
        self.NewGamePage.new_goto_setting_page().new_setting_goto_collection()
        self.get_class2()
        self.poco.poco_assert(collection_image)
        return self

    def test34_setting_goto_language(self):
        language = "Language"
        self.stop_app(self.water_sort_android)
        self.start_app(self.water_sort_android)
        self.get_class()
        self.PolicyPage.close_log()
        self.NewHomePage.new_goto_game_page()
        self.NewGamePage.new_goto_setting_page().new_setting_goto_language()
        self.get_class2()
        self.poco.poco_assert_text(language)
        return self

    def test35_change_language(self):
        french_language = "Langue"
        self.get_class()
        self.NewGamePage.new_change_language_french()
        self.get_class2()
        self.poco.poco_assert_text(french_language)
        return self

    def test36_contact_us(self):
        self.stop_app(self.water_sort_android)
        self.start_app(self.water_sort_android)
        self.get_class()
        self.PolicyPage.close_log()
        self.NewHomePage.new_goto_game_page()
        self.NewGamePage.new_goto_setting_page().new_goto_contact_us()
        self.exists_assert(self.GamePage.email_image)
        return self

    def test37_goto_term_of_service(self):
        self.stop_app(self.water_sort_android)
        self.start_app(self.water_sort_android)
        self.get_class()
        self.PolicyPage.close_log()
        self.NewHomePage.new_goto_game_page()
        self.NewGamePage.new_goto_setting_page().new_setting_goto_terms_service()
        self.exists_assert(self.PolicyPage.terms_of_service_picture)
        return self

    def test38_goto_privacy_policy(self):
        self.stop_app(self.water_sort_android)
        self.start_app(self.water_sort_android)
        self.get_class()
        self.PolicyPage.close_log()
        self.NewHomePage.new_goto_game_page()
        self.NewGamePage.new_goto_setting_page().new_setting_goto_privacy_policy()
        self.exists_assert(self.PolicyPage.privacy_policy_picture)
        return self

    def test39_restart_tool(self):
        """
        点击重开道具
        :return:
        """

        self.stop_app(self.water_sort_android)
        self.start_app(self.water_sort_android)
        self.get_class()
        empty_tube = self.GamePage.empty_tube
        self.PolicyPage.close_log()
        self.sleep_time()
        self.NewHomePage.new_get_debug().new_goto_game_page()
        self.NewGamePage.new_debug_win(10).new_close_debug().new_click_restart_tool()
        self.GamePage.ad_close()
        self.exists_assert(empty_tube)
        return self

    def test40_withdraw_tool(self):
        """
        点击撤回道具一次
        :return:
        """
        self.get_class()
        self.NewHomePage.new_expand_debug()
        self.NewGamePage.new_debug_win(10).new_click_undo_tool()
        self.GamePage.ad_close()
        self.NewGamePage.new_click_undo_tool()
        self.assert_equal("2", self.NewGamePage.get_withdraw_number())
        self.not_exists_assert(self.GamePage.tube_tops)
        return self

    def test41_withdraw_tool_three(self):
        """
        点击撤回道具三次
        :return:
        """
        self.get_class()
        self.NewPolicyPage.first_open_android_app()
        self.PolicyPage.close_log()
        self.get_class()
        self.NewPolicyPage.accept_goto_guidance()
        self.NewGuidance.first_guidance_step1().first_guidance_step2()
        self.NewGamePage.new_game_victory()
        self.NewGuidance.completed_level2()
        self.NewGamePage.new_game_victory().new_click_undo_tool()
        self.sleep_time()
        self.GamePage.ad_close()
        self.NewGamePage.new_game_back_home()
        self.NewHomePage.new_get_debug().new_goto_game_page()
        self.NewGamePage.new_debug_win(10).new_debug_doone(1)
        self.exists_assert(self.GamePage.tube_tops)
        self.NewGamePage.new_click_undo_tool().new_click_undo_tool().new_click_undo_tool()
        self.exists_assert(self.GamePage.empty_tube)
        return self

    def test42_add_tube(self):
        """
        点击加瓶道具一次
        :return:
        """
        ad_image = "Image_AD"
        self.stop_app(self.water_sort_android)
        self.start_app(self.water_sort_android)
        self.get_class()
        self.PolicyPage.close_log()
        self.NewHomePage.new_goto_game_page()
        self.sleep_time()
        self.NewGamePage.new_click_add_tube()
        self.GamePage.ad_close()
        self.sleep_time()
        self.assert_equal("1", self.NewGamePage.get_add_tube_number())
        self.NewGamePage.new_click_add_tube()
        self.get_class2()
        self.poco.poco_assert(ad_image)
        return self

    def test43_tips_tool(self):
        """
        点击提示道具一次
        :return:
        """
        ad_image = "Image_AD"
        self.stop_app(self.water_sort_android)
        self.start_app(self.water_sort_android)
        self.get_class()
        self.PolicyPage.close_log()
        self.NewHomePage.new_goto_game_page()
        self.NewGamePage.new_click_tips_tool()
        self.GamePage.ad_close()
        self.sleep_time(2)
        self.assert_equal("1", self.NewGamePage.new_get_tips_number())
        self.NewGamePage.new_click_tips_tool()
        self.get_class2()
        self.assert_equal(ad_image, self.NewGamePage.new_no_tips_name())
        return self

    def test44_skip_tool(self):
        """
        跳过关卡道具
        :return:
        """
        self.get_class()
        element = "Button_NoUse"
        first_tube = [150, 1460]
        fourth_tube = [1008, 1409]
        self.NewGamePage.new_click_restart_tool()
        for i in range(3):
            self.image_click(first_tube).image_click(fourth_tube)
            self.NewGamePage.new_click_restart_tool()
        self.NewGamePage.skip_level()
        self.GamePage.ad_close()
        self.sleep_time(10)
        self.get_class2()
        self.poco.poco_assert(element)
        self.exists_assert(self.GamePage.fourth_star_Face)
        return self

    def test45_banner_ads(self):
        """
        去除广告的边框
        :return:
        """
        purchase_button = "Button_OK"
        self.stop_app(self.water_sort_android)
        self.start_app(self.water_sort_android)
        self.get_class()
        self.PolicyPage.close_log()
        self.NewHomePage.new_goto_game_page()
        self.NewGamePage.ads_banner()
        self.get_class2()
        self.poco.poco_assert(purchase_button)
        return self

    def test46_open_chest(self):
        self.get_class()
        self.NewPolicyPage.first_open_android_app()
        self.PolicyPage.close_log()
        self.get_class()
        self.NewPolicyPage.accept_goto_guidance()
        self.NewGuidance.first_guidance_step1().first_guidance_step2()
        self.NewGamePage.new_game_victory()
        self.NewGuidance.completed_level2()
        self.NewGamePage.new_game_victory().new_game_back_home()
        self.NewHomePage.new_get_debug().new_get_level_android("9").new_goto_game_page()
        self.NewGamePage.new_debug_win(20).new_debug_doone()
        self.GamePage.ad_close()
        self.sleep_time(10)
        self.exists_assert(self.GamePage.chest_item_withdraw)
        self.exists_assert(self.GamePage.chest_coin)
        return self

    def test47_get_chest_no_double(self):
        self.get_class()
        self.NewGamePage.new_get_chest_no_double().new_game_victory()
        self.assert_equal("1", self.NewGamePage.get_withdraw_number())
        self.NewGamePage.new_close_debug().new_game_back_home()
        self.assert_equal("20", self.NewHomePage.get_coin_number())
        return self

    def test48_get_tube(self):
        element = "Button_Use"
        self.stop_app(self.water_sort_android)
        self.start_app(self.water_sort_android)
        self.get_class()
        self.PolicyPage.close_log()
        self.NewHomePage.new_get_debug().new_get_level_android("12").new_goto_game_page()
        self.NewGamePage.new_debug_win(20).new_debug_doone()
        self.GamePage.ad_close()
        self.sleep_time(5)
        self.get_class2()
        self.poco.poco_assert(element)
        return self

    def test49_tube_no_thanks(self):
        """
        在rewards页面点击no thanks
        :return:
        """
        self.get_class()
        self.NewGamePage.new_click_no_thanks().new_game_victory()
        self.sleep_time()
        self.exists_assert(self.GamePage.empty_tube)
        return self

    def test50_tube_use(self):
        """
        在rewards页面点击use
        :return:
        """
        element = "Button_Use"
        self.stop_app(self.water_sort_android)
        self.start_app(self.water_sort_android)
        self.get_class()
        self.PolicyPage.close_log()
        self.NewHomePage.new_get_debug().new_get_level_android("12").new_goto_game_page()
        self.NewGamePage.new_debug_win(20).new_debug_doone()
        self.GamePage.ad_close()
        self.sleep_time(5)
        self.NewGamePage.new_click_use().new_game_victory()
        self.exists_assert(self.GamePage.second_empty_tube)
        return self

    def test51_get_background(self):
        """
        直接得到背景page
        :return:
        """
        self.stop_app(self.water_sort_android)
        self.start_app(self.water_sort_android)
        self.get_class()
        self.PolicyPage.close_log()
        self.NewHomePage.new_get_debug().new_get_level_android("20").new_goto_game_page()
        self.NewGamePage.new_debug_win(20).new_debug_doone()
        self.GamePage.ad_close()
        self.sleep_time(5)
        self.exists_assert(self.GamePage.reward_background)
        return self

    def test52_no_use_background(self):
        self.stop_app(self.water_sort_android)
        self.start_app(self.water_sort_android)
        self.get_class()
        self.PolicyPage.close_log()
        self.NewHomePage.new_get_debug().new_get_level_android("20").new_goto_game_page()
        self.NewGamePage.new_debug_win(20).new_debug_doone()
        self.GamePage.ad_close()
        self.sleep_time(5)
        self.NewGamePage.new_click_no_thanks().new_game_victory()
        self.NewGamePage.new_close_debug().new_goto_setting_page().new_setting_goto_collection()
        self.NewCollectionPage.new_goto_theme_page()
        self.exists_assert(self.CollectPage.choose_first_background)
        return self

    def test53_use_background(self):
        self.stop_app(self.water_sort_android)
        self.start_app(self.water_sort_android)
        self.get_class()
        self.PolicyPage.close_log()
        self.NewHomePage.new_get_debug().new_get_level_android("20").new_goto_game_page()
        self.NewGamePage.new_debug_win(20).new_debug_doone()
        self.GamePage.ad_close()
        self.sleep_time(5)
        self.NewGamePage.new_click_use().new_game_victory()
        self.NewGamePage.new_close_debug().new_goto_setting_page().new_setting_goto_collection()
        self.NewCollectionPage.new_goto_theme_page()
        self.not_exists_assert(self.CollectPage.choose_first_background)
        return self

    def test54_coin_get_background(self):
        """
        金币获得背景
        :return:
        """
        self.stop_app(self.water_sort_android)
        self.start_app(self.water_sort_android)
        self.get_class()
        self.PolicyPage.close_log()
        self.NewHomePage.new_get_debug().new_get_level_android("590").new_debug_get_coin("999").new_goto_game_page()
        self.NewGamePage.new_close_debug().new_game_back_home()
        self.sleep_time()
        self.NewHomePage.challenge_page_no_thanks()
        self.NewGamePage.new_goto_setting_page().new_setting_goto_collection()
        self.NewCollectionPage.new_goto_theme_page().new_swipe_bottom().new_get_coin_theme()
        self.assert_equal("399", self.NewHomePage.get_coin_number())
        return self

    def test55_collection_tube(self):
        """
        收藏页面的管页面展示是否正常
        :return:
        """
        self.stop_app(self.water_sort_android)
        self.start_app(self.water_sort_android)
        self.get_class()
        collection_tube_page = self.NewCollectionPage.collection_tube_page
        self.PolicyPage.close_log()
        self.NewGamePage.new_goto_setting_page().new_setting_goto_collection()
        self.exists_assert(collection_tube_page)
        return self

    def test56_collection_change_tube(self):
        """
        在收藏页面的管页面切换管
        :return:
        """
        self.get_class()
        self.NewCollectionPage.new_choose_love_tube()
        self.NewGamePage.new_game_back_home().new_setting_close()
        self.NewHomePage.new_get_debug().new_goto_game_page()
        self.NewGamePage.new_debug_win(20)
        self.exists_assert(self.NewCollectionPage.love_tube_tops)
        return self

    def test57_collection_theme(self):
        """
        收藏页面的theme页面表现正常
        :return:
        """
        self.stop_app(self.water_sort_android)
        self.start_app(self.water_sort_android)
        self.get_class()
        self.PolicyPage.close_log()
        collection_theme_page = self.NewCollectionPage.collection_theme_tube
        self.NewGamePage.new_goto_setting_page().new_setting_goto_collection()
        self.NewCollectionPage.new_goto_theme_page()
        self.exists_assert(collection_theme_page)
        return self

    def test58_collection_change_theme(self):
        """
        在收藏页面切换theme
        :return:
        """
        self.get_class()
        self.NewCollectionPage.new_choose_mountain_theme()
        self.NewGamePage.new_game_back_home().new_setting_close()
        self.NewHomePage.new_get_debug().new_goto_game_page()
        self.exists_assert(self.NewCollectionPage.game_page_mountain)
        return self

    def test59_first_goto_challenge(self):
        """
        首次弹出挑战弹窗，并点击no，thanks
        :return:
        """
        self.get_class()
        element = self.NewHomePage.challenge_no
        element2 = self.NewHomePage.level_chest_button
        self.NewPolicyPage.first_open_android_app()
        self.PolicyPage.close_log()
        self.get_class()
        self.NewPolicyPage.accept_goto_guidance()
        self.NewGuidance.first_guidance_step1().first_guidance_step2()
        self.NewGamePage.new_game_victory()
        self.NewGuidance.completed_level2()
        self.NewGamePage.new_game_victory().new_game_back_home()
        self.NewHomePage.new_get_debug().new_get_level_android("25").new_goto_game_page()
        self.NewGamePage.new_debug_win(20).new_debug_doone()
        self.GamePage.ad_close()
        self.sleep_time(10)
        self.NewGamePage.new_get_chest_no_double()
        self.sleep_time()
        self.NewGamePage.new_game_victory().new_close_debug().new_game_back_home()
        self.get_class2()
        self.poco.poco_assert(element)
        self.NewHomePage.challenge_page_no_thanks()
        self.poco.poco_assert(element2)
        return self

    def test60_first_goto_challenge(self):
        """
        首次弹出挑战弹窗，并选择进入挑战模式
        :return:
        """
        self.get_class()
        element = self.NewHomePage.challenge_no
        element2 = self.NewChallengePage.normal_first_level
        element3 = self.NewChallengePage.purchase_level
        self.NewPolicyPage.first_open_android_app()
        self.PolicyPage.close_log()
        self.get_class()
        self.NewPolicyPage.accept_goto_guidance()
        self.NewGuidance.first_guidance_step1().first_guidance_step2()
        self.NewGamePage.new_game_victory()
        self.NewGuidance.completed_level2()
        self.NewGamePage.new_game_victory().new_game_back_home()
        self.NewHomePage.new_get_debug().new_get_level_android("25").new_goto_game_page()
        self.NewGamePage.new_debug_win(20).new_debug_doone()
        self.GamePage.ad_close()
        self.sleep_time(10)
        self.NewGamePage.new_get_chest_no_double()
        self.sleep_time()
        self.NewGamePage.new_game_victory().new_close_debug().new_game_back_home()
        self.get_class2()
        self.poco.poco_assert(element)
        self.NewHomePage.challenge_page_continue()
        self.sleep_time()
        self.poco.poco_assert(element2)
        self.poco.poco_assert(element3)
        return self

    def test61_lock_level(self):
        """
        没有足够的金币点击解锁
        :return:
        """
        self.stop_app(self.water_sort_android)
        self.start_app(self.water_sort_android)
        self.get_class()
        self.PolicyPage.close_log()
        self.NewHomePage.new_goto_challenge_page()
        self.NewChallengePage.click_coins_purchase_level()
        self.get_class2()
        self.poco.poco_assert(self.NewChallengePage.get_coins_ad)
        return self

    def test62_unlock_level(self):
        """
        有足够的金币解锁关卡
        :return:
        """
        self.stop_app(self.water_sort_android)
        self.start_app(self.water_sort_android)
        self.get_class()
        element = self.NewChallengePage.unlock_level_go
        self.PolicyPage.close_log()
        self.NewHomePage.new_get_debug().new_debug_get_coin("999").new_goto_challenge_page()
        self.NewChallengePage.click_coins_purchase_level()
        self.get_class2()
        self.poco.poco_assert_text(element)
        return self

    def test63_goto_challenge_level(self):
        """
        点击进入挑战模式关卡
        :return:
        """
        self.get_class()
        element = self.NewGamePage.undo_button
        self.NewChallengePage.click_coins_purchase_level()
        self.get_class2()
        self.poco.poco_assert(element)
        return self

    def test64_challenge_game_failed(self):
        """
        挑战模式时间结束，游戏失败，弹出失败弹窗
        :return:
        """
        self.stop_app(self.water_sort_android)
        self.start_app(self.water_sort_android)
        self.get_class()
        self.PolicyPage.close_log()
        self.NewHomePage.new_get_debug().new_goto_challenge_page()
        self.NewChallengePage.click_coins_purchase_level().new_debug_reduce_time(2, 3)
        self.get_class2()
        self.poco.poco_assert(self.NewHomePage.challenge_continue)
        self.poco.poco_assert_text(self.NewChallengePage.time_is_up)
        return self

    def test65_challenge_failed_continue(self):
        """
        在挑战模式的倒计时结束页面点击增加时间
        :return:
        """
        self.get_class()
        self.NewChallengePage.new_click_add_minutes()
        self.GamePage.ad_close()
        self.sleep_time()
        self.get_class2()
        self.poco.poco_assert(self.NewGamePage.tips_button)
        return self

    def test66_challenge_failed_no_thanks(self):
        """
        在挑战模式的倒计时结束页面点击不复活
        :return:
        """
        self.stop_app(self.water_sort_android)
        self.start_app(self.water_sort_android)
        self.get_class()
        self.PolicyPage.close_log()
        self.NewHomePage.new_get_debug().new_goto_challenge_page()
        self.NewChallengePage.click_coins_purchase_level().new_debug_reduce_time(2, 3)
        self.NewChallengePage.new_click_no_thanks()
        self.get_class2()
        self.poco.poco_assert(self.NewChallengePage.normal_first_level)
        return self

    def test67_challenge_victory(self):
        """
        挑战模式游戏胜利
        :return:
        """
        self.get_class()
        element = "Button_Back"
        element2 = "+ 30"
        self.NewChallengePage.click_coins_purchase_level()
        self.NewGamePage.new_debug_win(30).new_debug_doone()
        self.GamePage.ad_close()
        self.sleep_time()
        self.get_class2()
        self.poco.poco_assert(element)
        self.poco.poco_assert_text(element2)
        return self

    def test68_victory_click_continue(self):
        """
        在挑战模式结算页面点击continue
        :return:
        """
        self.get_class()
        self.NewChallengePage.new_challenge_continue()
        self.get_class2()
        self.poco.poco_assert(self.NewChallengePage.play_again)
        return self

    def test69_challenge_play_again(self):
        """
        挑战模式点击play_again按钮
        :return:
        """
        self.get_class()
        element = self.NewGamePage.tips_button
        self.NewChallengePage.new_challenge_play_again()
        self.sleep_time(5)
        self.GamePage.ad_close()
        self.sleep_time()
        self.NewChallengePage.new_unlock_level()
        self.sleep_time()
        self.get_class2()
        self.poco.poco_assert(element)
        return self

    def test70_change_hard(self):
        """
        切换至hard页面
        :return:
        """

        self.stop_app(self.water_sort_android)
        self.start_app(self.water_sort_android)
        self.get_class()
        element = "Complete 12 normal levels to unlock the hard ones"
        self.PolicyPage.close_log()
        self.NewHomePage.new_get_debug().new_goto_challenge_page()
        self.NewChallengePage.new_goto_hard_page()
        self.get_class2()
        self.poco.poco_assert_text(element)
        return self

    def test71_unlock_hard(self):
        """
        解锁后的hard页面
        :return:
        """
        self.stop_app(self.water_sort_android)
        self.start_app(self.water_sort_android)
        self.get_class()
        self.PolicyPage.close_log()
        self.NewHomePage.new_get_debug().new_get_level_android("86").new_debug_get_coin("999").new_goto_game_page()
        self.NewGamePage.new_close_debug().new_game_back_home()
        self.NewHomePage.new_expand_debug().new_goto_challenge_page()
        self.NewChallengePage.new_get_hard_level()











