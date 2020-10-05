from PySide2.QtWidgets import (QDialog, QMessageBox)

from ui_out_file_diag import Ui_Dialog

class OutputFileNameDialog(QDialog):
    def __init__(self):
        super(OutputFileNameDialog, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.buttonBox.accepted.connect(self.set_chosen_ext)
        self.chosen_extension = ""

    def set_chosen_ext(self):
        self.chosen_extension = self.ui.comboBox.currentText()

    def get_chosen_ext(self):
        return self.chosen_extension