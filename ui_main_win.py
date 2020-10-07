# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(614, 527)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(12)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.input_url_line = QLineEdit(self.centralwidget)
        self.input_url_line.setObjectName(u"input_url_line")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_url_line.sizePolicy().hasHeightForWidth())
        self.input_url_line.setSizePolicy(sizePolicy)
        self.input_url_line.setMinimumSize(QSize(500, 40))

        self.horizontalLayout_2.addWidget(self.input_url_line)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_4.setContentsMargins(0, -1, 0, -1)
        self.output_file_line = QLineEdit(self.centralwidget)
        self.output_file_line.setObjectName(u"output_file_line")
        sizePolicy.setHeightForWidth(self.output_file_line.sizePolicy().hasHeightForWidth())
        self.output_file_line.setSizePolicy(sizePolicy)
        self.output_file_line.setMinimumSize(QSize(400, 40))

        self.horizontalLayout_4.addWidget(self.output_file_line)

        self.choose_out_file_btn = QPushButton(self.centralwidget)
        self.choose_out_file_btn.setObjectName(u"choose_out_file_btn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.choose_out_file_btn.sizePolicy().hasHeightForWidth())
        self.choose_out_file_btn.setSizePolicy(sizePolicy1)
        self.choose_out_file_btn.setMinimumSize(QSize(100, 40))
        self.choose_out_file_btn.setMaximumSize(QSize(104, 16777215))

        self.horizontalLayout_4.addWidget(self.choose_out_file_btn)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_5.setContentsMargins(0, -1, 0, -1)
        self.cookies_file_line = QLineEdit(self.centralwidget)
        self.cookies_file_line.setObjectName(u"cookies_file_line")
        sizePolicy.setHeightForWidth(self.cookies_file_line.sizePolicy().hasHeightForWidth())
        self.cookies_file_line.setSizePolicy(sizePolicy)
        self.cookies_file_line.setMinimumSize(QSize(400, 40))

        self.horizontalLayout_5.addWidget(self.cookies_file_line)

        self.choose_cookies_btn = QPushButton(self.centralwidget)
        self.choose_cookies_btn.setObjectName(u"choose_cookies_btn")
        sizePolicy1.setHeightForWidth(self.choose_cookies_btn.sizePolicy().hasHeightForWidth())
        self.choose_cookies_btn.setSizePolicy(sizePolicy1)
        self.choose_cookies_btn.setMinimumSize(QSize(100, 40))
        self.choose_cookies_btn.setMaximumSize(QSize(104, 16777215))

        self.horizontalLayout_5.addWidget(self.choose_cookies_btn)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.start_btn = QPushButton(self.centralwidget)
        self.start_btn.setObjectName(u"start_btn")
        self.start_btn.setEnabled(False)
        self.start_btn.setMinimumSize(QSize(0, 40))
        self.start_btn.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout.addWidget(self.start_btn)

        self.stop_btn = QPushButton(self.centralwidget)
        self.stop_btn.setObjectName(u"stop_btn")
        self.stop_btn.setEnabled(False)
        self.stop_btn.setMinimumSize(QSize(0, 40))
        self.stop_btn.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout.addWidget(self.stop_btn)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.output_log = QTextBrowser(self.centralwidget)
        self.output_log.setObjectName(u"output_log")
        self.output_log.setMinimumSize(QSize(600, 250))

        self.verticalLayout.addWidget(self.output_log)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 614, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"CiulaLezioni", None))
        self.input_url_line.setText(QCoreApplication.translate("MainWindow", u"https://www.youtube.com/watch?v=MDCwSBbxxss", None))
        self.input_url_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Input URL", None))
        self.output_file_line.setText(QCoreApplication.translate("MainWindow", u"/home/andrea/CiulaLezioni/gigi.mp4", None))
        self.output_file_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Output file", None))
        self.choose_out_file_btn.setText(QCoreApplication.translate("MainWindow", u"Select", None))
        self.cookies_file_line.setText(QCoreApplication.translate("MainWindow", u"/home/andrea/Downloads/youtube.com_cookies.txt", None))
        self.cookies_file_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Cookies file", None))
        self.choose_cookies_btn.setText(QCoreApplication.translate("MainWindow", u"Select", None))
        self.start_btn.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.stop_btn.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.output_log.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Cantarell'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Lato'; font-size:11pt;\"><br /></p></body></html>", None))
    # retranslateUi

