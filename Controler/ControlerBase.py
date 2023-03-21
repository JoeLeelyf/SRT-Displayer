# 此类是所有控制类的基类，用于控制各个部分的持续时间

from PyQt5.QtGui import QColor


class ControlerBase:
    Baseline_Dur = 0
    Gap_Dur1 = 0
    Gap_Dur2 = 0
    Gap_Dur3 = 0
    Gap_Dur4 = 0
    Gap_Dur5 = 0

    Wait_Dur1 = 0
    Wait_Dur2 = 0

    Display_Dur = 0
    Listen_Dur = 0
    Imagine_Dur = 0
    Speak_Dur = 0

    Wait_Color = QColor(192, 192, 192)
    Imagine_Color = QColor(0, 0, 250)
    Speak_Color = QColor(250, 0, 0)

    Font_Size = 40
    Circle_Size = 100
    Circle_Gap = 20

    Word_List = []
    Input_FileName = ''
    Audio_DirName = ''
    Output_DirName = ''

    def SetBaseLineDur(self, Baseline_Dur=0):
        self.Baseline_Dur = Baseline_Dur

    def SetDisplayDur(self, Display_Dur=0):
        self.Display_Dur = Display_Dur

    def SetListenDur(self, Listen_Dur=0):
        self.Listen_Dur = Listen_Dur

    def SetImagineDur(self, Imagine_Dur=0):
        self.Imagine_Dur = Imagine_Dur

    def SetSpeakDur(self, Speak_Dur=0):
        self.Speak_Dur = Speak_Dur

    def SetGapDur1(self, Gap_Dur1=0):
        self.Gap_Dur1 = Gap_Dur1

    def SetGapDur2(self, Gap_Dur2=0):
        self.Gap_Dur2 = Gap_Dur2

    def SetGapDur3(self, Gap_Dur3=0):
        self.Gap_Dur3 = Gap_Dur3

    def SetGapDur4(self, Gap_Dur4=0):
        self.Gap_Dur4 = Gap_Dur4

    def SetGapDur5(self, Gap_Dur5=0):
        self.Gap_Dur5 = Gap_Dur5

    def SetWaitDur1(self, Wait_Dur1=0):
        self.Wait_Dur1 = Wait_Dur1

    def SetWaitDur2(self, Wait_Dur2=0):
        self.Wait_Dur2 = Wait_Dur2

    def SetInputFileName(self, Input_FileName):
        self.Input_FileName = Input_FileName

    def SetAudioDirName(self, Audio_DirName):
        self.Audio_DirName = Audio_DirName

    def SetOutputDirName(self, Output_DirName):
        self.Output_DirName = Output_DirName

    def SetWaitColor(self, r=192, g=192, b=192):
        self.Wait_Color = QColor(r, g, b)

    def SetImageColor(self, r=0, g=0, b=250):
        self.Imagine_Color = QColor(r, g, b)

    def SetSpeakColor(self, r=250, g=0, b=0):
        self.Speak_Color = QColor(r, g, b)

    def SetCircleSize(self, size=100):
        self.Circle_Size = size

    def SetCircleGap(self, size=50):
        self.Circle_Gap = size

    def SetFontSize(self, size=40):
        self.Font_Size = size
