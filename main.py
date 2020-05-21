import sys
from PyQt5.QtWidgets import (QLineEdit, QPushButton, QApplication,
                             QVBoxLayout, QDialog, QLabel, QFormLayout, QGroupBox, QMainWindow, QPlainTextEdit,
                             QHBoxLayout, QGridLayout, QComboBox, QErrorMessage, QMessageBox, QCheckBox, QTableWidget,
                             QTableWidgetItem)
import qtmodern.styles
import qtmodern.windows
import valid
import db
from datetime import date

database = db.DataBase()
employees = database.get_all_pracownicy()


class Form(QDialog):
    def search_window(self):
        self.searcher.show()

    def add_window(self):
        self.adder.show()

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.adder = Adder()
        self.searcher = Searcher()
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
        self.button3.clicked.connect(self.search_window)


class Searcher(QDialog):
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
        # todo dodać wszystkie prettyNames
        self.table.clear()
        prettyNames = {
            "drukarka_laserowa":"Drukarka laserowa",
            "drukarka_iglowa":"Drukarka igłowa",
            "drukarka_atramentowa":"Drukarka atramentowa",
            "laptop":"Laptop",
            "telefon":"Telefon",
            "Kabel_zasilajacy":"Kabel zasilający",
            "Kabel_sygnalowy":"Kabel sygnałowy",
            "Toner_czarny":"Toner czarny",
            "Toner_kolorowy":"Toner kolorowy",
            "Opakowanie": "Opakowanie",
            "Zasilacz": "Zasilacz",
            "Tusz_czarny":"Tusz czarny",
            "Tusz_kolorowy":"Tusz kolorowy",
            "Tasma_barwiaca":"Taśma barwiąca",
            "Mysz_usb":"Mysz USB",
            "Case_obudowa":"Obudowa",
            "Karta_pamieci":"Karta pamięci",
            "Karta_sim":"Karta SIM"
        }
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
        self.setMinimumSize(1500,900)

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

        # drukarka atramentowa
        if self.typeList.currentIndex() == 0:
            check_list = {}
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
            check_list = {}
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
            check_list = {}
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
            check_list = {}
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
            check_list = {}
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
        types = [self.detailLayoutInk, self.detailLayoutLaser, self.detailLayoutPoint, self.detailLayoutLaptop,
                 self.detailLayoutTelephone]
        for i in range(0, len(types)):
            types[i].hide()

        print(self.typeList.currentIndex())
        types[self.typeList.currentIndex()].show()
        return

    def __init__(self, parent=None):
        super(Adder, self).__init__(parent)

        self.mainLayout = QVBoxLayout()
        self.setFixedSize(600, 1000)
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
