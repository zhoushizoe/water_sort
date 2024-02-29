from ws_base.base_poco import BasePoco
from ws_base.base_ws import BaseElement
from ws_base.base_ws import IosBaseElement
from ws_base.base_android_poco import BaseAndroidPoco
from airtest.cli.parser import cli_setup
from airtest.core.api import *
from new_ws_page.new_game_page import NewGamePage
from ws_page.game_page import GamePage


class NewChallengePage(BaseElement):
    """
    挑战模式页面
    """
    normal_first_level = "ChallengeItem_Normal_0_1"
    purchase_level = "Button_Buy"
    get_coins_ad = "Image_AD"
    # 解锁未通关关卡按钮
    unlock_level_go = "Go"
    # debug中确定减少的时间
    Accelerator_ = "Accelerator_.*"
    # debug中减少时间
    ReduceTime_ = "ReduceTime_.*"
    # time is up页面文案
    time_is_up = "Time is up!"
    # failed页面点击+2 minutes
    add_minutes = "+2 minutes"
    # failed页面点击no，thanks
    no_thanks = "No, thanks"
    # 结算页面的continue按钮
    continue_button = "Button_Back"
    # 挑战模式重玩关卡按钮
    play_again = "Button_RePlay"
    # 已经解锁的关卡按钮
    go_button = "Button_Go"
    # hard页面按钮
    hard_button_text = "Hard"
    list1 = ["ChallengeItem_Normal_1_2", "ChallengeItem_Normal_2_3", "ChallengeItem_Normal_3_4",
             "ChallengeItem_Normal_4_5", "ChallengeItem_Normal_5_6", "ChallengeItem_Normal_6_7",
             "ChallengeItem_Normal_7_8", "ChallengeItem_Normal_8_9"]
    list2 = ["ChallengeItem_Normal_9_10", "ChallengeItem_Normal_10_11", "ChallengeItem_Normal_11_12"]
    hard_level_1 = "ChallengeItem_Hard_0_1"

    def __init__(self):
        self.BasePoco = BasePoco()
        self.IosBaseElement = IosBaseElement()
        self.BaseAndroidPoco = BaseAndroidPoco()
        self.NewGamePage = NewGamePage()
        self.GamePage = GamePage()

    def click_coins_purchase_level(self):
        """
        点击金币购买关卡
        :return:
        """
        self.BasePoco.get_element_pos_click_name(self.purchase_level)
        return self

    def new_debug_reduce_time(self, times, number):
        """
        减少挑战模式的时间
        :param times:
        :param number:
        :return:
        """
        for i in range(times):
            self.BasePoco.regular_poco_text(self.Accelerator_)
        for j in range(number):
            self.BasePoco.regular_poco_text(self.ReduceTime_)
        return self

    def new_click_add_minutes(self):
        """
        点击增加时间按钮
        :return:
        """
        self.BasePoco.get_element_pos_click(self.add_minutes)
        return self

    def new_click_no_thanks(self):
        """
        在失败页面点击no，thanks按钮
        :return:
        """
        self.BasePoco.get_element_pos_click(self.no_thanks)
        return self

    def new_challenge_continue(self):
        """
        在结算页面点击继续按钮
        :return:
        """
        self.BasePoco.get_element_pos_click_name(self.continue_button)
        return self

    def new_challenge_play_again(self):
        """
        重玩关卡
        :return:
        """
        self.BasePoco.get_element_pos_click_name(self.play_again)
        return self

    def new_unlock_level(self):
        """
        解锁之后的挑战关卡
        :return:
        """
        self.BasePoco.get_element_pos_click_name(self.go_button)
        return self

    def new_goto_hard_page(self):
        self.BasePoco.get_element_pos_click(self.hard_button_text)
        return self

    def new_goto_level(self, times, element_name):
        """
        点击关卡按钮
        :param times:
        :param element_name:
        :return:
        """
        for i in range(times):
            self.BasePoco.get_element_pos_click_name(element_name, 0.07)
        return self

    def new_get_hard_level_1(self):
        """
        通过19个普通挑战关卡得到hard关卡
        :return:
        """
        for level in self.list1:
            print(level)
            self.BasePoco.get_element_pos_click_name(level, 0.07).get_element_pos_click_name(level, 0.07)
            self.sleep_time()
            self.NewGamePage.new_debug_win(30).new_debug_doone()
            self.sleep_time(5)
            self.GamePage.ad_close()
            self.sleep_time(4)
            self.new_challenge_continue()
            self.sleep_time(4)
        self.image_swipe([956, 2727], [952, 2072])
        self.sleep_time()
        for level2 in self.list2:
            print(level2)
            self.BasePoco.get_element_pos_click_name(level2, 0.07).get_element_pos_click_name(level2, 0.07)
            self.sleep_time()
            self.NewGamePage.new_debug_win(30).new_debug_doone()
            self.sleep_time(5)
            self.GamePage.ad_close()
            self.sleep_time(4)
            self.new_challenge_continue()
            self.sleep_time(4)
        return self

    def swipe_one_page(self):
        """
        滑动关卡区一屏
        :return:
        """
        self.image_swipe([956, 2727], [952, 2072])
        return self

    def new_goto_challenge_hard_level_1(self):
        self.BasePoco.get_element_pos_click_name(self.hard_level_1, 0.07)
        return self



if __name__ == "__main__":
    if not cli_setup():
        auto_setup(__file__, logdir=True, devices=[
            "android://127.0.0.1:5037/R3CW10C3D9N?cap_method=ADBCAP&touch_method=MAXTOUCH&", ])
    NewChallengePage().swipe_one_page()
