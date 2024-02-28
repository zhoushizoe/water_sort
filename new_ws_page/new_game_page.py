from airtest.core.api import auto_setup
from ws_base.base_poco import BasePoco
from ws_base.base_ws import BaseElement
from ws_base.base_ws import IosBaseElement
from ws_base.base_android_poco import BaseAndroidPoco
from airtest.cli.parser import cli_setup


class NewGamePage(BaseElement):
    debug_doone = "DoOne"
    victory_play_button = "Button_Play"
    game_goto_home_button = "Button_Back"
    setting_button = "Button_Setting"
    setting_close_button = "Button_Close"
    debug_close_button = "Close"
    switch_tops_button = "TopsSwitch"
    # 设置页面的收藏按钮
    collection_button = "Button_Base"
    # 设置页面的进入调整页面按钮
    language_button = "LanguageButton"
    # 点击法语button
    french_button = "Français"
    # 设置页面contact us 按钮
    contact_us_button = "ContactButton"
    # 设置页面 服务条款button
    terms_service_button = "TermOfServiceButton"
    # 设置页面隐私弹窗button
    privacy_policy_button = "PrivacyButton"
    # 首页宝箱button
    level_chest_button = "Button_LevelChest"
    # 重开道具button
    restart_button = "Button_Restart"
    # 撤回道具button
    undo_button = "Button_Undo"
    # 游戏页面元素
    game_page_ui = "UI_ClassicGame(Clone)"
    # 撤回道具的数量
    undo_number = "front"
    # 加管道具button
    add_button = "Button_AddBottle"
    # 无道具image
    ad_image = "Image_AD"
    # 提示道具按钮
    tips_button = "Button_Tip"
    # 跳过关卡按钮
    skip_level_button = "Button_ForceWin"
    # 开宝箱页面
    chest_page_image = "OneGroup"
    # 开宝箱的第一个奖励
    first_reward = "Item_Prop_1_1"
    # 开宝箱的no，thanks
    no_thanks_button = "Button_NO"
    # 获得瓶子或者球或者背景时点击no ，thanks
    no_use = "Button_Skip"
    # 获得瓶子或者球或者背景时点击use
    use_button = "Button_Use"

    def __init__(self):
        self.BasePoco = BasePoco()
        self.IosBaseElement = IosBaseElement()
        self.BaseAndroidPoco = BaseAndroidPoco()

    def new_debug_win(self, time=40):
        """
        点击debug的win按钮
        :return:
        """
        self.BasePoco.UnityPoco("LayoutGroup").child("DebugButton(Clone)")[9].click()
        self.sleep_time(time)
        return self

    def new_debug_doone(self, times=2):
        """
        点击debug的doone按钮
        :param times:点击几次
        :return:
        """
        for i in range(times):
            self.BasePoco.get_element_pos_click(self.debug_doone)
            self.sleep_time(1)
        return self

    def new_game_victory(self):
        """
        在游戏结算页面点击下一关
        :return:
        """
        self.BasePoco.unity_poco_click(self.victory_play_button)
        return self

    def new_game_back_home(self):
        """
        游戏页面点击返回按钮返回首页
        :return:
        """
        self.BasePoco.get_element_pos_click_name(self.game_goto_home_button)
        return self

    def new_goto_setting_page(self):
        self.BasePoco.get_element_pos_click_name(self.setting_button)
        return self

    def new_setting_close(self):
        self.BasePoco.get_element_pos_click_name(self.setting_close_button)
        return self

    def new_close_debug(self):
        self.BasePoco.get_element_pos_click(self.debug_close_button)
        return self

    def new_change_tops(self):
        self.BasePoco.get_element_pos_click_name(self.switch_tops_button)
        return self

    def new_setting_goto_collection(self):
        """
        从设置页面进入收藏页面
        :return:
        """
        self.BasePoco.get_element_pos_click_name(self.collection_button)
        return self

    def new_setting_goto_language(self):
        """
        从设置页面进入调整语言页面
        :return:
        """
        self.BasePoco.poco_for_pos_click(self.language_button, [0.9, 0.9])
        return self

    def new_change_language_french(self):
        """
        调整至法语
        :return:
        """
        self.BasePoco.get_element_pos_click(self.french_button)
        return self

    def new_goto_contact_us(self):
        """
        设置页面进入邮件页面
        :return:
        """
        self.BasePoco.poco_for_pos_click(self.contact_us_button, [0.9, 0.9])
        return self

    def new_setting_goto_terms_service(self):
        """
        设置页面进入服务条款h5页面
        :return:
        """
        self.BasePoco.unity_poco_click(self.terms_service_button)
        return self

    def new_setting_goto_privacy_policy(self):
        """
        设置页面进入隐私协议h5页面
        :return:
        """
        self.BasePoco.unity_poco_click(self.privacy_policy_button)
        return self

    def new_goto_chest_page(self):
        self.BasePoco.unity_poco_click(self.level_chest_button)
        return self

    def new_click_restart_tool(self):
        """
        点击重开按钮
        :return:
        """
        self.BasePoco.get_element_pos_click_name(self.restart_button)
        return self

    def new_click_undo_tool(self):
        """
        点击撤回按钮
        :return:
        """
        self.BasePoco.unity_poco_click(self.undo_button)
        return self

    def get_withdraw_number(self):
        withdraw_number = self.BasePoco.poco_offspring_get_text(self.game_page_ui, self.undo_button, self.undo_number)
        print(withdraw_number)
        return withdraw_number

    def get_add_tube_number(self):
        add_tube_number = self.BasePoco.poco_offspring_get_text(self.game_page_ui, self.add_button, self.undo_number)
        print(add_tube_number)
        return add_tube_number

    def get_add_tube_ad(self):
        """
        没有加管道具状态
        :return:
        """
        ad_tube_number = self.BasePoco.poco_offspring_get_name(self.game_page_ui, self.add_button, self.ad_image)
        print(ad_tube_number)
        return ad_tube_number

    def new_click_add_tube(self):
        """
        点击加瓶按钮
        :return:
        """
        self.BasePoco.get_element_pos_click_name(self.add_button)
        return self

    def new_click_tips_tool(self):
        """
        点击提示道具
        :return:
        """
        self.BasePoco.get_element_pos_click_name(self.tips_button)
        return self

    def new_get_tips_number(self):
        """
        有提示道具时，出现提示道具的数量
        :return:
        """
        tips_tool_number = self.BasePoco.poco_offspring_get_text(self.game_page_ui, self.tips_button, self.undo_number)
        print(tips_tool_number)
        return tips_tool_number

    def new_no_tips_name(self):
        """
        没有提示道具时得到对应的name
        :return:
        """
        ad_tips_number = self.BasePoco.poco_offspring_get_name(self.game_page_ui, self.tips_button, self.ad_image)
        print(ad_tips_number)
        return ad_tips_number

    def skip_level(self):
        self.BasePoco.get_element_pos_click_name(self.skip_level_button)
        return self

    def ads_banner(self):
        """
        游戏页面去除广告横幅
        :return:
        """
        self.BasePoco.get_element_pos_click_name(self.setting_close_button, 0)
        return self

    def get_chest_first_number(self):
        self.BasePoco.poco_offspring_get_text(self.chest_page_image, self.first_reward, self.undo_number)
        return self

    def new_get_chest_no_double(self):
        """
        开宝箱之后选择no_thanks
        :return:
        """
        self.BasePoco.get_element_pos_click_name(self.no_thanks_button)
        return self

    def new_click_no_thanks(self):
        self.BasePoco.get_element_pos_click_name(self.no_use, 0)
        return self

    def new_click_use(self):
        self.BasePoco.get_element_pos_click_name(self.use_button)
        return self




if __name__ == "__main__":
    if not cli_setup():
        auto_setup(__file__, logdir=True, devices=[
            "android://127.0.0.1:5037/R3CW10C3D9N?cap_method=ADBCAP&touch_method=MAXTOUCH&", ])
    NewGamePage().new_click_no_thanks()
