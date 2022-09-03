from PyQt6 import QtCore, QtWidgets
from utils.dialog import Dialog
from utils.copy import copy_to_clipboard
from sys import exit, argv


class Ui_PasswordGenerator(object):
    def __init__(self):
        super().__init__()
        self.useSymbols = False
        self.useNumbers = False
        self.useLowerCase = False
        self.useUpperCase = False

    def setupUi(self, PasswordGenerator):
        PasswordGenerator.setObjectName("PasswordGenerator")
        PasswordGenerator.resize(861, 523)
        self.centralwidget = QtWidgets.QWidget(PasswordGenerator)
        self.centralwidget.setObjectName("centralwidget")
        self.password_output = QtWidgets.QLineEdit(self.centralwidget)
        self.password_output.setGeometry(QtCore.QRect(420, 360, 401, 31))
        self.password_output.setObjectName("password_output")
        self.password_label = QtWidgets.QLabel(self.centralwidget)
        self.password_label.setGeometry(QtCore.QRect(20, 330, 391, 61))
        self.password_label.setObjectName("password_label")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 0, 811, 321))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.symbols = QtWidgets.QCheckBox(self.layoutWidget)
        self.symbols.setObjectName("symbols")
        self.symbols.stateChanged.connect(self.useSymbolsClicked)
        self.gridLayout.addWidget(self.symbols, 1, 1, 1, 1)
        self.password_length = QtWidgets.QComboBox(self.layoutWidget)
        self.password_length.setObjectName("password_length")
        for i in range(0, 127):
            self.password_length.addItem("")
        self.gridLayout.addWidget(self.password_length, 0, 1, 1, 1)

        self.lowercase = QtWidgets.QCheckBox(self.layoutWidget)
        self.lowercase.setObjectName("lowercase")
        self.lowercase.stateChanged.connect(self.useLowerCaseClicked)
        self.gridLayout.addWidget(self.lowercase, 3, 1, 1, 1)

        self.numbers = QtWidgets.QCheckBox(self.layoutWidget)
        self.numbers.setObjectName("numbers")
        self.numbers.stateChanged.connect(self.useNumbersClicked)
        self.gridLayout.addWidget(self.numbers, 2, 1, 1, 1)

        self.password_length_label = QtWidgets.QLabel(self.layoutWidget)
        self.password_length_label.setObjectName("password_length_label")
        self.gridLayout.addWidget(self.password_length_label, 0, 0, 1, 1)

        self.numbers_label = QtWidgets.QLabel(self.layoutWidget)
        self.numbers_label.setObjectName("numbers_label")
        self.gridLayout.addWidget(self.numbers_label, 2, 0, 1, 1)

        self.uppercase = QtWidgets.QCheckBox(self.layoutWidget)
        self.uppercase.setObjectName("uppercase")
        self.uppercase.stateChanged.connect(self.useUpperCaseClicked)
        self.gridLayout.addWidget(self.uppercase, 4, 1, 1, 1)

        self.uppercase_label = QtWidgets.QLabel(self.layoutWidget)
        self.uppercase_label.setObjectName("uppercase_label")
        self.gridLayout.addWidget(self.uppercase_label, 4, 0, 1, 1)

        self.lowercase_label = QtWidgets.QLabel(self.layoutWidget)
        self.lowercase_label.setObjectName("lowercase_label")
        self.gridLayout.addWidget(self.lowercase_label, 3, 0, 1, 1)

        self.symbols_label = QtWidgets.QLabel(self.layoutWidget)
        self.symbols_label.setObjectName("symbols_label")
        self.gridLayout.addWidget(self.symbols_label, 1, 0, 1, 1)

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(420, 330, 401, 24))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.generateButtonClicked)

        PasswordGenerator.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(PasswordGenerator)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 861, 22))
        self.menubar.setObjectName("menubar")
        PasswordGenerator.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(PasswordGenerator)
        self.statusbar.setObjectName("statusbar")
        PasswordGenerator.setStatusBar(self.statusbar)

        self.retranslateUi(PasswordGenerator)
        QtCore.QMetaObject.connectSlotsByName(PasswordGenerator)

    def retranslateUi(self, PasswordGenerator):
        _translate = QtCore.QCoreApplication.translate
        PasswordGenerator.setWindowTitle(_translate(
            "PasswordGenerator", "Password Generator"))
        self.password_label.setText(
            _translate("PasswordGenerator", "Password"))
        self.symbols.setText(_translate("PasswordGenerator", "( e.g. @#$%)"))
        self.password_length.setItemText(
            0, _translate("PasswordGenerator", "6"))
        for i in range(0, 128):
            self.password_length.setItemText(
                i, _translate("PasswordGenerator", f"{i+6}"))
        self.password_length.setItemText(
            123, _translate("PasswordGenerator", "256"))
        self.password_length.setItemText(
            124, _translate("PasswordGenerator", "512"))
        self.password_length.setItemText(
            125, _translate("PasswordGenerator", "1048"))
        self.password_length.setItemText(
            126, _translate("PasswordGenerator", "2048"))
        self.lowercase.setText(_translate(
            "PasswordGenerator", "( e.g. abcdefgh )"))
        self.numbers.setText(_translate("PasswordGenerator", "( e.g. 123456)"))
        self.password_length_label.setText(
            _translate("PasswordGenerator", "Password Length"))
        self.numbers_label.setText(_translate(
            "PasswordGenerator", "Include Numbers:"))
        self.uppercase.setText(_translate(
            "PasswordGenerator", "( e.g. ABCDEFGH )"))
        self.uppercase_label.setText(_translate(
            "PasswordGenerator", "Include Uppercase Characters:"))
        self.lowercase_label.setText(_translate(
            "PasswordGenerator", "Include Lowercase Characters:"))
        self.symbols_label.setText(_translate(
            "PasswordGenerator", "Include Symbols:"))
        self.pushButton.setText(_translate(
            "PasswordGenerator", "GeneratePassword"))

    def useSymbolsClicked(self):
        self.useSymbols = True if self.symbols.isChecked() else False
            
    def useNumbersClicked(self):
        self.useNumbers = True if self.numbers.isChecked() else False

    def useLowerCaseClicked(self):
        self.useLowerCase = True if self.lowercase.isChecked() else False

    def useUpperCaseClicked(self):
        self.useUpperCase = True if self.uppercase.isChecked() else False

    def generateButtonClicked(self):
        copy_to_clipboard(self.password_length)
        dlg = Dialog.CustomDialog()
        dlg.exec()


if __name__ == "__main__":
    app = QtWidgets.QApplication(argv)
    PasswordGenerator = QtWidgets.QMainWindow()
    ui = Ui_PasswordGenerator()
    ui.setupUi(PasswordGenerator)
    PasswordGenerator.show()
    exit(app.exec())
