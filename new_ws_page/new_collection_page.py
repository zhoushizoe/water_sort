from airtest.core.api import auto_setup
from ws_base.base_poco import BasePoco
from ws_base.base_ws import BaseElement
from ws_base.base_ws import IosBaseElement
from ws_base.base_android_poco import BaseAndroidPoco
from airtest.cli.parser import cli_setup
from airtest.core.api import *


class NewCollectionPage(BaseElement):
    # 收藏页面画面元素
    collection_image = "SelectGroup"
    theme_button = "ThemeGroup"
    # 收藏页面tube页面
    collection_tube_page = Template(r"../picture/collect_page_picture/collection_tube_page.png",
                                    record_pos=(0.008, 0.462), resolution=(1440, 3088))
    # 爱心瓶
    love_tube = Template(r"../picture/collect_page_picture/love_tube.png", threshold=0.95, record_pos=(0.31, 0.673),
                         resolution=(1440, 3088))
    # 爱心瓶的盖子
    love_tube_tops = Template(r"../picture/collect_page_picture/love_tube_tops.png", record_pos=(0.283, 0.065),
                              resolution=(1440, 3088))
    # 收藏页面theme页面
    collection_theme_tube = Template(r"../picture/collect_page_picture/collection_theme_tube.png",
                                     record_pos=(0.003, 0.469), resolution=(1440, 3088))
    # 收藏页面的山主题
    mountain_theme = Template(r"../picture/collect_page_picture/mountain_theme.png", threshold=0.9,
                              record_pos=(-0.314, 0.282), resolution=(1440, 3088))
    # 应用之后的山主题
    game_page_mountain = Template(r"../picture/collect_page_picture/game_page_mountion.png", record_pos=(0.007, 0.557),
                                  resolution=(1440, 3088))

    def __init__(self):
        self.BasePoco = BasePoco()
        self.IosBaseElement = IosBaseElement()
        self.BaseAndroidPoco = BaseAndroidPoco()

    def new_goto_theme_page(self):
        """
        收藏页面进入theme页面
        :return:
        """
        self.BasePoco.get_element_pos_click_name(self.theme_button)
        return self

    def new_swipe_bottom(self):
        self.image_swipe([707, 2915], [673, 368])
        return self

    def new_get_coin_theme(self):
        """
        购买600金币的主题
        :return:
        """
        theme_price = "600"
        self.BasePoco.get_element_pos_click(theme_price)
        return self

    def new_choose_love_tube(self):
        """
        切换爱心瓶
        :return:
        """
        self.image_click(self.love_tube)
        return self

    def new_choose_mountain_theme(self):
        """
        切换山主题
        :return:
        """
        self.image_click(self.mountain_theme)
        return self


if __name__ == "__main__":
    if not cli_setup():
        auto_setup(__file__, logdir=True, devices=[
            "android://127.0.0.1:5037/R3CW10C3D9N?cap_method=ADBCAP&touch_method=MAXTOUCH&", ])
    NewCollectionPage().new_get_coin_theme()
