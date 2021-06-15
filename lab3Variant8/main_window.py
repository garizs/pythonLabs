# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import logging
import os

import cv2
from PyQt5 import QtCore, QtWidgets

from find_rectangle import FindRectangle


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(314, 259)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(60, 80, 191, 30))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(60, 120, 191, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 60, 47, 13))
        self.label.setMaximumSize(QtCore.QSize(640, 480))
        self.label.setText("")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 314, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Колесников Иван ПРИ-18/1"))
        self.pushButton.setText(_translate("MainWindow", "Распознавание по изображению"))
        self.pushButton_2.setText(_translate("MainWindow", "Распознавание по вебкамере"))
        self.pushButton.clicked.connect(self.pushButton_handler)
        self.pushButton_2.clicked.connect(self.pushButton2_handler)

    def pushButton_handler(self):
        print("Button pressed")
        self.fileBrowse()

    def pushButton2_handler(self):
        self.findCamera()

    @staticmethod
    def fileBrowse():
        cv2.destroyAllWindows()
        file_path = QtWidgets.QFileDialog.getOpenFileName()
        extension = os.path.splitext(file_path[0])[1]
        if file_path[0] and extension in ['.jpg', '.png']:
            FindRectangle.image_find_rectangle(file_path[0])
        else:
            logging.error('Не выбран файл!')

    @staticmethod
    def findCamera():
        cv2.destroyAllWindows()
        FindRectangle.video_find_rectangle()