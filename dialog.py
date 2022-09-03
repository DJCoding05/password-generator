from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QDialog

class Dialog(QDialog):
    def __init__(self, title="Window", message="This is a message"):
        super().__init__()
        self.title = title
        self.setWindowTitle(self.title)

        QBtn = QtWidgets.QDialogButtonBox.StandardButton.Ok

        self.buttonBox = QtWidgets.QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QtWidgets.QVBoxLayout()
        self.message = QtWidgets.QLabel(message)
        self.layout.addWidget(self.message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)