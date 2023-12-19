from airtest.cli.parser import cli_setup
from airtest.core.api import *
from poco.drivers.ios import iosPoco
from ws_base.base_ws import BaseElement
from poco.drivers.android.uiautomation import AndroidUiautomationPoco


class AdjustTime(BaseElement):
    setting_button = Template(r"../picture/phone_system/setting_button.png", threshold=0.8, record_pos=(-0.119, -0.692),
                              resolution=(1440, 3088))
    system_setting_button = "Settings"
    google_search = "com.google.android.googlequicksearchbox:id/googleapp_search_widget_background_protection"
    time_and_language_button = Template(r"../picture/phone_system/time_and_language_button.png", threshold=0.9,
                                        record_pos=(-0.413, -0.204), resolution=(1440, 3088))
    date_and_time = "Date and time"
    # poco的set_date
    set_date = "Set date"
    # poco的日期调整：Saturday, December 30, 2023
    december_30 = "Saturday, December 30, 2023"
    # pcco的确定调整日期
    Done = "Done"

    def get_system_setting(self):
        poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
        self.system_keyevent("HOME")
        if poco(self.google_search).exists():
            self.image_swipe([616, 1892], [696, 767])
        self.assert_poco(self.setting_button, self.system_setting_button)
        return self

    def get_language(self):
        sleep(1)
        for i in range(2):
            if not exists(self.time_and_language_button):
                swipe([868, 2698], [759, 272])
        if exists(self.time_and_language_button):
            self.image_click(self.time_and_language_button)
        sleep(1)
        return self

    def goto_date_and_time(self):
        """
        进入调整时间和日期的页面
        :return:
        """
        self.assert_poco([417, 1552],self.date_and_time)
        return self

    def setting_date(self):
        self.assert_poco([211, 761], self.set_date)
        return self

    def change_date(self):
        self.assert_poco([1283, 2354], self.december_30)
        self.assert_poco([993, 2698], self.Done)
        return self

    def all_change_date(self):
        """
        调整日期的全流程
        :return:
        """
        self.get_system_setting().get_language().goto_date_and_time().setting_date().change_date()
        return self


if __name__ == "__main__":
    if not cli_setup():
        auto_setup(__file__, logdir=True, devices=[
            "android://127.0.0.1:5037/R3CW10C3D9N?cap_method=ADBCAP&touch_method=MAXTOUCH&", ])
    AdjustTime().all_change_date()
