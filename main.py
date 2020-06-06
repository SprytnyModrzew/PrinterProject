import os
import sys

from PyQt5.QtGui import QWindow
from PyQt5.QtWidgets import (QLineEdit, QPushButton, QApplication,
                             QVBoxLayout, QDialog, QLabel, QFormLayout, QGroupBox, QMainWindow, QPlainTextEdit,
                             QHBoxLayout, QGridLayout, QComboBox, QErrorMessage, QMessageBox, QCheckBox, QTableWidget,
                             QTableWidgetItem, QWidget)
import qtmodern.styles
import qtmodern.windows
import valid
import db
from datetime import date,datetime
import latex_converter

import des

des.initial()
des.create16keys()
# des.encrypt("admin")

if not os.path.exists("potwierdzenia.db"):
    # first use of program
    print('exists now')
    database = db.DataBase()
    database.sql_create_tables()
    des.encrypt("admin")
else:
    database = db.DataBase()
    print('existed')
employees = database.get_all_pracownicy()


def updateEmps():
    employeesTemp = database.get_all_pracownicy()
    print(employeesTemp)
    employees.clear()
    for i in range(0, len(employeesTemp)):
        employees.append(employeesTemp[i])
    print(employees)


class EmpFillForm(QWidget):
    def action(self):
        return

    def __init__(self, parent=None):
        super(EmpFillForm, self).__init__(parent)
        self.labelName = QLabel("Imię")
        self.lineName = QLineEdit()
        self.labelSurname = QLabel("Nazwisko")
        self.lineSurname = QLineEdit()

        self.labelEmpNumber = QLabel("Pracownik")
        self.lineEmpNumber = QComboBox()

        self.button = QPushButton()

        self.mainLayout = QVBoxLayout()

        self.formLayout = QFormLayout()

        self.button.clicked.connect(self.action)


class EmpAdder(EmpFillForm):
    def action(self):
        try:
            valid.name_valid(self.lineName.text())
            valid.surname_valid(self.lineSurname.text())
        except ValueError as error:
            error_dialog = QMessageBox()
            print(error.args)
            error_dialog.setWindowTitle("Error")
            error_dialog.setText(error.args[0])
            error_dialog.exec()
            return
        super(EmpAdder, self).action()
        print("woop")
        database.insert_pracownik(self.lineName.text(), self.lineSurname.text(), 'T')
        print("woop")
        updateEmps()
        self.destroy()

    def __init__(self, parent=None):
        super(EmpAdder, self).__init__(parent)
        self.setWindowTitle("Dodawanie pracownika")
        self.button.setText("Dodaj pracownika")
        self.formLayout.addRow(self.labelName, self.lineName)
        self.formLayout.addRow(self.labelSurname, self.lineSurname)

        self.mainLayout.addLayout(self.formLayout)
        self.mainLayout.addWidget(self.button)
        self.setLayout(self.mainLayout)


