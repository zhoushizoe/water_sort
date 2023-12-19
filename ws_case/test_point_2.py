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
        self.PolicyPage = PolicyPage(self.poco)
        self.NewGuidance = NewGuidance(self.poco)
        self.GamePage = GamePage(self.poco)
        self.GameHome = GameHome(self.poco)
        self.CollectPage = CollectPage(self.poco)
        self.AdjustTime = AdjustTime()

    def test33_game_new_start(self):
        """
        开局	玩家开始新的一局时上报
        activity_id
        activity_name：classic
        levelid
        rank_lid
        scene:"new：该关卡第一次开局
        :return:
        """
        point = "game_new_start"
        self.PolicyPage.first_start_android().close_information_page()
        self.PolicyPage.close_log().goto_guidance()
        self.NewGuidance.first_guidance_step1().first_guidance_step2()
        self.GamePage.game_victory()
        self.NewGuidance.completed_level2()
        self.clear_command()
        self.GamePage.game_victory()
        self.write_contrast2(point)
        return self

    def test34_game_new_start(self):
        """
        开局	玩家开始新的一局时上报
        scene:item：使用重开道具开局
        :return:
        """
        point = "game_new_start"
        self.clear_command()
        self.GamePage.tool_restart_click()
        self.write_contrast2(point)
        return self

    def test35_game_continue(self):
        """
        继续游玩	玩家继续残局游玩时上报
        :return:
        """
        point = "game_continue"
        self.GamePage.game_back_home()
        self.clear_command()
        self.GameHome.goto_game_page()
        self.write_contrast2(point)
        return self

    def test36_item_action(self):
        """
        道具操作	玩家发生道具使用时上报
        action_type:4：提示。使用提示道具
        :return:
        """
        point = "item_action"
        self.GamePage.tool_doone_click().ad_close()
        self.clear_command()
        self.GamePage.tool_doone_click()
        self.write_contrast2(point)
        return self

    @pytest.mark.flaky(reruns=3)
    def test37_item_action(self):
        """
        道具操作	玩家发生道具使用时上报
        action_type:2：撤回。使用撤回道具；
        :return:
        """
        point = "item_action"
        first_tube = [201, 1405]
        four_tube = [1174, 1460]
        self.PolicyPage.android_automate_process()
        self.NewGuidance.first_guidance_step1().first_guidance_step2()
        self.GamePage.game_victory()
        self.NewGuidance.completed_level2()
        self.GamePage.game_victory()
        self.image_click(first_tube).image_click(four_tube)
        self.GamePage.click_withdraw_tool().ad_close()
        self.clear_command()
        self.GamePage.click_withdraw_tool()
        self.write_contrast2(point)
        return self

    @pytest.mark.flaky(reruns=3)
    def test38_item_aciton(self):
        """
       道具操作	玩家发生道具使用时上报
       action_type:1：加瓶。使用加瓶道具；
       :return:
       """
        point = "item_action"
        self.stop_app(self.water_sort_android)
        self.start_app(self.water_sort_android)
        self.GameHome.goto_game_page()
        self.GamePage.tool_add_tube_click().ad_close()
        self.clear_command()
        self.GamePage.tool_add_tube_click()
        self.write_contrast2(point)
        return self

    def test39_item_aciton(self):
        """
        道具操作	玩家发生道具使用时上报
       action_type:3：重开。点击重开按钮，重开次数+1
       :return:
        """
        point = "item_action"
        self.clear_command()
        self.GamePage.tool_restart_click()
        self.write_contrast2(point)
        return self

    def test40_item_click(self):
        """
        道具点击	玩家点击道具button时上报
        1：加瓶。使用加瓶道具；
        :return:
        """
        point = "item_click"
        self.stop_app(self.water_sort_android)
        self.start_app(self.water_sort_android)
        self.GameHome.goto_game_page()
        self.clear_command()
        self.GamePage.tool_add_tube_click()
        self.write_contrast2(point)
        return self

    def test41_item_click(self):
        """
        道具点击	玩家点击道具button时上报
        2：撤回。使用撤回道具
        :return:
        """
        point = "item_click"
        self.stop_app(self.water_sort_android)
        self.start_app(self.water_sort_android)
        self.GameHome.goto_game_page()
        self.clear_command()
        self.GamePage.click_withdraw_tool()
        self.write_contrast2(point)
        return self

    def test42_item_click(self):
        """
        道具点击	玩家点击道具button时上报
        3：提示。使用提示道具
        :return:
        """
        point = "item_click"
        self.stop_app(self.water_sort_android)
        self.start_app(self.water_sort_android)
        self.GameHome.goto_game_page()
        self.clear_command()
        self.GamePage.tool_doone_click()
        self.write_contrast2(point)
        return self

    def test43_game_nomove(self):
        """
        无法移动	玩家操作触发无法移动提示时上报
        :return:
        """
        point = "game_nomove"
        self.stop_app(self.water_sort_android)
        self.start_app(self.water_sort_android)
        self.PolicyPage.close_log()
        self.GameHome.get_debug().get_level("160").goto_game_page()
        five_tube = [1076, 1091]
        ten_tube = [855, 1784]
        eleven_tube = [1081, 1818]
        twelve_tube = [1292, 1774]
        self.image_click(five_tube).image_click(eleven_tube)
        self.clear_command()
        self.image_click(ten_tube).image_click(twelve_tube)
        self.sleep_time()
        self.write_contrast2(point)
        return self

    def test44_game_win(self):
        """
        关卡胜利	关卡胜利时上报（插屏广告展示之前）
        :return:
        """
        point = "game_win"
        self.PolicyPage.first_start_android().close_information_page()
        self.PolicyPage.close_log().goto_guidance()
        self.NewGuidance.first_guidance_step1().first_guidance_step2()
        self.GamePage.game_victory()
        self.NewGuidance.completed_level2()
        self.GamePage.game_victory().game_back_home()
        self.GameHome.get_debug().goto_game_page()
        for i in range(4):
            self.GamePage.debug_doone()
        self.GamePage.language_setting_close().game_victory()
        self.sleep_time()
        self.GamePage.debug_win().debug_doone()
        self.clear_command()
        self.GamePage.debug_doone()
        self.sleep_time()
        self.write_contrast2(point)
        return self

    def test45_game_restart(self):
        """
        关卡重开	关卡重开时上报
        在关卡待十秒，返回首页
        :return:
        """
        point = "game_restart"
        self.stop_app(self.water_sort_android)
        self.start_app(self.water_sort_android)
        self.PolicyPage.close_log()
        self.GameHome.goto_game_page()
        self.sleep_time(10)
        self.GamePage.game_back_home()
        self.GameHome.get_debug().goto_game_page()
        self.GamePage.debug_doone().debug_doone().debug_doone()
        self.clear_command()
        self.GamePage.tool_restart_click()
        self.write_contrast2(point)
        return self

    def test46_game_restart(self):
        """
        关卡重开	关卡重开时上报
        在关卡待十秒，返回首页
        :return:
        """
        point = "game_restart"
        self.stop_app(self.water_sort_android)
        self.start_app(self.water_sort_android)
        self.PolicyPage.close_log()
        self.GameHome.goto_game_page()
        self.GamePage.tool_restart_click().ad_close()
        self.clear_command()
        self.sleep_time(10)
        self.GamePage.tool_restart_click()
        return self

    def test47_game_action(self):
        """
        游戏操作	玩家发生游玩操作时上报
        action_type:1：取消。点击相同瓶两次，选中后取消；
        :return:
        """
        first_tube = [201, 1405]
        four_tube = [1174, 1460]
        point = "game_action"
        self.PolicyPage.first_start_android().close_information_page()
        self.PolicyPage.close_log().goto_guidance()
        self.NewGuidance.first_guidance_step1().first_guidance_step2()
        self.GamePage.game_victory()
        self.NewGuidance.completed_level2()
        self.GamePage.game_victory()
        self.image_click(first_tube)
        self.clear_command()
        self.image_click(first_tube)
        self.write_contrast2(point)
        return self

    def test48_game_action(self):
        """
        游戏操作	玩家发生游玩操作时上报
        action_type:3：正确。发生倒水
        :return:
        """
        point = "game_action"
        first_tube = [201, 1405]
        four_tube = [1174, 1460]
        self.image_click(first_tube)
        self.clear_command()
        self.image_click(four_tube)
        self.write_contrast2(point)
        return self

    def test49_game_action(self):
        """
        游戏操作	玩家发生游玩操作时上报
        action_type:2：错误。选中瓶子A后，点击不可倒水的瓶子B，瓶子A被弹回；
        :return:
        """
        self.test48_game_action()
        return self

    @pytest.mark.flaky(reruns=3)
    def test50_max_start_level(self):

        """
        游戏操作	玩家发生游玩操作时上报
        action_type:1：取消。点击相同瓶两次，选中后取消；
        :return:
        """
        point = "max_start_level"
        self.PolicyPage.first_start_android().close_information_page()
        self.PolicyPage.close_log().goto_guidance()
        self.NewGuidance.first_guidance_step1().first_guidance_step2()
        self.GamePage.game_victory()
        self.NewGuidance.completed_level2()
        self.clear_command()
        self.GamePage.game_victory()
        self.write_contrast2_for_user(point)
        return self

    @pytest.mark.flaky(reruns=3)
    def test51_item_undo_num(self):
        """
        用户属性
        撤回道具持有数	道具数量变动时刷新
        增加
        :return:
        """
        point = "item_undo_num"
        self.PolicyPage.first_start_android().close_information_page()
        self.PolicyPage.close_log().goto_guidance()
        self.NewGuidance.first_guidance_step1().first_guidance_step2()
        self.GamePage.game_victory()
        self.NewGuidance.completed_level2()
        self.GamePage.game_victory()
        self.GamePage.click_withdraw_tool()
        self.clear_command()
        self.GamePage.ad_close()
        self.sleep_time()
        self.write_contrast2_for_user(point)
        return self

    @pytest.mark.flaky(reruns=3)
    def test52_item_undo_num(self):
        """
        用户属性
        撤回道具持有数	道具数量变动时刷新
        减少
        :return:
        """

        point = "item_undo_num"
        self.PolicyPage.first_start_android().close_information_page()
        self.PolicyPage.close_log().goto_guidance()
        self.NewGuidance.first_guidance_step1().first_guidance_step2()
        self.GamePage.game_victory()
        self.NewGuidance.completed_level2()
        self.GamePage.game_victory()
        first_tube = [201, 1405]
        four_tube = [1174, 1460]
        self.image_click(first_tube).image_click(four_tube)
        self.GamePage.click_withdraw_tool().ad_close()
        self.clear_command()
        self.GamePage.click_withdraw_tool()
        self.write_contrast2_for_user(point)
        return self

    @pytest.mark.flaky(reruns=3)
    def test53_item_tube_num(self):
        """
        用户属性
        加水瓶道具持有数	道具数量变动时刷新
        增加
        :return:
        """
        point = "item_tube_num"
        self.PolicyPage.first_start_android().close_information_page()
        self.PolicyPage.close_log().goto_guidance()
        self.NewGuidance.first_guidance_step1().first_guidance_step2()
        self.GamePage.game_victory()
        self.NewGuidance.completed_level2()
        self.GamePage.game_victory()
        self.GamePage.tool_add_tube_click()
        self.clear_command()
        self.GamePage.ad_close()
        self.sleep_time()
        self.write_contrast2_for_user(point)
        return self

    @pytest.mark.flaky(reruns=3)
    def test54_item_tube_num(self):
        """
        用户属性
        加水瓶道具持有数	道具数量变动时刷新
        减少
        :return:
        """
        point = "item_tube_num"
        self.clear_command()
        self.GamePage.tool_add_tube_click()
        self.write_contrast2_for_user(point)
        return self

    def test55_iap_times(self):
        """
        用户内购次数	用户成功内购时
        :return:
        """
        point = "iap_times"
        self.stop_app(self.water_sort_android)
        self.start_app(self.water_sort_android)
        self.GameHome.goto_ads_page()
        # self.clear_command()
        self.GameHome.purchase_click()
        self.write_contrast2_for_user(point)
        return self

    @pytest.mark.flaky(reruns=3)
    def test56_iap_totalvalue(self):
        """
        用户内购总价值（单位为美元）	用户成功内购时
        :return:
        """
        point = "iap_totalvalue"
        self.PolicyPage.first_start_android().close_information_page()
        self.PolicyPage.close_log().goto_guidance()
        self.NewGuidance.first_guidance_step1().first_guidance_step2()
        self.GamePage.game_victory()
        self.NewGuidance.completed_level2()
        self.GamePage.game_victory().game_back_home()
        self.GameHome.christmas_activities_start().goto_ads_page()
        self.clear_command()
        self.GameHome.purchase_click()
        self.write_contrast2_for_user(point)
        return self

    @pytest.mark.flaky(reruns=3)
    def test57_coin_hold_num(self):
        """
        当前金币持有数	金币数量发生变动时
        增加金币
        :return:
        """
        point = "coin_hold_num"
        self.stop_app(self.water_sort_android)
        self.start_app(self.water_sort_android)
        self.PolicyPage.close_log()
        self.GameHome.get_coin().ad_get_coins()
        self.clear_command()
        self.GamePage.ad_close()
        self.sleep_time()
        self.write_contrast2_for_user(point)
        return self

    @pytest.mark.flaky(reruns=3)
    def test58_coin_hold_num(self):
        """
        当前金币持有数	金币数量发生变动时
        减少
        :return:
        """
        point = "coin_hold_num"
        self.stop_app(self.water_sort_android)
        self.start_app(self.water_sort_android)
        self.PolicyPage.close_log()
        self.GameHome.get_debug().debug_get_coin("700")
        self.GamePage.close_debug().goto_setting_page().goto_collection_page()
        self.CollectPage.change_theme().swipe_bottom()
        self.clear_command()
        self.CollectPage.purchase_theme()
        self.write_contrast2_for_user(point)
        return self

    def test59_coin_cost_num(self):
        """
        累计消耗金币数	金币数量减少时
        :return:
        """
        point = "coin_cost_num"
        self.stop_app(self.water_sort_android)
        self.start_app(self.water_sort_android)
        self.PolicyPage.close_log()
        self.GameHome.get_debug().debug_get_coin("1500")
        self.GamePage.close_debug().goto_setting_page().goto_collection_page()
        self.CollectPage.change_theme().swipe_bottom()
        self.clear_command()
        self.CollectPage.purchase_theme_1500()
        self.write_contrast2_for_user(point)
        return self



