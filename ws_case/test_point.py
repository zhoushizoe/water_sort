import pytest
from airtest.cli.parser import cli_setup
from airtest.core.api import *
from ws_base.base_ws import BaseElement
from ws_page.policy_page import PolicyPage
from ws_base.base_point import GetPoint
from ws_base.base_point_user import GetPointUser


class TestPoint(BaseElement,GetPointUser,GetPoint):
    def setup_class(self):
        auto_setup(__file__, logdir=True,
                   devices=["android://127.0.0.1:5037/R3CW10C3D9N?cap_method=ADBCAP&touch_method=MAXTOUCH&", ])

    def import_class(self):
        self.PolicyPage = PolicyPage()

    def test1_app_first_open(self):
        """
        app_first_open
        首次启动游戏	玩家安装游戏首次打开时上报生命周期内仅上报一次
        :return:
        """
        point = "app_first_open"
        self.import_class()
        self.clear_command()
        self.PolicyPage.first_start_android()
        self.PolicyPage.close_information_page()
        self.sleep_time()
        self.contrast_step(point)
