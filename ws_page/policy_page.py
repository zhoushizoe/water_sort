# coding = utf-8
# Author: Zoe
# File: policy_page.py
# Time: 2023/10/16 2:19 下午
from ws_base.base_ws import BaseElement
from ws_base.base_ws import IosBaseElement
from airtest.core.api import *
from airtest.cli.parser import cli_setup
from ws_base.app_base_ws import WaterSortApp
from ws_page.guidance_page import NewGuidance


class PolicyPage(BaseElement, WaterSortApp, IosBaseElement):
    """
    首次打开游戏，进入隐私弹窗页面
    """
    policy_iknow_button = Template(r"../picture/policy_page_picture/policy_button.png", target_pos=6,
                                   record_pos=(-0.201, 0.21), resolution=(1096, 2560))
    close_log_listen = Template(r"../picture/policy_page_picture/close_log_listen.png", record_pos=(-0.099, -0.133),
                                resolution=(1096, 2560))
    terms_of_service = Template(r"../picture/policy_page_picture/terms_of_service.png", record_pos=(-0.117, -0.15),
                                resolution=(1096, 2560))
    privacy_policy = Template(r"../picture/policy_page_picture/privacy_policy.png", target_pos=8,
                              record_pos=(-0.237, -0.131), resolution=(1096, 2560))
    privacy_close = Template(r"../picture/policy_page_picture/privacy_close.png", record_pos=(0.0, 1.058),
                             resolution=(1096, 2560))
    information_image = Template(r"../picture/policy_page_picture/information_image.png", record_pos=(-0.001, 0.45),
                                 resolution=(1440, 3088))

    water_sort_ios_package = 'ios.water.sort.puzzle.inner'
    water_sort_ios_install = r"/Users/amber/Downloads/1108_1840/WaterSort.ipa"
    water_sort_android = "water.sort.puzzle.android.inner"
    package_name = "Water Sort"

    def first_start_ios(self):
        """
        iOS的首次打开游戏，弹出隐私弹窗
        :return:
        """
        # 卸载iOS包
        self.uninstall_ios(self.water_sort_ios_package)
        self.sleep_time()
        # 安装iOS包
        self.install_ios(self.water_sort_ios_install)
        # 首次打开iOS包
        self.ios_open_app(self.package_name)
        self.sleep_time()
        self.image_click([644, 1739])
        self.sleep_time()
        self.image_click([640, 1570])
        self.sleep_time()
        self.image_click([644, 1570])
        return self

    def first_start_android(self):
        """
        首次打开安卓
        :return:
        """
        self.clear_app(self.water_sort_android)
        self.sleep_time(1)
        self.first_start_app(self.water_sort_android)
        self.sleep_time()
        return self

    def close_information_page(self):
        """
        首次进入游戏，会出现是否接受通知的弹窗，选择通知
        :return:
        """
        if exists(self.information_image):
            self.image_click([712, 2482])
        else:
            return
        return self

    def goto_guidance(self):
        """
        点击隐私弹窗的i know按钮，进入新手引导
        :return: return 到新手引导页面：NewGuidance()
        """
        self.image_click_plus(self.policy_iknow_button, [711, 1928])
        self.sleep_time()
        return NewGuidance()

    # 关闭开启游戏时的日志弹窗
    def close_log(self):
        """
        安卓每次启动游戏都会有一个日志弹窗，没用，可以关闭
        :return:
        """
        self.image_click_plus(self.close_log_listen, [137, 1405])
        return self

    # 点击进入tos隐私弹窗页面
    def goto_tos(self):
        self.image_click(self.terms_of_service)
        sleep(3)
        return self

    # 点击进入pp隐私页面
    def goto_pp(self):
        self.image_click(self.privacy_policy)
        return self

    # 进入隐私弹窗后，点击close按钮回到引导弹窗
    def privicy_close(self):
        """
        进入隐私弹窗网页之后回到隐私弹窗页面
        :return:
        """
        self.image_click_plus(self.privacy_close, [747, 2915])
        return self

    def android_automate_process(self):
        """
        从首次打开游戏到进入新手引导全流程
        :return:
        """
        self.first_start_android().close_information_page().close_log().privicy_close().goto_guidance()
        return NewGuidance()


if __name__ == "__main__":
    if not cli_setup():
        auto_setup(__file__, logdir=True, devices=[
            "android://127.0.0.1:5037/R3CW10C3D9N?cap_method=MINICAP&touch_method=MAXTOUCH&", ])
    PolicyPage().first_start_android().close_information_page().close_log().privicy_close().goto_guidance()
