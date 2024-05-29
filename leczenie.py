import json
from pacjenci import odczyt, wybranie_pacjenta

def historia_wyswietlenie(id_zwierzaka, data):
    # Wyswietlenie historii leczenia danego zwierzaka

    zwierze = next(filter(lambda x: x['id'] == id_zwierzaka, data['zwierzeta']))
    for i in zwierze['historia_leczenia']:
        print(f"\nId_zabiegu: {i['id_zabiegu']}")
        print(f"Data wizyty: {i['data']}")
        print(f"Opis wizyty: {i['opis']}")
        print(f"Przypisane leki: {i['leki']}")
        print(f"Kwota brutto: {i['kwota']*1.23}")
        print("\n---------------------")

def historia_dodanie(id_zwierzaka, data):
    # Dodanie nowej pozycji do historii leczenia danego zwierzaka

    zwierz = data['zwierzeta'][id_zwierzaka-1]['historia_leczenia']

    if zwierz:
        nowe_id_zabiegu = max(zabieg['id_zabiegu'] for zabieg in zwierz) + 1
    else:
        nowe_id_zabiegu = id_zwierzaka*100+1

    
    data_zabiegu = input("Podaj datę: ")
    opis = input("Podaj opis: ")
    leki_liczba = int(input("Podaj liczbę leków: "))
    leki_zabieg = []
    for i in range(0, leki_liczba):
        lek = input("Podaj lek: ")
        leki_zabieg.append(lek)
    cena = float(input("Podaj cenę: "))

    nowe_leczenie = {
                    "id_zwierzaka": id_zwierzaka,
                    "id_zabiegu": nowe_id_zabiegu,
                    "data": data_zabiegu,
                    "opis": opis,
                    "leki": leki_zabieg,
                    "kwota": cena
                }

    zwierz.append(nowe_leczenie)

    with open('baza.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def leczenie_wybor():
    # Menu leczenia, możliwe wyświetlenie historii leczenia i dodanie nowego elementu
    
    while True:
        wybor = int(input("Wybierz jeśli: \n 1. Chcesz wyświetlić historię leczenia \n 2. Chcesz dodać historię kolejnej wizyty \n"))
        if wybor not in range(1,3):
            print("Podano niepoprawną wartość")
        else:
            break

    id_zwierzaka = wybranie_pacjenta()

    if wybor == 1:
        historia_wyswietlenie(id_zwierzaka, odczyt())
    else:
        historia_dodanie(id_zwierzaka, odczyt())
