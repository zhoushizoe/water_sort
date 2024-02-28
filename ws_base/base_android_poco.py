from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.cli.parser import cli_setup
from airtest.core.api import *


class BaseAndroidPoco:
    def __init__(self):
        self.AndroidUiautomationPoco = AndroidUiautomationPoco()

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

    def exist_element_click_other(self, element, element2):
        """
        如果存在某个元素，就点击另一个
        :return:
        """
        while True:
            if self.AndroidUiautomationPoco(element).exists():
                print(f"找到元素,进行点击操作{element2}")
                self.android_poco_name_click(element2)
            else:
                print("没有找到元素")
                break
        return self
