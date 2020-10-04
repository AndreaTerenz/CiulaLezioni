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
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 781, 531))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_4.setContentsMargins(20, -1, 20, -1)
        self.lineEdit = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_4.addWidget(self.lineEdit)

        self.choose_out_dir_btn = QPushButton(self.verticalLayoutWidget)
        self.choose_out_dir_btn.setObjectName(u"choose_out_dir_btn")
        self.choose_out_dir_btn.setMinimumSize(QSize(105, 0))
        self.choose_out_dir_btn.setMaximumSize(QSize(105, 16777215))

        self.horizontalLayout_4.addWidget(self.choose_out_dir_btn)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_5.setContentsMargins(20, -1, 20, -1)
        self.cookies_file_line = QLineEdit(self.verticalLayoutWidget)
        self.cookies_file_line.setObjectName(u"cookies_file_line")

        self.horizontalLayout_5.addWidget(self.cookies_file_line)

        self.choose_cookies_btn = QPushButton(self.verticalLayoutWidget)
        self.choose_cookies_btn.setObjectName(u"choose_cookies_btn")
        self.choose_cookies_btn.setMinimumSize(QSize(105, 0))
        self.choose_cookies_btn.setMaximumSize(QSize(105, 16777215))

        self.horizontalLayout_5.addWidget(self.choose_cookies_btn)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_3.setContentsMargins(20, -1, 20, -1)
        self.output_file_name_line = QLineEdit(self.verticalLayoutWidget)
        self.output_file_name_line.setObjectName(u"output_file_name_line")

        self.horizontalLayout_3.addWidget(self.output_file_name_line)

        self.go_btn = QPushButton(self.verticalLayoutWidget)
        self.go_btn.setObjectName(u"go_btn")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.go_btn.sizePolicy().hasHeightForWidth())
        self.go_btn.setSizePolicy(sizePolicy)
        self.go_btn.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_3.addWidget(self.go_btn)

        self.stop_btn = QPushButton(self.verticalLayoutWidget)
        self.stop_btn.setObjectName(u"stop_btn")
        sizePolicy.setHeightForWidth(self.stop_btn.sizePolicy().hasHeightForWidth())
        self.stop_btn.setSizePolicy(sizePolicy)
        self.stop_btn.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_3.addWidget(self.stop_btn)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.scrollArea = QScrollArea(self.verticalLayoutWidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMaximumSize(QSize(16777215, 280))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 777, 278))
        self.textBrowser = QTextBrowser(self.scrollAreaWidgetContents)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(-5, -9, 781, 371))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 28))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"CiulaLezioni", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Output folder", None))
        self.choose_out_dir_btn.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.cookies_file_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Cookies file", None))
        self.choose_cookies_btn.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.output_file_name_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Output file name", None))
        self.go_btn.setText(QCoreApplication.translate("MainWindow", u"Go", None))
        self.stop_btn.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Lato'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
    # retranslateUi

