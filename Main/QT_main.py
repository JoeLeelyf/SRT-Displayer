# 此文件为主文件，在运行时直接运行此文件即可

import sys
import time
import os
import threading

import pygame
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import Qt, QRect, QLine, QPoint, QRectF
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QPainter, QPen, QColor
from PyQt5.QtMultimedia import QSound

from file_init_ import Ui_Dialog
from MainWindow import Ui_MainWindow
from BaseFunc import OutputToCSV
from BaseFunc import WordSetReader
from Controler import ControlerBase


class MainWindowShow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindowShow, self).__init__(parent)
        self.setupUi()
        self.ChildDialog = FileDialogShow()
        self.Controler = ControlerBase.ControlerBase()
        self.pushButton.clicked.connect(self.onClicked)

    def setupUi(self):
        super(MainWindowShow, self).setupUi(self)

    def onClicked(self):
        self.ChildDialog.show()
        self.ChildDialog.signal.connect(self.get_file_name)

    def get_file_name(self, str_1, str_2, str_3):
        self.Controler.SetInputFileName(str_1)
        self.Controler.SetAudioDirName(str_2)
        self.Controler.SetOutputDirName(str_3)
        self.pushButton_2.setEnabled(True)
        self.pushButton_2.clicked.connect(self.display_word)

    def play_audio(self, *args):
        Gap = args[1] + args[2] + self.Controler.Listen_Dur
        pygame.init()
        track = pygame.mixer.Sound(os.path.join(self.Controler.Audio_DirName, str(args[0][2])))
        track.set_volume(1)
        time.sleep(2)
        track.play()
        while pygame.mixer.music.get_busy():
            pass

    def paint_circle(self, word_num=1, Qt_color_1=Qt.white, Qt_color_2=Qt.white):
        circle_size = self.Controler.Circle_Size
        circle_gap = self.Controler.Circle_Gap
        canvas = QtGui.QPixmap(circle_size * word_num + circle_gap * (word_num - 1), circle_size)
        canvas.fill(Qt.black)
        self.label.setPixmap(canvas)
        self.centralwidget.setStyleSheet('''QWidget{background-color:rgb(0,0,0);}''')

        # draw circle
        painter = QtGui.QPainter(self.label.pixmap())
        # set pen and brush color
        pen = QPen()
        pen.setStyle(Qt.NoPen)
        painter.setPen(pen)

        painter.setRenderHint(QPainter.Antialiasing)
        if word_num == 1:
            painter.setBrush(Qt_color_1)
            rect = QRect(0, 0, circle_size, circle_size)
            painter.drawEllipse(rect)
        else:
            # draw the first circle
            painter.setBrush(Qt_color_1)
            rect_1 = QRect(0, 0, circle_size, circle_size)
            painter.drawEllipse(rect_1)
            # draw the second circle
            painter.setBrush(Qt_color_2)
            rect_2 = QRect(canvas.width() - circle_size, 0, circle_size, circle_size)
            painter.drawEllipse(rect_2)
        painter.end()
        self.update()

    def display_circle(self, status, dur_time, word_num):
        if word_num == 1:
            if status == "wait":
                self.paint_circle(word_num=1, Qt_color_1=self.Controler.Wait_Color)
                QApplication.processEvents()
                time.sleep(dur_time)
                QApplication.processEvents()
            elif status == "imagine":
                self.paint_circle(word_num=1, Qt_color_1=self.Controler.Imagine_Color)
                QApplication.processEvents()
                time.sleep(dur_time)
                QApplication.processEvents()
            elif status == "speak":
                self.paint_circle(word_num=1, Qt_color_1=self.Controler.Speak_Color)
                QApplication.processEvents()
                time.sleep(dur_time)
                QApplication.processEvents()
        elif word_num == 2:
            if status == "wait":
                self.paint_circle(word_num=2, Qt_color_1=self.Controler.Wait_Color,
                                  Qt_color_2=self.Controler.Wait_Color)
                QApplication.processEvents()
                time.sleep(dur_time)
                QApplication.processEvents()
            elif status == "imagine":
                self.paint_circle(word_num=2, Qt_color_1=self.Controler.Imagine_Color,
                                  Qt_color_2=self.Controler.Wait_Color)
                QApplication.processEvents()
                time.sleep(dur_time / 2)
                QApplication.processEvents()
                self.paint_circle(word_num=2, Qt_color_1=self.Controler.Wait_Color,
                                  Qt_color_2=self.Controler.Imagine_Color)
                QApplication.processEvents()
                time.sleep(dur_time / 2)
                QApplication.processEvents()
            elif status == "speak":
                self.paint_circle(word_num=2, Qt_color_1=self.Controler.Speak_Color,
                                  Qt_color_2=self.Controler.Wait_Color)
                QApplication.processEvents()
                time.sleep(dur_time / 2)
                QApplication.processEvents()
                self.paint_circle(word_num=2, Qt_color_1=self.Controler.Wait_Color,
                                  Qt_color_2=self.Controler.Speak_Color)
                QApplication.processEvents()
                time.sleep(dur_time / 2)
                QApplication.processEvents()

    def display_word(self):
        self.label.clear()
        self.label.setFont(QFont("Times", 72, QFont.Bold))
        self.label.setStyleSheet('''QLabel{color:rgb(255,255,255);}''')
        self.pushButton.setEnabled(False)
        self.pushButton.setStyleSheet('''QPushButton{background-color:rgb(0,0,0);}''')
        self.pushButton_2.setEnabled(False)
        self.pushButton_2.setStyleSheet('''QPushButton{background-color:rgb(0,0,0);}''')
        word_reader = WordSetReader.WordSetReader(self.Controler.Input_FileName)
        # word_list includes the return lists of the csv file
        word_list = word_reader.ReadFromWordSet()

        for List in word_list:
            # init info about the word from List
            word = List[1]
            word_num = len(word)
            output_csv = OutputToCSV.OutputToCSV(self.Controler.Output_DirName, word)

            # play audio while display word, at different thread
            audio_thread = threading.Thread(target=self.play_audio,
                                            args=(List, self.Controler.Display_Dur,
                                                  self.Controler.Gap_Dur2))
            audio_thread.start()

            # display word
            self.label.setFont(QFont("Times", self.Controler.Font_Size, QFont.Bold))
            self.label.setStyleSheet('''QLabel{color:rgb(255,255,255);}''')
            self.label.setText(word)
            QApplication.processEvents()
            time.sleep(self.Controler.Display_Dur)
            QApplication.processEvents()
            self.label.clear()

            # wait for Wait_Dur1
            self.display_circle(status="wait", dur_time=self.Controler.Wait_Dur1, word_num=word_num)

            # start to imagine
            output_csv.OutputToCSV("Imagine Start", word)
            self.display_circle(status="imagine", dur_time=self.Controler.Imagine_Dur, word_num=word_num)
            output_csv.OutputToCSV("Imagine End", word)

            # wait for Wait_Dur2
            '''
            self.paint_circle(Qt_color_1=self.Controler.Wait_Color, Qt_color_2=self.Controler.Wait_Color)
            QApplication.processEvents()
            time.sleep(self.Controler.Wait_Dur2)
            QApplication.processEvents()
            '''
            self.display_circle(status="wait", dur_time=self.Controler.Wait_Dur2, word_num=word_num)

            # start to speak
            output_csv.OutputToCSV("Speak Start", word)
            self.display_circle(status="speak", dur_time=self.Controler.Speak_Dur, word_num=word_num)
            output_csv.OutputToCSV("Speak End", word)

            # set gap between tests
            self.paint_circle(word_num=word_num, Qt_color_1=Qt.black, Qt_color_2=Qt.black)
            QApplication.processEvents()
            time.sleep(self.Controler.Gap_Dur1)

        self.label.setStyleSheet('''QLabel{color:rgb(255,255,255);}''')
        self.label.setText("END")
        QApplication.processEvents()
        time.sleep(self.Controler.Gap_Dur1)


