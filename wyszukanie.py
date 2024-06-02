from pacjenci import odczyt, odczyt_danych_zwierzak

def usun_polskie_znaki(text):
    zamiana = str.maketrans(
        "ąĄćĆęĘłŁńŃóÓśŚźŹżŻ",
        "aa" "cc" "ee" "ll" "nn" "oo" "ss" "zz" "zz"
    )
    return text.translate(zamiana).lower()

def szukaj_chip(data):
    while True:
        chip_id = input("Podaj numer chipu: " ).upper()
        if len(chip_id) != 5:
            print("Nieprawidłowa długość ID chipu. ID powinno mieć 5 znaków.")
        else:
            break

    for zwierze in data['zwierzeta']:
        if zwierze['chip'] == True:
            if zwierze['id_chip'] == chip_id:
                odczyt_danych_zwierzak(zwierze)

def szukaj_imie(data):
    imie = input("Podaj imie zwierzaka: ").lower()
    imie = usun_polskie_znaki(imie)
    for zwierze in data['zwierzeta']:
        if imie == usun_polskie_znaki(zwierze['imie']):
            odczyt_danych_zwierzak(zwierze)

def wyszukanie():
    data = odczyt()
    while True:
        try:
            wartosc = int(input("Wybierz wyszukanie po:\n 1. numerze chipu\n 2. imieniu zwierzaka\nWybierz opcję: "))
            if wartosc == 1:
                szukaj_chip(data)
                break
            elif wartosc == 2:
                szukaj_imie(data)
                break
        except ValueError:
            print("Podano nieprawidłową wartość. Wybierz 1 lub 2.")