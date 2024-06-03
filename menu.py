from pacjenci import wyswietl_informacje_zwierzaka
from dodanie_pacjenta import dodanie_pacjenta
from leczenie import leczenie_wybor
from edycja_pacjenta import edytuj_dane
from wyszukanie import wyszukanie
from usuwanie import usuwanie_wybor, usuwanie_lekow_wybor
from leki import wyswietl_leki, leki_wybor


def pow_exit():
    while True:
        try:
            print("\n1. Powrót do menu głównego")
            print("2. Wyjście")
            print("\n--------------------\n")
            y = input("Wybierz 1, aby powrócić do menu głównego, lub 2 aby wyjść: ")
            print("\n--------------------")
            if int(y) < 0 or int(y) > 2:
                raise ValueError("\nProszę wybrać opcję z przedziału 1-2.\n")
            elif int(y) == 1:
                return y
            elif int(y) == 2:
                print("\nDo widzenia!")
                return 2
        except ValueError as e:
            print(e)


def menu():

    while True:
        try:
            print("\n1. Wyświetl dane pacjentów")
            print("2. Dodaj pacjenta")
            print("3. Podejmij leczenie | Historia leczenia")
            print("4. Edytuj dane pacjenta")
            print("5. Wyszukaj po numerze chipa lub imieniu")
            print("6. Usuń zwierzaka | Wyczyść bazę pacjentów")
            print("7. Wyświetl bazę leków")
            print("8. Dodaj | Edytuj lek")
            print("9. Usuń lek | Wyczyść bazę leków")
            print("10. Wyjście")
            x = int(input("\nWitamy w przychodni weterynaryjnej Zwierzogród! Wybierz opcję: "))
            print("\n--------------------\n")
            if x < 1 or x > 10:
                raise ValueError("Proszę wybrać opcję z przedziału 1-10.\n")
            elif x == 1:
                wyswietl_informacje_zwierzaka()
            elif x == 2:
                dodanie_pacjenta("baza.json")
            elif x == 3:
                leczenie_wybor()
            elif x == 4:
                edytuj_dane()
            elif x == 5:
                wyszukanie()
            elif x == 6:
                usuwanie_wybor()
            elif x == 7:
                wyswietl_leki()
            elif x == 8:
                leki_wybor()
            elif x == 9:
                usuwanie_lekow_wybor()
            elif x == 10:
                print("Do widzenia!")
                break
            if pow_exit() == 2:
                break
        except ValueError as e:
            print(f"{e}\n")


menu()
