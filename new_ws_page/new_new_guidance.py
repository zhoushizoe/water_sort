from airtest.core.api import auto_setup
from ws_base.base_poco import BasePoco
from ws_base.base_ws import BaseElement
from ws_base.base_ws import IosBaseElement
from ws_base.base_android_poco import BaseAndroidPoco
from airtest.cli.parser import cli_setup


class NewNewGuidance(BaseElement):
    # 倒水的包名
    water_sort_android = "water.sort.puzzle.android.inner"
    # 隐私弹窗的接受按钮
    accept_button = "Button_OK"

    def __init__(self):
        self.BasePoco = BasePoco()
        self.IosBaseElement = IosBaseElement()
        self.BaseAndroidPoco = BaseAndroidPoco()

