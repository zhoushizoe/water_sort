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


class TestPoint(BaseElement, GetPointUser, GetPointWater):
    water_sort_android = "water.sort.puzzle.android.inner"

    def setup_class(self):
        auto_setup(__file__, logdir=True,
                   devices=["android://127.0.0.1:5037/R3CW10C3D9N?cap_method=ADBCAP&touch_method=MAXTOUCH&", ])

    def setup(self):
        self.poco = BasePoco()
        self.PolicyPage = PolicyPage()
        self.NewGuidance = NewGuidance()
        self.GamePage = GamePage()
        self.GameHome = GameHome()
        self.CollectPage = CollectPage()
        self.AdjustTime = AdjustTime()

    def assert_result(self, point, correct_point):
        result = self.get_correct_log(point)
        print(f"正确的埋点为：{result}")
        assert result == correct_point

    def assert_result_user(self, point, correct_point):
        self.GetPointUser = GetPointUser()
        result = self.GetPointUser.get_correct_log_user(point)
        print(f"正确的埋点为：{result}")
        assert result == correct_point

    def test1_app_first_open(self):
        """
        app_first_open
        首次启动游戏	玩家安装游戏首次打开时上报生命周期内仅上报一次
        :return:
        """
        point = "app_first_open"
        correct_point = "app_first_open => {"
        self.clear_command()
        self.PolicyPage.first_start_android()
        self.PolicyPage.close_information_page()
        self.sleep_time()
        self.write_contrast2(point)
        self.assert_result(point, correct_point)
        return self

    def test2_app_open(self):
        """
        启动游戏	玩家非首次打开游戏时上报
        :return:
        """
        point = "app_open"
        correct_point = "app_open => {"
        self.stop_app(self.water_sort_android)
        self.clear_command()
        self.start_app(self.water_sort_android)
        self.write_contrast2(point)
        self.assert_result(point, correct_point)
        return self

    @pytest.mark.flaky(reruns=3)
    def test3_app_quit(self):
        point = "app_quit"
        correct_point = "app_quit => {"
        self.stop_app(self.water_sort_android)
        self.start_app(self.water_sort_android)
        self.clear_command()
        self.system_keyevent("HOME")
        self.sleep_time()
        self.write_contrast2(point)
        self.assert_result(point, correct_point)
        return self

    def test4_privacy_pv(self):
        """
        隐私弹窗展示	启动页结束后，隐私弹窗页面展示
        :return:
        """
        point = "privacy_pv"
        correct_point = "privacy_pv => {"
        self.PolicyPage.first_start_android()
        self.clear_command()
        self.PolicyPage.close_information_page()
        self.sleep_time(4)
        self.write_contrast2(point)
        self.assert_result(point, correct_point)
        return self

    def test5_privacy_click(self):
        """
        同意隐私政策	玩家在隐私弹窗页面点击同意
        :return:
        """

        point = "privacy_click"
        correct_point = "privacy_click => {"
        self.PolicyPage.close_log()
        self.clear_command()
        self.PolicyPage.goto_guidance()
        self.write_contrast2(point)
        self.assert_result(point, correct_point)
        return self

    def test6_settings_pv(self):
        """

        设置弹窗展示	设置弹窗展示时上报
        settings_scene:game
        :return:
        """
        point = "settings_pv"
        correct_point = "settings_pv => {settings_scene:game,"
        self.NewGuidance.first_guidance_step1().first_guidance_step2()
        self.GamePage.game_victory()
        self.NewGuidance.completed_level2()
        self.GamePage.game_victory()
        self.clear_command()
        self.GamePage.goto_setting_page()
        self.write_contrast2(point)
        self.assert_result(point, correct_point)
        return self

    def test7_settings_music(self):
        """
        打开/关闭音乐	设置弹窗点击音乐开关时上报
        result:off
        :return:
        """
        point = "settings_music"
        correct_point = "settings_music => {result:off,"
        self.clear_command()
        self.GamePage.click_music()
        self.sleep_time()
        self.write_contrast2(point)
        self.assert_result(point, correct_point)
        return self

    def test8_settings_music(self):
        """
       打开/关闭音乐	设置弹窗点击音乐开关时上报
       result:on
       :return:
       """
        point = "settings_music"
        correct_point = "settings_music => {result:on,"
        self.clear_command()
        self.GamePage.click_music()
        self.sleep_time()
        self.write_contrast2(point)
        self.assert_result(point, correct_point)
        return self

    def test9_settings_sound(self):
        """
        打开/关闭音效	设置弹窗点击音效开关时上报
        result:off
        :return:
        """
        point = "settings_sound"
        correct_point = "settings_sound => {result:off,"
        self.clear_command()
        self.GamePage.click_sound()
        self.write_contrast2(point)
        self.assert_result(point, correct_point)
        return self

    def test10_settings_sound(self):
        """
        打开/关闭音效	设置弹窗点击音效开关时上报
        result:on
        :return:
        """
        point = "settings_sound"
        correct_point = "settings_sound => {result:on,"
        self.clear_command()
        self.GamePage.click_sound()
        self.write_contrast2(point)
        self.assert_result(point, correct_point)
        return self

    def test11_settings_vibration(self):
        """
        打开/关闭振动	设置弹窗点击振动开关时上报
        result:off
        :return:
        """
        point = "settings_vibration"
        correct_point = "settings_vibration => {result:off,"
        self.clear_command()
        self.GamePage.click_vibration()
        self.write_contrast2(point)
        self.assert_result(point, correct_point)
        return self

    def test12_settings_vibration(self):
        """
        打开/关闭振动	设置弹窗点击振动开关时上报
        result:on
        :return:
        """
        point = "settings_vibration"
        correct_point = "settings_vibration => {result:on,"
        self.clear_command()
        self.GamePage.click_vibration()
        self.write_contrast2(point)
        self.assert_result(point, correct_point)
        return self

    def test13_settings_tops(self):
        """
        打开/关闭瓶盖	设置弹窗点击瓶盖开关时上报
        result:off
        :return:
        """
        point = "settings_tops"
        correct_point = "settings_tops => {result:off,"
        self.clear_command()
        self.GamePage.click_tops()
        self.write_contrast2(point)
        self.assert_result(point, correct_point)
        return self

    def test14_settings_tops(self):
        """
        打开/关闭瓶盖	设置弹窗点击瓶盖开关时上报
        result:on
        :return:
        """
        point = "settings_tops"
        correct_point = "settings_tops => {result:on,"
        self.clear_command()
        self.GamePage.click_tops()
        self.write_contrast2(point)
        self.assert_result(point, correct_point)
        return self

    def test15_settings_language(self):
        """
        语言选择	设置弹窗修改语言时上报
        :return:
        """
        point = "settings_language"
        correct_point = "settings_language => {language_before:en,language_after:fr,"
        self.clear_command()
        self.GamePage.poco_goto_language().poco_change_french()
        self.assert_result(point, correct_point)
        self.write_contrast2(point)
        return self

    def test16_settings_contact(self):
        """
        联系我们	设置弹窗点击contact时上报
        :return:
        """
        point = "settings_contact"
        correct_point = "settings_contact => {"
        self.GamePage.language_setting_close()
        self.clear_command()
        self.GamePage.poco_goto_contact()
        self.assert_result(point, correct_point)
        self.write_contrast2(point)
        return self

    def test17_settings_pv(self):
        """
        设置弹窗展示	设置弹窗展示时上报

        :return:
        """
        point = "settings_pv"
        correct_point = "settings_pv => {settings_scene:home,"
        self.stop_app(self.water_sort_android)
        self.start_app(self.water_sort_android)
        self.PolicyPage.close_log()
        self.sleep_time(4)
        self.GameHome.christmas_activities_start()
        self.clear_command()
        self.GamePage.goto_setting_page()
        self.assert_result(point, correct_point)
        self.write_contrast2(point)
        return self

    def test18_collection_pv(self):
        """
        收藏界面展示	收藏界面展示时上报
        collection_scene：home
        :return:
        """
        point = "collection_pv"
        correct_point = "collection_pv => {collection_scene:home,"
        self.clear_command()
        self.GamePage.goto_collection_page()
        self.write_contrast2(point)
        self.assert_result(point, correct_point)
        return self

    def test19_collection_pv(self):
        """
        收藏界面展示	收藏界面展示时上报
        collection_scene：game
        :return:
        """
        point = "collection_pv"
        correct_point = "collection_pv => {collection_scene:game,"
        self.GamePage.collect_back_setting().setting_close()
        self.GameHome.goto_game_page()
        self.GamePage.goto_setting_page()
        self.clear_command()
        self.GamePage.goto_collection_page()
        self.write_contrast2(point)
        self.assert_result(point, correct_point)
        return self

    @pytest.mark.flaky(reruns=3)
    def test20_collection_tube(self):
        """
        更换瓶子	点击更换瓶子时上报
        :return:
        """
        point = "collection_tube"
        correct_point = "collection_tube => {tube_before:1,tube_after:2,"
        self.stop_app(self.water_sort_android)
        self.start_app(self.water_sort_android)
        self.PolicyPage.close_log()
        self.sleep_time(3)
        self.GameHome.get_debug().get_level("30").goto_game_page()
        self.GamePage.close_debug().goto_setting_page().goto_collection_page()
        self.clear_command()
        self.CollectPage.change_skin()
        self.write_contrast2(point)
        self.assert_result(point, correct_point)
        return self

    def test21_collection_theme(self):
        """
        更换背景	点击更换背景时上报
        :return:
        """
        point = "collection_theme"
        correct_point = "collection_theme => {theme_before:1,theme_after:2,"
        self.CollectPage.change_theme()
        self.clear_command()
        self.CollectPage.change_skin()
        self.write_contrast2(point)
        self.assert_result(point, correct_point)
        return self

    def get_rate_score(self):
        """
        到达评分引导页面
        :return:
        """
        self.PolicyPage.android_automate_process()
        self.NewGuidance.first_guidance_step1().first_guidance_step2()
        self.GamePage.game_victory()
        self.NewGuidance.completed_level2()
        self.GamePage.game_victory()
        self.GamePage.game_back_home()
        self.sleep_time()
        self.GameHome.christmas_activities_start().get_debug().goto_game_page()
        for i in range(4):
            self.GamePage.debug_doone()
        return self

    def test22_rate_score(self):
        """
        评分反馈	好评弹窗点击反馈和关闭按钮上报
        score：0
        :return:
        """
        point = "rate_score"
        correct_point = "rate_score => {score:0,"
        self.get_rate_score()
        self.clear_command()
        self.GamePage.language_setting_close()
        self.write_contrast2(point)
        self.assert_result(point, correct_point)
        return self

    @pytest.mark.flaky(reruns=3)
    def test23_rate_score(self):
        """
        评分反馈	好评弹窗点击反馈和关闭按钮上报
        score：1
        :return:
        """
        point = "rate_score"
        correct_point = "rate_score => {score:1,"
        self.get_rate_score()
        self.GamePage.rate_us_one_star()
        self.clear_command()
        self.GamePage.rate_us_feedback()
        self.write_contrast2(point)
        self.assert_result(point, correct_point)
        return self

    def test24_rate_score(self):
        """
        评分反馈	好评弹窗点击反馈和关闭按钮上报
        score：5
        :return:
        """
        point = "rate_score"
        correct_point = "rate_score => {score:5,"
        self.get_rate_score()
        self.GamePage.rate_us_five_star()
        self.clear_command()
        self.GamePage.rate_us_feedback()
        self.write_contrast2(point)
        self.assert_result(point, correct_point)
        return self

    @pytest.mark.flaky(reruns=3)
    def get_levelchest(self, level):
        """
        到达开宝箱页面
        :return:
        """
        self.get_rate_score()
        self.GamePage.language_setting_close().game_victory()
        self.GamePage.close_debug().game_back_home()
        self.GameHome.expand_debug().get_level(level).goto_game_page()
        self.GamePage.debug_win()
        self.sleep_time(15)
        return self

    @pytest.mark.flaky(reruns=3)
    def test25_levelchest_show(self):
        """
        章节宝箱	章节宝箱出现，点击关闭
        close_choice:0：直接关闭
        :return:
        """
        point = "levelchest_show"
        correct_point = "levelchest_show => {close_choice:0,levelid:9,"
        self.get_levelchest("9")
        for i in range(2):
            self.GamePage.debug_doone()
        self.GamePage.ad_close()
        self.sleep_time(6)
        self.clear_command()
        self.GamePage.unlock_no_thanks()
        self.write_contrast2(point)
        self.assert_result(point, correct_point)
        return self

    @pytest.mark.flaky(reruns=3)
    def test26_levelchest_show(self):
        """
        章节宝箱	章节宝箱出现，点击关闭
        close_choice:1：观看激励后关闭
        :return:
        """
        point = "levelchest_show"
        correct_point = "levelchest_show => {close_choice:1,levelid:17,"
        self.get_levelchest("17")
        for i in range(2):
            self.GamePage.debug_doone()
        self.GamePage.ad_close()
        self.sleep_time(6)
        self.GamePage.unlock_button_ad()
        self.clear_command()
        self.GamePage.ad_close()
        self.sleep_time(4)
        self.write_contrast2(point)
        self.assert_result(point, correct_point)
        return self

    @pytest.mark.flaky(reruns=3)
    def test29_coin_increase(self):
        """
        金币增加	金币数量增加时上报
        increase_scene:reward
        :return:
        """
        point = "coin_increase"
        correct_point = "coin_increase => {increase_num:100,increase_scene:reward,"
        self.stop_app(self.water_sort_android)
        self.start_app(self.water_sort_android)
        self.sleep_time(4)
        self.PolicyPage.close_log()
        self.GameHome.get_coin().ad_get_coins()
        self.clear_command()
        self.GamePage.ad_close()
        self.sleep_time()
        self.write_contrast2(point)
        self.assert_result(point, correct_point)
        return self

    # @pytest.mark.flaky(reruns=3)
    # def test30_coin_increase(self):
    #     """
    #     金币增加	金币数量增加时上报
    #     increase_scene:activity
    #     :return:
    #     """
    #     point = "coin_increase"
    #     correct_point = "coin_increase => {increase_num:50,increase_scene:activity,"
    #     self.get_rate_score()
    #     self.GamePage.language_setting_close().game_victory().close_debug().game_back_home()
    #     self.GameHome.expand_debug().get_level("5").goto_game_page()
    #     self.clear_command()
    #     self.GamePage.debug_win().debug_doone().debug_doone()
    #     self.GamePage.ad_close()
    #     self.sleep_time(5)
    #     self.write_contrast2(point)
    #     self.assert_result(point, correct_point)
    #     return self

    @pytest.mark.flaky(reruns=3)
    def test31_coin_increase(self):
        """
        金币增加	金币数量增加时上报
        increase_scene:chapter
        :return:
        """
        point = "coin_increase"
        correct_point = "coin_increase => {increase_num:20,increase_scene:chapter,"
        self.stop_app(self.water_sort_android)
        self.start_app(self.water_sort_android)
        self.PolicyPage.close_log()
        self.sleep_time(4)
        self.GameHome.get_debug().get_level("9").goto_game_page()
        self.clear_command()
        self.GamePage.debug_win().debug_doone().debug_doone().ad_close()
        self.sleep_time(4)
        self.write_contrast2(point)
        self.assert_result(point, correct_point)
        return self

    @pytest.mark.flaky(reruns=3)
    def test32_coin_decrease(self):
        """
        金币减少	金币数量减少时上报
        decrease_num
        decrease_scene
        :return:
        """
        point = "coin_decrease"
        correct_point = "coin_decrease => {decrease_num:600,decrease_scene:theme,"
        self.PolicyPage.android_automate_process()
        self.NewGuidance.first_guidance_step1().first_guidance_step2()
        self.GamePage.game_victory()
        self.NewGuidance.completed_level2()
        self.GamePage.game_victory()
        self.GamePage.game_back_home()
        self.sleep_time()
        self.GameHome.christmas_activities_start()
        self.sleep_time(4)
        self.GameHome.get_debug().debug_get_coin("700")
        self.GamePage.close_debug().goto_setting_page().goto_collection_page()
        self.CollectPage.change_theme().swipe_bottom()
        self.clear_command()
        self.CollectPage.purchase_theme()
        self.write_contrast2(point)
        self.assert_result(point, correct_point)

    def test28_backpop_show(self):
        """
        回归弹窗展示	用户展示回归弹窗时上报
        :return:
        """
        point = "backpop_show"
        correct_point = "backpop_show => {"
        self.stop_app(self.water_sort_android)
        self.AdjustTime.all_change_date()
        self.clear_command()
        self.start_app(self.water_sort_android)
        self.sleep_time(4)
        self.write_contrast2(point)
        self.assert_result(point, correct_point)
        return self