class EmpEditor(EmpFillForm):
    def setEmp(self):
        self.lineName.setText(employees[self.lineEmpNumber.currentIndex()]["Imie"])
        self.lineSurname.setText(employees[self.lineEmpNumber.currentIndex()]["Nazwisko"])
        if employees[self.lineEmpNumber.currentIndex()]["Aktywny"] == 'T':
            self.checkActive.setChecked(True)
        else:
            self.checkActive.setChecked(False)

    def deleteEmp(self):
        database.update_pracownicy(id_prac=employees[self.lineEmpNumber.currentIndex()]["Id_pracownika"],
                                   imie=employees[self.lineEmpNumber.currentIndex()]["Imie"],
                                   nazwisko=employees[self.lineEmpNumber.currentIndex()]["Nazwisko"],
                                   aktywny='N')
        updateEmps()
        self.destroy()

    def action(self):
        try:
            valid.name_valid(self.lineName.text())
            valid.surname_valid(self.lineSurname.text())
        except ValueError as error:
            error_dialog = QMessageBox()
            print(error.args)
            error_dialog.setWindowTitle("Error")
            error_dialog.setText(error.args[0])
            error_dialog.exec()
            return
        x = 'N'
        if self.checkActive.isChecked():
            x = 'T'
        database.update_pracownicy(id_prac=employees[self.lineEmpNumber.currentIndex()]["Id_pracownika"],
                                   imie=self.lineName.text(),
                                   nazwisko=self.lineSurname.text(),
                                   aktywny=x)
        updateEmps()
        self.lineEmpNumber.clear()
        for i in employees:
            self.lineEmpNumber.addItem(i["Imie"] + " " + i["Nazwisko"])
        self.destroy()
        return

    def __init__(self, parent=None):
        super(EmpEditor, self).__init__(parent)
        self.setWindowTitle("Edycja pracowników")
        self.formLayout.addRow(self.labelEmpNumber, self.lineEmpNumber)
        self.formLayout.addRow(self.labelName, self.lineName)
        self.formLayout.addRow(self.labelSurname, self.lineSurname)

        self.buttonDelete = QPushButton("Usuń pracownika")

        self.labelName.setText("Nowe imię")
        self.labelSurname.setText("Nowe nazwisko")
        self.mainLayout.addLayout(self.formLayout)
        self.checkActive = QCheckBox("Pracujący?")

        self.mainLayout.addWidget(self.checkActive)
        self.mainLayout.addWidget(self.button)
        self.mainLayout.addWidget(self.buttonDelete)
        self.setLayout(self.mainLayout)

        self.button.setText("Edytuj pracownika")

        self.buttonDelete.clicked.connect(self.deleteEmp)
        self.lineEmpNumber.currentIndexChanged.connect(self.setEmp)

        for i in employees:
            self.lineEmpNumber.addItem(i["Imie"] + " " + i["Nazwisko"])


class FillForm(QWidget):
    def add(self):
        return

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
        types = [self.detailLayoutInk, self.detailLayoutLaser, self.detailLayoutPoint, self.detailLayoutLaptop,
                 self.detailLayoutTelephone]
        for i in range(0, len(types)):
            types[i].hide()

        print(self.typeList.currentIndex())
        types[self.typeList.currentIndex()].show()
        return

    def __init__(self, parent=None):
        super(FillForm, self).__init__(parent)

        self.mainLayout = QVBoxLayout()
        # self.setFixedSize(600, 1000)
        self.formLayoutBox = QGroupBox()

        self.formLayout2 = QFormLayout()
        self.formLayoutBox2 = QGroupBox()
        self.description = QPlainTextEdit()
        self.labelDesc = QLabel("Opis uszkodzenia")
        self.formLayout2.addWidget(self.labelDesc)
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
        self.labelRepair = QLabel("Opis naprawy")
        self.repairSome = QPlainTextEdit()

        self.formLayout3.addWidget(self.labelUwag, 1, 1)
        self.formLayout3.addWidget(self.labelAcc, 1, 2)
        self.formLayout3.addWidget(self.empList, 2, 2)
        self.formLayout3.addWidget(self.addSome, 2, 1)

        self.formLayout2.addWidget(self.labelRepair)
        self.formLayout2.addWidget(self.repairSome)

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
        self.typeList.currentIndexChanged.connect(self.set_checkboxes)

        self.typeList.addItem("Drukarka atramentowa")
        self.typeList.addItem("Drukarka laserowa")
        self.typeList.addItem("Drukarka igłowa")
        self.typeList.addItem("Laptop")
        self.typeList.addItem("Telefon")


class Login(QDialog):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        self.textLabel = QLabel("Wpisz hasło dostępu")
        self.textPass = QLineEdit(self)

        self.textPass.setEchoMode(QLineEdit.Password)
        self.buttonLogin = QPushButton('Login', self)
        self.buttonLogin.clicked.connect(self.handleLogin)
        layout = QVBoxLayout(self)
        layout.addWidget(self.textLabel)
        layout.addWidget(self.textPass)
        layout.addWidget(self.buttonLogin)

    def handleLogin(self):
        if self.textPass.text() == des.decrypt():
            self.accept()
        else:
            QMessageBox.warning(
                self, 'Error', 'Niepoprawne hasło')


