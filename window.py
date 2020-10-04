from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog, QLineEdit
from ui_main_win import Ui_MainWindow
from enum import Enum
import re

class Window(QMainWindow):
    class FileDialogMode(Enum):
        OUTPUT_DIR  = 1
        COOKIES_TXT = 2

    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.choose_out_dir_btn.clicked.connect(self.choose_output_dir)
        self.ui.choose_cookies_btn.clicked.connect(self.choose_cookies_file)

        self.ui.output_dir_line.textChanged.connect(self.check_start)
        self.ui.cookies_file_line.textChanged.connect(self.check_start)
        self.ui.output_file_name_line.textChanged.connect(self.check_start)

        self.ui.start_stop_btn.clicked.connect(self.start_ciuling)

    def check_start(self):
        out_dir_txt  = self.ui.output_dir_line.text().strip()
        cookies_txt  = self.ui.cookies_file_line.text().strip()
        out_file_txt = self.ui.output_file_name_line.text().strip()

        self.ui.start_stop_btn.setEnabled((out_dir_txt != "" and cookies_txt != "" and out_file_txt != ""))

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

    def start_ciuling(self):
        out_dir  = self.ui.output_dir_line.text().strip()
        cookies  = self.ui.cookies_file_line.text().strip()
        out_file = self.ui.output_file_name_line.text().strip()

        print(f"Output directory: {out_dir}")
        print(f"Cookies txt file: {cookies}")
        print(f"Output file name: {out_file}")