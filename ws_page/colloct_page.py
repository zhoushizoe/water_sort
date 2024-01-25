from ws_base.base_ws import BaseElement
from airtest.core.api import *
from airtest.cli.parser import cli_setup
from ws_base.base_poco import BasePoco


class CollectPage(BaseElement):
    purchase_theme_600 = Template(r"../picture/collect_page_picture/purchase_theme_600.png", record_pos=(-0.309, 0.58),
                                  resolution=(1440, 3088))
    purchase_theme_1500_button = Template(r"../picture/collect_page_picture/purchase_theme_1500_button.png",
                                          record_pos=(0.327, 0.579), resolution=(1440, 3088))

    # def __init__(self, poco):
    #     self.BasePoco = poco

    def change_skin(self):
        """
        切换第二个皮肤
        :return:
        """
        self.image_click([737, 1332])
        return self

    def change_theme(self):
        """
        法语情况下切换到theme页面
        :return:
        """
        self.image_click([712, 943])
        return self

    def swipe_bottom(self):
        """
        滑到主题的底部
        :return:
        """
        self.image_swipe([707, 2915], [673, 368])
        return self

    def purchase_theme(self):
        """
        花600金币购买主题
        :return:
        """
        self.image_click(self.purchase_theme_600)
        return self

    def purchase_theme_1500(self):
        """
        花1500金币买主题
        :return:
        """
        self.image_click(self.purchase_theme_1500_button)
        return self