class ChangePass(QDialog):
    def __init__(self, parent=None):
        super(ChangePass, self).__init__(parent)
        self.passLabel = QLabel("Stare hasło")
        self.textPass = QLineEdit(self)
        self.passLabelNew = QLabel("Nowe hasło")
        self.textPassNew = QLineEdit(self)

        self.textPass.setEchoMode(QLineEdit.Password)
        self.textPassNew.setEchoMode(QLineEdit.Password)
        self.buttonLogin = QPushButton('Zmień hasło', self)
        self.buttonLogin.clicked.connect(self.handlePassChange)
        layout = QVBoxLayout(self)
        layout.addWidget(self.passLabel)
        layout.addWidget(self.textPass)
        layout.addWidget(self.passLabelNew)
        layout.addWidget(self.textPassNew)
        layout.addWidget(self.buttonLogin)

    def handlePassChange(self):
        if self.textPassNew.text() == "":
            QMessageBox.warning(
                self, 'Error', 'Nowe hasło nie może być puste')
        elif self.textPass.text() == des.decrypt() and self.textPassNew.text() != "":
            des.encrypt(self.textPassNew.text())
            self.accept()
        else:
            QMessageBox.warning(
                self, 'Error', 'Niepoprawne hasło')


class Form(QDialog):
    def change_pass(self):
        self.changer = ChangePass()
        self.changer.setWindowTitle("Zmiana hasła")
        self.changer.show()

    def search_window(self):
        self.searcher = Searcher()
        self.searcher.show()

    def add_window(self):
        self.adder = Adder()
        self.adder.show()

    def emp_add_window(self):
        self.empAdder = EmpAdder()
        self.empAdder.show()

    def emp_edit_window(self):
        self.empEditor = EmpEditor()
        self.empEditor.show()

    def login(self):
        self.login = Login()
        self.login.setWindowTitle("Logowanie")
        if self.login.exec() == QDialog.Accepted:
            self.button4.show()
            self.button5.show()
            self.button3.hide()
            self.button6.show()

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.setWindowTitle("Menu")
        self.setMinimumWidth(200)
        self.button = QPushButton("Dodaj potwierdzenie")
        self.button2 = QPushButton("Szukaj potwierdzeń")
        self.button3 = QPushButton("Specjalne przywileje")
        self.button4 = QPushButton("Dodaj pracownika")
        self.button5 = QPushButton("Edytuj/usuń pracownika")
        self.button6 = QPushButton("Zmień hasło dostępu")
        # Create layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(self.button)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)
        layout.addWidget(self.button4)
        layout.addWidget(self.button5)
        layout.addWidget(self.button6)
        # Set dialog layout
        self.setLayout(layout)
        # Add button signal to greetings slot
        self.button4.hide()
        self.button5.hide()
        self.button6.hide()

        self.button.clicked.connect(self.add_window)
        self.button2.clicked.connect(self.search_window)
        self.button3.clicked.connect(self.login)
        self.button4.clicked.connect(self.emp_add_window)
        self.button5.clicked.connect(self.emp_edit_window)
        self.button6.clicked.connect(self.change_pass)


