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
        MainWindow.resize(614, 511)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(12)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetFixedSize)
        self.verticalLayout.setContentsMargins(0, -1, 0, -1)
        self.url_layout = QHBoxLayout()
        self.url_layout.setObjectName(u"url_layout")
        self.input_url_line = QLineEdit(self.centralwidget)
        self.input_url_line.setObjectName(u"input_url_line")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_url_line.sizePolicy().hasHeightForWidth())
        self.input_url_line.setSizePolicy(sizePolicy)
        self.input_url_line.setMinimumSize(QSize(500, 35))

        self.url_layout.addWidget(self.input_url_line)


        self.verticalLayout.addLayout(self.url_layout)

        self.out_file_layout = QHBoxLayout()
        self.out_file_layout.setObjectName(u"out_file_layout")
        self.out_file_layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.out_file_layout.setContentsMargins(0, -1, 0, -1)
        self.output_file_line = QLineEdit(self.centralwidget)
        self.output_file_line.setObjectName(u"output_file_line")
        sizePolicy.setHeightForWidth(self.output_file_line.sizePolicy().hasHeightForWidth())
        self.output_file_line.setSizePolicy(sizePolicy)
        self.output_file_line.setMinimumSize(QSize(400, 35))

        self.out_file_layout.addWidget(self.output_file_line)

        self.choose_out_file_btn = QPushButton(self.centralwidget)
        self.choose_out_file_btn.setObjectName(u"choose_out_file_btn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.choose_out_file_btn.sizePolicy().hasHeightForWidth())
        self.choose_out_file_btn.setSizePolicy(sizePolicy1)
        self.choose_out_file_btn.setMinimumSize(QSize(100, 35))
        self.choose_out_file_btn.setMaximumSize(QSize(104, 16777215))

        self.out_file_layout.addWidget(self.choose_out_file_btn)


        self.verticalLayout.addLayout(self.out_file_layout)

        self.cookies_layout = QHBoxLayout()
        self.cookies_layout.setObjectName(u"cookies_layout")
        self.cookies_layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.cookies_layout.setContentsMargins(0, -1, 0, -1)
        self.cookies_file_line = QLineEdit(self.centralwidget)
        self.cookies_file_line.setObjectName(u"cookies_file_line")
        sizePolicy.setHeightForWidth(self.cookies_file_line.sizePolicy().hasHeightForWidth())
        self.cookies_file_line.setSizePolicy(sizePolicy)
        self.cookies_file_line.setMinimumSize(QSize(400, 35))

        self.cookies_layout.addWidget(self.cookies_file_line)

        self.choose_cookies_btn = QPushButton(self.centralwidget)
        self.choose_cookies_btn.setObjectName(u"choose_cookies_btn")
        sizePolicy1.setHeightForWidth(self.choose_cookies_btn.sizePolicy().hasHeightForWidth())
        self.choose_cookies_btn.setSizePolicy(sizePolicy1)
        self.choose_cookies_btn.setMinimumSize(QSize(100, 35))
        self.choose_cookies_btn.setMaximumSize(QSize(104, 16777215))

        self.cookies_layout.addWidget(self.choose_cookies_btn)


        self.verticalLayout.addLayout(self.cookies_layout)

        self.ctrls_layout = QHBoxLayout()
        self.ctrls_layout.setObjectName(u"ctrls_layout")
        self.start_btn = QPushButton(self.centralwidget)
        self.start_btn.setObjectName(u"start_btn")
        self.start_btn.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.start_btn.sizePolicy().hasHeightForWidth())
        self.start_btn.setSizePolicy(sizePolicy1)
        self.start_btn.setMinimumSize(QSize(0, 35))
        self.start_btn.setMaximumSize(QSize(200, 16777215))

        self.ctrls_layout.addWidget(self.start_btn)

        self.stop_btn = QPushButton(self.centralwidget)
        self.stop_btn.setObjectName(u"stop_btn")
        self.stop_btn.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.stop_btn.sizePolicy().hasHeightForWidth())
        self.stop_btn.setSizePolicy(sizePolicy1)
        self.stop_btn.setMinimumSize(QSize(0, 35))
        self.stop_btn.setMaximumSize(QSize(200, 16777215))

        self.ctrls_layout.addWidget(self.stop_btn)


        self.verticalLayout.addLayout(self.ctrls_layout)

        self.progress_log_ctrl_layout = QHBoxLayout()
        self.progress_log_ctrl_layout.setObjectName(u"progress_log_ctrl_layout")
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setMinimumSize(QSize(0, 35))
        self.progressBar.setValue(24)

        self.progress_log_ctrl_layout.addWidget(self.progressBar)

        self.show_hide_log_btn = QPushButton(self.centralwidget)
        self.show_hide_log_btn.setObjectName(u"show_hide_log_btn")
        sizePolicy1.setHeightForWidth(self.show_hide_log_btn.sizePolicy().hasHeightForWidth())
        self.show_hide_log_btn.setSizePolicy(sizePolicy1)
        self.show_hide_log_btn.setMinimumSize(QSize(0, 35))

        self.progress_log_ctrl_layout.addWidget(self.show_hide_log_btn)


        self.verticalLayout.addLayout(self.progress_log_ctrl_layout)

        self.output_log = QTextBrowser(self.centralwidget)
        self.output_log.setObjectName(u"output_log")
        self.output_log.setMinimumSize(QSize(600, 200))

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
        self.input_url_line.setText("")
        self.input_url_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Input URL", None))
        self.output_file_line.setText("")
        self.output_file_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Output file", None))
        self.choose_out_file_btn.setText(QCoreApplication.translate("MainWindow", u"Select", None))
        self.cookies_file_line.setText("")
        self.cookies_file_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Cookies file", None))
        self.choose_cookies_btn.setText(QCoreApplication.translate("MainWindow", u"Select", None))
        self.start_btn.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.stop_btn.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.show_hide_log_btn.setText(QCoreApplication.translate("MainWindow", u"Hide log", None))
        self.output_log.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Cantarell'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Lato'; font-size:11pt;\"><br /></p></body></html>", None))
    # retranslateUi

