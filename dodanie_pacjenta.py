import json
from pacjenci import odczyt
from datetime import datetime

def zapis_bazy(plik, baza):
    with open(plik, 'w', encoding='utf-8') as f:
        json.dump(baza, f, indent=4, ensure_ascii=False)

def duplikat_chipu(id_chip):
    data = odczyt()
    return True if all(zwierze['id_chip'] != id_chip for zwierze in data['zwierzeta']) else False

def podanie_chipu():
    while True:
        czy_chip = input("Czy zwierze posiada chip? (y/n): ").lower()
        if czy_chip == "y":
            while True:
                chip_numer = input("Podaj ID chipu (5 znaków): ").upper()
                if len(chip_numer) != 5:
                    print("Nieprawidłowa długość ID chipu. ID powinno mieć 5 znaków.")
                elif not duplikat_chipu(chip_numer):
                    print("W bazie istnieje już rekord z podanym numerem chipu.")
                else:
                    return True, chip_numer
        elif czy_chip == "n":
            return False, None
        else:
            print("Niepoprawna wartość. Wybierz 'y' lub 'n'.")

def dodanie_pacjenta(plik='baza.json'):
    baza = odczyt()

    typ = input("Podaj typ zwierzęcia: ")
    imie = input("Podaj imię zwierzęcia: ")
    waga = float(input("Podaj wagę zwierzęcia: "))

    while True:
        data_urodzenia = input("Podaj datę (dd-mm-yyyy): ")
        try:
            datetime.strptime(data_urodzenia, "%d-%m-%Y")
            break
        except ValueError:
            print("Podano niepoprawny format daty. Spróbuj ponownie.")

    zgon = False
    wlasciciel_imie_nazwisko = input("Podaj imię i nazwisko właściciela: ")
    wlasciciel_telefon = input("Podaj telefon właściciela: ")

    czy_chip, chip_id = podanie_chipu()

    nowe_id = max([zwierze["id"] for zwierze in baza["zwierzeta"]]) + 1

    nowy_zwierzak = {
        "id": nowe_id,
        "typ": typ,
        "imie": imie,
        "waga": waga,
        "data_urodzenia": data_urodzenia,
        "zgon": zgon,
        "chip": czy_chip,
        "id_chip": chip_id,
        "wlasciciel": {
            "imie_nazwisko": wlasciciel_imie_nazwisko,
            "telefon": wlasciciel_telefon
        },
        "historia_leczenia":[]
    }

    baza["zwierzeta"].append(nowy_zwierzak)
    zapis_bazy(plik, baza)