class FileDialogShow(QDialog, Ui_Dialog):
    signal = QtCore.pyqtSignal(str, str, str)

    def __init__(self, parent=None):
        super(FileDialogShow, self).__init__(parent)
        self.setupUi()
        self.retranslateUi(self)

        self.buttonBox.accepted.connect(self.slot)

    def setupUi(self):
        super(FileDialogShow, self).setupUi(self)

    def slot(self):
        f_name = self.lineEdit.text()
        dir_name_1 = self.lineEdit_2.text()
        dir_name_2 = self.lineEdit_3.text()
        self.signal.emit(f_name, dir_name_1, dir_name_2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window_1 = MainWindowShow()
    dialog_1 = FileDialogShow()

    # set time gap
    window_1.Controler.SetDisplayDur(2)
    window_1.Controler.SetWaitDur1(2)
    window_1.Controler.SetImagineDur(1)
    window_1.Controler.SetWaitDur2(2)
    window_1.Controler.SetSpeakDur(1)
    window_1.Controler.SetGapDur1(2)

    # set color
    window_1.Controler.SetWaitColor()
    window_1.Controler.SetImageColor()
    window_1.Controler.SetSpeakColor()

    # set font size
    window_1.Controler.SetFontSize(100)
    # set circle size
    window_1.Controler.SetCircleSize(100)
    window_1.Controler.SetCircleGap(10)

    # initialize, and set file name and directory
    window_1.label.setText("<font color=white size=2000>Welcome to the Word Displayer</font>")
    window_1.show()
    window_1.pushButton_2.setEnabled(False)

    sys.exit(app.exec_())
