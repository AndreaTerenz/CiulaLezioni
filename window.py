from PySide2.QtWidgets import (QApplication, QMainWindow, QWidget,
                               QFileDialog, QLineEdit)

from enum import Enum
import re

from ui_main_win import Ui_MainWindow
from dialog import OutputFileNameDialog

class Window(QMainWindow):
    class FileDialogMode(Enum):
        OUTPUT_DIR  = 1
        COOKIES_TXT = 2

    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.to_disable_when_start = [
            self.ui.choose_cookies_btn,
            self.ui.choose_out_dir_btn,
            self.ui.cookies_file_line,
            self.ui.output_dir_line,
            self.ui.output_file_name_line,
            self.ui.start_btn
        ]

        self.text_lines = {
            "output_dir" : self.ui.output_dir_line,
            "cookies_file" : self.ui.cookies_file_line,
            "output_file" : self.ui.output_file_name_line
        }

        self.ui.choose_out_dir_btn.clicked.connect(self.choose_output_dir)
        self.ui.choose_cookies_btn.clicked.connect(self.choose_cookies_file)

        self.ui.output_dir_line.textChanged.connect(self.check_start)
        self.ui.cookies_file_line.textChanged.connect(self.check_start)
        self.ui.output_file_name_line.textChanged.connect(self.check_start)

        self.ui.start_btn.clicked.connect(self.start_ciuling)
        self.ui.stop_btn.clicked.connect(self.stop_ciuling)

        self.has_started = False
        
        x = OutputFileNameDialog()
        
        if (x.exec_()):
            print(x.get_chosen_ext())

    def check_start(self):
        all_filled_in = True
        for k, l in self.text_lines.items():
            t = l.text().strip()
            all_filled_in = all_filled_in and (t != "")

        self.ui.start_btn.setEnabled(all_filled_in)

    def choose_output_dir(self):
        self.choose_file(self.FileDialogMode.OUTPUT_DIR, self.ui.output_dir_line)

    def choose_cookies_file(self):
        self.choose_file(self.FileDialogMode.COOKIES_TXT, self.ui.cookies_file_line)

    def choose_output_file(self):
        self.choose_file(self.FileDialogMode.OUTPUT_FILE, self.ui.output_file_name_line)

    def choose_file(self, mode, text_line):
        if (isinstance(mode, self.FileDialogMode) and isinstance(text_line, QLineEdit)):
            dialog = QFileDialog(self)
            dialog.setAcceptMode(QFileDialog.AcceptOpen)

            if (mode == self.FileDialogMode.OUTPUT_DIR):
                dialog.setFileMode(QFileDialog.Directory)
                dialog.setOption(QFileDialog.ShowDirsOnly, True)
            elif (mode == self.FileDialogMode.COOKIES_TXT):
                dialog.setOption(QFileDialog.ReadOnly, True)
                dialog.setFileMode(QFileDialog.ExistingFile)
                dialog.setNameFilter("Text files (*.txt)")

            if dialog.exec_():
                text_line.setText(dialog.selectedFiles()[0])

    def add_to_log(self, str):
        self.ui.output_log.setText(self.ui.output_log.toPlainText() + str)

    def stop_ciuling(self):
        for x in self.to_disable_when_start:
            x.setEnabled(True)

        self.ui.stop_btn.setEnabled(False)

        for k, l in self.text_lines.items():
            l.setText("")

    def start_ciuling(self):
         
         
        self.has_started = True

        for x in self.to_disable_when_start:
            x.setEnabled(False)

        self.ui.stop_btn.setEnabled(True)

        out_dir  = self.text_lines["output_dir"].text().strip()
        cookies  = self.text_lines["cookies_file"].text().strip()
        out_file = self.text_lines["output_file"].text().strip()

        self.add_to_log(f"Output directory: {out_dir}\n")
        self.add_to_log(f"Cookies txt file: {cookies}\n")
        self.add_to_log(f"Output file name: {out_file}\n")

        ##### THE CIULING HAPPENS HERE #####