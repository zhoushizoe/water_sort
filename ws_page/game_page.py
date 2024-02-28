from ws_base.base_ws import BaseElement
from airtest.core.api import *
from airtest.cli.parser import cli_setup
from ws_page.game_home_page import GameHome
from ws_base.base_poco import BasePoco


class GamePage(BaseElement, BasePoco):
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
    # 结算页面的下一关按钮
    victory_english_button = Template(r"../picture/game_page_picture/victory_english_button.png",
                                      record_pos=(-0.01, 0.638),
                                      resolution=(1440, 3088))

    # 广告关闭按钮
    ad_close_button = Template(r"../picture/game_page_picture/ad_close_button.png", record_pos=(0.454, -0.953),
                               resolution=(1440, 3088))

    # 开启宝箱，看广告获得双倍
    double_ad_button = Template(r"../picture/game_page_picture/double_ad_button.png", record_pos=(-0.154, 0.422),
                                resolution=(1440, 3088))
    # 重开道具按钮
    tool_restart_button = Template(r"../picture/game_page_picture/tool_restart_button.png", record_pos=(-0.326, 0.778),
                                   resolution=(1440, 3088))
    # 提示道具按钮
    tool_doone_button = Template(r"../picture/game_page_picture/tool_doone_button.png", record_pos=(0.109, 0.779),
                                 resolution=(1440, 3088))
    # 加管道具按钮
    tool_add_tube_button = Template(r"../picture/game_page_picture/tool_add_tube_button.png", record_pos=(0.329, 0.781),
                                    resolution=(1440, 3088))
    # 跳关按钮
    game_skip_button = Template(r"../picture/game_page_picture/game_skip_button.png", record_pos=(0.397, -0.796),
                                resolution=(1440, 3088))
    # 评分引导的不同星星表情
    first_star_face = Template(r"../picture/game_page_picture/first_star_face.png", threshold=0.9,
                               record_pos=(-0.006, -0.24), resolution=(1440, 3088))
    second_star_face = Template(r"../picture/game_page_picture/second_star_face.png", threshold=0.9,
                                record_pos=(0.0, -0.238), resolution=(1440, 3088))
    third_star_face = Template(r"../picture/game_page_picture/third_star_face.png", threshold=0.9,
                               record_pos=(0.005, -0.235),
                               resolution=(1440, 3088))
    fourth_star_Face = Template(r"../picture/game_page_picture/fourth_star_Face.png", threshold=0.9,
                                record_pos=(0.005, -0.243),
                                resolution=(1440, 3088))
    fifth_star_face = Template(r"../picture/game_page_picture/fifth_star_face.png", threshold=0.9,
                               record_pos=(-0.003, -0.245),
                               resolution=(1440, 3088))
    please_dont_delete = Template(r"../picture/game_page_picture/please_dont_delete.png", record_pos=(-0.067, -0.108),
                                  resolution=(1440, 3088))
    # gp页面的倒水icon
    water_sort_icon = Template(r"../picture/game_page_picture/water_sort_icon.png", record_pos=(-0.344, -0.731),
                               resolution=(1440, 3088))
    # 瓶盖
    tube_tops = Template(r"../picture/game_page_picture/tube_tops.png", record_pos=(0.393, -0.292),
                         resolution=(1440, 3088))
    # 设置页面瓶盖关闭
    tops_close = Template(r"../picture/game_page_picture/tops_close.png", threshold=0.8, record_pos=(0.017, -0.028),
                          resolution=(1440, 3088))
    tops_open = Template(r"../picture/game_page_picture/tops_open.png", threshold=0.8, record_pos=(0.003, -0.015),
                         resolution=(1440, 3088))

    # 游戏中的banner关闭按钮
    close_banner_button = Template(r"../picture/game_page_picture/close_banner_button.png", record_pos=(0.432, 0.889),
                                   resolution=(1440, 3088))

    email_image = Template(r"../picture/game_page_picture/email_image.png", record_pos=(-0.051, -0.616),
                           resolution=(1440, 3088))
    empty_tube = Template(r"../picture/game_page_picture/empty_tube.png", record_pos=(0.34, -0.045),
                          resolution=(1440, 3088))
    chest_item_withdraw = Template(r"../picture/game_page_picture/chest_item_withdraw.png", record_pos=(-0.18, -0.523),
                                   resolution=(1440, 3088))
    chest_coin = Template(r"../picture/game_page_picture/chest_coin.png", record_pos=(0.213, -0.525),
                          resolution=(1440, 3088))
    second_empty_tube = Template(r"../picture/game_page_picture/second_empty_tube.png", record_pos=(0.124, 0.287),
                                 resolution=(1440, 3088))
    reward_background = Template(r"../picture/game_page_picture/reward_backgroud.png", record_pos=(-0.003, -0.207),
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

    def click_music(self):
        """
        poco的方式点击音乐按钮
        :return:
        """
        Music_Switch = "MusicSwitch"
        self.unity_poco_click(Music_Switch)
        return self

    def click_sound(self):
        """
        poco的方式点击音效按钮
        :return:
        """
        Sound_Switch = "SoundSwitch"
        self.unity_poco_click(Sound_Switch)
        return self

    def click_vibration(self):
        """
        poco的方式点击震动
        :return:
        """
        Vibrate_Switch = "VibrateSwitch"
        self.unity_poco_click(Vibrate_Switch)
        return self

    def click_tops(self):
        """
        poco的方式点击瓶盖开关
        :return:
        """
        Tops_Switch = "TopsSwitch"
        self.unity_poco_click(Tops_Switch)
        return self

    def goto_language_page(self):
        """
        进入设置页面后，点击进入语言页面
        :return:
        """
        self.image_click_coord(self.setting_language_button, [934, 1650])
        self.sleep_time(2)
        return self

    def poco_goto_language(self):
        """
        使用poco的方法在设置页面进入语言页面
        :return:
        """
        element = "UI_MainMenuSetting(Clone)"
        offspring1 = "LanguageButton"
        offspring2 = "Button"
        self.poco_offspring_click(element, offspring1, offspring2)
        return self

    def poco_change_french(self):
        """
        切换法语
        :return:
        """
        french = "SelectionLanguageButton_Item (1)"
        self.unity_poco_click(french)
        return self

    def language_setting_close(self):
        """
        点击语言页面的关闭按钮
        :return:
        """
        self.image_click_plus(self.setting_close_button, [1214, 702])
        self.sleep_time(2)
        return self

    def language_confirm(self):
        """
        语言页面的确定按钮
        :return:
        """
        self.UnityPoco("UI_LanguageSetting(Clone)").offspring("Button").click()
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

    def poco_goto_contact(self):
        """
        poco的方式进入邮件页面
        :return:
        """
        self.UnityPoco("UI_MainMenuSetting(Clone)").offspring("ContactButton").offspring("Button_Base").click()
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
        self.image_click_coord(self.setting_collection_button, [1061, 1700])
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

    def pad_game_back_home(self):
        self.image_click([270, 90])
        return self

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

    def pad_close_debug(self):
        """
        pad中的关闭debug
        :return:
        """
        self.image_click([52, 47])
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

    def debug_doone(self):
        self.image_click(self.debug_doone_button)
        self.sleep_time(1)
        return self

    def pad_debug_doone(self):
        self.image_click([1286, 101])
        self.sleep_time(1)
        return self

    def unlock_no_thanks(self):
        """
        获得奖励页面点击不，谢谢按钮
        :return:
        """
        self.image_click([722, 2374])
        self.sleep_time()
        return self

    def unlock_button_ad(self):
        """
        在获得宝箱的页面点击claim x2
        :return:
        """
        # Button_AD = "Button_AD"
        # self.BasePoco.unity_poco_click(Button_AD)
        self.image_click(self.double_ad_button)
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

    def rate_us_close(self):
        """
        评分引导页面点击关闭按钮
        :return:
        """
        close_button = "Button_Close"
        self.unity_poco_click(close_button)
        return self

    def rate_us_one_star(self):
        """
        点击评分引导一颗星星
        :return:
        """
        self.image_click([363, 1504])
        return self

    def rate_us_five_star(self):
        """
        点击评分引导五颗星星
        :return:
        """
        self.image_click([1150, 1484])
        return self

    def rate_us_feedback(self):
        """
        点击评分引导反馈按钮
        :return:
        """
        Button_OK = "Button_OK"
        self.image_click([712, 1818])
        return self

    def ad_close(self):
        self.sleep_time(4)
        if exists(self.victory_english_button):
            return self
        else:
            self.sleep_time(15)
            if exists(self.ad_close_button):
                self.image_click(self.ad_close_button)
            else:
                self.system_keyevent("BACK")
                self.image_click([1384, 152])
        return self

    def pad_ad_close(self):
        self.sleep_time(4)
        if exists(self.victory_english_button):
            return self
        else:
            self.sleep_time(15)
            if exists(self.ad_close_button):
                self.image_click(self.ad_close_button)
            else:
                self.system_keyevent("BACK")
                self.image_click([1384, 152])
        return self

    def tool_restart_click(self):
        """
        点击重开道具
        :return:
        """
        self.image_click(self.tool_restart_button)
        return self

    def tool_doone_click(self):
        """
        点击提示道具
        :return:
        """
        self.image_click_plus(self.tool_doone_button, [889, 2630])
        return self

    def tool_add_tube_click(self):
        """
        点击加管道具
        :return:
        """
        self.image_click_plus(self.tool_add_tube_button, [1204, 2644])
        return self

    def game_skip(self):
        """
        点击跳关
        :return:
        """
        self.image_click_plus(self.game_skip_button, [1220, 395])
        return self

    def close_banner(self):
        self.image_click(self.close_banner_button)
        return self

    def debug_minus_time(self):
        self.image_click([182, 257]).image_click([182, 257])
        self.image_click([1045, 112]).image_click([1045, 112]).image_click([1045, 112])


if __name__ == "__main__":
    if not cli_setup():
        auto_setup(__file__, logdir=True, devices=[
            "android://127.0.0.1:5037/R3CW10C3D9N?cap_method=MINICAP&touch_method=MAXTOUCH&", ])
    GamePage().rate_us_close()
