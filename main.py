import sys
from PyQt5.QtWidgets import (QLineEdit, QPushButton, QApplication,
                             QVBoxLayout, QDialog, QLabel, QFormLayout, QGroupBox, QMainWindow, QPlainTextEdit,
                             QHBoxLayout, QGridLayout, QComboBox, QErrorMessage, QMessageBox, QCheckBox)
import qtmodern.styles
import qtmodern.windows
import valid
import db
from datetime import date

database = db.DataBase()
employees = database.get_all_pracownicy()


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
    def add(self):
        types = ["drukarka_atramentowa", "drukarka_laserowa", "drukarka_iglowa", "laptop", "telefon"]

        print(types[self.typeList.currentIndex()])
        print(self.lineClientNumber.text())
        print(employees[self.empList.currentIndex()]["Id_pracownika"])
        database.insert_potwierdzenie(data=date.today(),
                                      typ=types[self.typeList.currentIndex()],
                                      nazwa_urzadzenia=self.lineModel.text(),
                                      sn=self.lineNumber.text(),
                                      nazwa_klienta=self.lineClient.text(),
                                      nr_tel=self.lineClientNumber.text(),
                                      opis_uszk=self.description.toPlainText(),
                                      informacje_dodatkowe=self.addSome.toPlainText(),
                                      opis_naprawy="",
                                      id_prac=employees[self.empList.currentIndex()]["Id_pracownika"])
        print(database.get_all_pracownicy())
        self.destroy()

    def validate(self):
        try:
            valid.device_name_valid(self.lineModel.text())
            valid.serial_number_valid(self.lineNumber.text())
            valid.client_name_valid(self.lineClient.text())
            valid.phone_number_valid(self.lineClientNumber.text())
            valid.description_valid(self.description.toPlainText())
        except ValueError as error:
            error_dialog = QMessageBox()
            print(error.args)
            error_dialog.setWindowTitle("Error")
            error_dialog.setText(error.args[0])
            error_dialog.exec()
            return
        self.add()
        # jarkowe wstawianie do bazki

    def set_checkboxes(self):
        types = [self.detailLayoutInk, self.detailLayoutLaser, self.detailLayoutPoint, self.detailLayoutLaptop, self.detailLayoutTelephone]
        for i in range(0, len(types)):
            types[i].hide()

        print(self.typeList.currentIndex())
        types[self.typeList.currentIndex()].show()
        return

    def __init__(self, parent=None):
        super(Adder, self).__init__(parent)

        self.mainLayout = QVBoxLayout()
        self.setFixedSize(600,1000)
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

        self.detailLayoutLaser = QGroupBox()
        self.detailLayoutInk = QGroupBox()
        self.detailLayoutPoint = QGroupBox()
        self.detailLayoutLaptop = QGroupBox()
        self.detailLayoutTelephone = QGroupBox()


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

        self.buttonFinish = QPushButton("Dodaj potwierdzenie")

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

        # drukarka laserowa
        self.layoutLaser = QVBoxLayout()
        self.laserButtons = {
            "power": QCheckBox("Kabel zasilający"),
            "signal": QCheckBox("Kabel sygnałowy"),
            "black_toner": QCheckBox("Czarny toner"),
            "color_toner": QCheckBox("Kolorowy toner"),
            "packing": QCheckBox("Opakowanie")
        }
        for key in self.laserButtons:
            self.layoutLaser.addWidget(self.laserButtons[key])
        self.detailLayoutLaser.setLayout(self.layoutLaser)
        self.mainLayout.addWidget(self.detailLayoutLaser)
        # drukarka igłowa
        self.layoutPoint = QVBoxLayout()
        self.pointButtons = {
            "power": QCheckBox("Kabel zasilający"),
            "signal": QCheckBox("Kabel sygnałowy"),
            "tape": QCheckBox("Taśma barwiąca"),
            "power_box": QCheckBox("Zasilacz"),
            "packing": QCheckBox("Opakowanie")
        }
        for key in self.pointButtons:
            self.layoutPoint.addWidget(self.pointButtons[key])
        self.detailLayoutPoint.setLayout(self.layoutPoint)
        self.mainLayout.addWidget(self.detailLayoutPoint)
        # drukarka atramentowa
        self.layoutInk = QVBoxLayout()
        self.inkButtons = {
            "power": QCheckBox("Kabel zasilający"),
            "signal": QCheckBox("Kabel sygnałowy"),
            "power_box": QCheckBox("Zasilacz"),
            "black_ink": QCheckBox("Czarny tusz"),
            "color_ink": QCheckBox("Kolorowy tusz"),
            "packing": QCheckBox("Opakowanie")
        }
        for key in self.inkButtons:
            self.layoutInk.addWidget(self.inkButtons[key])
        self.detailLayoutInk.setLayout(self.layoutInk)
        self.mainLayout.addWidget(self.detailLayoutInk)
        # laptop
        self.layoutLaptop = QVBoxLayout()
        self.laptopButtons = {
            "power": QCheckBox("Kabel zasilający"),
            "power_box": QCheckBox("Zasilacz"),
            "mouse": QCheckBox("Mysz USB"),
            "packing": QCheckBox("Opakowanie")
        }
        for key in self.laptopButtons:
            self.layoutLaptop.addWidget(self.laptopButtons[key])
        self.detailLayoutLaptop.setLayout(self.layoutLaptop)
        self.mainLayout.addWidget(self.detailLayoutLaptop)
        # komórka
        self.layoutPhone = QVBoxLayout()
        self.phoneButtons = {
            "power": QCheckBox("Kabel zasilający"),
            "charger": QCheckBox("Ładowarka"),
            "case": QCheckBox("Obudowa"),
            "mem_card": QCheckBox("Karta pamięci"),
            "sim_card": QCheckBox("Karta SIM"),
            "packing": QCheckBox("Opakowanie")
        }
        for key in self.phoneButtons:
            self.layoutPhone.addWidget(self.phoneButtons[key])
        self.detailLayoutTelephone.setLayout(self.layoutPhone)
        self.mainLayout.addWidget(self.detailLayoutTelephone)

        self.detailLayoutTelephone.hide()
        self.detailLayoutLaptop.hide()
        self.detailLayoutLaser.hide()
        self.detailLayoutPoint.hide()
        self.mainLayout.addWidget(self.formLayoutBox2)
        self.mainLayout.addWidget(self.formLayoutBox3)

        self.mainLayout.addWidget(self.buttonFinish)

        self.setLayout(self.mainLayout)

        self.buttonFinish.clicked.connect(self.validate)

        self.typeList.addItem("Drukarka atramentowa")
        self.typeList.addItem("Drukarka laserowa")
        self.typeList.addItem("Drukarka igłowa")
        self.typeList.addItem("Laptop")
        self.typeList.addItem("Telefon")

        # adding employees from db
        self.typeList.currentIndexChanged.connect(self.set_checkboxes)

        for i in employees:
            self.empList.addItem(i["Imie"] + " " + i["Nazwisko"])


if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    form = Form()
    qtmodern.styles.dark(app)
    form.show()
    # Run the main Qt loop
    sys.exit(app.exec_())
