# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'output_file_ext_dialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(410, 123)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(400, 0))
        self.label.setStyleSheet(u"color: rgb(238, 238, 236);")
        self.label.setTextFormat(Qt.RichText)
        self.label.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label)

        self.extension_combo = QComboBox(Dialog)
        self.extension_combo.addItem("")
        self.extension_combo.addItem("")
        self.extension_combo.addItem("")
        self.extension_combo.setObjectName(u"extension_combo")

        self.verticalLayout_2.addWidget(self.extension_combo)


        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Output video name is missing a valid extension, choose one from the list below", None))
        self.extension_combo.setItemText(0, QCoreApplication.translate("Dialog", u"mp4", None))
        self.extension_combo.setItemText(1, QCoreApplication.translate("Dialog", u"mkv", None))
        self.extension_combo.setItemText(2, QCoreApplication.translate("Dialog", u"avi", None))

    # retranslateUi

