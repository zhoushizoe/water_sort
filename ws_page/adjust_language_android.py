from airtest.cli.parser import cli_setup
from airtest.core.api import *
from poco.drivers.ios import iosPoco
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from ws_page.adjust_time_android import AdjustTime
from ws_base.base_poco import BasePoco

from ws_base.base_ws import BaseElement


class AdjustLanguage(BaseElement):
    coord1 = [1125, 2782]
    coord2 = [1017, 850]

    # def __init__(self, poco):
    #     self.AdjustTime = AdjustTime()
    #     self.BasePoco = BasePoco()
    def get_adjust(self):
        self.AdjustTime = AdjustTime()

    def goto_setting_page(self):
        """
        进入setting页面
        :return:
        """
        self.AdjustTime = AdjustTime()
        # self.BasePoco = poco
        self.AdjustTime.get_system_setting()
        return self

    def goto_language_date(self):
        """
        进入调整语言和日期的设置页面
        :return:
        """
        self.AdjustTime = AdjustTime()
        self.AdjustTime.get_language()
        return self

    def goto_language_page(self):
        """
        进入调整语言的页面
        :return:
        """
        self.BasePoco.AndroidUiautomationPoco("android.widget.FrameLayout").child(
            "android.widget.LinearLayout").offspring(
            "com.android.settings:id/content_frame").child("android.widget.LinearLayout").offspring(
            "com.android.settings:id/recycler_view").child("android.widget.LinearLayout")[0].child(
            "android.widget.RelativeLayout").click()
        return self

    def get_simplified_chinese(self):
        """
        点击简体中文
        :return:
        """

        simplified_chinese = "简体中文（中国）"
        self.BasePoco.find_element(simplified_chinese, self.coord1, self.coord2)
        self.BasePoco.android_poco_click(simplified_chinese)
        return self

    def get_english(self):
        """
        点击英文
        :return:
        """
        english = "English (United States)"
        self.BasePoco.find_element(english, self.coord1, self.coord2)
        self.BasePoco.android_poco_click(english)
        return self

    def click_apply(self):
        for i in range(3):
            swipe(self.coord1, self.coord2)
            sleep(2)
        self.BasePoco.AndroidUiautomationPoco("android.widget.FrameLayout").child(
            "android.widget.LinearLayout").offspring("com.android.settings:id/content_frame").child(
            "android.widget.LinearLayout").offspring("com.android.settings:id/container_material").child(
            "android.widget.ScrollView").child("android.widget.LinearLayout").child(
            "android.widget.ScrollView").offspring("com.android.settings:id/apply_btn_layout").child(
            "android.widget.LinearLayout").offspring("com.android.settings:id/apply_button").click()
        return self


if __name__ == "__main__":
    if not cli_setup():
        auto_setup(__file__, logdir=True, devices=[
            "android://127.0.0.1:5037/R3CW10C3D9N?cap_method=ADBCAP&touch_method=MAXTOUCH&", ])
    AdjustLanguage().get_english().click_apply()
