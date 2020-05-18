import sys
from PyQt5.QtWidgets import (QLineEdit, QPushButton, QApplication,
                             QVBoxLayout, QDialog, QLabel, QFormLayout, QGroupBox, QMainWindow, QPlainTextEdit,
                             QHBoxLayout, QGridLayout, QComboBox)
import qtmodern.styles
import qtmodern.windows
import valid


class Form(QDialog):
    def add_window(self):
        self.adder.show()

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.adder = Adder()
        self.button = QPushButton("Dodaj")
        self.button2 = QPushButton("Edytuj")
        self.button3 = QPushButton("Szukaj")
        # Create layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(self.button)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)
        # Set dialog layout
        self.setLayout(layout)
        # Add button signal to greetings slot
        self.button.clicked.connect(self.add_window)


class Adder(QDialog):
    def __init__(self, parent=None):
        super(Adder, self).__init__(parent)

        self.mainLayout = QVBoxLayout()

        self.formLayoutBox = QGroupBox()

        self.formLayout2 = QFormLayout()
        self.formLayoutBox2 = QGroupBox("Opis uszkodzenia")
        self.description = QPlainTextEdit()
        self.formLayout2.addWidget(self.description)
        self.formLayoutBox2.setLayout(self.formLayout2)

        self.typeList = QComboBox()
        self.typeLabel = QLabel("Typ przedmiotu")
        self.mainLayout.addWidget(self.typeLabel)
        self.mainLayout.addWidget(self.typeList)

        self.formLayoutBox3 = QGroupBox()
        self.formLayout3 = QGridLayout()
        self.empList = QComboBox()
        self.addSome = QPlainTextEdit()
        self.labelUwag = QLabel("Dodatkowe uwagi")
        self.labelAcc = QLabel("Urządzenie przyjął")
        self.formLayout3.addWidget(self.labelUwag, 1, 1)
        self.formLayout3.addWidget(self.labelAcc, 1, 2)
        self.formLayout3.addWidget(self.empList, 2, 2)
        self.formLayout3.addWidget(self.addSome, 2, 1)
        self.formLayoutBox3.setLayout(self.formLayout3)

        self.formLayout = QFormLayout()
        self.lineModel = QLineEdit()
        self.lineNumber = QLineEdit()
        self.lineClient = QLineEdit()
        self.lineClientNumber = QLineEdit()
        self.formLayout.addRow(
            QLabel("Nazwa/model urządzenia"), self.lineModel
        )
        self.formLayout.addRow(
            QLabel("Numer seryjny urządzenia"), self.lineNumber
        )
        self.formLayout.addRow(
            QLabel("Nazwa klienta"), self.lineClient
        )
        self.formLayout.addRow(
            QLabel("Numer kontaktowy"), self.lineClientNumber
        )
        self.formLayoutBox.setLayout(self.formLayout)
        self.mainLayout.addWidget(self.formLayoutBox)
        self.mainLayout.addWidget(self.formLayoutBox2)
        self.mainLayout.addWidget(self.formLayoutBox3)
        self.setLayout(self.mainLayout)


if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    form = Form()
    qtmodern.styles.dark(app)
    form.show()
    # Run the main Qt loop
    sys.exit(app.exec_())
