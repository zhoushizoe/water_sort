from airtest.core.api import auto_setup
from ws_base.base_poco import BasePoco
from ws_base.base_ws import BaseElement
from ws_base.base_ws import IosBaseElement
from ws_base.base_android_poco import BaseAndroidPoco
from airtest.cli.parser import cli_setup


class NewHomePage(BaseElement):
    #
    debug_enter_first_text = "Enter text..."
    debug_close_button = "closeButton"
    debug_get_coin_button = "PingZi_Lan"
    home_level_button = "Button"
    # 首页购买广告按钮
    ads_purchase_button = "Button_ADS"
    # 首页宝箱按钮
    level_chest_button = "Button_LevelChest"
    # 首页宝箱页面continue按钮
    chest_continue = "Button_OK"
    # 首页宝箱页面的关闭按钮
    chest_close_button = "Button_Close"
    # debug展开按钮
    debug_expand = "Open"
    # 首页金币
    coin_image = "CoinGroup"
    # 金币按钮文案
    coin_text = "CoinText"
    # 数量
    item_number = "front"
    # 弹出的challenge弹窗上的继续按钮
    challenge_continue = "Button_Go"
    # 弹出的challenge弹窗上的no， thanks按钮
    challenge_no = "Button_No"
    # 首页challenge按钮
    challenge_button = "Challenge"

    def __init__(self):
        self.BasePoco = BasePoco()
        self.IosBaseElement = IosBaseElement()
        self.BaseAndroidPoco = BaseAndroidPoco()

    def new_get_debug(self):
        """
        得到debug的工具栏
        :return:
        """
        self.image_click([782, 1262], times=10)
        self.BasePoco.UnityPoco("LayoutGroup").child("DebugButton(Clone)")[1].click()
        self.BasePoco.get_element_pos_click(self.debug_enter_first_text)
        self.BasePoco.unity_poco_click(self.debug_close_button).unity_poco_click(self.debug_close_button)
        self.sleep_time()
        return self

    def new_get_level_android(self, level):
        """
        使用debug得到想要的关卡
        :param level:
        :return:
        """
        level_enter = "Enter text..."
        self.BasePoco.UnityPoco("LayoutGroup").child("DebugButton(Clone)")[1].click()
        self.BasePoco.get_element_pos_click(self.debug_enter_first_text)
        for i in range(4):
            self.delete_word()
        self.input_word(level)
        self.sleep_time(1)
        self.BasePoco.unity_poco_click(self.debug_close_button).unity_poco_click(self.debug_close_button)
        return self

    def new_debug_get_coin(self, coin_number):
        """
        使用debug得到金币
        :return:
        """
        self.BasePoco.UnityPoco("LayoutGroup").child("DebugButton(Clone)")[1].click()
        self.BasePoco.get_element_pos_click_name(self.debug_get_coin_button)
        for i in range(4):
            self.delete_word()
        self.input_word(coin_number)
        self.sleep_time(1)
        self.BasePoco.unity_poco_click(self.debug_close_button).unity_poco_click(self.debug_close_button)
        return self

    def new_goto_game_page(self):
        self.BasePoco.unity_poco_click(self.home_level_button)
        return self

    def new_ads_purchase(self):
        """
        首页点击购买广告弹窗
        :return:
        """
        self.BasePoco.get_element_pos_click_name(self.ads_purchase_button)
        return self

    def new_goto_level_chest_page(self):
        """
        首页点击宝箱
        :return:
        """
        self.BasePoco.unity_poco_click(self.level_chest_button)
        return self

    def new_chest_continue(self):
        """
        宝箱页面点击继续按钮
        :return:
        """
        self.BasePoco.unity_poco_click(self.chest_continue)
        return self

    def new_chest_close(self):
        """
        点击宝箱页面的关闭按钮
        :return:
        """
        self.BasePoco.get_element_pos_click_name(self.chest_close_button)
        return self

    def new_expand_debug(self):
        """
        展开debug
        :return:
        """
        self.BasePoco.get_element_pos_click(self.debug_expand, 0.03)
        return self

    def get_coin_number(self):
        coin_number = self.BasePoco.poco_offspring_get_text(self.coin_image, self.coin_text, self.item_number)
        print(coin_number)
        return coin_number

    def challenge_page_no_thanks(self):
        """
        达到条件后首次返回首页弹出挑战模式弹窗，点击no，thanks
        :return:
        """
        self.BasePoco.get_element_pos_click_name(self.challenge_no, 0)
        # self.BasePoco.poco_exist(self.challenge_no)
        return self

    def challenge_page_continue(self):
        """
         达到条件后首次返回首页弹出挑战模式弹窗，点击continue
        :return:
        """
        self.BasePoco.poco_exist(self.challenge_continue)
        return self

    def new_goto_challenge_page(self):
        """
        从首页点击进入挑战模式首页
        :return:
        """
        self.BasePoco.get_element_pos_click(self.challenge_button, 0)
        return self


if __name__ == "__main__":
    if not cli_setup():
        auto_setup(__file__, logdir=True, devices=[
            "android://127.0.0.1:5037/R3CW10C3D9N?cap_method=ADBCAP&touch_method=MAXTOUCH&", ])
    NewHomePage().new_goto_challenge_page()
