from airtest.core.api import auto_setup
from ws_base.base_poco import BasePoco
from ws_base.base_ws import BaseElement
from ws_base.base_ws import IosBaseElement
from ws_base.base_android_poco import BaseAndroidPoco
from airtest.cli.parser import cli_setup


class NewPolicyPage(BaseElement):
    # 倒水的包名
    water_sort_android = "water.sort.puzzle.android.inner"
    # 隐私弹窗的接受按钮
    accept_button = "Button_OK"

    def __init__(self):
        self.BasePoco = BasePoco()
        self.IosBaseElement = IosBaseElement()
        self.BaseAndroidPoco = BaseAndroidPoco()

    def first_open_android_app(self):
        """
       首次打开安卓
       :return:
       """
        information_button = "com.android.permissioncontroller:id/permission_icon"
        allow_button = "com.android.permissioncontroller:id/permission_allow_button"
        self.clear_app(self.water_sort_android)
        self.sleep_time(1)
        self.start_app(self.water_sort_android)
        self.sleep_time()
        self.BaseAndroidPoco.exist_element_click_other(information_button, allow_button)
        return self

    def accept_goto_guidance(self):
        """
        在隐私弹窗页面点击接受按钮进入新手引导
        :return:
        """
        self.BasePoco.unity_poco_click(self.accept_button)
        return self


if __name__ == "__main__":
    if not cli_setup():
        auto_setup(__file__, logdir=True, devices=[
            "android://127.0.0.1:5037/R3CW10C3D9N?cap_method=ADBCAP&touch_method=MAXTOUCH&", ])
    NewPolicyPage().first_open_android_app()
