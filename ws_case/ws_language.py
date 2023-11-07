# coding = utf-8
# Author: Zoe
# File: ws_language.py
# Time: 2023/10/18 3:28 下午
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

ST.SAVE_IMAGE = False
# 暂时关闭截图
# 设置全局的截图精度为90
ST.SNAPSHOT_QUALITY = 90


class WaterSortLanguage:
    language = "英语"
    name = rf"{language}/{language}"
    # language = "印尼语"
    first_tube = [185, 938]
    second_tube = [436, 894]
    third_tube = [687, 929]
    fourth_tube = [933, 837]
    fifth_tube = [308, 1493]
    sixth_tube = [541, 1559]
    seventh_tube = [766, 1445]

    def __init__(self):
        self.PolicyPage = PolicyPage
        self.NewGuidance = NewGuidance
        self.FourTubeGamePage = FourTubeGamePage
        self.FiveTubeGamePage = FiveTubeGamePage
        self.SevenTubeGamePage = SevenTubeGamePage
        self.GameHome = GameHome
        self.NineTubeGamePage = NineTubeGamePage
        self.VictoryStep = VictoryStep
        self.BaseElement = BaseElement()

    def file_path(self, folder_name):
        path = f"/Users/amber/PycharmProjects/Water Sort/ws_case/log/{folder_name}"
        if os.path.exists(path):
            return self
        else:
            os.makedirs(path)
        return self

    def policy_page(self):
        """
        清除数据，重新进入游戏
        关闭日志弹窗
        截图隐私弹窗
        :return:
        """
        policy_page = "隐私弹窗"
        self.PolicyPage().first_start_ws()
        # 隐私弹窗截图
        self.BaseElement.get_snapshot(policy_page, self.name)

        return self

    def guidance_page(self):
        """
        从隐私弹窗页面点击按钮进入第一步引导
        第一步引导有两个文案
        进入第二个新手引导，完成之后到第三关
        :return:
        """
        first_step1 = "第一步引导文案1"
        first_step2 = "第一步引导文案2"
        victory_page = "胜利页面"
        self.PolicyPage().goto_guidance()
        # 第一步新手引导的截图
        self.BaseElement.get_snapshot(first_step1, self.name)
        self.NewGuidance().first_guidance_step1()
        # 新手引导第二步截图
        self.BaseElement.get_snapshot(first_step2, self.name)
        self.NewGuidance().first_guidance_step2()
        # 胜利页面截图
        self.BaseElement.get_snapshot(victory_page, self.name)

        self.NewGuidance().guidance_victory()
        self.NewGuidance().second_guidance_step1().second_guidance_step2().second_guidance_step3(). \
            second_guidance_step1().guidance_victory()
        # snapshot(filename=f"{self.language}_游戏页面关卡文案.png")
        return self

    def no_internet_toast(self):
        self.FourTubeGamePage().withdraw_tool()
        snapshot(filename=f"{self.language}_无网弹窗文案.png")
        return self

    def no_move_toast(self):
        sleep(3)
        self.FourTubeGamePage().goto_home_site()
        self.GameHome().get_debug().get_level("7")
        sleep(2)
        self.GameHome().goto_game_page()
        sleep(2)
        self.SevenTubeGamePage().tube_position(self.SevenTubeGamePage().fourth_tube).tube_position(
            self.SevenTubeGamePage().sixth_tube).tube_position(self.SevenTubeGamePage().fifth_tube).tube_position(
            self.SevenTubeGamePage().seventh_tube)
        snapshot(filename=f"{self.language}_无法移动toast.png")
        return self

    def get_reward(self):
        """
        第十二关
        :return:
        """
        self.SevenTubeGamePage().close_debug()
        self.FourTubeGamePage().goto_home_site()
        self.GameHome().open_debug()
        self.GameHome().get_level("12")
        sleep(2)
        self.GameHome().goto_game_page()
        sleep(2)
        self.VictoryStep().debug_win(20)
        self.VictoryStep().twelve_level()
        sleep(5)
        snapshot(filename=f"{self.language}_获得玫瑰瓶子.png")
        self.VictoryStep().rewards_get_button()
        self.SevenTubeGamePage().game_victory_page()
        return self

    def setting_page(self):
        self.SevenTubeGamePage().close_debug()
        self.SevenTubeGamePage().goto_setting_page()
        snapshot(filename=f"{self.language}_设置页面.png")
        self.SevenTubeGamePage().setting_collection()
        snapshot(filename=f"{self.language}_收藏页面.png")
        self.SevenTubeGamePage().collect_goto_setting().setting_language()
        snapshot(filename=f"{self.language}_设置页面语言页面.png")
        self.SevenTubeGamePage().setting_close().setting_contact_us()
        snapshot(filename=f"{self.language}_邮件页面.png")
        keyevent("back")
        keyevent("back")
        keyevent("back")
        self.SevenTubeGamePage().setting_close().goto_game_home()
        snapshot(filename=f"{self.language}_游戏首页.png")
        return self

    def scoring_guidance(self):
        self.GameHome().goto_game_page()
        self.GameHome().open_debug()
        self.VictoryStep().debug_win(20).thirteenth_level()
        snapshot(filename=f"{self.language}_评分引导.png")
        self.SevenTubeGamePage().close_score_guidance().game_victory_page()
        return self

    def unlock_twenty_level(self):
        self.SevenTubeGamePage().close_debug()
        self.FourTubeGamePage().goto_game_home()
        self.GameHome().open_debug()
        self.GameHome().get_level("20")
        sleep(2)
        self.GameHome().goto_game_page()
        sleep(2)
        self.VictoryStep().debug_win(20)
        self.VictoryStep().twenty_level()
        sleep(7)
        snapshot(filename=f"{self.language}_20关解锁背景.png")
        self.VictoryStep().rewards_get_button()
        self.SevenTubeGamePage().game_victory_page()
        return self

    def unlock_twenty_four(self):
        """
        二十四关解锁
        :return:
        """
        self.unlock_level("24", 30)
        self.VictoryStep().twenty_four()
        sleep(7)
        snapshot(filename=f"{self.language}_24关解锁柠檬鸡尾酒.png")
        self.VictoryStep().rewards_get_button()
        self.SevenTubeGamePage().game_victory_page()
        return self

    def unlock_thirty_fifth_level(self):
        """
        第三十五关解锁
        :return:
        """
        self.unlock_level("35", 30)
        self.VictoryStep().thirty_fifth_level()
        sleep(7)
        snapshot(filename=f"{self.language}_35关解锁背景.png")
        self.VictoryStep().rewards_get_button()
        self.SevenTubeGamePage().game_victory_page()
        return self

    def unlock_level(self, level, second):
        """
        解锁背景或者瓶子的前置步骤
        :param level: 需要解锁的关卡
        :param second: 等待的debug的秒数
        :return:
        """
        sleep(3)
        self.SevenTubeGamePage().close_debug()
        self.FourTubeGamePage().goto_game_home()
        self.GameHome().open_debug()
        self.GameHome().get_level(level)
        sleep(2)
        self.GameHome().goto_game_page()
        sleep(2)
        self.VictoryStep().debug_win(second)
        return self

    def unlock_fortieth_level(self):
        """
        第四十关解锁
        :return:
        """
        self.unlock_level("40", 30)
        self.VictoryStep().fortieth_level()
        sleep(7)
        snapshot(filename=f"{self.language}_40关解锁小熊瓶子.png")
        self.VictoryStep().rewards_get_button()
        self.SevenTubeGamePage().game_victory_page()
        return self

    def unlock_fiftieth_level(self):
        """
        第五十关解锁
        :return:
        """
        self.unlock_level("50", 40)
        self.VictoryStep().fiftieth_level()
        sleep(7)
        snapshot(filename=f"{self.language}_50关解锁背景.png")
        self.VictoryStep().rewards_get_button()
        self.SevenTubeGamePage().game_victory_page()
        return self

    def unlock_sixtieth_level(self):
        """
        第六十关解锁
        :return:
        """
        self.unlock_level("60", 40)
        self.VictoryStep().sixtieth_level()
        sleep(7)
        snapshot(filename=f"{self.language}_60关解锁奶油顶.png")
        self.VictoryStep().rewards_get_button()
        self.SevenTubeGamePage().game_victory_page()
        return self

    def unlock_seventieth_level(self):
        """
        第七十关解锁
        :return:
        """
        self.unlock_level("70", 40)
        self.VictoryStep().seventieth_level()
        sleep(7)
        snapshot(filename=f"{self.language}_70关解锁主题.png")
        self.VictoryStep().rewards_get_button()
        self.SevenTubeGamePage().game_victory_page()
        return self

    def unlock_eightieth_level(self):
        """
        第八十关解锁
        :return:
        """
        self.unlock_level("80", 40)
        self.VictoryStep().eightieth_level()
        sleep(7)
        snapshot(filename=f"{self.language}_80关解锁苏打瓶.png")
        self.VictoryStep().rewards_get_button()
        self.SevenTubeGamePage().game_victory_page()
        return self

    def unlock_ninetieth_level(self):
        """
        第九十关解锁
        :return:
        """
        self.unlock_level("90", 40)
        self.VictoryStep().ninetieth_level()
        sleep(7)
        snapshot(filename=f"{self.language}_90关解锁主题.png")
        self.VictoryStep().rewards_get_button()
        self.SevenTubeGamePage().game_victory_page()
        return self

    def unlock_hundred_ten_level(self):
        """
        第一百一十关解锁
        :return:
        """
        self.unlock_level("110", 40)
        self.VictoryStep().hundred_ten_level()
        sleep(7)
        snapshot(filename=f"{self.language}_110关解锁矿泉水.png")
        self.VictoryStep().rewards_get_button()
        self.SevenTubeGamePage().game_victory_page()
        return self

    def unlock_hundred_twenty_level(self):
        """
        第一百二十关解锁
        :return:
        """
        self.unlock_level("120", 40)
        self.VictoryStep().hundred_twenty_level()
        sleep(7)
        snapshot(filename=f"{self.language}_120关解锁背景.png")
        self.VictoryStep().rewards_get_button()
        self.SevenTubeGamePage().game_victory_page()
        return self

    def unlock_hundred_fifty_level(self):
        """
        第一百五十关解锁
        :return:
        """
        self.unlock_level("150", 40)
        self.VictoryStep().hundred_fifty_level()
        sleep(7)
        snapshot(filename=f"{self.language}_150关解锁藤蔓瓶.png")
        self.VictoryStep().rewards_get_button()
        self.SevenTubeGamePage().game_victory_page()
        return self

    def unlock_hundred_sixty_level(self):
        """
        第一百六十关解锁
        :return:
        """
        self.unlock_level("160", 40)
        self.VictoryStep().hundred_sixty_level()
        sleep(7)
        snapshot(filename=f"{self.language}_160关解锁主题.png")
        self.VictoryStep().rewards_get_button()
        self.SevenTubeGamePage().game_victory_page()
        return self

    def unlock_two_hundred_level(self):
        """
        第两百关解锁
        :return:
        """
        self.unlock_level("200", 40)
        self.VictoryStep().two_hundred_level()
        sleep(7)
        snapshot(filename=f"{self.language}_200关解锁爱心瓶.png")
        self.VictoryStep().rewards_get_button()
        self.SevenTubeGamePage().game_victory_page()
        return self

    def unlock_two_hundred_ten(self):
        """
        第两百一十关解锁
        :return:
        """
        self.unlock_level("210", 40)
        self.VictoryStep().two_hundred_ten()
        sleep(7)
        snapshot(filename=f"{self.language}_210关解锁主题.png")
        self.VictoryStep().rewards_get_button()
        self.SevenTubeGamePage().game_victory_page()
        return self

    def unlock_two_hundred_fifty(self):
        """
        第两百五十关解锁
        :return:
        """
        self.unlock_level("250", 40)
        self.VictoryStep().two_hundred_fifty()
        sleep(7)
        snapshot(filename=f"{self.language}_250关解锁玉兰花瓶.png")
        self.VictoryStep().rewards_get_button()
        self.SevenTubeGamePage().game_victory_page()
        return self

    def unlock_two_hundred_sixty(self):
        """
        第两百六十关解锁
        :return:
        """
        self.unlock_level("260", 40)
        self.VictoryStep().two_hundred_sixty()
        sleep(7)
        snapshot(filename=f"{self.language}_260关解锁主题.png")
        self.VictoryStep().rewards_get_button()
        self.SevenTubeGamePage().game_victory_page()
        return self

    def unlock_three_hundred_ten(self):
        """
        第三百一十关解锁
        :return:
        """
        self.unlock_level("310", 40)
        self.VictoryStep().three_hundred_ten()
        sleep(7)
        snapshot(filename=f"{self.language}_310关解锁木塞瓶.png")
        self.VictoryStep().rewards_get_button()
        self.SevenTubeGamePage().game_victory_page()
        return self

    def unlock_three_hundred_twenty(self):
        """
        第三百二十关解锁
        :return:
        """
        self.unlock_level("320", 40)
        self.VictoryStep().three_hundred_twenty()
        sleep(7)
        snapshot(filename=f"{self.language}_320关解锁主题.png")
        self.VictoryStep().rewards_get_button()
        self.SevenTubeGamePage().game_victory_page()
        return self

    def unlock_three_hundred_seventy(self):
        """
        第三百七十关解锁
        :return:
        """
        self.unlock_level("370", 40)
        self.VictoryStep().three_hundred_seventy()
        sleep(7)
        snapshot(filename=f"{self.language}_370关解锁可乐瓶.png")
        self.VictoryStep().rewards_get_button()
        self.SevenTubeGamePage().game_victory_page()
        return self

    def unlock_three_hundred_eighty(self):
        """
        第三百八十关解锁
        :return:
        """
        self.unlock_level("380", 40)
        self.VictoryStep().three_hundred_eighty()
        sleep(7)
        snapshot(filename=f"{self.language}_380关解锁背景主题.png")
        self.VictoryStep().rewards_get_button()
        self.SevenTubeGamePage().game_victory_page()
        return self

    def unlock_four_hundred_forty(self):
        """
        第四百四十关解锁
        :return:
        """
        self.unlock_level("440", 40)
        self.VictoryStep().four_hundred_forty()
        sleep(7)
        snapshot(filename=f"{self.language}_440关解锁汽水瓶.png")
        self.VictoryStep().rewards_get_button()
        self.SevenTubeGamePage().game_victory_page()
        return self

    def unlock_five_hundred_fifty(self):
        """
        第四百五十关解锁
        :return:
        """
        self.unlock_level("450", 40)
        self.VictoryStep().four_hundred_fifty()
        sleep(7)
        snapshot(filename=f"{self.language}_450关解锁主题.png")
        self.VictoryStep().rewards_get_button()
        self.SevenTubeGamePage().game_victory_page()
        return self

    def unlock_five_hundred_ten(self):
        """
        第五百一十关解锁
        :return:
        """
        self.unlock_level("510", 40)
        self.VictoryStep().five_hundred_ten()
        sleep(7)
        snapshot(filename=f"{self.language}_510关解锁木塞瓶.png")
        self.VictoryStep().rewards_get_button()
        self.SevenTubeGamePage().game_victory_page()
        return self

    def unlock_five_hundred_twenty(self):
        """
        第五百一十关解锁
        :return:
        """
        self.unlock_level("520", 40)
        self.VictoryStep().five_hundred_twenty()
        sleep(7)
        snapshot(filename=f"{self.language}_510关解锁主题.png")
        self.VictoryStep().rewards_get_button()
        self.SevenTubeGamePage().game_victory_page()
        return self

    def reward(self):
        self.SevenTubeGamePage().close_debug()
        self.FourTubeGamePage().goto_game_home()
        self.GameHome().get_reward_page()
        snapshot(filename=f"{self.language}_宝箱页面.png")
        self.GameHome().goto_game_page()
        return self