class Editor(FillForm):
    def add(self):
        types = ["drukarka_atramentowa", "drukarka_laserowa", "drukarka_iglowa", "laptop", "telefon"]

        database.update_potwierdzenie(
            nr_potw=self.confirmNumber,
            nazwa_urzadzenia=self.lineModel.text(),
            sn=self.lineNumber.text(),
            nazwa_klienta=self.lineClient.text(),
            nr_tel=self.lineClientNumber.text(),
            opis_uszk=self.description.toPlainText(),
            informacje_dodatkowe=self.addSome.toPlainText(),
            opis_naprawy=self.repairSome.toPlainText(),
            imie=self.empName,
            nazwisko=self.empSurname)

        check_list = {}
        # drukarka atramentowa
        if self.typeList.currentIndex() == 0:
            for key in self.inkButtons:
                if self.inkButtons[key].isChecked():
                    check_list[key] = "T"
                else:
                    check_list[key] = "N"
            print(check_list)
            database.update_drukarka_atramentowa(
                nr_potw=self.confirmNumber,
                kabel_sygn=check_list["signal"],
                kabel_zas=check_list["power"],
                zasilacz=check_list["power_box"],
                opakowanie=check_list["packing"],
                tusz_bk=check_list["black_ink"],
                tusz_col=check_list["color_ink"]
            )
        # drukarka laserowa
        if self.typeList.currentIndex() == 1:
            for key in self.laserButtons:
                if self.laserButtons[key].isChecked():
                    check_list[key] = "T"
                else:
                    check_list[key] = "N"
            print(check_list)
            database.update_drukarka_laserowa(nr_potw=self.confirmNumber,
                                              kabel_sygn=check_list["signal"],
                                              kabel_zas=check_list["power"],
                                              toner_bk=check_list["black_toner"],
                                              toner_col=check_list["color_toner"],
                                              opakowanie=check_list["packing"])
        # drukarka igłowa
        if self.typeList.currentIndex() == 2:
            for key in self.pointButtons:
                if self.pointButtons[key].isChecked():
                    check_list[key] = "T"
                else:
                    check_list[key] = "N"
            print(check_list)
            database.update_drukarka_iglowa(nr_potw=self.confirmNumber,
                                            kabel_sygn=check_list["signal"],
                                            kabel_zas=check_list["power"],
                                            tasma=check_list["tape"],
                                            zasilacz=check_list["power_box"],
                                            opakowanie=check_list["packing"])
        # laptop
        if self.typeList.currentIndex() == 3:
            for key in self.laptopButtons:
                if self.laptopButtons[key].isChecked():
                    check_list[key] = "T"
                else:
                    check_list[key] = "N"
            print(check_list)
            database.update_laptop(nr_potw=self.confirmNumber,
                                   kabel_zas=check_list["power"],
                                   mysz=check_list["mouse"],
                                   zasilacz=check_list["power_box"],
                                   opakowanie=check_list["packing"])
        # telefon
        if self.typeList.currentIndex() == 4:
            for key in self.phoneButtons:
                if self.phoneButtons[key].isChecked():
                    check_list[key] = "T"
                else:
                    check_list[key] = "N"
            print(check_list)
            database.update_telefon(nr_potw=self.confirmNumber,
                                    kabel_zas=check_list["power"],
                                    karta_pamieci=check_list["mem_card"],
                                    karta_sim=check_list["sim_card"],
                                    opakowanie=check_list["packing"],
                                    case_ob=check_list["case"],
                                    ladowarka=check_list["charger"])
        latex_converter.to_pdf(
            empname=employees[self.empList.currentIndex()]["Imie"] + " " + employees[self.empList.currentIndex()][
                "Nazwisko"],
            devicename=self.lineModel.text(),
            serialnumber=self.lineNumber.text(),
            clientname=self.lineClient.text(),
            number=self.lineClientNumber.text(),
            shwang=self.description.toPlainText(),
            confirm=self.confirmNumber,
            data=self.date,
            dicts=check_list
        )
        self.destroy()

    def __init__(self, confirm_edit_number, parent=None):
        super(Editor, self).__init__(parent)

        self.setWindowTitle("Edycja potwierdzeń")

        y = database.get_potwierdzenia_by_id(confirm_edit_number)[0]
        self.confirmNumber = y['Nr_potwierdzenia']
        self.date = y["Data"]
        self.empName = y["Imie"]
        self.empSurname = y["Nazwisko"]

        self.typeLabel.hide()
        self.typeList.hide()
        self.empList.hide()
        self.labelAcc.hide()

        # filling out the gaps
        self.addSome.setPlainText(y["Informacje_dodatkowe"])
        self.description.setPlainText(y["Opis_uszkodzenia"])

        self.lineClient.setText(y["Nazwa_klienta"])
        self.lineClientNumber.setText(str(y["Nr_tel"]))
        self.lineNumber.setText(y["Numer_seryjny"])
        self.lineModel.setText(y["Nazwa_urzadzenia"])
        self.repairSome.setPlainText(y["Opis_naprawy"])

        if y['Typ_urzadzenia'] == 'drukarka_atramentowa':
            self.typeList.setCurrentIndex(0)
            if y["Dodatkowe"]['Kabel_zasilajacy'] == 'T':
                self.inkButtons['power'].setChecked(True)
            else:
                self.inkButtons['power'].setChecked(False)
            if y["Dodatkowe"]['Kabel_sygnalowy'] == 'T':
                self.inkButtons['signal'].setChecked(True)
            else:
                self.inkButtons['signal'].setChecked(False)
            if y["Dodatkowe"]['Zasilacz'] == 'T':
                self.inkButtons['power_box'].setChecked(True)
            else:
                self.inkButtons['power_box'].setChecked(False)
            if y["Dodatkowe"]['Tusz_czarny'] == 'T':
                self.inkButtons['black_ink'].setChecked(True)
            else:
                self.inkButtons['black_ink'].setChecked(False)
            if y["Dodatkowe"]['Tusz_kolorowy'] == 'T':
                self.inkButtons['color_ink'].setChecked(True)
            else:
                self.inkButtons['color_ink'].setChecked(False)
            if y["Dodatkowe"]['Opakowanie'] == 'T':
                self.inkButtons['packing'].setChecked(True)
            else:
                self.inkButtons['packing'].setChecked(False)

        if y['Typ_urzadzenia'] == 'drukarka_laserowa':
            self.typeList.setCurrentIndex(1)
            if y["Dodatkowe"]['Kabel_zasilajacy'] == 'T':
                self.laserButtons['power'].setChecked(True)
            else:
                self.laserButtons['power'].setChecked(False)
            if y["Dodatkowe"]['Kabel_sygnalowy'] == 'T':
                self.laserButtons['signal'].setChecked(True)
            else:
                self.laserButtons['signal'].setChecked(False)
            if y["Dodatkowe"]['Toner_czarny'] == 'T':
                self.laserButtons['black_toner'].setChecked(True)
            else:
                self.laserButtons['black_toner'].setChecked(False)
            if y["Dodatkowe"]['Toner_kolorowy'] == 'T':
                self.laserButtons['color_toner'].setChecked(True)
            else:
                self.laserButtons['color_toner'].setChecked(False)
            if y["Dodatkowe"]['Opakowanie'] == 'T':
                self.laserButtons['packing'].setChecked(True)
            else:
                self.laserButtons['packing'].setChecked(False)

        if y['Typ_urzadzenia'] == 'drukarka_iglowa':
            self.typeList.setCurrentIndex(2)
            if y["Dodatkowe"]['Kabel_zasilajacy'] == 'T':
                self.pointButtons['power'].setChecked(True)
            else:
                self.pointButtons['power'].setChecked(False)
            if y["Dodatkowe"]['Kabel_sygnalowy'] == 'T':
                self.pointButtons['signal'].setChecked(True)
            else:
                self.pointButtons['signal'].setChecked(False)
            if y["Dodatkowe"]['Zasilacz'] == 'T':
                self.pointButtons['power_box'].setChecked(True)
            else:
                self.pointButtons['power_box'].setChecked(False)
            if y["Dodatkowe"]['Tasma_barwiaca'] == 'T':
                self.pointButtons['tape'].setChecked(True)
            else:
                self.pointButtons['tape'].setChecked(False)
            if y["Dodatkowe"]['Opakowanie'] == 'T':
                self.pointButtons['packing'].setChecked(True)
            else:
                self.pointButtons['packing'].setChecked(False)

        if y['Typ_urzadzenia'] == 'laptop':
            self.typeList.setCurrentIndex(3)
            if y["Dodatkowe"]['Kabel_zasilajacy'] == 'T':
                self.laptopButtons['power'].setChecked(True)
            else:
                self.laptopButtons['power'].setChecked(False)
            if y["Dodatkowe"]['Zasilacz'] == 'T':
                self.laptopButtons['power_box'].setChecked(True)
            else:
                self.laptopButtons['power_box'].setChecked(False)
            if y["Dodatkowe"]['Mysz_usb'] == 'T':
                self.laptopButtons['mouse'].setChecked(True)
            else:
                self.laptopButtons['mouse'].setChecked(False)
            if y["Dodatkowe"]['Opakowanie'] == 'T':
                self.laptopButtons['packing'].setChecked(True)
            else:
                self.laptopButtons['packing'].setChecked(False)

        if y['Typ_urzadzenia'] == 'telefon':
            self.typeList.setCurrentIndex(4)
            if y["Dodatkowe"]['Kabel_zasilajacy'] == 'T':
                self.phoneButtons['power'].setChecked(True)
            else:
                self.phoneButtons['power'].setChecked(False)
            if y["Dodatkowe"]['Ladowarka'] == 'T':
                self.phoneButtons['charger'].setChecked(True)
            else:
                self.phoneButtons['charger'].setChecked(False)
            if y["Dodatkowe"]['Karta_sim'] == 'T':
                self.phoneButtons['sim_card'].setChecked(True)
            else:
                self.phoneButtons['sim_card'].setChecked(False)
            if y["Dodatkowe"]['Karta_pamieci'] == 'T':
                self.phoneButtons['mem_card'].setChecked(True)
            else:
                self.phoneButtons['mem_card'].setChecked(False)
            if y["Dodatkowe"]['Opakowanie'] == 'T':
                self.phoneButtons['packing'].setChecked(True)
            else:
                self.phoneButtons['packing'].setChecked(False)
            if y["Dodatkowe"]['Case_obudowa'] == 'T':
                self.phoneButtons['case'].setChecked(True)
            else:
                self.phoneButtons['case'].setChecked(False)


