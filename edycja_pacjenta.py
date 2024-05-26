import json
from pacjenci import wyswietl_informacje_zwierzaka, odczyt


def sprawdz_klucz(zwierze, klucz):
    if klucz in zwierze:
        return True
    else:
        print(f"Klucz '{klucz}' nie istnieje dla tego zwierzaka.")
        return False

def edytuj_dane_zwierzaka(data, id_zwierzaka):
    zwierze = next(filter(lambda x: x['id'] == id_zwierzaka, data['zwierzeta']))
    while True:
        klucz = input("Podaj nazwę klucza, który chcesz edytować: ").lower()
        if sprawdz_klucz(zwierze, klucz):
            nowa_wartosc = input("Podaj nową wartość: ")
            zwierze[klucz] = nowa_wartosc
            print(f"Pomyślnie zaktualizowano wartość klucza '{klucz}' dla zwierzaka o ID {id_zwierzaka}.")
            break
    return data

# Funkcja główna do edycji danych zwierzaka
def edytuj_dane():

    id_zwierzaka = wyswietl_informacje_zwierzaka()

    result = edytuj_dane_zwierzaka(odczyt(), id_zwierzaka)

    with open('baza.json', 'w', encoding='utf-8') as file:
        json.dump(result, file, ensure_ascii=False, indent=4)

