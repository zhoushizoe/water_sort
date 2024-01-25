from poco.drivers.unity3d import UnityPoco
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.cli.parser import cli_setup
from airtest.core.api import *


class BasePoco:
    def __init__(self):
        self.AndroidUiautomationPoco = AndroidUiautomationPoco()
        self.UnityPoco = UnityPoco()

    def android_poco_click(self, element):
        """
        poco元素的简单点击操作
        :param element:
        :return:
        """
        self.AndroidUiautomationPoco(text=element).click()
        return self

    def android_poco_name_click(self, element):
        self.AndroidUiautomationPoco(name=element).click()
        return self

    def find_element(self, element, coord1, coord2):
        """
        如果页面上没有元素，滑动屏幕
        :param element:
        :return:
        """
        while True:
            if self.AndroidUiautomationPoco(text=element).exists():
                print("找到元素")
                break  # 如果找到元素，则跳出循环
            else:
                print("没有找到元素")
                swipe(coord1, coord2)
        return self

    def unity_poco_click(self, element):
        self.UnityPoco(element).click()
        return self

    def poco_exist(self, element):
        """
        如果存在某个元素，就点击
        :param element:
        :return:
        """
        if self.UnityPoco(element).exists():
            self.UnityPoco(element).click()
        return self

    def poco_assert(self, element):
        """
        poco的断言方法
        :param element:
        :return:
        """
        try:
            assert self.UnityPoco(element)
            print(f"页面存在{element}")
        except AssertionError as e:
            print(f"页面不存在{element}")
            raise e

    def poco_offspring_click(self, element, offspring1, offspring2):
        self.UnityPoco(element).offspring(offspring1).offspring(offspring2).click()
        return self
