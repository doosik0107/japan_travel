# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
import sys
import wx
from japan_db import *

class Holiday_Gui(QMainWindow):
    def __init__(self):
        super().__init__()
        #self.initUI()

    #def initUI(self):
        holiday_db = japan_holiday()
        holiday_db.search_holiday()
        result = holiday_db.cur.fetchall()
        back_size = wx.GetDisplaySize()
        back_width = back_size[0]
        back_height = back_size[1]
        self.setGeometry((back_width/2)-400,(back_height/2)-300,300,600)
        #gui창크기
        self.setWindowTitle('holiday')

        listwidget = QListWidget()
        for (name,day) in result:
            text = name + " " + day
            listwidget.addItem(text)

        self.setCentralWidget(listwidget)
        self.show()


