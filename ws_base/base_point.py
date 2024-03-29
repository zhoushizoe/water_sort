# coding = utf-8
# Author: Zoe
# File: base_point.py
# Time: 2023/11/17 11:49
import re
import subprocess
from airtest.core.api import *
import yaml


class GetPointWater:
    """
    1.前置条件
    2.清除数据
    3.进行操作（操作的步骤放在框架外）
    4.过滤埋点，进行对比（能过滤到证明有埋点或者需要断言，断言的标准就是是否过滤到了埋点）
    5.写入文件
    6.一些操作之后对埋点进行对比


    """

    def clear_command(self):
        """
        2.清除数据
        :return:
        """
        # clear = "adb logcat -c"
        clear = ["adb", "logcat", "-c"]
        process = subprocess.call(clear)
        # process.wait()
        # process.kill()
        print("清除日志已完成")
        return self

    def read_point(self, key):
        """
        取出对应的埋点，得到需要过滤的信息
        :return:
        """
        with open(r"/Users/amber/PycharmProjects/Water Sort/ws_base/standard_point_water.yaml", "r", encoding="utf-8") as f:
            all_data = yaml.safe_load(f)
            get_data = all_data[key]
            print(get_data)
            return get_data

    def output_command(self, key):
        # sleep(3)
        """
        过滤埋点
        """
        grep_info = self.read_point(key)
        command = f"adb logcat -d | grep '{grep_info}'"
        grep_output = subprocess.check_output(command, shell=True)
        grep_output = grep_output.decode()
        grep_output = grep_output.strip()
        print(grep_output + "output")
        return grep_output

    def get_correct_log(self, key):
        """
        得到对应的想要的数据
        :param key:
        :return:
        """
        raw_string = self.output_command(key)
        pattern = r'EVENT_SEND\s+:\s+(.*?)\s*lib_net_status:'
        # 使用正则表达式提取目标部分
        # match = re.search(pattern, raw_string)
        # if match:
        #     extracted_content = match.group(1)
        #     # print(extracted_content)
        #     extracted_string = extracted_content.strip()
        #     return extracted_string
        # else:
        #     print("没找到对应log")
        matches = re.findall(pattern, raw_string)
        if matches:
            extracted_strings = [match.strip() for match in matches]
            extracted_string = ' '.join(extracted_strings)
            print(extracted_string)
            return extracted_string
        else:
            print("没找到对应log")
    # def write_contrast(self, key):
    #     with open("contrast.yaml", "a", encoding="utf-8") as f:
    #         yaml.dump(self.get_correct_log(key), f)

    def write_contrast2(self, key):
        """
        将正确的数据写入文件中
        :param key:
        :return:
        """
        with open("test1.txt", "a", encoding="utf-8") as f:
            f.write(self.get_correct_log(key) + "\n")
        return self

    def contrast_step(self, key):
        """
        点击操作之后的步骤
        :return:
        """
        # sleep(10)
        self.read_point(key)
        self.output_command(key)
        self.get_correct_log(key)
        self.write_contrast2(key)


if __name__ == "__main__":
    GetPoint().read_point("settings_music")
