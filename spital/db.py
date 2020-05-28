import sqlite3


class DataBase:
    def __init__(self):
        self.conn = sqlite3.connect('potwierdzenia.db')
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.cursor.close()
        self.conn.close()

    def sql_create_tables(self):
        sql_create_table_pracownicy = "CREATE TABLE Pracownicy (" \
                                      "Id_pracownika INTEGER PRIMARY KEY AUTOINCREMENT," \
                                      "Imie VARCHAR(20) NOT NULL," \
                                      "Nazwisko VARCHAR(20) NOT NULL);"
        self.cursor.execute(sql_create_table_pracownicy)

        sql_create_table_potwierdzenia = "CREATE TABLE Potwierdzenia (" \
                                         "Nr_potwierdzenia INTEGER PRIMARY KEY AUTOINCREMENT," \
                                         "Data DATE NOT NULL," \
                                         "Typ_urzadzenia VARCHAR(25) NOT NULL," \
                                         "Nazwa_urzadzenia VARCHAR(30) NOT NULL," \
                                         "Nr_seryjny VARCHAR(20) NOT NULL," \
                                         "Nazwa_klienta VARCHAR(25) NOT NULL," \
                                         "Nr_telefonu_klienta INTEGER(9) NOT NULL," \
                                         "Opis_uszkodzenia VARCHAR(255) NOT NULL," \
                                         "Informacje_dodatkowe VARCHAR(255) NULL," \
                                         "Opis_naprawy VARCHAR(255) NULL," \
                                         "Id_pracownika INTEGER NOT NULL," \
                                         "FOREIGN KEY(Id_pracownika) REFERENCES Pracownicy(Id_pracownika));"
        self.cursor.execute(sql_create_table_potwierdzenia)

        sql_create_table_drukarka_laserowa = "CREATE TABLE Drukarka_laserowa (" \
                                                  "Id_urzadzenia INTEGER PRIMARY KEY AUTOINCREMENT," \
                                                  "Typ_urzadzenia VARCHAR(25) NOT NULL," \
                                                  "Id_potwierdzenia INTEGER NOT NULL," \
                                                  "Kabel_zasilajacy VARCHAR(1) NULL," \
                                                  "Kabel_sygnalowy VARCHAR(1) NULL," \
                                                  "Toner_czarny VARCHAR(1) NULL," \
                                                  "Toner_kolorowy VARCHAR(1) NULL," \
                                                  "Opakowanie VARCHAR(1) NULL," \
                                                  "FOREIGN KEY(Id_potwierdzenia) REFERENCES Potwierdzenia(Id_potwierdzenia));"
        self.cursor.execute(sql_create_table_drukarka_laserowa)

        sql_create_table_drukarka_iglowa = "CREATE TABLE Drukarka_iglowa(" \
                                                "Id_urzadzenia INTEGER PRIMARY KEY AUTOINCREMENT," \
                                                "Typ_urzadzenia VARCHAR(25) NOT NULL," \
                                                "Id_potwierdzenia INTEGER NOT NULL," \
                                                "Kabel_zasilajacy VARCHAR(1) NULL," \
                                                "Kabel_sygnalowy VARCHAR(1) NULL," \
                                                "Zasilacz VARCHAR(1) NULL," \
                                                "Tasma_barwiaca VARCHAR(1) NULL," \
                                                "Opakowanie VARCHAR(1) NULL," \
                                                "FOREIGN KEY(Id_potwierdzenia) REFERENCES Potwierdzenia(Id_potwierdzenia));"
        self.cursor.execute(sql_create_table_drukarka_iglowa)

        sql_create_table_drukarka_atramentowa = "CREATE TABLE Drukarka_atramentowa (" \
                                                     "Id_urzadzenia INTEGER PRIMARY KEY AUTOINCREMENT," \
                                                     "Typ_urzadzenia VARCHAR(25) NOT NULL," \
                                                     "Id_potwierdzenia INTEGER NOT NULL," \
                                                     "Kabel_zasilajacy VARCHAR(1) NULL," \
                                                     "Kabel_sygnalowy VARCHAR(1) NULL," \
                                                     "Zasilacz VARCHAR(1) NULL," \
                                                     "Tusz_czarny VARCHAR(1) NULL," \
                                                     "Tusz_kolorowy VARCHAR(1) NULL," \
                                                     "Opakowanie VARCHAR(1) NULL," \
                                                     "FOREIGN KEY(Id_potwierdzenia) REFERENCES Potwierdzenia(Id_potwierdzenia));"
        self.cursor.execute(sql_create_table_drukarka_atramentowa)

        sql_create_table_laptop = "CREATE TABLE Laptop (" \
                                       "Id_urzadzenia INTEGER PRIMARY KEY AUTOINCREMENT," \
                                       "Typ_urzadzenia VARCHAR(25) NOT NULL," \
                                       "Id_potwierdzenia INTEGER NOT NULL," \
                                       "Zasilacz VARCHAR(1) NULL," \
                                       "Kabel_zasilajacy VARCHAR(1) NULL," \
                                       "Mysz_usb VARCHAR(1) NULL," \
                                       "Opakowanie VARCHAR(1) NULL," \
                                       "FOREIGN KEY(Id_potwierdzenia) REFERENCES Potwierdzenia(Id_potwierdzenia));"
        self.cursor.execute(sql_create_table_laptop)

        sql_create_table_telefon = "CREATE TABLE Telefon (" \
                                        "Id_urzadzenia INTEGER PRIMARY KEY AUTOINCREMENT," \
                                        "Typ_urzadzenia VARCHAR(25) NOT NULL," \
                                        "Id_potwierdzenia INTEGER NOT NULL," \
                                        "Ladowarka VARCHAR(1) NULL," \
                                        "Kabel_zasilajacy VARCHAR(1) NULL," \
                                        "Case_obudowa VARCHAR(1) NULL," \
                                        "Karta_sim VARCHAR(1) NULL," \
                                        "Karta_pamieci VARCHAR(1) NULL," \
                                        "Opakowanie VARCHAR(1) NULL," \
                                        "FOREIGN KEY(Id_potwierdzenia) REFERENCES Potwierdzenia(Id_potwierdzenia));"
        self.cursor.execute(sql_create_table_telefon)
        self.conn.commit()

    def insert_pracownik(self, imie, nazwisko):
        sql_insert_pracownik = "INSERT INTO Pracownicy (Imie, Nazwisko) VALUES ('{}', '{}');".format(imie, nazwisko)
        self.cursor.execute(sql_insert_pracownik)
        self.conn.commit()

    def get_last_nr_potwierdzenia(self):
        sql_select_last_nr_potwierdzenia = "SELECT Nr_potwierdzenia FROM Potwierdzenia ORDER BY Nr_potwierdzenia DESC"
        self.cursor.execute(sql_select_last_nr_potwierdzenia)
        x = self.cursor.fetchone()
        return x[0]

    def insert_potwierdzenie(self, data, typ, nazwa_urzadzenia, sn, nazwa_klienta, nr_tel, opis_uszk, informacje_dodatkowe, opis_naprawy, id_prac):
        sql_insert_potwierdzenie = "INSERT INTO Potwierdzenia (Data, Typ_urzadzenia, Nazwa_urzadzenia, Nr_seryjny, Nazwa_klienta, Nr_telefonu_klienta, Opis_uszkodzenia," \
                                   "Informacje_dodatkowe, Opis_naprawy, Id_pracownika) VALUES ('{}','{}','{}','{}','{}', {}, '{}', '{}', '{}', {})" \
                                   "".format(data, typ, nazwa_urzadzenia, sn, nazwa_klienta, nr_tel, opis_uszk, informacje_dodatkowe, opis_naprawy, id_prac)
        self.cursor.execute(sql_insert_potwierdzenie)
        self.conn.commit()

    def insert_drukarka_atramentowa(self, typ, kabel_zas, kabel_sygn, zasilacz, tusz_bk, tusz_col, opakowanie):
        nr_potwierdzenia = self.get_last_nr_potwierdzenia()
        sql_insert_into_drukarka_atramentowa = "INSERT INTO Drukarka_atramentowa (Typ_urzadzenia, Id_potwierdzenia, Kabel_zasilajacy, Kabel_sygnalowy, Zasilacz, Tusz_czarny, Tusz_kolorowy, Opakowanie) " \
                                               "VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}');".format(typ, nr_potwierdzenia, kabel_zas, kabel_sygn, zasilacz, tusz_bk, tusz_col, opakowanie)
        self.cursor.execute(sql_insert_into_drukarka_atramentowa)
        self.conn.commit()

    def insert_drukarka_laserowa(self, typ, kabel_zas, kabel_sygn, toner_bk, toner_col, opakowanie):
        nr_potwierdzenia = self.get_last_nr_potwierdzenia()
        sql_insert_into_drukarka_laserowa = "INSERT INTO Drukarka_laserowa (Typ_urzadzenia, Id_potwierdzenia, Kabel_zasilajacy, Kabel_sygnalowy, Toner_czarny, Toner_kolorowy, Opakowanie) " \
                                            "VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}');".format(typ, nr_potwierdzenia, kabel_zas, kabel_sygn, toner_bk, toner_col, opakowanie)
        self.cursor.execute(sql_insert_into_drukarka_laserowa)
        self.conn.commit()

    def insert_drukarka_iglowa(self, typ, kabel_zas, kabel_sygn, zasilacz, tasma, opakowanie):
        nr_potwierdzenia = self.get_last_nr_potwierdzenia()
        sql_insert_into_drukarka_iglowa = "INSERT INTO Drukarka_iglowa (Typ_urzadzenia, Id_potwierdzenia, Kabel_zasilajacy, Kabel_sygnalowy, Zasilacz, Tasma_barwiaca, Opakowanie)" \
                                          "VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}');".format(typ, nr_potwierdzenia, kabel_zas, kabel_sygn, zasilacz, tasma, opakowanie)
        self.cursor.execute(sql_insert_into_drukarka_iglowa)
        self.conn.commit()

    def insert_laptop(self, typ, zasilacz, kabel_zas, mysz, opakowanie):
        nr_potwierdzenia = self.get_last_nr_potwierdzenia()
        sql_insert_into_laptop = "INSERT INTO Laptop (Typ_urzadzenia, Id_potwierdzenia, Zasilacz, Kabel_zasilajacy, Mysz_usb, Opakowanie) " \
                                 "VALUES ('{}', '{}', '{}', '{}', '{}', '{}');".format(typ, nr_potwierdzenia, zasilacz, kabel_zas, mysz, opakowanie)
        self.cursor.execute(sql_insert_into_laptop)
        self.conn.commit()

    def insert_telefon(self, typ, kabel_zas, ladowarka, case_ob, karta_sim, karta_pamieci, opakowanie):
        nr_potwierdzenia = self.get_last_nr_potwierdzenia()
        sql_insert_into_telefon = "INSERT INTO Telefon (Typ_urzadzenia, Id_potwierdzenia, Kabel_zasilajacy, Ladowarka, Case_obudowa, Karta_sim, Karta_pamieci, Opakowanie)" \
                                  "VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}');".format(typ, nr_potwierdzenia, kabel_zas, ladowarka, case_ob, karta_sim, karta_pamieci, opakowanie)
        self.cursor.execute(sql_insert_into_telefon)
        self.conn.commit()


    def get_all_pracownicy(self):
        sql_select_pracownicy = "SELECT * FROM Pracownicy"
        self.cursor.execute(sql_select_pracownicy)
        pracownik =  self.cursor.fetchall()
        listx = []
        for x in pracownik:
            dict = {
                "Id_pracownika": x[0],
                "Imie": x[1],
                "Nazwisko": x[2]
            }
            listx.append(dict)
        return listx


    def sql_get_potwierdzenia(self, typ):
        listx = []
        for x in typ:
            if(x[0] == "laptop"):
                sql_select_all = "SELECT * FROM Potwierdzenia p JOIN Pracownicy x ON p.Id_pracownika = x.Id_pracownika " \
                                 "JOIN Laptop l ON p.Nr_potwierdzenia = l.Id_potwierdzenia WHERE p.Nr_potwierdzenia = {};".format(x[1])
                self.cursor.execute(sql_select_all)
                potw = self.cursor.fetchall()
                for z in potw:
                    dict = {"Nr_potwierdzenia": z[0],
                            "Data": z[1],
                            "Typ_urzadzenia": z[2],
                            "Nazwa_urzadzenia": z[3],
                            "Numer_seryjny": z[4],
                            "Nazwa_klienta": z[5],
                            "Nr_tel": z[6],
                            "Opis_uszkodzenia": z[7],
                            "Informacje_dodatkowe": z[8],
                            "Opis_naprawy": z[9],
                            "Id_pracownika": z[10],
                            "Imie": z[12],
                            "Nazwisko": z[13],
                            "Dodatkowe":
                                {"Zasilacz": z[17],
                                "Kabel_zasilajacy": z[18],
                                "Mysz_usb": z[19],
                                "Opakowanie": z[20]}
                            }
                listx.append(dict)
            elif(x[0] == "telefon"):
                sql_select_all = "SELECT * FROM Potwierdzenia p JOIN Pracownicy x ON p.Id_pracownika = x.Id_pracownika " \
                                 "JOIN Telefon t ON p.Nr_potwierdzenia = t.Id_potwierdzenia WHERE p.Nr_potwierdzenia = {};".format(x[1])
                self.cursor.execute(sql_select_all)
                potw = self.cursor.fetchall()
                for z in potw:
                    dict = {"Nr_potwierdzenia": z[0],
                            "Data": z[1],
                            "Typ_urzadzenia": z[2],
                            "Nazwa_urzadzenia": z[3],
                            "Numer_seryjny": z[4],
                            "Nazwa_klienta": z[5],
                            "Nr_tel": z[6],
                            "Opis_uszkodzenia": z[7],
                            "Informacje_dodatkowe": z[8],
                            "Opis_naprawy": z[9],
                            "Id_pracownika": z[10],
                            "Imie": z[12],
                            "Nazwisko": z[13],
                            "Dodatkowe":
                                {"Kabel_zasilajacy": z[17],
                                "Ladowarka": z[18],
                                "Case_obudowa": z[19],
                                "Karta_sim": z[20],
                                "Karta_pamieci": z[21],
                                "Opakowanie": z[22]}
                            }
                    listx.append(dict)
            elif(x[0] == "drukarka_atramentowa"):
                sql_select_all = "SELECT * FROM Potwierdzenia p JOIN Pracownicy x ON p.Id_pracownika = x.Id_pracownika " \
                                 "JOIN Drukarka_atramentowa a ON p.Nr_potwierdzenia = a.Id_potwierdzenia WHERE p.Nr_potwierdzenia = {};".format(x[1])
                self.cursor.execute(sql_select_all)
                potw = self.cursor.fetchall()
                for z in potw:
                    dict = {"Nr_potwierdzenia": z[0],
                            "Data": z[1],
                            "Typ_urzadzenia": z[2],
                            "Nazwa_urzadzenia": z[3],
                            "Numer_seryjny": z[4],
                            "Nazwa_klienta": z[5],
                            "Nr_tel": z[6],
                            "Opis_uszkodzenia": z[7],
                            "Informacje_dodatkowe": z[8],
                            "Opis_naprawy": z[9],
                            "Id_pracownika": z[10],
                            "Imie": z[12],
                            "Nazwisko": z[13],
                            "Dodatkowe":
                                {"Kabel_zasilajacy": z[17],
                                "Kabel_sygnalowy": z[18],
                                "Zasilacz": z[19],
                                "Tusz_czarny": z[20],
                                "Tusz_kolorowy": z[21],
                                "Opakowanie": z[22]}
                            }
                    listx.append(dict)
            elif(x[0] == "drukarka_laserowa"):
                sql_select_all = "SELECT * FROM Potwierdzenia p JOIN Pracownicy x ON p.Id_pracownika = x.Id_pracownika " \
                                 "JOIN Drukarka_laserowa d ON p.Nr_potwierdzenia = d.Id_potwierdzenia WHERE p.Nr_potwierdzenia = {};".format(x[1])
                self.cursor.execute(sql_select_all)
                potw = self.cursor.fetchall()
                for z in potw:
                    dict = {"Nr_potwierdzenia": z[0],
                            "Data": z[1],
                            "Typ_urzadzenia": z[2],
                            "Nazwa_urzadzenia": z[3],
                            "Numer_seryjny": z[4],
                            "Nazwa_klienta": z[5],
                            "Nr_tel": z[6],
                            "Opis_uszkodzenia": z[7],
                            "Informacje_dodatkowe": z[8],
                            "Opis_naprawy": z[9],
                            "Id_pracownika": z[10],
                            "Imie": z[12],
                            "Nazwisko": z[13],
                            "Dodatkowe":
                                {"Kabel_zasilajacy": z[17],
                                "Kabel_sygnalowy": z[18],
                                "Toner_czarny": z[19],
                                "Toner_kolorowy": z[20],
                                "Opakowanie": z[21]}
                            }
                    listx.append(dict)
            elif(x[0] == "drukarka_iglowa"):
                sql_select_all = "SELECT * FROM Potwierdzenia p JOIN Pracownicy x ON p.Id_pracownika = x.Id_pracownika " \
                                 "JOIN Drukarka_iglowa i ON p.Nr_potwierdzenia = i.Id_potwierdzenia WHERE p.Nr_potwierdzenia = {};".format(x[1])
                self.cursor.execute(sql_select_all)
                potw = self.cursor.fetchall()
                for z in potw:
                    dict = {"Nr_potwierdzenia": z[0],
                            "Data": z[1],
                            "Typ_urzadzenia": z[2],
                            "Nazwa_urzadzenia": z[3],
                            "Numer_seryjny": z[4],
                            "Nazwa_klienta": z[5],
                            "Nr_tel": z[6],
                            "Opis_uszkodzenia": z[7],
                            "Informacje_dodatkowe": z[8],
                            "Opis_naprawy": z[9],
                            "Id_pracownika": z[10],
                            "Imie": z[12],
                            "Nazwisko": z[13],
                            "Dodatkowe":
                                {"Kabel_zasilajacy": z[17],
                                "Kabel_sygnalowy": z[18],
                                "Zasilacz": z[19],
                                "Tasma_barwiaca": z[20],
                                "Opakowanie": z[21]}
                            }
                    listx.append(dict)
        return listx

    def get_potwierdzenia_all(self):
        sql_select_typ = "SELECT Typ_urzadzenia, Nr_potwierdzenia FROM Potwierdzenia;"
        self.cursor.execute(sql_select_typ)
        typ = self.cursor.fetchall()
        return self.sql_get_potwierdzenia(typ)

    def get_potwierdzenia_by_id(self, id):
        sql_select_typ = "SELECT Typ_urzadzenia, Nr_potwierdzenia FROM Potwierdzenia WHERE Nr_potwierdzenia = {};".format(id)
        self.cursor.execute(sql_select_typ)
        typ = self.cursor.fetchall()
        return self.sql_get_potwierdzenia(typ)

    def get_potwierdzenia_by_sn(self, sn):
        sql_select_typ = "SELECT Typ_urzadzenia, Nr_potwierdzenia FROM Potwierdzenia WHERE Nr_seryjny = '{}';".format(sn)
        self.cursor.execute(sql_select_typ)
        typ = self.cursor.fetchall()
        return self.sql_get_potwierdzenia(typ)

    def get_potwierdzenia_by_nazwa_urzadzenia(self, nazwa_urz):
        sql_select_typ = "SELECT Typ_urzadzenia, Nr_potwierdzenia FROM Potwierdzenia WHERE Nazwa_urzadzenia = '{}';".format(nazwa_urz)
        self.cursor.execute(sql_select_typ)
        typ = self.cursor.fetchall()
        return self.sql_get_potwierdzenia(typ)

    def get_potwierdzenia_by_nazwa_klienta(self, nazwa_klienta):
        sql_select_typ = "SELECT Typ_urzadzenia, Nr_potwierdzenia FROM Potwierdzenia WHERE Nazwa_klienta = '{}';".format(nazwa_klienta)
        self.cursor.execute(sql_select_typ)
        typ = self.cursor.fetchall()
        return self.sql_get_potwierdzenia(typ)

    def update_potwierdzenie(self, nr_potw, nazwa_urzadzenia, sn, nazwa_klienta, nr_tel, opis_uszk, informacje_dodatkowe, opis_naprawy, imie, nazwisko):
        sel_id_prac = "SELECT Id_pracownika FROM Pracownicy WhERE Imie = '{}' AND Nazwisko = '{}'".format(imie, nazwisko)
        self.cursor.execute(sel_id_prac)
        id_prac = self.cursor.fetchone()
        sql_update_potwierdzenie = "UPDATE Potwierdzenia SET " \
                                   "Nazwa_urzadzenia = '{}'," \
                                   "Nr_seryjny = '{}'," \
                                   "Nazwa_klienta = '{}'," \
                                   "Nr_telefonu_klienta = {}," \
                                   "Opis_uszkodzenia = '{}'," \
                                   "Informacje_dodatkowe = '{}'," \
                                   "Opis_naprawy = '{}'," \
                                   "Id_pracownika = {} " \
                                   "WHERE Nr_potwierdzenia = {}".format(nazwa_urzadzenia, sn, nazwa_klienta, nr_tel, opis_uszk, informacje_dodatkowe, opis_naprawy, id_prac[0], nr_potw)
        self.cursor.execute(sql_update_potwierdzenie)
        self.conn.commit()

    def update_drukarka_atramentowa(self, nr_potw, kabel_zas,  kabel_sygn, zasilacz, tusz_bk, tusz_col, opakowanie):
        sql_update_drukarka_atramentowa = "UPDATE Drukarka_atramentowa SET " \
                                       "Kabel_zasilajacy = '{}'," \
                                       "Kabel_sygnalowy = '{}'," \
                                       "Zasilacz = '{}'," \
                                       "Tusz_czarny = '{}'," \
                                       "Tusz_kolorowy = '{}'," \
                                       "Opakowanie = '{}' " \
                                       "WHERE Id_potwierdzenia = {}".format(kabel_zas, kabel_sygn, zasilacz, tusz_bk, tusz_col, opakowanie, nr_potw)
        self.cursor.execute(sql_update_drukarka_atramentowa)
        self.conn.commit()

    def update_drukarka_laserowa(self, nr_potw, kabel_zas,  kabel_sygn, toner_bk, toner_col, opakowanie):
        sql_update_drukarka_laserowa = "UPDATE Drukarka_laserowa SET " \
                                       "Kabel_zasilajacy = '{}'," \
                                       "Kabel_sygnalowy = '{}'," \
                                       "Toner_czarny = '{}'," \
                                       "Toner_kolorowy = '{}'," \
                                       "Opakowanie = '{}' " \
                                       "WHERE Id_potwierdzenia = {}".format(kabel_zas, kabel_sygn, toner_bk, toner_col, opakowanie, nr_potw)
        self.cursor.execute(sql_update_drukarka_laserowa)
        self.conn.commit()

    def update_drukarka_iglowa(self, nr_potw, kabel_zas, kabel_sygn, zasilacz, tasma, opakowanie):
        sql_update_drukarka_iglowa = "UPDATE Drukarka_iglowa SET " \
                                       "Kabel_zasilajacy = '{}'," \
                                       "Kabel_sygnalowy = '{}'," \
                                       "Zasilacz = '{}'," \
                                       "Tasma_barwiaca = '{}'," \
                                       "Opakowanie = '{}' " \
                                       "WHERE Id_potwierdzenia = {}".format(kabel_zas, kabel_sygn, zasilacz, tasma, opakowanie, nr_potw)
        self.cursor.execute(sql_update_drukarka_iglowa)
        self.conn.commit()

    def update_laptop(self, nr_potw, zasilacz, kabel_zas, mysz, opakowanie):
        sql_update_laptop = "UPDATE Laptop SET " \
                            "Zasilacz = '{}'," \
                            "Kabel_zasilajacy = '{}'," \
                            "Mysz_usb = '{}'," \
                            "Opakowanie = '{}' " \
                            "WHERE Id_potwierdzenia = {}".format(zasilacz, kabel_zas, mysz, opakowanie, nr_potw)
        self.cursor.execute(sql_update_laptop)
        self.conn.commit()

    def update_telefon(self, nr_potw, kabel_zas, ladowarka, case_ob, karta_sim, karta_pamieci, opakowanie):
        sql_update_telefon = "UPDATE Telefon SET " \
                             "Kabel_zasilajacy = '{}'," \
                             "Ladowarka = '{}'," \
                             "Case_obudowa = '{}'," \
                             "Karta_sim = '{}'," \
                             "Karta_pamieci = '{}'," \
                             "Opakowanie = '{}' " \
                             "WHERE Id_potwierdzenia = {}".format(kabel_zas, ladowarka, case_ob, karta_sim, karta_pamieci, opakowanie, nr_potw)
        self.cursor.execute(sql_update_telefon)
        self.conn.commit()

    def update_pracownicy(self, id_prac, imie, nazwisko):
        sql_update_pracownik = "UPDATE Pracownicy SET " \
                               "Imie = '{}'," \
                               "Nazwisko = '{}' " \
                               "WHERE Id_pracownika = {};".format(imie, nazwisko, id_prac)
        print(sql_update_pracownik)
        self.cursor.execute(sql_update_pracownik)
        self.conn.commit()


