# 该模块从csv文件中读取数据并以list的方式返回数据
# 默认的csv文件格式为1, [word/setence]

import csv
import os


class WordSetReader:
    Dir_Name = ''
    File_Name = ''
    Dir_File_Name = ''

    def __init__(self, File_Name, Dir_Name='') -> None:
        # 当未指定输入的文件目录时，默认为同一工作目录下的Word Set文件夹
        if Dir_Name == '':
            os.chdir("..")
            Dir_Name = os.path.join(os.getcwd(), "WordSet")
        self.Dir_Name = Dir_Name

        self.File_Name = File_Name
        self.Dir_File_Name = os.path.join(Dir_Name, File_Name)

    def ReadFromWordSet(self):
        os.chdir(self.Dir_Name)
        with open(self.File_Name, mode='r', encoding="utf-8") as CsvFile:
            Reader = csv.reader(CsvFile)
            # 此处若直接返回Reader，将提示I/O on closed file错误
            # 因为在主函数中调用时此文件已关闭
            Return = []
            for i in Reader:
                Return.append(i)
            return Return
