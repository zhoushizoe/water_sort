# coding = utf-8
# Author: Zoe
# File: victory_step.py
# Time: 2023/10/20 6:20 下午
from ws_base.base_ws import BaseElement
from airtest.core.api import *
from airtest.cli.parser import cli_setup


class VictoryStep(BaseElement):
    use_button = Template(r"../picture/game_page_picture/use_button.png", record_pos=(-0.203, 0.35),
                          resolution=(1096, 2560))

    def tube_position(self, position):
        self.image_click(position)
        sleep(1.5)
        return self

    def debug_win(self, second):
        self.image_click([770, 39])
        sleep(second)
        return self

    def rewards_get_button(self):
        self.image_click(self.use_button)
        sleep(4)
        return self

    def pass_level(self):
        self.image_click([44, 44])
        sleep(1)
        return self

    def thirteenth_level(self):
        """
        第十三关
        :return:
        """
        third_tube = [515, 912]
        fourth_tube = [727, 864]
        sixth_tube = [231, 1474]
        seventh_tube = [453, 1549]
        ninth_tube = [845, 1592]
        self.tube_position(third_tube).tube_position(seventh_tube). \
            tube_position(fourth_tube).tube_position(ninth_tube). \
            tube_position(third_tube).tube_position(sixth_tube)

    def twelve_level(self):
        """
        第十二关通关
        :return:
        """
        first_tube = [185, 938]
        second_tube = [436, 894]
        third_tube = [687, 929]
        fourth_tube = [933, 837]
        fifth_tube = [308, 1493]
        sixth_tube = [541, 1559]
        seventh_tube = [766, 1445]
        self.tube_position(second_tube).tube_position(fourth_tube). \
            tube_position(third_tube).tube_position(fourth_tube). \
            tube_position(first_tube).tube_position(third_tube)
        return self

    def twenty_level(self):
        """
        二十关通关
        :return:
        """
        first_tube = [113, 888]
        second_tube = [321, 940]
        third_tube = [533, 949]
        sixth_tube = [264, 1497]
        self.tube_position(first_tube).tube_position(third_tube). \
            tube_position(sixth_tube).tube_position(second_tube). \
            tube_position(third_tube).tube_position(sixth_tube)
        return self

    def twenty_four(self):
        """
        第二十四关通关
        :return:
        """
        first_tube = [185, 938]
        second_tube = [436, 894]
        third_tube = [687, 929]
        fourth_tube = [933, 837]
        self.tube_position(second_tube).tube_position(third_tube).\
            tube_position(fourth_tube).tube_position(third_tube).\
            tube_position(fourth_tube).tube_position(first_tube)
        return self
        pass

    def thirty_fifth_level(self):
        """
        第三十五关通关的最后几步
        :return:
        """
        first_tube = [101, 995]
        second_tube = [295, 956]
        third_tube = [449, 889]
        fourth_tube = [638, 1008]
        fifth_tube = [793, 956]
        sixth_tube = [978, 903]
        seventh_tube = [220, 1537]
        eighth_tube = [383, 1449]
        ninth_tube = [533, 1533]
        tenth_tube = [678, 1515]
        eleventh_tube = [898, 1519]
        self.tube_position(fifth_tube).tube_position(first_tube). \
            tube_position(third_tube).tube_position(fourth_tube). \
            tube_position(fifth_tube).tube_position(fourth_tube)
        return self

    def fortieth_level(self):
        """
        第四十关解锁
        :return:
        """
        first_tube = [101, 995]
        second_tube = [295, 956]
        third_tube = [449, 889]
        fourth_tube = [638, 1008]
        fifth_tube = [793, 956]
        sixth_tube = [978, 903]
        seventh_tube = [220, 1537]
        eighth_tube = [383, 1449]
        ninth_tube = [533, 1533]
        tenth_tube = [678, 1515]
        eleventh_tube = [898, 1519]
        self.tube_position(fifth_tube).tube_position(ninth_tube). \
            tube_position(second_tube).tube_position(fifth_tube). \
            tube_position(second_tube).tube_position(sixth_tube). \
            tube_position(fourth_tube).tube_position(fifth_tube). \
            tube_position(second_tube).tube_position(eleventh_tube). \
            tube_position(third_tube).tube_position(fourth_tube)
        return self

    def fiftieth_level(self):
        """
        第五十关最后几步
        :return:
        """
        first_tube = [101, 995]
        second_tube = [295, 956]
        third_tube = [449, 889]
        fourth_tube = [638, 1008]
        fifth_tube = [793, 956]
        sixth_tube = [978, 903]
        seventh_tube = [220, 1537]
        eighth_tube = [383, 1449]
        ninth_tube = [533, 1533]
        tenth_tube = [678, 1515]
        eleventh_tube = [898, 1519]
        self.tube_position(first_tube).tube_position(fifth_tube). \
            tube_position(fourth_tube).tube_position(sixth_tube)

    def sixtieth_level(self):
        """
        第六十关最后几步
        :return:
        """
        first_tube = [114, 969]
        second_tube = [356, 916]
        third_tube = [559, 911]
        fourth_tube = [753, 978]
        fifth_tube = [956, 947]
        sixth_tube = [273, 1546]
        seventh_tube = [453, 1502]
        eighth_tube = [603, 1511]
        ninth_tube = [859, 1515]
        self.tube_position(fifth_tube).tube_position(sixth_tube). \
            tube_position(third_tube).tube_position(fifth_tube). \
            tube_position(sixth_tube).tube_position(third_tube)
        return self

    def seventieth_level(self):
        """
        第七十关最后几步
        :return:
        """
        first_tube = [101, 995]
        second_tube = [295, 956]
        third_tube = [449, 889]
        fifth_tube = [793, 956]
        self.tube_position(first_tube).tube_position(fifth_tube). \
            tube_position(second_tube).tube_position(third_tube)

    def eightieth_level(self):
        """
        第八十关最后几步
        :return:
        """
        first_tube = [101, 995]
        fourth_tube = [638, 1008]
        sixth_tube = [978, 903]
        seventh_tube = [220, 1537]
        ninth_tube = [533, 1533]
        self.tube_position(first_tube).tube_position(fourth_tube). \
            tube_position(sixth_tube).tube_position(ninth_tube). \
            tube_position(seventh_tube).tube_position(sixth_tube)
        return self

    def ninetieth_level(self):
        """
        第九十关最后几步通关
        :return:
        """
        first_tube = [114, 969]
        second_tube = [356, 916]
        third_tube = [559, 911]
        fourth_tube = [753, 978]
        fifth_tube = [956, 947]
        sixth_tube = [273, 1546]
        seventh_tube = [453, 1502]
        eighth_tube = [603, 1511]
        ninth_tube = [859, 1515]
        self.tube_position(first_tube).tube_position(sixth_tube). \
            tube_position(fourth_tube).tube_position(sixth_tube). \
            tube_position(ninth_tube).tube_position(fourth_tube)

    def hundred_ten_level(self):
        """
        第一百一十关最后几步通关
        :return:
        """
        first_tube = [101, 995]
        second_tube = [295, 956]
        third_tube = [449, 889]
        fourth_tube = [638, 1008]
        fifth_tube = [793, 956]
        sixth_tube = [978, 903]
        seventh_tube = [220, 1537]
        eighth_tube = [383, 1449]
        ninth_tube = [533, 1533]
        tenth_tube = [678, 1515]
        eleventh_tube = [898, 1519]
        self.tube_position(first_tube).tube_position(third_tube). \
            tube_position(fourth_tube).tube_position(sixth_tube). \
            tube_position(second_tube).tube_position(first_tube)
        return self

    def hundred_twenty_level(self):
        """
        一百二十关最后几步
        :return:
        """
        second_tube = [295, 956]
        fifth_tube = [793, 956]
        seventh_tube = [220, 1537]
        eighth_tube = [383, 1449]
        ninth_tube = [533, 1533]
        self.tube_position(seventh_tube).tube_position(eighth_tube). \
            tube_position(second_tube).tube_position(seventh_tube). \
            tube_position(fifth_tube).tube_position(ninth_tube)
        return self

    def hundred_fifty_level(self):
        """
        一百五十关最后几步
        :return:
        """
        first_tube = [101, 995]
        second_tube = [295, 956]
        third_tube = [449, 889]
        fourth_tube = [638, 1008]
        fifth_tube = [793, 956]
        sixth_tube = [978, 903]
        seventh_tube = [220, 1537]
        eighth_tube = [383, 1449]
        ninth_tube = [533, 1533]
        tenth_tube = [678, 1515]
        eleventh_tube = [898, 1519]
        self.tube_position(fourth_tube).tube_position(sixth_tube). \
            tube_position(eighth_tube).tube_position(ninth_tube). \
            tube_position(first_tube).tube_position(eighth_tube)
        return self

    def hundred_sixty_level(self):
        """
        第一百六十关后几步
        :return:
        """
        first_tube = [101, 995]
        second_tube = [295, 956]
        third_tube = [449, 889]
        fourth_tube = [638, 1008]
        fifth_tube = [793, 956]
        sixth_tube = [978, 903]
        seventh_tube = [220, 1537]
        eighth_tube = [383, 1449]
        ninth_tube = [533, 1533]
        tenth_tube = [678, 1515]
        eleventh_tube = [898, 1519]
        self.tube_position(sixth_tube).tube_position(eleventh_tube). \
            tube_position(sixth_tube).tube_position(ninth_tube). \
            tube_position(second_tube).tube_position(sixth_tube)
        return self

    def two_hundred_level(self):
        first_tube = [101, 995]
        second_tube = [295, 956]
        third_tube = [449, 889]
        fourth_tube = [638, 1008]
        fifth_tube = [793, 956]
        sixth_tube = [978, 903]
        seventh_tube = [220, 1537]
        eighth_tube = [383, 1449]
        ninth_tube = [533, 1533]
        tenth_tube = [678, 1515]
        eleventh_tube = [898, 1519]
        self.tube_position(second_tube).tube_position(third_tube). \
            tube_position(fifth_tube).tube_position(third_tube). \
            tube_position(second_tube).tube_position(fifth_tube). \
            tube_position(sixth_tube).tube_position(fifth_tube). \
            tube_position(first_tube).tube_position(second_tube)
        return self

    def two_hundred_ten(self):
        first_tube = [101, 995]
        second_tube = [295, 956]
        third_tube = [449, 889]
        fourth_tube = [638, 1008]
        fifth_tube = [793, 956]
        sixth_tube = [978, 903]
        seventh_tube = [220, 1537]
        eighth_tube = [383, 1449]
        ninth_tube = [533, 1533]
        tenth_tube = [678, 1515]
        eleventh_tube = [898, 1519]
        self.tube_position(first_tube).tube_position(second_tube). \
            tube_position(sixth_tube).tube_position(second_tube). \
            tube_position(first_tube).tube_position(ninth_tube)
        return self

    def two_hundred_fifty(self):
        """
        第二百五十关最后几步
        :return:

        """
        first_tube = [101, 995]
        second_tube = [295, 956]
        third_tube = [449, 889]
        fourth_tube = [638, 1008]
        fifth_tube = [793, 956]
        sixth_tube = [978, 903]
        seventh_tube = [220, 1537]
        eighth_tube = [383, 1449]
        ninth_tube = [533, 1533]
        tenth_tube = [678, 1515]
        eleventh_tube = [898, 1519]
        self.tube_position(first_tube).tube_position(sixth_tube).\
            tube_position(second_tube).tube_position(sixth_tube).\
            tube_position(first_tube).tube_position(ninth_tube)
        return self

    def two_hundred_sixty(self):
        """
        第两百六十关最后几关
        :return:
        """
        first_tube = [101, 995]
        second_tube = [295, 956]
        third_tube = [449, 889]
        fourth_tube = [638, 1008]
        fifth_tube = [793, 956]
        sixth_tube = [978, 903]
        seventh_tube = [220, 1537]
        eighth_tube = [383, 1449]
        ninth_tube = [533, 1533]
        tenth_tube = [678, 1515]
        eleventh_tube = [898, 1519]
        self.tube_position(fourth_tube).tube_position(ninth_tube). \
            tube_position(first_tube).tube_position(eighth_tube). \
            tube_position(first_tube).tube_position(tenth_tube). \
            tube_position(first_tube).tube_position(seventh_tube)
        return self

    def three_hundred_ten(self):
        """
        第三百一十最后几关
        :return:
        """
        first_tube = [101, 995]
        second_tube = [295, 956]
        third_tube = [449, 889]
        fourth_tube = [638, 1008]
        fifth_tube = [793, 956]
        sixth_tube = [978, 903]
        seventh_tube = [220, 1537]
        eighth_tube = [383, 1449]
        ninth_tube = [533, 1533]
        tenth_tube = [678, 1515]
        eleventh_tube = [898, 1519]
        self.tube_position(second_tube).tube_position(fifth_tube). \
            tube_position(second_tube).tube_position(ninth_tube). \
            tube_position(eighth_tube).tube_position(tenth_tube)
        return self

    def three_hundred_twenty(self):
        """
        第三百二十最后几关
        :return:
        """
        first_tube = [101, 995]
        second_tube = [295, 956]
        third_tube = [449, 889]
        fourth_tube = [638, 1008]
        fifth_tube = [793, 956]
        sixth_tube = [978, 903]
        seventh_tube = [220, 1537]
        eighth_tube = [383, 1449]
        ninth_tube = [533, 1533]
        tenth_tube = [678, 1515]
        eleventh_tube = [898, 1519]
        self.tube_position(second_tube).tube_position(fifth_tube). \
            tube_position(ninth_tube).tube_position(tenth_tube). \
            tube_position(seventh_tube).tube_position(ninth_tube)
        return self

    def three_hundred_seventy(self):
        """
        第三百七十最后几步
        :return:
        """
        first_tube = [101, 995]
        second_tube = [295, 956]
        third_tube = [449, 889]
        fourth_tube = [638, 1008]
        fifth_tube = [793, 956]
        sixth_tube = [978, 903]
        seventh_tube = [220, 1537]
        eighth_tube = [383, 1449]
        ninth_tube = [533, 1533]
        tenth_tube = [678, 1515]
        eleventh_tube = [898, 1519]
        self.tube_position(seventh_tube).tube_position(ninth_tube)
        return self

    def three_hundred_eighty(self):
        """
        第三百八十最后几步
        :return:
        """
        first_tube = [101, 995]
        second_tube = [295, 956]
        third_tube = [449, 889]
        fourth_tube = [638, 1008]
        fifth_tube = [793, 956]
        sixth_tube = [978, 903]
        seventh_tube = [220, 1537]
        eighth_tube = [383, 1449]
        ninth_tube = [533, 1533]
        tenth_tube = [678, 1515]
        eleventh_tube = [898, 1519]
        self.tube_position(third_tube).tube_position(eleventh_tube). \
            tube_position(third_tube).tube_position(second_tube). \
            tube_position(sixth_tube).tube_position(third_tube)
        return self

    def four_hundred_forty(self):
        """
        第四百四十最后几步
        :return:
        """
        first_tube = [101, 995]
        second_tube = [295, 956]
        third_tube = [449, 889]
        fourth_tube = [638, 1008]
        fifth_tube = [793, 956]
        sixth_tube = [978, 903]
        seventh_tube = [220, 1537]
        eighth_tube = [383, 1449]
        ninth_tube = [533, 1533]
        tenth_tube = [678, 1515]
        eleventh_tube = [898, 1519]
        self.tube_position(second_tube).tube_position(eighth_tube). \
            tube_position(fourth_tube).tube_position(fifth_tube). \
            tube_position(fourth_tube).tube_position(seventh_tube)
        return self

    def four_hundred_fifty(self):
        """
        第四百五十最后几步
        :return:
        """
        first_tube = [101, 995]
        second_tube = [295, 956]
        third_tube = [449, 889]
        fourth_tube = [638, 1008]
        fifth_tube = [793, 956]
        sixth_tube = [978, 903]
        seventh_tube = [220, 1537]
        eighth_tube = [383, 1449]
        ninth_tube = [533, 1533]
        tenth_tube = [678, 1515]
        eleventh_tube = [898, 1519]
        self.tube_position(second_tube).tube_position(sixth_tube). \
            tube_position(third_tube).tube_position(ninth_tube)
        return self

    def five_hundred_ten(self):
        """
        第五百一十关最后几步
        :return:
        """
        first_tube = [101, 995]
        second_tube = [295, 956]
        third_tube = [449, 889]
        fourth_tube = [638, 1008]
        fifth_tube = [793, 956]
        sixth_tube = [978, 903]
        seventh_tube = [220, 1537]
        eighth_tube = [383, 1449]
        ninth_tube = [533, 1533]
        tenth_tube = [678, 1515]
        eleventh_tube = [898, 1519]
        self.tube_position(second_tube).tube_position(eighth_tube). \
            tube_position(ninth_tube).tube_position(third_tube). \
            tube_position(first_tube).tube_position(ninth_tube)
        return self

    def five_hundred_twenty(self):
        """
        第五百二十关最后几步
        :return:
        """
        first_tube = [101, 995]
        second_tube = [295, 956]
        third_tube = [449, 889]
        fourth_tube = [638, 1008]
        fifth_tube = [793, 956]
        sixth_tube = [978, 903]
        seventh_tube = [220, 1537]
        eighth_tube = [383, 1449]
        ninth_tube = [533, 1533]
        tenth_tube = [678, 1515]
        eleventh_tube = [898, 1519]
        self.tube_position(third_tube).tube_position(seventh_tube)

    def five_hundred_ninety(self):
        """
        第五百九十关最后几步
        :return:
        """
        first_tube = [101, 995]
        second_tube = [295, 956]
        third_tube = [449, 889]
        fourth_tube = [638, 1008]
        fifth_tube = [793, 956]
        sixth_tube = [978, 903]
        seventh_tube = [220, 1537]
        eighth_tube = [383, 1449]
        ninth_tube = [533, 1533]
        tenth_tube = [678, 1515]
        eleventh_tube = [898, 1519]
        self.tube_position(first_tube).tube_position(fourth_tube). \
            tube_position(fifth_tube).tube_position(fourth_tube). \
            tube_position(fifth_tube).tube_position(second_tube)
        return self





if __name__ == "__main__":
    if not cli_setup():
        auto_setup(__file__, logdir=True, devices=[
            "android://127.0.0.1:5037/QV710QR43F?cap_method=MINICAP&&ori_method=MINICAPORI&&touch_method=MAXTOUCH", ])
    VictoryStep().twelve_level()
