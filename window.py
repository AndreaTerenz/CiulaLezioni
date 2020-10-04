from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog, QLineEdit
from ui_main_win import Ui_MainWindow
from enum import Enum

class Window(QMainWindow):
    class FileDialogMode(Enum):
        OUTPUT_DIR  = 1
        COOKIES_TXT = 2
        OUTPUT_FILE = 3

    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.choose_out_dir_btn.clicked.connect(self.choose_output_dir)
        self.ui.choose_cookies_btn.clicked.connect(self.choose_cookies_file)
        self.ui.set_output_file_btn.clicked.connect(self.choose_output_file)

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
            else:
                dialog.setOption(QFileDialog.ReadOnly, True)
                
                if (mode == self.FileDialogMode.COOKIES_TXT):
                    dialog.setFileMode(QFileDialog.ExistingFile)
                    dialog.setNameFilter("Text files (*.txt)")
                elif (mode == self.FileDialogMode.OUTPUT_FILE):
                    dialog.setFileMode(QFileDialog.AnyFile)
                    dialog.setNameFilter("Videos (*.mp4 *.mkv *.avi)")

            if dialog.exec_():
                text_line.setText(dialog.selectedFiles()[0])