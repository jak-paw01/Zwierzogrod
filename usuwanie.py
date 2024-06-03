from pacjenci import odczyt, znajdz_min_max_id
from dodanie_pacjenta import zapis_bazy


def podglad():
    data = odczyt()
    for zwierze in data['zwierzeta']:
        print(f"Id: {zwierze['id']}, imię: {zwierze['imie']}")


def usun_zwierzaka(data):
    podglad()
    min_id, max_id = znajdz_min_max_id(data)
    while True:
        try:
            zwierz = int(input("\nPodaj id zwierzaka, którego chcesz usunąć: "))
            if zwierz < min_id or zwierz > max_id:
                raise ValueError(f"Id {zwierz} jest spoza zakresu (min: {min_id}, max: {max_id}).")
            else:
                del data['zwierzeta'][zwierz - 1]
                print(f"Usunięto zwierzaka o id {zwierz} z bazy pacjentów.")
                zapis_bazy('baza.json', data)
                break

        except ValueError as e:
            print(e)


def wyczysc_baze(data):
    data['zwierzeta'] = []
    print("Wyczyszczono bazę pacjentów.")
    zapis_bazy('baza.json', data)


def usuwanie_wybor():
    data = odczyt()
    while True:
        try:
            wartosc = int(input("1. Usuń zwierzaka z bazy\n2. Wyczyść bazę pacjentów\n\nWybierz opcję: "))
            print("\n--------------------\n")
            if wartosc == 1:
                usun_zwierzaka(data)
                break
            elif wartosc == 2:
                wyczysc_baze(data)
                break
            else:
                print("Wybierz opcję 1 lub 2.\n")
        except ValueError:
            print("Podano nieprawidłową wartość. Wybierz 1 lub 2.")
