import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget
from PySide2 import QtCore
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader

from ui_main_win import Ui_MainWindow

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.choose_out_dir_btn.clicked.connect(self.gigi)
    
    def gigi(self):
        self.ui.textBrowser.setText(self.ui.textBrowser.toPlainText() + "\nGIIIIGI")

if __name__ == '__main__':
    #boh
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)
    # Create the Qt Application
    app = QApplication(sys.argv)    

    window = Window()
    window.show()

    # Run the main Qt loop
    sys.exit(app.exec_())