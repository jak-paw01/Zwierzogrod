import json
from datetime import datetime

def odczyt():
    with open('baza.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def znajdz_min_max_id(data):
    ids = [zwierze['id'] for zwierze in data['zwierzeta']]
    return min(ids), max(ids)

def odczyt_danych_zwierzak(zwierze):
    print(f"ID: {zwierze['id']}")
    print(f"Typ: {zwierze['typ']}")
    print(f"Imię: {zwierze['imie']}")
    print(f"Waga: {zwierze['waga']} kg")
    wiek = oblicz_wiek(zwierze['data_urodzenia'])
    print(f"Wiek: {wiek} lat")
    print(f"Zgon: {'Tak' if zwierze['zgon'] else 'Nie'}")
    print(f"Id chipu: {zwierze['id_chip'] if zwierze['chip'] == True else 'Brak chipu'}")
    print(f"Właściciel: {zwierze['wlasciciel']['imie_nazwisko']}")
    print(f"Numer telefonu właściciela: {zwierze['wlasciciel']['telefon']}")

def wyswietl_informacje_zwierzaka():
    data = odczyt()

    id_zwierzaka = wybranie_pacjenta()
    for zwierze in data['zwierzeta']:
        if zwierze['id'] == id_zwierzaka:
            print("--------------------")
            print("Dane zwierzaka:")
            odczyt_danych_zwierzak(zwierze)
#nowa funkcja - powinna  zmieniać datę urodzenia na obecny wiek - działa
def oblicz_wiek(data_urodzenia):
    dzisiaj = datetime.now()
    data_urodzenia = datetime.strptime(data_urodzenia, "%d-%m-%Y")
    wiek = dzisiaj.year - data_urodzenia.year - ((dzisiaj.month, dzisiaj.day) < (data_urodzenia.month, data_urodzenia.day))
    return wiek

def wyswietl_informacje_zwierzaka():
    data = odczyt()

    id_zwierzaka = wybranie_pacjenta()
    for zwierze in data['zwierzeta']:
        if zwierze['id'] == id_zwierzaka:
            wiek = oblicz_wiek(zwierze['data_urodzenia'])
            print("--------------------")
            print("Dane zwierzaka:")
            print(f"ID: {zwierze['id']}")
            print(f"Typ: {zwierze['typ']}")
            print(f"Imię: {zwierze['imie']}")
            print(f"Waga: {zwierze['waga']} kg")
            print(f"Wiek: {wiek} lat/a")
            print(f"Zgon: {'Tak' if zwierze['zgon'] else 'Nie'}")
            print(f"Właściciel: {zwierze['wlasciciel']['imie_nazwisko']}")
            print(f"Numer telefonu właściciela: {zwierze['wlasciciel']['telefon']}")
            print("Historia leczenia:")
            for zabieg in zwierze['historia_leczenia']:
                print(f"  - ID zabiegu: {zabieg['id_zabiegu']}")
                print(f"    Data: {zabieg['data']}")
                print(f"    Opis: {zabieg['opis']}")
                leki = ', '.join(zabieg.get('leki', [])) if zabieg.get('leki') else "brak"
                print(f"    Leki: {leki}")
            print("\n--------------------")
            return id_zwierzaka



def wybranie_pacjenta():
    data = odczyt()

    for zwierze in data['zwierzeta']:
        print(f"Id: {zwierze['id']}, imię: {zwierze['imie']}")
    
    min_id, max_id = znajdz_min_max_id(data)

    while True:
        try:
            id_wybrany = int(input("\nPodaj id zwierzęcia w celu wyświetlenia pełnych informacji o nim: \n"))

            if id_wybrany < min_id or id_wybrany > max_id:
                raise ValueError(f"Id {id_wybrany} jest spoza zakresu (min: {min_id}, max: {max_id}).")
            
            else:
                break
        
        except ValueError as e:
            print(e)

    return id_wybrany
