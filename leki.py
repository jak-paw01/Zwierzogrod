from pacjenci import odczyt
from dodanie_pacjenta import zapis_bazy
from wyszukanie import usun_polskie_znaki
from edycja_pacjenta import sprawdz_klucz


def wyswietl_leki():
    data = odczyt()
    for lek in data["leki"]:
        print(f"ID: {lek['id']}, nazwa: {lek['nazwa']}, cena: {lek['cena']},")
    print("\n--------------------")


def dodaj_lek(data):
    nazwa = str(input("Podaj nazwę leku: "))
    cena = int(input("Podaj cenę leku: "))

    nowe_id = max([lek["id"] for lek in data["leki"]]) + 1

    nowy_lek = {
        "id": nowe_id,
        "nazwa": nazwa,
        "cena": cena
    }

    data["leki"].append(nowy_lek)
    zapis_bazy('baza.json', data)
    print("\nDodano lek do bazy.")
    print("\n--------------------")


def edytuj_lek(data, id_leku):
    lek = next(filter(lambda x: x['id'] == id_leku, data['leki']))
    while True:
        klucz = usun_polskie_znaki(input("Podaj nazwę klucza, który chcesz edytować: ").lower())
        if sprawdz_klucz(lek, klucz):
            nowa_wartosc = input("Podaj nową wartość: ")
            lek[klucz] = nowa_wartosc
            print(f"\nPomyślnie zaktualizowano wartość klucza '{klucz}' dla leku o ID {id_leku}.")
            print("\n--------------------")
            break
    return data


def edycja_leku(data):
    wyswietl_leki()
    id_leku = int(input("Podaj ID leku, który chcesz edytować: "))
    result = edytuj_lek(data, id_leku)
    zapis_bazy('baza.json', result)


def leki_wybor():
    data = odczyt()
    while True:
        try:
            wartosc = int(input("1. Dodaj lek do bazy\n2. Edytuj lek\n\nWybierz opcję: "))
            print("\n--------------------\n")
            if wartosc == 1:
                dodaj_lek(data)
                break
            elif wartosc == 2:
                edycja_leku(data)
                break
            else:
                print("Wybierz opcję 1 lub 2.\n")
        except ValueError:
            print("Podano nieprawidłową wartość. Wybierz 1 lub 2.")
