# coding = utf-8
# Author: Zoe
# File: game_home_page.py
# Time: 2023/10/18 5:20 下午
from ws_base.base_ws import BaseElement
from ws_base.base_ws import IosBaseElement
from airtest.core.api import *
from airtest.cli.parser import cli_setup


class GameHome(BaseElement, IosBaseElement):
    game_icon = Template(r"../picture/home_page_picture/game_icon.png", record_pos=(-0.03, -0.238),
                         resolution=(1096, 2560))
    debug_passward = Template(r"../picture/home_page_picture/debug_passward.png", record_pos=(-0.08, -0.422),
                              resolution=(1096, 2560))
    debug_bingo = Template(r"../picture/home_page_picture/debug_bingo.png", record_pos=(0.423, 0.956),
                           resolution=(1096, 2560))
    debug_delete_button = Template(r"../picture/home_page_picture/delete_button.png", record_pos=(0.423, 0.803),
                                   resolution=(1096, 2560))
    debug_fugure_button = Template(r"../picture/home_page_picture/debug_fugure_button.png", record_pos=(-0.429, 0.958),
                                   resolution=(1096, 2560))
    debug_close_button = Template(r"../picture/home_page_picture/debug_close_button.png", record_pos=(-0.015, -0.509),
                                  resolution=(1096, 2560))
    home_level_button = Template(r"../picture/home_page_picture/home_level_button.png", record_pos=(-0.237, 0.403),
                                 resolution=(1096, 2560))
    input_fields = Template(r"../picture/home_page_picture/input_fields.png", threshold=0.8,
                            record_pos=(-0.178, -0.965), resolution=(1440, 3088))
    debug_level = Template(r"../picture/home_page_picture/debug_level.png", threshold=0.9, target_pos=6,
                           record_pos=(-0.193, -0.378), resolution=(1440, 3088))
    dubug_yes = Template(r"../picture/home_page_picture/dubug_yes.png", record_pos=(0.375, 0.827),
                         resolution=(1440, 3088))

    goto_game_button = Template(r"../picture/home_page_picture/goto_game_button.png", threshold=0.5,
                                record_pos=(-0.249, 0.429), resolution=(1440, 3088))
    # 首页展开debug按钮
    expand_debug_button = Template(r"../picture/home_page_picture/expand_debug_button.png", target_pos=5,
                                   record_pos=(-0.468, -0.975),
                                   resolution=(1440, 3088))
    # 首页的去广告button
    ads_button = Template(r"../picture/home_page_picture/ads_button.png", record_pos=(-0.272, -0.929),
                          resolution=(1440, 3088))
    # 去广告内购的购买按钮
    ads_buy_button = Template(r"../picture/home_page_picture/ads_buy_button.png", record_pos=(-0.022, 0.902),
                              resolution=(1440, 3088))
    # 回到首页按钮
    goto_home_button = Template(r"../picture/game_page_picture/goto_home_button.png", record_pos=(-0.284, -1.094),
                                resolution=(1096, 2560))
    # 圣诞活动的点击button
    christmas_button = Template(r"../picture/home_page_picture/christmas_button.png", target_pos=6,
                                record_pos=(-0.229, 0.308), resolution=(1440, 3088))
    # 首页获得金币按钮
    home_get_coin_button = Template(r"../picture/home_page_picture/home_get_coin_button.png",
                                    record_pos=(0.201, -0.928), resolution=(1440, 3088))
    # 获得金币弹窗按钮
    ad_get_coin = Template(r"../picture/home_page_picture/ad_get_coin.png", record_pos=(0.01, 0.221),
                           resolution=(1440, 3088))
    # 购买去广告弹窗页面层button
    ads_purchase_usd_button = Template(r"../picture/home_page_picture/ads_purchase_usd_button.png",
                                       record_pos=(-0.09, 0.444), resolution=(1440, 3088))
    # 活动模式弹窗，go按钮
    activicity_page_go_button = Template(r"../picture/home_page_picture/activicity_page_go_button.png",
                                         record_pos=(0.003, 0.297), resolution=(1440, 3088))
    # 游戏中的banner关闭按钮
    close_banner_button = Template(r"../picture/home_page_picture/close_banner_button.png", record_pos=(0.432, 0.889),
                                   resolution=(1440, 3088))
    # pad中首页的挑战模式弹窗的go按钮
    pad_activity_go_button = Template(r"../picture/home_page_picture/pad_activity_gp_button.png",
                                      record_pos=(-0.152, 0.188), resolution=(1620, 2160))

    # def __init__(self, poco):
    #     self.BasePoco = poco

    def get_debug(self):
        """
        在游戏首页开启debug并回到首页
        :return:
        """
        # self.sleep_time(4)
        # if exists(self.game_icon):
        #     self.image_click(self.game_icon, times=7)
        # else:
        self.image_click([782, 1262], times=10)
        self.sleep_time(1)
        self.image_click_plus(self.input_fields, [462, 167])
        self.image_click_plus(self.debug_passward, [619, 1002])
        self.image_click_plus(self.debug_close_button, [702, 1312])
        self.image_click_plus(self.debug_close_button, [702, 850])
        return self

    def pad_get_debug(self):
        """
        在游戏首页开启debug并回到首页
        :return:
        """
        # self.sleep_time(4)
        # if exists(self.game_icon):
        #     self.image_click(self.game_icon, times=7)
        # else:
        self.image_click([799, 746], times=10)
        self.sleep_time(1)
        self.image_click([270, 68])
        self.image_click_plus(self.debug_passward, [619, 1002])
        self.image_click_plus(self.debug_close_button, [702, 1312])
        self.image_click_plus(self.debug_close_button, [702, 850])
        return self

    def get_level(self, level):
        """
        开启debug后，进入debug，得到想要的关卡
        :param level:希望的关卡
        :return:
        """
        self.image_click_plus(self.input_fields, [339, 172])
        self.sleep_time(1)
        self.image_click([599, 973])
        self.sleep_time(1)
        for i in range(4):
            self.delete_word()
        self.input_word(level)
        self.sleep_time(1)
        # self.image_click([822, 1819])
        self.sleep_time(1)
        self.image_click(self.debug_close_button, times=2)
        self.sleep_time()
        return self

    def pad_get_level(self, level):
        """
        pad上的得到level关卡
        :return:
        """
        self.sleep_time(1)
        self.image_click([300, 117])
        self.sleep_time(1)
        self.image_click([739, 627])
        self.sleep_time(1)
        self.ios_delete_text().ios_inter_word(level)
        self.sleep_time()
        self.image_click([803, 514]).image_click([803, 514])
        self.sleep_time()
        return self

    def pad_get_coin(self, coin):
        """
        pad上的得到level关卡
        :return:
        """
        self.image_click([300, 117])
        self.image_click([1082, 616])
        self.sleep_time(1)
        self.ios_delete_text().ios_inter_word(coin)
        self.sleep_time()
        self.image_click([803, 514]).image_click([803, 514])
        self.sleep_time()
        return self

    def debug_get_coin(self, coin):
        """
        开启debug后，进入debug，得到想要的关卡
        :param coin: 想要的金币数量
        :return:
        """
        self.image_click_plus(self.input_fields, [404, 173])
        self.sleep_time(1)
        self.image_click([1007, 988])
        self.sleep_time(1)
        for i in range(4):
            self.delete_word()
        self.input_word(coin)
        self.sleep_time(1)
        # self.image_click([822, 1819])
        self.sleep_time(1)
        self.image_click(self.debug_close_button, times=2)
        self.sleep_time()
        return self

    def goto_game_page(self):
        """
        从首页进入游戏页面
        :return:
        """
        self.sleep_time()
        self.image_click_plus(self.goto_game_button, [698, 2202])
        self.sleep_time(3)
        return self

    def expand_debug(self):
        """
        在首页展开debug
        :return:
        """
        self.sleep_time()
        self.image_click_plus(self.expand_debug_button, [44, 127])
        return self

    def open_debug(self):
        sleep(1)
        self.image_click([35, 26])
        sleep(3)
        return self

    def get_reward_page(self):
        self.image_click([954, 307])
        sleep(3)
        return self

    def reward_goto_home(self):
        self.image_click([916, 619])
        sleep(3)
        return self

    def get_unlock_level(self, level):
        """
        在首页展开debug后，得到想要的关卡，然后进入游戏
        :param level:
        :return:
        """
        self.expand_debug().get_level(level).goto_game_page()
        self.sleep_time()
        return self

    def goto_ads_page(self):
        """
        进入广告购买弹窗
        :return:
        """
        self.image_click(self.ads_button)
        return self

    def purchase_ads(self):
        """
        ads弹窗中点击购买按钮
        :return:
        """
        self.image_click(self.ads_purchase_usd_button)
        return self

    def purchase_click(self):
        """
        点击内购购买按钮
        :return:
        """
        self.image_click(self.ads_buy_button)
        return self

    def christmas_activities_start(self):
        """
        圣诞活动期间弹出活动弹窗，点击确认
        :return:
        """
        button_ok = "Button_OK"
        if exists(self.christmas_button):
            self.image_click(self.christmas_button)
            self.image_click(self.christmas_button)
        if exists(self.goto_home_button):
            self.image_click(self.goto_home_button)
        return self

    def get_coin(self):
        """
        在首页点击获得金币按钮
        :return:
        """
        self.image_click(self.home_get_coin_button)
        return self

    def ad_get_coins(self):
        """
        在获得金币的弹窗点击获得金币
        :return:
        """
        self.image_click(self.ad_get_coin)
        return self

    def activicity_page_go(self):
        """
        在弹出的活动弹窗上点击go
        :return:
        """
        self.image_click(self.activicity_page_go_button)
        return self

    def pad_activity_page_go(self):
        """
        在pad挑战弹窗上点击go
        :return:
        """
        self.image_click(self.pad_activity_go_button)
        return self


if __name__ == "__main__":
    if not cli_setup():
        auto_setup(__file__, logdir=True, devices=[
            "android://127.0.0.1:5037/R3CW10C3D9N?cap_method=MINICAP&touch_method=MAXTOUCH&", ])
    GameHome().christmas_activities_start()
