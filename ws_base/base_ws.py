# coding = utf-8
# Author: Zoe
# File: base_ws.py
# Time: 2023/10/16 11:14 上午
"""
如果要使用poco进行点击操作的话，需要调用放在之后

"""
from airtest.cli.parser import cli_setup
from airtest.core.api import *
from poco.drivers.ios import iosPoco
from poco.drivers.android.uiautomation import AndroidUiautomationPoco


class BaseElement:
    def clear_app(self, package):
        """
        清除应用数据（仅安卓）
        :param package:
        :return:
        """
        clear_app(package)
        return self

    def uninstall_ios(self, package):
        """
        卸载应用，安卓与ios通用
        :param package:
        :return:
        """
        uninstall(package)
        sleep(4)
        return self

    def uninstall(self, package):
        """
        卸载应用，安卓与ios通用
        :param package:
        :return:
        """
        uninstall(package)
        self.sleep_time()
        return self

    def install_ios(self, package):
        install(package)
        self.sleep_time()
        return self

    def install(self, package):
        """
        安装应用（安卓与iOS通用）
        :param package:
        :return:
        """
        install(package)
        self.sleep_time()
        return self

    def image_click(self, image, times=1):
        """
        使用图片或者绝对坐标进行点击（iOS与安卓通用）
        :param image:
        :param times:
        :return:
        """
        touch(image, times)
        return self

    # def poco_click(self, element):
    #     """
    #     使用poco元素点击
    #     :param element:
    #     :return:
    #     """
    #     poco = UnityPoco()
    #     poco(element).click()
    #     return self

    # 使用图像识别拖动

    def image_swipe(self, place, to):
        """
        使用图片或者坐标进行滑动（iOS与安卓通用）
        :param place:
        :param to:
        :return:
        """
        swipe(place, to)
        return self

    def stop_app(self, package):
        """
        杀掉应用进程（iOS与安卓通用）
        :param package:
        :return:
        """
        stop_app(package)
        sleep(2)
        return self

    def start_app(self, package):
        """
        打开应用（目前iOS17不支持）
        :param package:
        :return:
        """
        start_app(package)
        sleep(5)
        return self

    # 删除输入的文字
    def delete_word(self):
        """
        删除文字（安卓独有）
        :return:
        """
        keyevent("KEYCODE_DEL")
        sleep(0.5)
        return self

    # 输入所需要的文字
    def input_word(self, word):
        """
        输入文字（安卓独有）
        :param word:
        :return:
        """
        text(word)
        self.sleep_time(1)
        return self

    def get_snapshot(self, filename, language):
        """
        截图，多语言的时候需要文件名和语言（安卓 iOS通用）
        :param filename:截图的内容
        :param language:语言
        :return:
        """
        snapshot(filename=language + filename + ".png")
        return self

    def snapshot_log(self, filename):
        """
        仅仅需要截图log时候的截图（（安卓iOS通用））
        :param filename:
        :return:
        """
        snapshot(filename=filename + ".png")
        return self

    def sleep_time(self, second=2):
        """
        睡眠时间，默认是两秒
        :param second:
        :return:
        """
        sleep(second)
        return self

    # 进行图片点击操作时同时使用坐标点击
    def image_click_plus(self, image, coordinate):
        """
        防止图片找不到，做一个判断语句，如果有图片就点击图片，否则用坐标点击
        :param image:图片
        :param coordinate:坐标
        :return:
        """
        wait(image)
        if exists(image):
            self.image_click(image)
        else:
            self.image_click(coordinate)
        return self

    def system_keyevent(self, para):
        """
        封装的一些键盘操作，部分iOS可用
        :param para: back：返回键；HOME：回到手机首页；
        :return:
        """
        keyevent(para)
        return self

    def image_click_coord(self, picture, coord):
        """
        判断是否存在某一个图片，如果存在，点击对应的坐标
        :return:
        """
        if exists(picture):
            self.image_click(coord)
        return self

    def assert_poco(self, image, element, timeout=3):
        """
        如果存在poco元素，就进行点击，如果不存在，就进行图片点击
        :param image:
        :param element:
        :return:
        """
        poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
        poco(element).wait(timeout)
        if poco(element).exists():
            poco(element).click()
        else:
            self.image_click(image)
        return self

    def wait_image(self, image):
        """
        等待某个图片出现
        :param image:
        :return:
        """
        wait(image)
        return self

    # def wait_poco(self, element, timeout=3):
    #     """
    #     等待三秒，出现对应的poco元素，如果出现就点击操作
    #     :param element:
    #     :param timeout:
    #     :return:
    #     """
    #     poco = UnityPoco()
    #     poco(element).wait(timeout).click()
    #     return self

    def exists_assert(self, correct_result):
        """
        断言存在
        :param correct_result:
        :return:
        """
        try:
            assert_exists(correct_result)
            print(f"页面存在图片{correct_result}")
        except AssertionError as e:
            print(f"页面不存在图片{correct_result}")
            raise e
        self.sleep_time(5)

    def assert_equal(self, correct_data, actually_data):
        """
        断言相等
        :param correct_data:
        :param actually_data:
        :return:
        """
        if correct_data == actually_data:
            assert True
        else:
            print(f"{correct_data}不等于{actually_data}")
            assert False

    def not_exists_assert(self, correct_result):

        """
        断言存在
        :param correct_result:
        :return:
        """
        try:
            assert_not_exists(correct_result)
            print(f"页面不存在图片{correct_result}")
        except AssertionError as e:
            print(f"页面存在图片{correct_result}")
            raise e


class IosBaseElement:
    """
    封装关于iOS特殊的一些操作
    """

    def ios_delete_text(self, number=3):
        """
        ios中删除输入的字符
        :return:
        """
        for i in range(number):
            text("\b", enter=False)
        return self

    def ios_inter_word(self, word, enter=False):
        """
          iOS的text()接口默认会在给定的输入字符后面加一个换行符 \n 。
          如果不想要输入之后出现换行的效果，可以把enter = False传到text()接口里面
        :return: 
        """""

        text(word, enter)
        return self

    def goback_home(self):
        """
        将应用回到后台，回到手机主页
        :return:
        """
        keyevent("HOME")
        return self

    def ios_open_app(self, app_name):
        """
        airtest中的[start_app]不支持iOS17
        游戏的名称永远是英文的，所以使用poco的方式打开应用
        :param app_name:app在首页显示的应用名字
        :return:
        """
        poco = iosPoco()
        poco(app_name).click()
        return self


if __name__ == "__main__":
    if not cli_setup():
        auto_setup(__file__, logdir=True, devices=[
            "ios:///http://127.0.0.1:8300", ])
    # unity_poco = UnityPoco()
    # BaseElement().assert_poco()
