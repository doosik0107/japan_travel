# -*- coding: utf-8 -*-
from holiday_gui import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import wx


class Main_Gui(QMainWindow,QWidget):

    FROM, SUBJECT, DATE = range(3)

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

        Holiday_button = QPushButton("휴일",self)
        Holiday_button.move(700,20)
        Holiday_button.resize(60,30)

        self.dataGroupBox = QGroupBox("Inbox")
        self.dataView = QTreeView()
        self.dataView.setRootIsDecorated(False)
        self.dataView.setAlternatingRowColors(True)

        dataLayout = QHBoxLayout()
        dataLayout.addWidget(self.dataView)
        self.dataGroupBox.setLayout(dataLayout)

        model = self.createMailModel(self)
        self.dataView.setModel(model)
        self.addMail(model, 'service@github.com', 'Your Github Donation', '03/25/2017 02:05 PM')
        self.addMail(model, 'support@github.com', 'Github Projects', '02/02/2017 03:05 PM')
        self.addMail(model, 'service@phone.com', 'Your Phone Bill', '01/01/2017 04:05 PM')

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.dataGroupBox)
        self.setLayout(mainLayout)
        Holiday_button.clicked.connect(self.Holiday_clicked)
        self.show()

    def Holiday_clicked(self):
        holiday_app.show()

    def createMailModel(self, parent):
        model = QStandardItemModel(0, 3, parent)
        model.setHeaderData(self.FROM, Qt.Horizontal, "From")
        model.setHeaderData(self.SUBJECT, Qt.Horizontal, "Subject")
        model.setHeaderData(self.DATE, Qt.Horizontal, "Date")
        return model

    def addMail(self, model, mailFrom, subject, date):
        model.insertRow(0)
        model.setData(model.index(0, self.FROM), mailFrom)
        model.setData(model.index(0, self.SUBJECT), subject)
        model.setData(model.index(0, self.DATE), date)



if __name__=='__main__':
    wxapp = wx.App(False)
    app=QApplication(sys.argv)
    travel_app = Main_Gui()
    holiday_app = Holiday_Gui()
    sys.exit(app.exec_())