if __name__ == "__main__":
    if not cli_setup():
        auto_setup(__file__, logdir=True, devices=[
            "ios:///http://127.0.0.1:8300", ])
    # WaterSortLanguage().policy_page().guidance_page().no_internet_toast(). \
    #     no_move_toast().get_reward().setting_page().scoring_guidance(). \
    #     unlock_twenty_level().unlock_twenty_four()
    # WaterSortLanguage().unlock_thirty_fifth_level(). \
    #     unlock_fortieth_level().unlock_fiftieth_level().unlock_sixtieth_level(). \
    #     unlock_seventieth_level().unlock_eightieth_level().unlock_ninetieth_level(). \
    #     unlock_hundred_ten_level().unlock_hundred_twenty_level()
    # WaterSortLanguage().unlock_hundred_fifty_level(). \
    #     unlock_hundred_sixty_level().unlock_two_hundred_level().unlock_two_hundred_ten(). \
    #     unlock_two_hundred_fifty().unlock_two_hundred_sixty().unlock_three_hundred_ten(). \
    #     unlock_three_hundred_twenty().unlock_three_hundred_seventy().unlock_three_hundred_eighty(). \
    #     unlock_four_hundred_forty().unlock_five_hundred_fifty().unlock_five_hundred_ten().reward()
    WaterSortLanguage().file_path("英语").policy_page().guidance_page()