from pacjenci import wyswietl_informacje_zwierzaka
from dodanie_pacjenta import dodanie_pacjenta
from leczenie import leczenie_wybor
from edycja_pacjenta import edytuj_dane


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
            print("5. Wyjście")
            x = input("\nWitamy w przychodni weterynaryjnej Zwierzogród! Wybierz opcję: ")
            print("\n--------------------\n")
            if int(x) < 1 or int(x) > 5:
                raise ValueError("Proszę wybrać opcję z przedziału 1-5.\n")
            elif int(x) == 1:
                wyswietl_informacje_zwierzaka()
            elif int(x) == 2:
                dodanie_pacjenta("baza.json")
            elif int(x) == 3:
                leczenie_wybor()
            elif int(x) == 4:
                edytuj_dane()
            elif int(x) == 5:
                print("Do widzenia!")
                break
            if pow_exit() == 2:
                break
        except ValueError as e:
            print(f"{e}\n")


menu()
