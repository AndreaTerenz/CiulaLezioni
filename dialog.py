from PySide2.QtWidgets import (QDialog, QMessageBox)

from ui_out_file_diag import Ui_Dialog

class OutputFileNameDialog(QDialog):
    def __init__(self):
        super(OutputFileNameDialog, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)