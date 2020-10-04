import sys
from PySide2.QtWidgets import QApplication
from PySide2 import QtCore

from window import Window

if __name__ == '__main__':
    #boh
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)
    # Create the Qt Application
    app = QApplication(sys.argv)    

    window = Window()
    window.show()

    # Run the main Qt loop
    sys.exit(app.exec_())