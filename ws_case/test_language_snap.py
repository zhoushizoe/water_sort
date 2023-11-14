from airtest.core.api import *
from airtest.cli.parser import cli_setup
from ws_page.policy_page import PolicyPage
from ws_page.guidance_page import NewGuidance
from ws_page.four_tube_game_page import FourTubeGamePage
from ws_page.five_tube_game_page import FiveTubeGamePage
from ws_page.seven_tube_game_page import SevenTubeGamePage
from ws_page.game_home_page import GameHome
from ws_page.nine_tube_game_page import NineTubeGamePage
from ws_page.victory_step import VictoryStep
from ws_base.base_ws import BaseElement
from ws_page.game_page import GamePage

ST.SAVE_IMAGE = False
# 暂时关闭截图
# 设置全局的截图精度为90
ST.SNAPSHOT_QUALITY = 90


class TestWatertLanguage(BaseElement):
    auto_setup(__file__, logdir=True,
               devices=["android://127.0.0.1:5037/R3CW10C3D9N?cap_method=MINICAP&touch_method=MAXTOUCH&", ])
    language = "test_1"
    name = rf"{language}/{language}"

    def file_path(self, folder_name):
        path = f"/Users/amber/PycharmProjects/Water Sort/ws_case/log/{folder_name}"
        if os.path.exists(path):
            return self
        else:
            os.makedirs(path)
        return self

    def test1_policy_android(self):
        """
        安卓的隐私弹窗页面截图
        :return:
        """
        page = "隐私弹窗"
        self.PolicyPage = PolicyPage()
        self.file_path(self.name)
        self.PolicyPage.first_start_android().close_information_page().close_log().privicy_close()
        self.get_snapshot(page, self.name)
        return self

    def test2_guidance_step1(self):
        """
        新手引导第一步
        :return:
        """
        page1 = "新手引导第一步"
        page2 = "新手引导第二步"
        page3 = "胜利页面"
        self.PolicyPage = PolicyPage()
        self.NewGuidance = NewGuidance()
        self.PolicyPage.goto_guidance()
        self.get_snapshot(page1, self.name)

    def test3_guidance_step3(self):
        """
        新手引导第二步
        :return:
        """
        page = "新手引导第二步"
        self.NewGuidance = NewGuidance()
        self.NewGuidance.first_guidance_step1()
        self.get_snapshot(page, self.name)

    def test4_victory_page(self):
        """
        新手引导后的胜利页面
        :return:
        """
        page = "胜利页面"
        self.NewGuidance = NewGuidance()
        self.NewGuidance.first_guidance_step2().sleep_time(5)
        self.get_snapshot(page, self.name)

    def test5_setting_page(self):
        """
        设置页面
        :return:
        """
        page = "设置页面"
        self.GamePage = GamePage()
        self.NewGuidance = NewGuidance()
        self.sleep_time()
        self.GamePage.game_victory()
        self.NewGuidance.completed_level2()
        self.sleep_time()
        self.GamePage.game_victory().goto_setting_page()
        self.get_snapshot(page, self.name)

    def test6_setting_language(self):
        """
        从设置页面到语言页面
        :return:
        """
        page = "设置语言页面"
        self.GamePage = GamePage()
        self.GamePage.goto_language_page()
        self.get_snapshot(page, self.name)

    def test7_contact_us(self):
        """
        从语言页面回到设置页面，然后点击进入邮件页面
        :return:
        """
        page = "邮件页面"
        self.GamePage = GamePage()
        self.GamePage.language_setting_close().goto_contact_us()
        self.get_snapshot(page, self.name)

    def test8_collect(self):
        """
        从邮件页面回到设置页面，然后进入收藏页面
        :return:
        """
        page = "收藏页面"
        self.GamePage = GamePage()
        self.GamePage.contact_goto_setting().goto_collection_page()
        self.get_snapshot(page, self.name)

    def test9_no_inter_toast(self):
        """
        从收藏页面回到游戏页面，点击道具，弹出无网toast
        :return:
        """
        page = "无网toast"
        self.GamePage = GamePage()
        self.GamePage.collect_back_setting().setting_close().click_withdraw_tool()
        self.sleep_time(6)
        self.get_snapshot(page, self.name)

    def test9_no_step_toast(self):
        """
        从第三关回到首页，开启debug，进入23关，两步操作后弹出无法移动的toast
        :return:
        """
        page = "无法移动toast"
        self.GamePage = GamePage()
        self.GameHome = GameHome()
        self.GamePage.game_back_home()
        self.GameHome.get_debug().get_level("23").goto_game_page()
        self.GamePage.level23_no_step()
        self.sleep_time(1)
        self.get_snapshot(page, self.name)

    def test10_reward(self):
        """
        得到第一个奖励页面
        :return:
        """
        page = "玫瑰瓶子解锁"
        self.GamePage = GamePage()
        self.GameHome = GameHome()
        self.GamePage.close_debug().game_back_home()
        self.GameHome.expand_debug().get_level("12").goto_game_page()
        self.GamePage.debug_win().debug_do_one()
        self.sleep_time(4)
        self.get_snapshot(page, self.name)

    def unlock(self, page, level):
        """
        解锁步骤
        :param page:
        :param level:
        :return:
        """

        # page = "极光解锁"
        self.GamePage = GamePage()
        self.GameHome = GameHome()
        self.GamePage.unlock_no_thanks().game_victory().close_debug().game_back_home()
        self.GameHome.expand_debug().get_level(level).goto_game_page()
        self.GamePage.debug_win().debug_do_one()
        self.sleep_time(4)
        self.get_snapshot(page, self.name)
        return self

    def test11_unlock(self):
        page = "极光解锁"
        level = "20"
        self.unlock(page, level)

    def test12_unlock(self):
        page = "柠檬鸡尾酒解锁"
        level = "24"
        self.unlock(page, level)

    def test13_unlock(self):
        page = "薰衣草田"
        level = "35"
        self.unlock(page, level)

    def test14_unlock(self):
        page = "小熊瓶子"
        level = "40"
        self.unlock(page, level)

    def test15_unlock(self):
        page = "逶迤山脉"
        level = "50"
        self.unlock(page, level)
        return self

    def test16_unlock(self):
        page = "奶油顶"
        level = "60"
        self.unlock(page, level)
        return self

    def test17_unlock(self):
        page = "翠绿原野"
        level = "70"
        self.unlock(page, level)
        return self

    def test18_unlock(self):
        page = "苏打瓶"
        level = "80"
        self.unlock(page, level)
        return self

    def test19_unlock(self):
        page = "瑰色黎明"
        level = "90"
        self.unlock(page, level)
        return self

    def test20_unlock(self):
        page = "矿泉水"
        level = "110"
        self.unlock(page, level)
        return self

    def test21_unlock(self):
        page = "湖光山色"
        level = "120"
        self.unlock(page, level)
        return self

    def test22_unlock(self):
        page = "藤蔓瓶"
        level = "150"
        self.unlock(page, level)
        return self

    def test23_unlock(self):
        page = "迷雾森林"
        level = "160"
        self.unlock(page, level)
        return self

    def test24_unlock(self):
        page = "爱心瓶"
        level = "200"
        self.unlock(page, level)
        return self

    def test25_unlock(self):
        page = "星垂平野"
        level = "210"
        self.unlock(page, level)
        return self

    def test26_unlock(self):
        page = "玉兰花瓶"
        level = "250"
        self.unlock(page, level)
        return self

    def test27_unlock(self):
        page = "湖光静影"
        level = "260"
        self.unlock(page, level)
        return self

    def test28_unlock(self):
        page = "爱心瓶"
        level = "200"
        self.unlock(page, level)
        return self

    def test29_unlock(self):
        page = "木塞瓶"
        level = "310"
        self.unlock(page, level)
        return self

    def test30_unlock(self):
        page = "海天一色"
        level = "320"
        self.unlock(page, level)
        return self

    def test31_unlock(self):
        page = "可乐瓶"
        level = "370"
        self.unlock(page, level)
        return self

    def test32_unlock(self):
        page = "城堡风光"
        level = "380"
        self.unlock(page, level)
        return self

    def test33_unlock(self):
        page = "汽水瓶"
        level = "440"
        self.unlock(page, level)
        return self

    def test34_unlock(self):
        page = "极目天光"
        level = "450"
        self.unlock(page, level)
        return self

    def test35_unlock(self):
        page = "木塞宽瓶"
        level = "510"
        self.unlock(page, level)
        return self

    def test36_unlock(self):
        page = "日出江花"
        level = "520"
        self.unlock(page, level)
        return self

    def test37_unlock(self):
        page = "薄荷鸡尾酒"
        level = "590"
        self.unlock(page, level)
        return self

    def test38_unlock(self):
        page = "富士山下"
        level = "600"
        self.unlock(page, level)
        return self
