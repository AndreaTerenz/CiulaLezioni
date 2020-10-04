import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog
from PySide2 import QtCore
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader

from ui_main_win import Ui_MainWindow

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.choose_out_dir_btn.clicked.connect(self.choose_output_dir)
        self.ui.choose_cookies_btn.clicked.connect(self.choose_cookies_file)
    
    def choose_output_dir(self):
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.Directory)
        dialog.setOption(QFileDialog.ShowDirsOnly, True)
        dialog.setAcceptMode(QFileDialog.AcceptOpen)

        if dialog.exec_():
            self.ui.output_dir_line.setText(dialog.selectedFiles()[0])

    def choose_cookies_file(self):
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.ExistingFile)
        dialog.setOption(QFileDialog.ReadOnly, True)
        dialog.setAcceptMode(QFileDialog.AcceptOpen)
        dialog.setNameFilter("Text files (*.txt)")

        if dialog.exec_():
            self.ui.cookies_file_line.setText(dialog.selectedFiles()[0])

if __name__ == '__main__':
    #boh
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)
    # Create the Qt Application
    app = QApplication(sys.argv)    

    window = Window()
    window.show()

    # Run the main Qt loop
    sys.exit(app.exec_())