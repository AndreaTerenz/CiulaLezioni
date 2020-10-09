import re
import os.path
import subprocess
import shlex
from subprocess        import Popen, PIPE
from enum              import Enum
from urllib.parse      import urlparse
from PySide2.QtWidgets import (QApplication, QMainWindow, QWidget,
                               QFileDialog, QLineEdit, QMessageBox, QScrollBar)

from ui_main_win import Ui_MainWindow

class Window(QMainWindow):
    class FileDialogMode(Enum):
        OUTPUT_FILE = 1
        COOKIES_TXT = 2

    class UIMode(Enum):
        RUNNING = 0
        IDLE = 1

    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.to_disable_when_start = [
            self.ui.cookies_layout,
            self.ui.url_layout,
            self.ui.out_file_layout,
            self.ui.start_btn
        ]

        self.text_lines = {
            "input_url" : self.ui.input_url_line,
            "output_file" : self.ui.output_file_line,
            "cookies_file" : self.ui.cookies_file_line
        }

        self.ui.choose_out_file_btn.clicked.connect(self.choose_output_file)
        self.ui.choose_cookies_btn.clicked.connect(self.choose_cookies_file)

        for k, l in self.text_lines.items():
            l.textChanged.connect(self.check_start)

        self.ui.start_btn.clicked.connect(self.start_ciuling)
        self.ui.stop_btn.clicked.connect(self.stop_ciuling)
        self.ui.show_hide_log_btn.clicked.connect(self.toggle_log)

        self.has_started = False
        self.check_start()

        self.toggle_log()

    def toggle_log(self):
        hidden = not(self.ui.output_log.isHidden())
        self.ui.output_log.setHidden(hidden)

        self.ui.show_hide_log_btn.setText("Show log" if hidden else "Hide log")
        
        self.ui.centralwidget.adjustSize()
        self.adjustSize()

    def check_start(self):
        all_filled_in = True
        for k, l in self.text_lines.items():
            t = l.text().strip()
            all_filled_in = all_filled_in and (t != "")

        self.ui.start_btn.setEnabled(all_filled_in)

    def choose_cookies_file(self):
        self.choose_file(self.FileDialogMode.COOKIES_TXT, self.ui.cookies_file_line)

    def choose_output_file(self):
        self.choose_file(self.FileDialogMode.OUTPUT_FILE, self.ui.output_file_line)

    def choose_file(self, mode:FileDialogMode, text_line:QLineEdit):
        dialog = QFileDialog(self)
        dialog.setOption(QFileDialog.ReadOnly, True)
        
        if (mode == self.FileDialogMode.OUTPUT_FILE):
            dialog.setAcceptMode(QFileDialog.AcceptSave)
            dialog.setFileMode(QFileDialog.AnyFile)
            dialog.setNameFilter("Video files (*.mp4 *.avi *.mkv)")
        elif (mode == self.FileDialogMode.COOKIES_TXT):
            dialog.setAcceptMode(QFileDialog.AcceptOpen)
            dialog.setFileMode(QFileDialog.ExistingFile)
            dialog.setNameFilter("Text files (*.txt)")

        if dialog.exec_():
            text_line.setText(dialog.selectedFiles()[0])

    def add_to_log(self, str):
        sb = self.ui.output_log.verticalScrollBar()
        sb_already_max = (sb.value() == sb.maximum())

        self.ui.output_log.setText(self.ui.output_log.toPlainText() + str)

        if (sb_already_max):
            sb.setValue(sb.maximum())

        self.ui.output_log.repaint()

    def setUI(self, mode:UIMode, resetArgs=False):
        if (mode == self.UIMode.RUNNING):
            for x in self.to_disable_when_start:
                x.setEnabled(False)
            self.ui.stop_btn.setEnabled(True)
        if (mode == self.UIMode.IDLE):
            for x in self.to_disable_when_start:
                x.setEnabled(True)

            self.ui.stop_btn.setEnabled(False)

            if resetArgs:
                for k, l in self.text_lines.items():
                    l.setText("")        

    def stop_ciuling(self):
        self.setUI(self.UIMode.IDLE, resetArgs=True)

    def show_error_box(self, msg,title=""):
        (QMessageBox(QMessageBox.Critical, title, msg)).exec_()

    def check_url(self, url:str):
        res = urlparse(url)
        return (res.scheme != "" and res.netloc != "")

    def run(self, command):
        process = Popen(command, stdout=PIPE, shell=True)
        done = False
        while not(done):
            line = process.stdout.readline().rstrip()
            done = (not line)
            if not done:
                yield line

    def start_ciuling(self):
        ### CHECK OUTPUT FILE NAME ###

        in_url   = self.text_lines["input_url"].text().strip()
        out_file = self.text_lines["output_file"].text().strip()
        cookies  = self.text_lines["cookies_file"].text().strip()

        self.add_to_log("Checking input arguments...")
        if not(os.path.isfile(cookies)):
            self.show_error_box(f"Cookies file \"{cookies}\" not found", "File not found")
        elif not(cookies.lower().endswith(".txt")):
            self.show_error_box(f"Given cookies file \"{cookies}\" is not a .txt", "Invalid file")
        elif not(self.check_url(in_url)):
            self.show_error_box(f"Given string \"{in_url}\" is not a valid URL", "Invalid url")
        else:
            self.add_to_log("done\n\n")

            self.has_started = True

            self.setUI(self.UIMode.RUNNING)

            self.add_to_log(f"Source URL: {in_url}\n")
            self.add_to_log(f"Cookies txt file: {cookies}\n")
            self.add_to_log(f"Output file name: {out_file}\n\n")

            ##### THE CIULING HAPPENS HERE #####

            for path in self.run(f"youtube-dl --no-color --cookies {cookies} -o {out_file} {in_url}"):
                self.add_to_log(str(path) + "\n")

            self.add_to_log("Done\n")
            self.setUI(self.UIMode.IDLE)                