# 本模块用于将输入的字符串连同时间戳、标准日期时间格式输出到csv文件
# 文件的每一行格式如下：
# time, format time, basic information, string

import csv
import time
from datetime import datetime
import os


class OutputToCSV:
    File_Name = ''
    Dir_Name = ''
    Dir_File_Name = ''

    def __init__(self, Dir_Name='', File_Name='') -> None:
        # 默认存储结果的文件夹目录为工作区下的OutputCSV
        if Dir_Name == '':
            os.chdir("..")
            Dir_Name = os.path.join(os.getcwd(), "OutputCSV")
        self.Dir_Name = Dir_Name
        # 默认存储文件名称为"%m-%d-%H-%M-%S.csv"
        if File_Name == '':
            File_Name = time.strftime(
                "%m-%d-%H-%M-%S", time.localtime(time.time()))
        self.File_Name = File_Name

        self.Dir_File_Name = os.path.join(self.Dir_Name, self.File_Name)
        self.Dir_File_Name += '.csv'

    def OutputToCSV(self, BasicInfo, Str, Format='%m-%d-%H-%M-%S.%f'):
        TimeStamp = time.time()
        FormatTime = datetime.now().strftime('%m-%d-%H-%M-%S.%f')[:-3]
        os.chdir(self.Dir_Name)
        Output_List = [TimeStamp, FormatTime, BasicInfo, Str]
        with open(self.File_Name, mode="a+", encoding="utf-8-sig", newline='') as CsvFile:
            writer = csv.writer(CsvFile)
            writer.writerow(Output_List)
