# -*- coding: utf-8 -*-
from holiday_gui import *
from PyQt5.QtWidgets import *
import sys
import wx


class Main_Gui(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        print(wx.GetDisplaySize())
        back_size = wx.GetDisplaySize()
        back_width = back_size[0]
        back_height = back_size[1]
        self.setGeometry((back_width/2)-400,(back_height/2)-300,800,600)
        #gui창크기
        self.setWindowTitle('travel')

        self.Search_label = QLabel("검색어 : ",self)
        self.Search_label.resize(50,30)
        self.Search_label.move(10,20)

        self.Search_inputbox = QLineEdit(self)
        self.Search_inputbox.move(60,20)
        self.Search_inputbox.resize(150,30)

        Search_button = QPushButton("검색",self)
        Search_button.move(220,20)
        Search_button.resize(60,30)

        Search_button.clicked.connect(self.Search_clicked)
        self.show()

    def Search_clicked(self):
        app = QApplication(sys.argv)
        holiday_app = Holiday_Gui()
        sys.exit(app.exec_())





if __name__=='__main__':
    wxapp = wx.App(False)
    app=QApplication(sys.argv)
    travel_app = Main_Gui()
    sys.exit(app.exec_())