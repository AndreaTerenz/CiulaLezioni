from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog
from ui_main_win import Ui_MainWindow
from enum import Enum

class Window(QMainWindow):
    class FileDialogMode(Enum):
        OUTPUT_DIR = 1
        COOKIES_TXT = 2

    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.choose_out_dir_btn.clicked.connect(self.choose_output_dir)
        self.ui.choose_cookies_btn.clicked.connect(self.choose_cookies_file)

    def choose_output_dir(self):
        text = self.choose_file(self.FileDialogMode.OUTPUT_DIR)

        if text != None:
            self.ui.output_dir_line.setText(text)

    def choose_cookies_file(self):
        text = self.choose_file(self.FileDialogMode.COOKIES_TXT)

        if text != None:
            self.ui.cookies_file_line.setText(text)

    def choose_file(self, mode):
        dialog = QFileDialog(self)
        dialog.setAcceptMode(QFileDialog.AcceptOpen)

        if (mode == self.FileDialogMode.OUTPUT_DIR):
            dialog.setFileMode(QFileDialog.Directory)
            dialog.setOption(QFileDialog.ShowDirsOnly, True)
        elif (mode == self.FileDialogMode.COOKIES_TXT):
            dialog.setOption(QFileDialog.ReadOnly, True)
            dialog.setNameFilter("Text files (*.txt)")

        if dialog.exec_():
            return dialog.selectedFiles()[0]
        
        return None