class Searcher(QWidget):
    def edit(self):
        self.editor = Editor(self.table.item(self.table.currentRow(), 0).text())
        self.editor.show()
        self.table.clear()
        self.table.setColumnCount(0)
        self.table.setRowCount(0)
        self.destroy()

    def search_all(self):
        self.display(database.get_potwierdzenia_all())

    def search_by_confirm(self):
        x = self.inputConfirm.text()
        if x:
            y = database.get_potwierdzenia_by_id(x)
            self.display(y)

    def search_by_device_name(self):
        x = self.inputDeviceName.text()
        y = database.get_potwierdzenia_by_nazwa_urzadzenia(x)
        self.display(y)

    def search_by_serial_number(self):
        x = self.inputSerial.text()
        y = database.get_potwierdzenia_by_sn(x)
        print(y)
        self.display(y)

    def search_by_client_name(self):
        x = self.inputClientName.text()
        y = database.get_potwierdzenia_by_nazwa_klienta(x)
        self.display(y)

    def display(self, y):
        self.table.clear()
        prettyNames = {
            "drukarka_laserowa": "Drukarka laserowa",
            "drukarka_iglowa": "Drukarka igłowa",
            "drukarka_atramentowa": "Drukarka atramentowa",
            "laptop": "Laptop",
            "telefon": "Telefon",
            "Kabel_zasilajacy": "Kabel zasilający",
            "Kabel_sygnalowy": "Kabel sygnałowy",
            "Toner_czarny": "Toner czarny",
            "Toner_kolorowy": "Toner kolorowy",
            "Opakowanie": "Opakowanie",
            "Zasilacz": "Zasilacz",
            "Tusz_czarny": "Tusz czarny",
            "Tusz_kolorowy": "Tusz kolorowy",
            "Tasma_barwiaca": "Taśma barwiąca",
            "Mysz_usb": "Mysz USB",
            "Case_obudowa": "Obudowa",
            "Karta_pamieci": "Karta pamięci",
            "Karta_sim": "Karta SIM",
            "Ladowarka": "Ładowarka"
        }
        print(y)
        self.table.setRowCount(len(y))
        self.table.setColumnCount(11)
        self.table.setHorizontalHeaderItem(0, QTableWidgetItem("Nr potwierdzenia"))
        self.table.setHorizontalHeaderItem(1, QTableWidgetItem("Data"))
        self.table.setHorizontalHeaderItem(2, QTableWidgetItem("Typ"))
        self.table.setHorizontalHeaderItem(3, QTableWidgetItem("Nazwa"))
        self.table.setHorizontalHeaderItem(4, QTableWidgetItem("Numer seryjny"))
        self.table.setHorizontalHeaderItem(5, QTableWidgetItem("Nazwa klienta"))
        self.table.setHorizontalHeaderItem(6, QTableWidgetItem("Nr telefonu"))
        self.table.setHorizontalHeaderItem(7, QTableWidgetItem("Przyjął"))
        self.table.setHorizontalHeaderItem(8, QTableWidgetItem("Dodatkowe"))
        self.table.setHorizontalHeaderItem(9, QTableWidgetItem("Opis uszkodzenia"))
        self.table.setHorizontalHeaderItem(10, QTableWidgetItem("Opis naprawy"))
        for i in range(0, len(y)):
            self.table.setItem(i, 0, QTableWidgetItem(str(y[i]["Nr_potwierdzenia"])))
            self.table.setItem(i, 1, QTableWidgetItem(y[i]["Data"]))
            self.table.setItem(i, 2, QTableWidgetItem(prettyNames[y[i]["Typ_urzadzenia"]]))
            self.table.setItem(i, 3, QTableWidgetItem(y[i]["Nazwa_urzadzenia"]))
            self.table.setItem(i, 4, QTableWidgetItem(y[i]["Numer_seryjny"]))
            self.table.setItem(i, 5, QTableWidgetItem(y[i]["Nazwa_klienta"]))
            self.table.setItem(i, 6, QTableWidgetItem(str(y[i]["Nr_tel"])))
            self.table.setItem(i, 7, QTableWidgetItem(y[i]["Imie"] + " " + y[i]["Nazwisko"]))
            text = ""
            count = 0
            for key in y[i]["Dodatkowe"]:
                if y[i]["Dodatkowe"][key] == "T":
                    if count:
                        text = text + ", " + prettyNames[key]
                    else:
                        text = prettyNames[key]
                    count = count + 1
            self.table.setItem(i, 8, QTableWidgetItem(text))
            self.table.setItem(i, 9, QTableWidgetItem(y[i]["Opis_uszkodzenia"]))
            self.table.setItem(i, 10, QTableWidgetItem(y[i]["Opis_naprawy"]))
        self.table.resizeColumnsToContents()

    def __init__(self, parent=None):
        super(Searcher, self).__init__(parent)

        self.setWindowTitle("Wyszukiwanie potwierdzeń")
        self.setMinimumSize(1500, 900)

        self.mainLayout = QVBoxLayout()
        self.menuLayout = QHBoxLayout()

        # szukanie po potwierdzeniu
        self.confirmLayout = QVBoxLayout()
        self.labelConfirm = QLabel("Numer potwierdzenia:")
        self.inputConfirm = QLineEdit()
        self.buttonConfirm = QPushButton("Szukaj")
        self.confirmLayout.addWidget(self.labelConfirm)
        self.confirmLayout.addWidget(self.inputConfirm)
        self.confirmLayout.addWidget(self.buttonConfirm)

        self.menuLayout.addLayout(self.confirmLayout)
        # szukanie po nr seryjnym
        self.serialLayout = QVBoxLayout()
        self.labelSerial = QLabel("Numer seryjny:")
        self.inputSerial = QLineEdit()
        self.buttonSerial = QPushButton("Szukaj")
        self.serialLayout.addWidget(self.labelSerial)
        self.serialLayout.addWidget(self.inputSerial)
        self.serialLayout.addWidget(self.buttonSerial)

        self.menuLayout.addLayout(self.serialLayout)
        # szukanie po nazwie
        self.deviceNameLayout = QVBoxLayout()
        self.labelDeviceName = QLabel("Nazwa urzadzenia:")
        self.inputDeviceName = QLineEdit()
        self.buttonDeviceName = QPushButton("Szukaj")
        self.deviceNameLayout.addWidget(self.labelDeviceName)
        self.deviceNameLayout.addWidget(self.inputDeviceName)
        self.deviceNameLayout.addWidget(self.buttonDeviceName)

        self.menuLayout.addLayout(self.deviceNameLayout)

        # nazwa klienta
        self.clientNameLayout = QVBoxLayout()
        self.labelClientName = QLabel("Nazwa klienta:")
        self.inputClientName = QLineEdit()
        self.buttonClientName = QPushButton("Szukaj")
        self.clientNameLayout.addWidget(self.labelClientName)
        self.clientNameLayout.addWidget(self.inputClientName)
        self.clientNameLayout.addWidget(self.buttonClientName)

        self.menuLayout.addLayout(self.clientNameLayout)

        self.mainLayout.addLayout(self.menuLayout)

        self.table = QTableWidget()
        self.mainLayout.addWidget(self.table)

        self.buttonShowAll = QPushButton("Pokaż wszystkie wpisy")
        self.mainLayout.addWidget(self.buttonShowAll)

        self.setLayout(self.mainLayout)
        self.buttonConfirm.clicked.connect(self.search_by_confirm)
        self.buttonDeviceName.clicked.connect(self.search_by_device_name)
        self.buttonSerial.clicked.connect(self.search_by_serial_number)
        self.buttonShowAll.clicked.connect(self.search_all)
        self.buttonClientName.clicked.connect(self.search_by_client_name)

        self.table.itemDoubleClicked.connect(self.edit)


