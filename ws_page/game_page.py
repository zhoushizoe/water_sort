from ws_base.base_ws import BaseElement
from airtest.core.api import *
from airtest.cli.parser import cli_setup

from ws_page.game_home_page import GameHome


class GamePage(BaseElement):
    # 胜利弹窗下一关按钮
    victory_button = Template(r"../picture/game_page_picture/victory_next_button.png", target_pos=6,
                              record_pos=(-0.249, 0.581), resolution=(1440, 3088))
    # 游戏页面的设置按钮
    setting_button = Template(r"../picture/game_page_picture/setting_button.png", record_pos=(-0.406, -1.097),
                              resolution=(1096, 2560))
    # 游戏页面的语言按钮
    setting_language_button = Template(r"../picture/game_page_picture/setting_language_button.png",
                                       record_pos=(-0.303, 0.25), resolution=(1440, 3088))
    # 设置页面的关闭按钮
    setting_close_button = Template(r"../picture/game_page_picture/setting_close_button.png",
                                    record_pos=(0.348, -0.611), resolution=(1096, 2560))
    # 设置页面的联系我们按钮
    contact_us_button = Template(r"../picture/game_page_picture/contact_us_button.png", record_pos=(-0.31, 0.388),
                                 resolution=(1440, 3088))
    # 设置页面的收藏页面按钮
    setting_collection_button = Template(r"../picture/game_page_picture/setting_collection_button.png",
                                         record_pos=(-0.299, 0.11), resolution=(1440, 3088))
    # 回到首页按钮
    goto_home_button = Template(r"../picture/game_page_picture/goto_home_button.png", record_pos=(-0.284, -1.094),
                                resolution=(1096, 2560))
    # 撤回道具按钮
    withdraw_tool_button = Template(r"../picture/game_page_picture/withdraw_tool_button.png", record_pos=(0.002, 0.833),
                                    resolution=(1096, 2560))
    # 缩小debug弹窗
    debug_close_button = Template(r"../picture/game_page_picture/debug_colse_button.png", threshold=0.9,
                                  record_pos=(-0.453, -0.951), resolution=(1440, 3088))
    # debug中win按钮
    debug_win_button = Template(r"../picture/game_page_picture/debug_win_button.png", record_pos=(0.199, -0.955),
                                resolution=(1440, 3088))
    # debug中的最后几步操作按钮
    debug_doone_button = Template(r"../picture/game_page_picture/debug_doone_button.png", record_pos=(0.295, -0.957),
                                  resolution=(1440, 3088))

    def game_victory(self):
        """
        点击游戏页面的胜利按钮，进入下一关
        :return:
        """
        self.image_click_plus(self.victory_button, [727, 2379])
        return self

    def goto_setting_page(self):
        """
        点击设置按钮，进入设置页面
        :return:
        """
        self.image_click_plus(self.setting_button, [132, 211])
        self.sleep_time(1)
        return self

    def goto_language_page(self):
        """
        进入设置页面后，点击进入语言页面
        :return:
        """
        self.image_click_coord(self.setting_language_button, [934, 1650])
        self.sleep_time(2)
        return self

    def language_setting_close(self):
        """
        点击语言页面的关闭按钮
        :return:
        """
        self.image_click_plus(self.setting_close_button, [1214, 702])
        self.sleep_time(2)
        return self

    def setting_close(self):
        """
        点击设置页面的关闭按钮
        :return:
        """
        self.image_click_plus(self.setting_close_button, [1214, 702])
        self.sleep_time(1)
        return self

    def goto_contact_us(self):
        """
        点击进入邮件页面
        :return:
        """
        self.image_click_coord(self.contact_us_button, [1071, 2094])
        self.sleep_time()
        self.system_keyevent("BACK")
        return self

    def contact_goto_setting(self):
        """
        从邮箱页面回到设置页面，点击物理back键就可以(仅安卓)
        :return:
        """
        self.system_keyevent("BACK")
        return self

    def goto_collection_page(self):
        """
        从设置页面进入收藏页面
        :return:
        """
        self.image_click_coord(self.setting_collection_button, [943, 1485])
        self.sleep_time()
        return self

    def collect_back_setting(self):
        """
        从收藏页面回到设置页面
        :return:
        """
        self.image_click_plus(self.goto_home_button, [113, 196])
        self.sleep_time(1)
        return self

    def click_withdraw_tool(self):
        """
        点击撤回按钮
        :return:
        """
        self.image_click_plus(self.withdraw_tool_button, [737, 2590])
        return self

    def game_back_home(self):
        """
        从游戏页面回到首页
        :return:
        """
        self.image_click_plus(self.goto_home_button, [329, 196])
        self.sleep_time(1)
        return GameHome

    def level23_no_step(self):
        """
        出现无法移动toast的前置步骤
        :return:
        """
        self.sleep_time()
        self.image_click([493, 938]).image_click([769, 1628]).image_click([1076, 849]).image_click([1036, 1645])
        return self

    def close_debug(self):
        """
        关闭debug
        :return:
        """
        self.image_click_plus(self.debug_close_button, [103, 172])
        return self

    def debug_win(self, second=40):
        """
        点击debug的win按钮会自动开始游戏，直到最后几步
        :return:
        """
        self.image_click_plus(self.debug_win_button, [1002, 167])
        self.sleep_time(second)
        return self

    def debug_do_one(self):
        """
        点击debug中的do_one按钮
        :return:
        """
        for i in range(7):
            self.image_click(self.debug_doone_button)
            self.sleep_time(3)
        return self

    def unlock_no_thanks(self):
        """
        获得奖励页面点击不，谢谢按钮
        :return:
        """
        self.image_click([640, 2464])
        self.sleep_time()
        return self

    def unlock_step(self):
        """
        在解锁页面点击no thanks，然后点击胜利按钮，关闭debug，回到首页

        """
        self.unlock_no_thanks().game_victory().close_debug().game_back_home()
        return self

    def congratulation_back_home(self):
        """
        在通关弹窗返回到首页
        :return:
        """
        self.image_click([631, 2170])
        return self

if __name__ == "__main__":
    if not cli_setup():
        auto_setup(__file__, logdir=True, devices=[
            "android://127.0.0.1:5037/R3CW10C3D9N?cap_method=MINICAP&touch_method=MAXTOUCH&", ])
    GamePage().unlock_step()
