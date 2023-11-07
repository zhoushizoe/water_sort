# coding = utf-8
# Author: Zoe
# File: adjust_time.py
# Time: 2023/11/3 16:49
from ws_base.base_ws import BaseElement
from airtest.core.api import *
from airtest.cli.parser import cli_setup


class AdjustTime(BaseElement):
    phone_home = Template(r"../picture/phone_system/phone_home.png", record_pos=(-0.004, -0.162),
                          resolution=(1440, 3088))
    setting_button = Template(r"../picture/phone_system/setting_button.png", threshold=0.8, record_pos=(-0.119, -0.692),
                              resolution=(1440, 3088))
    time_and_language_button = Template(r"../picture/phone_system/time_and_language_button.png", threshold=0.9,
                                        record_pos=(-0.413, -0.204), resolution=(1440, 3088))
    iphone_setting_button = Template(r"../picture/phone_system/iphone_setting_button.png", record_pos=(0.111, 0.419),
                                     resolution=(1284, 2778))
    iphone_generic_button = Template(r"../picture/phone_system/iphone_generic_button.png", record_pos=(-0.376, 0.696),
                                     resolution=(1284, 2778))

    water_sort_icon = Template(r"../picture/phone_system/water_sort_icon.png", record_pos=(-0.343, 0.424),
                               resolution=(1284, 2778))
    monday = [358, 2034]
    tuesday = [537, 2025]
    wednesday = [721, 2034]
    thursday = [895, 2039]
    friday = [1074, 2029]
    saturday = [1253, 2025]
    sunday = [183, 2167]

    def get_setting_button(self):
        keyevent("HOME")
        sleep(2)
        if exists(self.phone_home):
            self.image_swipe([616, 1892], [696, 767])
            sleep(1)

        if not exists(self.setting_button):
            self.image_click([767, 2844])
        return self

    def get_language(self):
        self.image_click(self.setting_button)
        sleep(1)
        for i in range(2):
            if not exists(self.time_and_language_button):
                swipe([868, 2698], [759, 272])
        if exists(self.time_and_language_button):
            self.image_click(self.time_and_language_button)
        sleep(1)
        self.image_click([417, 1552])
        return self

    def adjust_date_mon(self, date):
        """
        调整到周一的时间
        :return:
        """
        # 点击进入调整日期页面
        self.image_click([776, 840])
        self.sleep_time(1)
        # 调整到周一的日期
        self.image_click(date)
        # 点击确定
        self.image_click([1024, 2704])
        return self

    def check_push(self):
        """
        下拉拦，查看推送
        :return:
        """
        self.image_swipe([877, 13], [955, 1804])
        self.sleep_time(2)
        return self

    def push_back_setting(self):
        """
        从push推送页面回到设置页面
        :return:
        """
        self.image_click([206, 2443])
        self.sleep_time(1)
        return self

    def ios_setting(self):
        """
        ios的设置按钮点击
        :return:
        """
        keyevent("HOME")
        if exists(self.iphone_setting_button):
            self.image_click(self.iphone_setting_button)
        else:
            self.image_swipe([470, 2028], [1071, 2073])
        if exists(self.iphone_setting_button):
            self.image_click(self.iphone_setting_button)
        return self

    def ios_generic(self):
        # 点击iOS的通用
        if exists(self.iphone_generic_button):
            self.image_click(self.iphone_generic_button)
        return self

    def date_time(self):
        # iphone 13 pro max 的日期与时间坐标
        self.image_click([481, 1923])
        # iphone 13 pro max 进入调整时间页面
        self.image_click([675, 900])
        return self

    def adjust_start_time(self):
        # iphone 13 pro max 的原始日期调整
        self.image_click([1121, 1423])
        self.sleep_time()
        self.image_click([54, 198], times=2)
        keyevent("HOME")
        self.image_swipe([1067, 2152], [81, 2058])
        return self

    def ios_push_adjust_time(self, date):
        # iphone 13 pro max 的push日期调整
        self.image_click(date)
        self.sleep_time()
        self.image_click([54, 198], times=2)
        keyevent("HOME")
        # 下拉菜单
        self.image_swipe([1067, 2152], [81, 2058])
        # 查看通知
        self.image_swipe([252, 4], [252, 1891])
        self.sleep_time()
        self.image_swipe([247, 2044], [256, 1405])
        return self

    def ios_goback_home(self):
        """
        从通知栏回到首页
        :return:
        """
        self.image_swipe([553, 2693], [599, 108])
        self.sleep_time()
        return self

    def goto_game(self):
        if exists(self.water_sort_icon):
            self.image_click(self.water_sort_icon)
        else:
            self.image_swipe([1067, 2152], [81, 2058])
        if exists(self.water_sort_icon):
            self.image_click(self.water_sort_icon)
            return self


if __name__ == "__main__":
    if not cli_setup():
        auto_setup(__file__, logdir=True, devices=[
            "ios:///http://127.0.0.1:8300", ])
    AdjustTime().ios_setting().ios_generic()
