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
from ws_page.activity_page import ActivityPage


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
        self.ActivityPage = ActivityPage()

    def get_point_time(self, point, about_time_key):
        result = self.get_correct_log(point)
        print(f"正确的埋点为：{result}")
        last_time_start = result.find(f"{about_time_key}") + len(f"{about_time_key}")
        last_time_end = result.find(",", last_time_start)
        last_time = float(result[last_time_start:last_time_end])
        print(last_time)
        return last_time

    def extract_string_point(self, correct_point, about_time_key):
        """
        正确的埋点的除去时间部分
        :param about_time_key:
        :param correct_point:
        :return:
        """
        last_time_start = correct_point.find(f"{about_time_key}") + len(f"{about_time_key}")
        last_time_end = correct_point.find(",", last_time_start)
        extract_string = correct_point[:last_time_start] + correct_point[last_time_end:]
        print(extract_string)
        return extract_string

    def get_point_extract_string(self, point, about_time_key):
        """
        得到的埋点的除去时间部分
        :param point:
        :param about_time_key:
        :return:
        """
        result = self.get_correct_log(point)
        print(f"正确的埋点为：{result}")
        last_time_start = result.find(f"{about_time_key}") + len(f"{about_time_key}")
        last_time_end = result.find(",", last_time_start)
        extract_string = result[:last_time_start] + result[last_time_end:]
        print(extract_string)
        return extract_string

    def assert_result(self, point, correct_point):
        result = self.get_correct_log(point)
        print(f"正确的埋点为：{result}")
        assert result == correct_point

    def assert_result_user(self, point, correct_point):
        self.GetPointUser = GetPointUser()
        result = self.GetPointUser.get_correct_log_user(point)
        print(f"正确的埋点为：{result}")
        assert result == correct_point

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
        correct_point = "game_new_start => {activity_name:classic,activity_id:0,levelid:3,rank_lid:3,scene:new,"
        self.PolicyPage.first_start_android().close_information_page()
        self.PolicyPage.close_log().goto_guidance()
        self.NewGuidance.first_guidance_step1().first_guidance_step2()
        self.GamePage.game_victory()
        self.NewGuidance.completed_level2()
        self.clear_command()
        self.GamePage.game_victory()
        self.write_contrast2(point)
        self.assert_result(point, correct_point)
        return self

    def test34_game_new_start(self):
        """
        开局	玩家开始新的一局时上报
        scene:item：使用重开道具开局
        :return:
        """
        point = "game_new_start"
        correct_point = "game_new_start => {activity_name:classic,activity_id:0,levelid:3,rank_lid:3,scene:item,"
        self.clear_command()
        self.GamePage.tool_restart_click()
        self.write_contrast2(point)
        self.assert_result(point, correct_point)
        return self

    def test35_game_continue(self):
        """
        继续游玩	玩家继续残局游玩时上报
        :return:
        """
        point = "game_continue"
        correct_point = "game_continue => {activity_name:classic,activity_id:0,levelid:3,restart_num:1,level_status:jjee,eeaa,aajj,****,"
        self.GamePage.game_back_home()
        self.clear_command()
        self.GameHome.goto_game_page()
        self.write_contrast2(point)
        self.assert_result(point, correct_point)
        return self

    def test36_item_action(self):
        """
        道具操作	玩家发生道具使用时上报
        action_type:4：提示。使用提示道具
        :return:
        """
        point = "item_action"
        correct_point = "item_action => {activity_name:classic,activity_id:0,levelid:3,action_type:4,restart_num:1,"
        self.GamePage.tool_doone_click().ad_close()
        self.clear_command()
        self.GamePage.tool_doone_click()
        self.write_contrast2(point)
        self.assert_result(point, correct_point)
        return self

    @pytest.mark.flaky(reruns=3)
    def test37_item_action(self):
        """
        道具操作	玩家发生道具使用时上报
        action_type:2：撤回。使用撤回道具；
        :return:
        """
        point = "item_action"
        correct_point = "item_action => {activity_name:classic,activity_id:0,levelid:3,action_type:2,restart_num:0,"
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
        self.assert_result(point, correct_point)
        return self

    @pytest.mark.flaky(reruns=3)
    def test38_item_aciton(self):
        """
       道具操作	玩家发生道具使用时上报
       action_type:1：加瓶。使用加瓶道具；
       :return:
       """
        point = "item_action"
        correct_point = "item_action => {activity_name:classic,activity_id:0,levelid:3,action_type:1,restart_num:0,"
        self.stop_app(self.water_sort_android)
        self.start_app(self.water_sort_android)
        self.GameHome.goto_game_page()
        self.GamePage.tool_add_tube_click().ad_close()
        self.clear_command()
        self.GamePage.tool_add_tube_click()
        self.write_contrast2(point)
        self.assert_result(point, correct_point)
        return self

    def test39_item_aciton(self):
        """
        道具操作	玩家发生道具使用时上报
       action_type:3：重开。点击重开按钮，重开次数+1
       :return:
        """
        point = "item_action"
        correct_point = "item_action => {activity_name:classic,activity_id:0,levelid:3,action_type:3,restart_num:0,"
        self.clear_command()
        self.GamePage.tool_restart_click()
        self.write_contrast2(point)
        self.assert_result(point, correct_point)
        return self

    def test40_item_click(self):
        """
        道具点击	玩家点击道具button时上报
        1：加瓶。使用加瓶道具；
        :return:
        """
        point = "item_click"
        correct_point = "item_click => {activity_name:classic,activity_id:0,levelid:3,action_type:1,"
        self.stop_app(self.water_sort_android)
        self.start_app(self.water_sort_android)
        self.GameHome.goto_game_page()
        self.clear_command()
        self.GamePage.tool_add_tube_click()
        self.write_contrast2(point)
        self.assert_result(point, correct_point)
        return self

    def test41_item_click(self):
        """
        道具点击	玩家点击道具button时上报
        2：撤回。使用撤回道具
        :return:
        """
        point = "item_click"
        correct_point = "item_click => {activity_name:classic,activity_id:0,levelid:3,action_type:2,"
        self.stop_app(self.water_sort_android)
        self.start_app(self.water_sort_android)
        self.GameHome.goto_game_page()
        self.clear_command()
        self.GamePage.click_withdraw_tool()
        self.write_contrast2(point)
        self.assert_result(point, correct_point)
        return self

    def test42_item_click(self):
        """
        道具点击	玩家点击道具button时上报
        3：提示。使用提示道具
        :return:
        """
        point = "item_click"
        correct_point = "item_click => {activity_name:classic,activity_id:0,levelid:3,action_type:4,"
        self.stop_app(self.water_sort_android)
        self.start_app(self.water_sort_android)
        self.GameHome.goto_game_page()
        self.clear_command()
        self.GamePage.tool_doone_click()
        self.write_contrast2(point)
        self.assert_result(point, correct_point)
        return self

    def test43_game_nomove(self):
        """
        无法移动	玩家操作触发无法移动提示时上报
        :return:
        """
        point = "game_nomove"
        correct_point = "game_nomove => {activity_name:classic,activity_id:0,levelid:160,restart_num:0,level_move:2,"
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
        self.assert_result(point, correct_point)
        return self

    def test44_game_win(self):
        """
        关卡胜利	关卡胜利时上报（插屏广告展示之前）
        :return:
        """
        point = "game_win"
        correct_point = "game_win => {activity_name:classic,activity_id:0,levelid:4,restart_num:0,level_time:54.20,win_num:4,level_move:9,"
        about_time_key = "level_time:"
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
        self.GamePage.debug_win(20).debug_doone()
        self.clear_command()
        self.GamePage.debug_doone()
        self.sleep_time(4)
        self.write_contrast2(point)
        print("进入时间的判断")
        assert 53 <= self.get_point_time(point, about_time_key) <= 62
        print("时间判断成功")
        string1 = self.extract_string_point(correct_point, about_time_key)
        string2 = self.get_point_extract_string(point, about_time_key)
        if string1 == string2:
            assert True
        else:
            print("除去时间之外埋点不正确")
            assert False
        return self

    def test45_game_restart(self):
        """
        关卡重开	关卡重开时上报
        在关卡待十秒，返回首页
        :return:
        """
        point = "game_restart"
        correct_point = "game_restart => {activity_name:classic,activity_id:0,levelid:5,restart_num:0,level_time:30.83,level_move:3,"
        about_time_key = "level_time:"
        self.stop_app(self.water_sort_android)
        self.start_app(self.water_sort_android)
        self.PolicyPage.close_log()
        self.GameHome.goto_game_page()
        self.sleep_time(10)
        self.GamePage.game_back_home()
        self.GameHome.get_debug().goto_game_page()
        self.GamePage.debug_doone().debug_doone().debug_doone()
        self.clear_command()
        self.GamePage.close_debug().tool_restart_click()
        self.write_contrast2(point)
        print("进入时间的判断")
        assert 29 <= self.get_point_time(point, about_time_key) <= 46
        print("时间判断成功")
        string1 = self.extract_string_point(correct_point, about_time_key)
        string2 = self.get_point_extract_string(point, about_time_key)
        if string1 == string2:
            assert True
        else:
            print("除去时间之外埋点不正确")
            assert False
        return self

    def test46_game_restart(self):
        """
        关卡重开	关卡重开时上报
        在关卡待十秒，返回首页
        :return:
        """
        point = "game_restart"
        correct_point = "game_restart => {activity_name:classic,activity_id:0,levelid:5,restart_num:2,level_time:12,level_move:0,"
        about_time_key = "level_time:"
        self.stop_app(self.water_sort_android)
        self.start_app(self.water_sort_android)
        self.PolicyPage.close_log()
        self.GameHome.goto_game_page()
        self.GamePage.tool_restart_click().ad_close()
        self.clear_command()
        self.sleep_time(10)
        self.GamePage.tool_restart_click()
        self.write_contrast2(point)
        print("进入时间的判断")
        assert 10 <= self.get_point_time(point, about_time_key) <= 21
        print("时间判断成功")
        string1 = self.extract_string_point(correct_point, about_time_key)
        string2 = self.get_point_extract_string(point, about_time_key)
        if string1 == string2:
            assert True
        else:
            print("除去时间之外埋点不正确")
            assert False
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
        correct_point = "game_action => {activity_name:classic,activity_id:0,levelid:3,action_type:1,restart_num:0,pause_time:2.06,status_later:jjee,eeaa,aajj,****,"
        about_time_key = "pause_time:"
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
        print("进入时间的判断")
        assert 1 <= self.get_point_time(point, about_time_key) <= 4
        print("时间判断成功")
        string1 = self.extract_string_point(correct_point, about_time_key)
        string2 = self.get_point_extract_string(point, about_time_key)
        if string1 == string2:
            assert True
        else:
            print("除去时间之外埋点不正确")
            assert False
        return self

    def test48_game_action(self):
        """
        游戏操作	玩家发生游玩操作时上报
        action_type:3：正确。发生倒水
        :return:
        """
        point = "game_action"
        correct_point = "game_action => {activity_name:classic,activity_id:0,levelid:3,action_type:3,restart_num:0,pause_time:2.10,status_later:jj**,eeaa,aajj,ee**,"
        about_time_key = "pause_time:"
        first_tube = [201, 1405]
        four_tube = [1174, 1460]
        self.image_click(first_tube)
        self.clear_command()
        self.image_click(four_tube)
        self.write_contrast2(point)
        print("进入时间的判断")
        assert 1 <= self.get_point_time(point, about_time_key) <= 4
        print("时间判断成功")
        string1 = self.extract_string_point(correct_point, about_time_key)
        string2 = self.get_point_extract_string(point, about_time_key)
        if string1 == string2:
            assert True
        else:
            print("除去时间之外埋点不正确")
            assert False
        return self

    def test49_game_action(self):
        """
        游戏操作	玩家发生游玩操作时上报
        action_type:2：错误。选中瓶子A后，点击不可倒水的瓶子B，瓶子A被弹回；
        :return:
        """
        point = "game_action"
        correct_point = "game_action => {activity_name:classic,activity_id:0,levelid:3,action_type:2,restart_num:0,pause_time:2.10,status_later:jj**,eeaa,aajj,ee**,"
        about_time_key = "pause_time:"
        first_tube = [201, 1405]
        four_tube = [1174, 1460]
        self.image_click(first_tube)
        self.clear_command()
        self.image_click(four_tube)
        self.write_contrast2(point)
        print("进入时间的判断")
        assert 1 <= self.get_point_time(point, about_time_key) <= 4
        print("时间判断成功")
        string1 = self.extract_string_point(correct_point, about_time_key)
        string2 = self.get_point_extract_string(point, about_time_key)
        if string1 == string2:
            assert True
        else:
            print("除去时间之外埋点不正确")
            assert False
        return self

    @pytest.mark.flaky(reruns=3)
    def test50_max_start_level(self):

        """
        游戏操作	玩家发生游玩操作时上报
        action_type:1：取消。点击相同瓶两次，选中后取消；
        :return:
        """
        point = "max_start_level"
        correct_point = "max_start_level => 3"
        self.PolicyPage.first_start_android().close_information_page()
        self.PolicyPage.close_log().goto_guidance()
        self.NewGuidance.first_guidance_step1().first_guidance_step2()
        self.GamePage.game_victory()
        self.NewGuidance.completed_level2()
        self.clear_command()
        self.GamePage.game_victory()
        self.write_contrast2_for_user(point)
        self.assert_result_user(point, correct_point)
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
        correct_point = "item_undo_num => 3"
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
        self.assert_result_user(point, correct_point)
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
        correct_point = "item_undo_num => 3"
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
        self.assert_result_user(point, correct_point)
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
        correct_point = "item_tube_num => 1"
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
        self.assert_result_user(point, correct_point)
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
        correct_point = "item_tube_num => 0"
        self.clear_command()
        self.GamePage.tool_add_tube_click()
        self.write_contrast2_for_user(point)
        self.assert_result_user(point, correct_point)
        return self

    def test55_iap_times(self):
        """
        用户内购次数	用户成功内购时
        :return:
        """
        point = "iap_times"
        correct_point = "iap_times => 1"
        self.stop_app(self.water_sort_android)
        self.start_app(self.water_sort_android)
        self.GameHome.goto_ads_page().purchase_ads()
        # self.clear_command()
        self.GameHome.purchase_click()
        self.write_contrast2_for_user(point)
        self.assert_result_user(point, correct_point)
        return self

    @pytest.mark.flaky(reruns=3)
    def test56_iap_totalvalue(self):
        """
        用户内购总价值（单位为美元）	用户成功内购时
        :return:
        """
        point = "iap_totalvalue"
        correct_point = "iap_totalvalue => 4.99"
        self.PolicyPage.first_start_android().close_information_page()
        self.PolicyPage.close_log().goto_guidance()
        self.NewGuidance.first_guidance_step1().first_guidance_step2()
        self.GamePage.game_victory()
        self.NewGuidance.completed_level2()
        self.GamePage.game_victory().game_back_home()
        self.GameHome.christmas_activities_start().goto_ads_page().purchase_ads()
        self.clear_command()
        self.GameHome.purchase_click()
        self.write_contrast2_for_user(point)
        self.assert_result_user(point, correct_point)
        return self

    @pytest.mark.flaky(reruns=3)
    def test57_coin_hold_num(self):
        """
        当前金币持有数	金币数量发生变动时
        增加金币
        :return:
        """
        point = "coin_hold_num"
        correct_point = "coin_hold_num => 100"
        self.stop_app(self.water_sort_android)
        self.start_app(self.water_sort_android)
        self.PolicyPage.close_log()
        self.GameHome.get_coin().ad_get_coins()
        self.clear_command()
        self.GamePage.ad_close()
        self.sleep_time()
        self.write_contrast2_for_user(point)
        self.assert_result_user(point, correct_point)
        return self

    @pytest.mark.flaky(reruns=3)
    def test58_coin_hold_num(self):
        """
        当前金币持有数	金币数量发生变动时
        减少
        :return:
        """
        point = "coin_hold_num"
        correct_point = "coin_hold_num => 100"
        self.stop_app(self.water_sort_android)
        self.start_app(self.water_sort_android)
        self.PolicyPage.close_log()
        self.GameHome.get_debug().debug_get_coin("700")
        self.GamePage.close_debug().goto_setting_page().goto_collection_page()
        self.CollectPage.change_theme().swipe_bottom()
        self.clear_command()
        self.CollectPage.purchase_theme()
        self.write_contrast2_for_user(point)
        self.assert_result_user(point, correct_point)
        return self

    def test59_coin_cost_num(self):
        """
        累计消耗金币数	金币数量减少时
        :return:
        """
        point = "coin_cost_num"
        correct_point = "coin_cost_num => 2100"
        self.stop_app(self.water_sort_android)
        self.start_app(self.water_sort_android)
        self.PolicyPage.close_log()
        self.GameHome.get_debug().debug_get_coin("1500")
        self.GamePage.close_debug().goto_setting_page().goto_collection_page()
        self.CollectPage.change_theme().swipe_bottom()
        self.clear_command()
        self.CollectPage.purchase_theme_1500()
        self.write_contrast2_for_user(point)
        self.assert_result_user(point, correct_point)
        return self

    def test61_game_skip(self):
        """
        跳过关卡	玩家点击三次重开后触发跳过关卡按钮，并点击
        :return:
        """
        point = "game_skip"
        correct_point = "game_skip => {activity_name:classic,activity_id:0,levelid:3,rank_lid:3,restart_num:3,"
        self.PolicyPage.first_start_android().close_information_page()
        self.PolicyPage.close_log().goto_guidance()
        self.NewGuidance.first_guidance_step1().first_guidance_step2()
        self.GamePage.game_victory()
        self.NewGuidance.completed_level2()
        self.GamePage.game_victory()
        first_tube = [201, 1405]
        four_tube = [1174, 1460]
        for i in range(3):
            self.image_click(first_tube).image_click(four_tube)
            self.GamePage.tool_restart_click()
        self.clear_command()
        self.GamePage.game_skip()
        self.write_contrast2(point)
        self.assert_result(point, correct_point)
        return self

    def test27_iap_purchase_success(self):
        """
        购买成功 	公共库事件
        :return:
        """
        point = "iap_purchase_success"
        correct_point = "iap_purchase_success => {store:debug,scene:home,product_id:remove_ads,order_id:null,transaction_id:f3dfc93c-806d-410d-bc4d-44151b3a0e17,price:4.98999977111816,currency:USD,"
        about_time_key = "transaction_id:"
        self.stop_app(self.water_sort_android)
        self.start_app(self.water_sort_android)
        self.PolicyPage.close_log()
        self.sleep_time()
        self.GameHome.goto_ads_page()
        self.clear_command()
        self.sleep_time()
        self.GameHome.purchase_ads().purchase_click()
        self.sleep_time()
        self.write_contrast2(point)
        string1 = self.extract_string_point(correct_point, about_time_key)
        string2 = self.get_point_extract_string(point, about_time_key)
        if string1 == string2:
            assert True
        else:
            print("除去时间之外埋点不正确")
            assert False
        return self

    def test1_game_new_start_normal(self):
        """
        活动模式normal新开局
        :return:
        """
        point = "game_new_start"
        correct_point = "game_new_start => {activity_name:normal,activity_id:1,levelid:1,rank_lid:3,scene:new,"
        self.PolicyPage.first_start_android().close_information_page()
        self.PolicyPage.close_log().goto_guidance()
        self.NewGuidance.first_guidance_step1().first_guidance_step2()
        self.GamePage.game_victory()
        self.NewGuidance.completed_level2()
        self.GamePage.game_victory().game_back_home()
        self.GameHome.get_debug().get_level("100").debug_get_coin("999").goto_game_page()
        self.GamePage.close_debug().game_back_home()
        self.GameHome.activicity_page_go()
        self.ActivityPage.unlock_level(self.ActivityPage.level_1)
        self.clear_command()
        self.ActivityPage.unlock_level(self.ActivityPage.level_1)
        self.sleep_time(1)
        self.write_contrast2(point)
        self.assert_result(point, correct_point)
        return self

    def test2_game_new_start_hard(self):
        point = "game_new_start"
        correct_point = "game_new_start => {activity_name:hard,activity_id:2,levelid:1,rank_lid:15,scene:new,"
        level1 = self.ActivityPage.level_1
        level2 = self.ActivityPage.level_2
        level3 = self.ActivityPage.level_3
        level4 = self.ActivityPage.level_4
        level5 = self.ActivityPage.level_5
        level6 = self.ActivityPage.level_6
        level7 = self.ActivityPage.level_7
        level8 = self.ActivityPage.level_8
        level9 = self.ActivityPage.level_9
        level10 = self.ActivityPage.level_10
        level11 = self.ActivityPage.level_11
        level12 = self.ActivityPage.level_12
        self.GamePage.game_back_home()
        self.GameHome.expand_debug()
        self.ActivityPage.activity_victory(level1)
        self.ActivityPage.activity_victory(level2)
        self.ActivityPage.activity_victory(level3)
        self.ActivityPage.activity_victory(level4)
        self.ActivityPage.activity_victory(level5)
        self.ActivityPage.activity_victory(level6)
        self.ActivityPage.activity_victory(level7)
        self.ActivityPage.activity_victory(level8)
        self.ActivityPage.activity_victory(level9)
        self.ActivityPage.challenge_swipe()
        self.ActivityPage.activity_victory(level10)
        self.ActivityPage.activity_victory(level11)
        self.ActivityPage.activity_victory(level12)
        self.ActivityPage.goto_hard_page().unlock_level(level1)
        self.clear_command()
        self.ActivityPage.unlock_level(level1)
        self.sleep_time()
        self.write_contrast2(point)
        self.assert_result(point, correct_point)
        return self

    def test3_game_new_start_play_again(self):
        point = "game_new_start"
        correct_point = "game_new_start => {activity_name:hard,activity_id:2,levelid:1,rank_lid:16,scene:playagain,"
        level1 = self.ActivityPage.level_1
        self.GamePage.debug_win().debug_doone().debug_doone().ad_close()
        self.ActivityPage.activity_over_continue()
        self.ActivityPage.unlock_level(level1)
        self.GamePage.ad_close()
        self.clear_command()
        self.ActivityPage.unlock_level(level1)
        self.sleep_time(1)
        self.write_contrast2(point)
        self.assert_result(point, correct_point)
        return self

    def test4_game_continue_hard(self):
        point = "game_continue"
        correct_point = "game_continue => {activity_name:hard,activity_id:2,levelid:1,restart_num:0,level_status:lkc*,bcke,jgid,bage,licd,daik,gjgb,aiel,jald,beck,j***,****,"
        level1 = self.ActivityPage.level_1
        first_tube = [113, 1121]
        eleventh_tube = [1107, 1771]
        self.image_click(first_tube).image_click(eleventh_tube)
        self.GamePage.close_debug().game_back_home()
        self.clear_command()
        self.ActivityPage.unlock_level(level1)
        self.sleep_time(1)
        self.write_contrast2(point)
        self.assert_result(point, correct_point)
        return self

    def test5_game_win_hard(self):
        """
        关卡胜利	关卡胜利时上报（插屏广告展示之前）
        :return:
        """
        point = "game_win"
        correct_point = "game_win => {activity_name:hard,activity_id:2,levelid:1,restart_num:0,level_time:79,win_num:19,level_move:36,"
        about_time_key = "level_time:"
        self.GameHome.expand_debug()
        self.GamePage.debug_win().debug_doone()
        self.clear_command()
        self.GamePage.debug_doone()
        self.sleep_time(1)
        self.write_contrast2(point)
        print("进入时间的判断")
        assert 60 <= self.get_point_time(point, about_time_key) <= 85
        print("时间判断成功")
        string1 = self.extract_string_point(correct_point, about_time_key)
        string2 = self.get_point_extract_string(point, about_time_key)
        if string1 == string2:
            assert True
        else:
            print("除去时间之外埋点不正确")
            assert False
        return self

    def test6_game_restart_hard(self):
        point = "game_restart"
        correct_point = "game_restart => {activity_name:hard,activity_id:2,levelid:2,restart_num:0,level_time:9,level_move:1,"
        about_time_key = "level_time:"
        first_tube = [113, 1121]
        eleventh_tube = [1107, 1771]
        level2 = self.ActivityPage.level_2
        self.GamePage.ad_close()
        self.ActivityPage.activity_over_continue()
        self.ActivityPage.unlock_level(level2).unlock_level(level2)
        self.image_click(first_tube).image_click(eleventh_tube)
        self.clear_command()
        self.GamePage.close_debug().tool_restart_click()
        self.sleep_time(1)
        self.write_contrast2(point)
        print("进入时间的判断")
        assert 9 <= self.get_point_time(point, about_time_key) <= 14
        print("时间判断成功")
        string1 = self.extract_string_point(correct_point, about_time_key)
        string2 = self.get_point_extract_string(point, about_time_key)
        if string1 == string2:
            assert True
        else:
            print("除去时间之外埋点不正确")
            assert False
        return self

    def test7_game_action_hard(self):
        """
                游戏操作	玩家发生游玩操作时上报
                action_type:1：取消。点击相同瓶两次，选中后取消；
                :return:
                """
        first_tube = [113, 1121]
        four_tube = [1174, 1460]
        point = "game_action"
        correct_point = "game_action => {activity_name:hard,activity_id:2,levelid:2,action_type:1,restart_num:0,pause_time:1,status_later:fjdb,afie,bdli,lcfa,ceib,jcia,dfle,cjal,bedj,****,****,"
        about_time_key = "pause_time:"
        self.GamePage.ad_close()
        self.clear_command()
        self.image_click(first_tube).image_click(first_tube)
        self.write_contrast2(point)
        print("进入时间的判断")
        assert 1 <= self.get_point_time(point, about_time_key) <= 4
        print("时间判断成功")
        string1 = self.extract_string_point(correct_point, about_time_key)
        string2 = self.get_point_extract_string(point, about_time_key)
        if string1 == string2:
            assert True
        else:
            print("除去时间之外埋点不正确")
            assert False
        return self

    def test8_item_action_hard(self):
        """
        道具操作	玩家发生道具使用时上报
        action_type:4：提示。使用提示道具
        :return:
        """
        point = "item_action"
        correct_point = "item_action => {activity_name:hard,activity_id:2,levelid:2,action_type:4,restart_num:0,"
        self.GamePage.tool_doone_click().ad_close()
        self.clear_command()
        self.GamePage.tool_doone_click()
        self.write_contrast2(point)
        self.assert_result(point, correct_point)
        return self

    def test9_item_click_hard(self):
        point = "item_click"
        correct_point = "item_click => {activity_name:hard,activity_id:2,levelid:2,action_type:4,"
        self.clear_command()
        self.GamePage.tool_doone_click()
        self.write_contrast2(point)
        self.assert_result(point, correct_point)
        return self

    def test10_game_skip_hard(self):
        point = "game_skip"
        correct_point = "game_skip => {activity_name:hard,activity_id:2,levelid:2,rank_lid:17,restart_num:21,"
        first_tube = [113, 1121]
        eleventh_tube = [1107, 1771]
        self.GamePage.ad_close()
        self.GamePage.tool_restart_click().ad_close()
        self.image_click(first_tube).image_click(eleventh_tube)
        self.GamePage.tool_restart_click().ad_close()
        self.image_click(first_tube).image_click(eleventh_tube)
        self.GamePage.tool_restart_click().ad_close()
        self.GamePage.image_click(first_tube).image_click(eleventh_tube)
        self.GamePage.tool_restart_click().ad_close()
        self.clear_command()
        self.GamePage.game_skip().ad_close()
        self.sleep_time(1)
        self.write_contrast2(point)
        self.assert_result(point, correct_point)
        return self

    def test11_game_continue_normal(self):
        point = "game_continue"
        correct_point = "game_continue => {activity_name:normal,activity_id:1,levelid:1,restart_num:0,level_status:dej*,hjef,igcg,fabb,jhea,dcdd,feij,abac,ifgg,bihc,h***,****,"
        level1 = self.ActivityPage.level_1
        first_tube = [113, 1121]
        eleventh_tube = [1107, 1771]
        self.PolicyPage.first_start_android().close_information_page()
        self.PolicyPage.close_log().goto_guidance()
        self.NewGuidance.first_guidance_step1().first_guidance_step2()
        self.GamePage.game_victory()
        self.NewGuidance.completed_level2()
        self.GamePage.game_victory().game_back_home()
        self.GameHome.get_debug().get_level("100").debug_get_coin("999").goto_game_page()
        self.GamePage.close_debug().game_back_home()
        self.GameHome.activicity_page_go()
        self.ActivityPage.unlock_level(level1).unlock_level(level1)
        self.image_click(first_tube).image_click(eleventh_tube)
        self.GamePage.game_back_home()
        self.clear_command()
        self.ActivityPage.unlock_level(level1)
        self.sleep_time()
        self.write_contrast2(point)
        self.assert_result(point, correct_point)
        return self

    def test12_game_win_normal(self):
        point = "game_win"
        correct_point = "game_win => {activity_name:normal,activity_id:1,levelid:1,restart_num:0,level_time:107,win_num:3,level_move:35,"
        about_time_key = "level_time:"
        level1 = self.ActivityPage.level_1
        self.GameHome.expand_debug()
        self.GamePage.debug_win().debug_doone()
        self.clear_command()
        self.GamePage.debug_doone()
        self.sleep_time(1)
        self.write_contrast2(point)
        print("进入时间的判断")
        assert 60 <= self.get_point_time(point, about_time_key) <= 85
        print("时间判断成功")
        string1 = self.extract_string_point(correct_point, about_time_key)
        string2 = self.get_point_extract_string(point, about_time_key)
        if string1 == string2:
            assert True
        else:
            print("除去时间之外埋点不正确")
            assert False
        return self

    def test13_game_restart_normal(self):
        point = "game_restart"
        correct_point = "game_restart => {activity_name:normal,activity_id:1,levelid:2,restart_num:0,level_time:9,level_move:1,"
        about_time_key = "level_time:"
        first_tube = [113, 1121]
        eleventh_tube = [1107, 1771]
        level2 = self.ActivityPage.level_2
        self.GamePage.ad_close()
        self.ActivityPage.activity_over_continue()
        self.ActivityPage.unlock_level(level2).unlock_level(level2)
        self.image_click(first_tube).image_click(eleventh_tube)
        self.clear_command()
        self.GamePage.close_debug().tool_restart_click()
        self.sleep_time(1)
        self.write_contrast2(point)
        print("进入时间的判断")
        assert 8 <= self.get_point_time(point, about_time_key) <= 14
        print("时间判断成功")
        string1 = self.extract_string_point(correct_point, about_time_key)
        string2 = self.get_point_extract_string(point, about_time_key)
        if string1 == string2:
            assert True
        else:
            print("除去时间之外埋点不正确")
            assert False
        return self

    def test14_game_action_normal(self):
        self.GamePage.ad_close()
        first_tube = [164, 975]
        four_tube = [1248, 1922]
        point = "game_action"
        correct_point = "：game_action => {activity_name:normal,activity_id:1,levelid:2,action_type:3,restart_num:0,pause_time:1,status_later:iica,jgke,fkgk,jjcc,ddff,kihj,ddga,ceaa,ghee,ifhh,****,****,"
        about_time_key = "pause_time:"
        self.clear_command()
        self.sleep_time()
        self.image_click(first_tube).image_click(four_tube)
        self.write_contrast2(point)
        print("进入时间的判断")
        assert 1 <= self.get_point_time(point, about_time_key) <= 4
        print("时间判断成功")
        string1 = self.extract_string_point(correct_point, about_time_key)
        string2 = self.get_point_extract_string(point, about_time_key)
        if string1 == string2:
            assert True
        else:
            print("除去时间之外埋点不正确")
            assert False
        return self

    def test15_item_action_normal(self):
        point = "item_action"
        correct_point = "item_action => {activity_name:normal,activity_id:1,levelid:2,action_type:4,restart_num:0,"
        self.GamePage.tool_doone_click().ad_close()
        self.clear_command()
        self.GamePage.tool_doone_click()
        self.write_contrast2(point)
        self.assert_result(point, correct_point)
        return self

    def test16_item_click_normal(self):
        """
        道具点击	玩家点击道具button时上报
        1：加瓶。使用加瓶道具；
        :return:
        """
        point = "item_click"
        correct_point = "item_click => {activity_name:normal,activity_id:1,levelid:2,action_type:4,"
        self.clear_command()
        self.GamePage.tool_doone_click()
        self.write_contrast2(point)
        self.assert_result(point, correct_point)
        return self

    def test17_iap_purchase_success_banner(self):
        point = "iap_purchase_success"
        correct_point = "iap_purchase_success => {store:debug,scene:home,product_id:remove_ads,order_id:null,transaction_id:f3dfc93c-806d-410d-bc4d-44151b3a0e17,price:4.98999977111816,currency:USD,"
        about_time_key = "transaction_id:"
        self.stop_app(self.water_sort_android)
        self.start_app(self.water_sort_android)
        self.PolicyPage.close_log()
        self.sleep_time()
        self.GameHome.goto_game_page()
        self.GamePage.close_banner()
        self.GameHome.purchase_ads().purchase_click()
        self.sleep_time()
        self.write_contrast2(point)
        string1 = self.extract_string_point(correct_point, about_time_key)
        string2 = self.get_point_extract_string(point, about_time_key)
        if string1 == string2:
            assert True
        else:
            print("除去时间之外埋点不正确")
            assert False
        return self


