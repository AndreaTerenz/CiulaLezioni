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
        MainWindow.resize(553, 459)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(12)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(20, -1, 20, -1)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_4.setContentsMargins(0, -1, 0, -1)
        self.output_dir_line = QLineEdit(self.centralwidget)
        self.output_dir_line.setObjectName(u"output_dir_line")
        self.output_dir_line.setMinimumSize(QSize(400, 0))

        self.horizontalLayout_4.addWidget(self.output_dir_line)

        self.choose_out_dir_btn = QPushButton(self.centralwidget)
        self.choose_out_dir_btn.setObjectName(u"choose_out_dir_btn")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.choose_out_dir_btn.sizePolicy().hasHeightForWidth())
        self.choose_out_dir_btn.setSizePolicy(sizePolicy)
        self.choose_out_dir_btn.setMinimumSize(QSize(100, 0))
        self.choose_out_dir_btn.setMaximumSize(QSize(104, 16777215))

        self.horizontalLayout_4.addWidget(self.choose_out_dir_btn)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_5.setContentsMargins(0, -1, 0, -1)
        self.cookies_file_line = QLineEdit(self.centralwidget)
        self.cookies_file_line.setObjectName(u"cookies_file_line")
        self.cookies_file_line.setMinimumSize(QSize(400, 0))

        self.horizontalLayout_5.addWidget(self.cookies_file_line)

        self.choose_cookies_btn = QPushButton(self.centralwidget)
        self.choose_cookies_btn.setObjectName(u"choose_cookies_btn")
        sizePolicy.setHeightForWidth(self.choose_cookies_btn.sizePolicy().hasHeightForWidth())
        self.choose_cookies_btn.setSizePolicy(sizePolicy)
        self.choose_cookies_btn.setMinimumSize(QSize(100, 0))
        self.choose_cookies_btn.setMaximumSize(QSize(104, 16777215))

        self.horizontalLayout_5.addWidget(self.choose_cookies_btn)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_3.setContentsMargins(0, -1, 0, -1)
        self.output_file_name_line = QLineEdit(self.centralwidget)
        self.output_file_name_line.setObjectName(u"output_file_name_line")
        self.output_file_name_line.setMinimumSize(QSize(400, 0))

        self.horizontalLayout_3.addWidget(self.output_file_name_line)

        self.go_stop_btn = QPushButton(self.centralwidget)
        self.go_stop_btn.setObjectName(u"go_stop_btn")
        sizePolicy.setHeightForWidth(self.go_stop_btn.sizePolicy().hasHeightForWidth())
        self.go_stop_btn.setSizePolicy(sizePolicy)
        self.go_stop_btn.setMinimumSize(QSize(100, 0))
        self.go_stop_btn.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_3.addWidget(self.go_stop_btn)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.output_log = QTextBrowser(self.centralwidget)
        self.output_log.setObjectName(u"output_log")
        self.output_log.setMinimumSize(QSize(0, 250))

        self.verticalLayout.addWidget(self.output_log)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 553, 28))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"CiulaLezioni", None))
        self.output_dir_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Output folder", None))
        self.choose_out_dir_btn.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.cookies_file_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Cookies file", None))
        self.choose_cookies_btn.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.output_file_name_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Output file name", None))
        self.go_stop_btn.setText(QCoreApplication.translate("MainWindow", u"Go", None))
        self.output_log.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Lato'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
    # retranslateUi

