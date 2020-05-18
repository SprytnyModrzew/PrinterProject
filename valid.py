polish_small_characters = ['ą', 'ć', 'ę', 'ł', 'ń', 'ó', 'ś', 'ź', 'ż']
polish_big_characters = ['Ą', 'Ć', 'Ę', 'Ł', 'Ń', 'Ó', 'Ś', 'Ź', 'Ż']


def name_valid(name):
    if len(name) <= 0:
        #print("Imię nie może być puste!")
        return False
    if name[0] < chr(65) or name[0] > chr(90):
        if name[0] not in polish_big_characters:
            #print("Imię powinno zaczynać się z dużej litery!")
            return False
    for i in range(1, len(name)):
        if name[i] < chr(97) or name[i] > chr(122):
            if name[i] not in polish_small_characters:
                #print("Imię powinno zawierać tylko litery!")
                return False
    return True


def surname_valid(surname):
    if len(surname) <= 0:
        #print("Nazwisko nie może być puste!")
        return False
    if surname[0] < chr(65) or surname[0] > chr(90):
        if surname[0] not in polish_big_characters:
            #print("Nazwisko powinno zaczynać się z dużej litery!")
            return False
    for i in range(1, len(surname)):
        if surname[i] < chr(97) or surname[i] > chr(122):
            if surname[i] not in polish_small_characters:
                #print("Nazwisko powinno zawierać tylko litery!")
                return False
    return True


def device_name_valid(devname):
    if len(devname) <= 0:
        #print("Nazwa urządzenia nie może być pusta!")
        return False
    if devname[0] == chr(32):
        #print("Nazwa urządzenia nie powinna zaczynać się od spacji!")
        return False
    for i in range(0, len(devname)):
        if devname[i] < chr(48) or devname[i] > chr(57):
            if devname[i] < chr(65) or devname[i] > chr(90):
                if devname[i] < chr(97) or devname[i] > chr(122):
                    if devname[i] not in polish_big_characters and devname[i] not in polish_small_characters:
                        if devname[i] != chr(32):
                            #print("Nazwa urządzenia powinna zawierać tylko cyfry, litery, spacje lub polskie znaki!")
                            return False
    return True


def serial_number_valid(sernumber):
    if len(sernumber) <= 0:
        #print("Numer seryjny nie może być pusty!")
        return False
    for i in range(0, len(sernumber)):
        if sernumber[i] < chr(48) or sernumber[i] > chr(57):
            if sernumber[i] < chr(65) or sernumber[i] > chr(90):
                if sernumber[i] < chr(97) or sernumber[i] > chr(122):
                    #print("Numer seryjny powinien zawierać tylko cyfry i litery!")
                    return False
    return True


def client_name_valid(client):
    if len(client) <= 0:
        #print("Nazwa klienta nie może być pusta!")
        return False
    return True


def phone_number_valid(phone):
    if len(phone) != 9:
        #print("Numer telefonu musi się składać z 9 cyfr!")
        return False
    for i in range(0, 9):
        if phone[i] < chr(48) or phone[i] > chr(57):
            #print("Numer telefonu musi się składać wyłącznie z cyfr!")
            return False
    return True


def description_valid(description):
    if len(description) <= 0:
        #print("Opis uszkodzenia nie może być pusty!")
        return False
    return True


def confirmation_number_valid(conf_number, last_number):
    if conf_number < 1 or conf_number > last_number:
        #print("Nie ma takiego potwierdzenia!")
        return False
    return True

