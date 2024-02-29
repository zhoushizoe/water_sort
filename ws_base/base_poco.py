from poco.drivers.unity3d import UnityPoco
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.cli.parser import cli_setup
from airtest.core.api import *


class BasePoco:
    def __init__(self):
        self.UnityPoco = UnityPoco()

    def unity_poco_click(self, element):
        self.UnityPoco(element).click()
        sleep(1)
        return self

    def poco_exist_text_click(self, element):
        """
        如果存在某个元素，就点击
        :param element:
        :return:
        """
        if self.UnityPoco(text=element).exists():
            print(f"存在元素{element}")
            self.UnityPoco(text=element).click()
        return self

    def poco_exist(self, element):
        """
        如果存在某个元素，就点击
        :param element:
        :return:
        """
        if self.UnityPoco(element).exists():
            print(f"存在元素{element}")
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
        sleep(1)

    def poco_assert_text(self, element):
        """
        poco的断言方法
        :param element:
        :return:
        """
        try:
            assert self.UnityPoco(text=element)
            print(f"页面存在{element}")
        except AssertionError as e:
            print(f"页面不存在{element}")
            raise e

    def poco_offspring_click(self, element, offspring1, offspring2):
        self.UnityPoco(element).offspring(offspring1).offspring(offspring2).click()
        sleep(1)
        return self

    def poco_offspring_get_text(self, element, offspring1, offspring2):
        """
        得到对应的元素的text属性
        :param element:
        :param offspring1:
        :param offspring2:
        :return:
        """
        get_text = self.UnityPoco(element).offspring(offspring1).offspring(offspring2).attr("text")
        print(get_text)
        return get_text

    def poco_offspring_get_name(self, element, offspring1, offspring2):
        """
        得到对应的元素的text属性
        :param element:
        :param offspring1:
        :param offspring2:
        :return:
        """
        get_name = self.UnityPoco(element).offspring(offspring1).offspring(offspring2).attr("name")
        print(get_name)
        return get_name

    def get_element_pos_click(self, element, add_pos=0.02):
        """
        在页面上得到对应的元素坐标之后,点击元素坐标
        :return:
        """
        pos = self.UnityPoco(text=element).attr("pos")
        pos1 = (pos[0], pos[1] + add_pos)
        print(pos1)
        self.UnityPoco.click(pos1)
        sleep(1)
        return self

    def get_element_pos_click_name(self, element, add_pos=0.02):
        """
        在页面上得到对应的元素坐标之后,点击元素坐标
        :return:
        """
        pos = self.UnityPoco(element).attr("pos")
        pos1 = (pos[0], pos[1] + add_pos)
        print(pos1)
        self.UnityPoco.click(pos1)
        sleep(1)
        return self

    def poco_for_pos_click(self, element, pos):
        """
        点击按钮上的不同坐标
        :return:
        """
        self.UnityPoco(element).focus(pos).click()
        sleep(1)
        return self

    def regular_poco_text(self, element, add_pos=0.02):
        """
        使用正则表达式得到对应的text坐标并点击
        :param element:
        :param add_pos:
        :return:
        """
        pos = self.UnityPoco(textMatches=element).attr("pos")
        pos1 = (pos[0], pos[1] + add_pos)
        print(pos1)
        self.UnityPoco.click(pos1)
        sleep(1)
        return self

