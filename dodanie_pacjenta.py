import json

plik = 'baza.json'


def wczytanie_bazy(plik):
    with open(plik, 'r', encoding='utf-8') as f:
        return json.load(f)


def zapis_bazy(plik, baza):
    with open(plik, 'w', encoding='utf-8') as f:
        json.dump(baza, f, indent=4, ensure_ascii=False)


def dodanie_pacjenta(plik):
    baza = wczytanie_bazy(plik)

    typ = input("Podaj typ zwierzęcia: ")
    imie = input("Podaj imię zwierzęcia: ")
    waga = float(input("Podaj wagę zwierzęcia: "))
    wiek = int(input("Podaj wiek zwierzęcia: "))
    zgon = False
    wlasciciel_imie_nazwisko = input("Podaj imię i nazwisko właściciela: ")
    wlasciciel_telefon = input("Podaj telefon właściciela: ")

    nowe_id = max([zwierze["id"] for zwierze in baza["zwierzeta"]]) + 1

    nowy_zwierzak = {
        "id": nowe_id,
        "typ": typ,
        "imie": imie,
        "waga": waga,
        "wiek": wiek,
        "zgon": zgon,
        "wlasciciel": {
            "imie_nazwisko": wlasciciel_imie_nazwisko,
            "telefon": wlasciciel_telefon
        },
        "historia_leczenia":[]
    }

    baza["zwierzeta"].append(nowy_zwierzak)
    zapis_bazy(plik, baza)



