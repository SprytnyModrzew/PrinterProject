polish_small_characters = ['ą', 'ć', 'ę', 'ł', 'ń', 'ó', 'ś', 'ź', 'ż']
polish_big_characters = ['Ą', 'Ć', 'Ę', 'Ł', 'Ń', 'Ó', 'Ś', 'Ź', 'Ż']


def name_valid(name):
    if len(name) <= 0:
        raise ValueError("Imię nie może być puste!")
    if name[0] < chr(65) or name[0] > chr(90):
        if name[0] not in polish_big_characters:
            raise ValueError("Imię powinno zaczynać się z dużej litery!")
    for i in range(1, len(name)):
        if name[i] < chr(97) or name[i] > chr(122):
            if name[i] not in polish_small_characters:
                raise ValueError("Imię powinno zawierać tylko litery!")
    return


def surname_valid(surname):
    if len(surname) <= 0:
        raise ValueError("Nazwisko nie może być puste!")
    if surname[0] < chr(65) or surname[0] > chr(90):
        if surname[0] not in polish_big_characters:
            raise ValueError("Nazwisko powinno zaczynać się z dużej litery!")
    for i in range(1, len(surname)):
        if surname[i] < chr(97) or surname[i] > chr(122):
            if surname[i] not in polish_small_characters:
                raise ValueError("Nazwisko powinno zawierać tylko litery!")
    return


def device_name_valid(devname):
    if len(devname) <= 0:
        raise ValueError("Nazwa urządzenia nie może być pusta!")
    if devname[0] == chr(32):
        raise ValueError("Nazwa urządzenia nie powinna zaczynać się od spacji!")
    for i in range(0, len(devname)):
        if devname[i] < chr(48) or devname[i] > chr(57):
            if devname[i] < chr(65) or devname[i] > chr(90):
                if devname[i] < chr(97) or devname[i] > chr(122):
                    if devname[i] not in polish_big_characters and devname[i] not in polish_small_characters:
                        if devname[i] != chr(32):
                            if devname[i] != chr(45):
                                raise ValueError(
                                    "Nazwa urządzenia powinna zawierać tylko cyfry, litery, spacje, polskie znaki lub '-'!")
    return


def serial_number_valid(sernumber):
    if len(sernumber) <= 0:
        raise ValueError("Numer seryjny nie może być pusty!")
    for i in range(0, len(sernumber)):
        if sernumber[i] < chr(48) or sernumber[i] > chr(57):
            if sernumber[i] < chr(65) or sernumber[i] > chr(90):
                if sernumber[i] < chr(97) or sernumber[i] > chr(122):
                    raise ValueError("Numer seryjny powinien zawierać tylko cyfry i litery!")
    return


def client_name_valid(client):
    if len(client) <= 0:
        raise ValueError("Nazwa klienta nie może być pusta!")
    return


def phone_number_valid(phone):
    if len(phone) != 9:
        print(phone)
        print(len(phone))
        raise ValueError("Numer telefonu musi się składać z 9 cyfr!")
    for i in range(0, 9):
        if phone[i] < chr(48) or phone[i] > chr(57):
            raise ValueError("Numer telefonu musi się składać wyłącznie z cyfr!")
    return


def description_valid(description):
    if len(description) <= 0:
        raise ValueError("Opis uszkodzenia nie może być pusty!")
    return


# never used
def confirmation_number_valid(conf_number, last_number):
    if conf_number < 1 or conf_number > last_number:
        raise ValueError("Nie ma takiego potwierdzenia!")
    return