class Adder(FillForm):
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
        print("poszlo")

        print(database.get_all_pracownicy())
        check_list = {}
        # drukarka atramentowa
        if self.typeList.currentIndex() == 0:
            for key in self.inkButtons:
                if self.inkButtons[key].isChecked():
                    check_list[key] = "T"
                else:
                    check_list[key] = "N"
            print(check_list)
            database.insert_drukarka_atramentowa(typ=types[self.typeList.currentIndex()],
                                                 kabel_sygn=check_list["signal"],
                                                 kabel_zas=check_list["power"],
                                                 zasilacz=check_list["power_box"],
                                                 opakowanie=check_list["packing"],
                                                 tusz_bk=check_list["black_ink"],
                                                 tusz_col=check_list["color_ink"]
                                                 )
        # drukarka laserowa
        if self.typeList.currentIndex() == 1:
            for key in self.laserButtons:
                if self.laserButtons[key].isChecked():
                    check_list[key] = "T"
                else:
                    check_list[key] = "N"
            print(check_list)
            database.insert_drukarka_laserowa(typ=types[self.typeList.currentIndex()],
                                              kabel_sygn=check_list["signal"],
                                              kabel_zas=check_list["power"],
                                              toner_bk=check_list["black_toner"],
                                              toner_col=check_list["color_toner"],
                                              opakowanie=check_list["packing"])
        # drukarka igłowa
        if self.typeList.currentIndex() == 2:
            for key in self.pointButtons:
                if self.pointButtons[key].isChecked():
                    check_list[key] = "T"
                else:
                    check_list[key] = "N"
            print(check_list)
            database.insert_drukarka_iglowa(typ=types[self.typeList.currentIndex()],
                                            kabel_sygn=check_list["signal"],
                                            kabel_zas=check_list["power"],
                                            tasma=check_list["tape"],
                                            zasilacz=check_list["power_box"],
                                            opakowanie=check_list["packing"])
        # laptop
        if self.typeList.currentIndex() == 3:
            for key in self.laptopButtons:
                if self.laptopButtons[key].isChecked():
                    check_list[key] = "T"
                else:
                    check_list[key] = "N"
            print(check_list)
            database.insert_laptop(typ=types[self.typeList.currentIndex()],
                                   kabel_zas=check_list["power"],
                                   mysz=check_list["mouse"],
                                   zasilacz=check_list["power_box"],
                                   opakowanie=check_list["packing"])
        # telefon
        if self.typeList.currentIndex() == 4:
            for key in self.phoneButtons:
                if self.phoneButtons[key].isChecked():
                    check_list[key] = "T"
                else:
                    check_list[key] = "N"
            print(check_list)
            database.insert_telefon(typ=types[self.typeList.currentIndex()],
                                    kabel_zas=check_list["power"],
                                    karta_pamieci=check_list["mem_card"],
                                    karta_sim=check_list["sim_card"],
                                    opakowanie=check_list["packing"],
                                    case_ob=check_list["case"],
                                    ladowarka=check_list["charger"])
            print(check_list)

        latex_converter.to_pdf(
            empname=employees[self.empList.currentIndex()]["Imie"] + " " + employees[self.empList.currentIndex()][
                "Nazwisko"],
            devicename=self.lineModel.text(),
            serialnumber=self.lineNumber.text(),
            clientname=self.lineClient.text(),
            number=self.lineClientNumber.text(),
            shwang=self.description.toPlainText(),
            confirm=database.get_last_nr_potwierdzenia(),
            data=datetime.now().strftime("%d/%m/%y %H:%M:%S"),
            dicts=check_list
        )
        self.destroy()

    def __init__(self, parent=None):
        super(Adder, self).__init__(parent)
        self.setWindowTitle("Dodawanie potwierdzeń")
        print(employees)
        for i in employees:
            if i["Aktywny"] == 'T':
                self.empList.addItem(i["Imie"] + " " + i["Nazwisko"])
        self.labelRepair.hide()
        self.repairSome.hide()


if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    form = Form()
    qtmodern.styles.light(app)
    form.show()
    # Run the main Qt loop
    sys.exit(app.exec_())
