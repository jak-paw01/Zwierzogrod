from pacjenci import wyswietl_informacje_zwierzaka
from dodanie_pacjenta import dodanie_pacjenta
from leczenie import leczenie_wybor
from edycja_pacjenta import edytuj_dane
from wyszukanie import wyszukanie
from usuwanie import usuwanie_wybor, usuwanie_lekow_wybor
from leki import wyswietl_leki, leki_wybor


def pow_exit(komunikat, operacja):
    while True:
        try:
            print(f"\n{komunikat}")
            print("\n1. Wykonaj ponownie")
            print("2. Powrót do menu głównego")
            print("\n--------------------\n")
            y = input("WYBIERZ 1, ABY WYKONAĆ OPERACJĘ PONOWNIE, LUB 2 ABY WRÓCIĆ DO MENU GŁÓWNEGO:")
            print("\n--------------------")
            if int(y) < 1 or int(y) > 2:
                raise ValueError("\nPROSZĘ WYBRAĆ OPCJĘ Z 1 LUB 2!\n")
            elif int(y) == 1:
                operacja()
            elif int(y) == 2:
                return
        except ValueError as e:
            print(e)

def menu():
    while True:
        try:
            print("\n=== MENU GŁÓWNE ===\n")
            print("1. Wyświetl dane pacjentów")
            print("2. Dodaj pacjenta")
            print("3. Podejmij leczenie | Historia leczenia")
            print("4. Edytuj dane pacjenta")
            print("5. Wyszukaj po numerze chipa lub imieniu")
            print("6. Usuń zwierzaka | Wyczyść bazę pacjentów")
            print("7. Wyświetl bazę leków")
            print("8. Dodaj | Edytuj lek")
            print("9. Usuń lek | Wyczyść bazę leków")
            print("10. Wyjście\n")
            x = int(input("ZNAJDUJESZ SIĘ W MENU GŁÓWNYM APLIKACJI! ABY WYBRAĆ OPCJĘ WPROWADŹ ODPOWIEDNIĄ CYFRĘ (1-10): "))
            print("\n--------------------\n")
            if x < 1 or x > 10:
                raise ValueError("PROSZĘ WYBRAC OPCJĘ Z PRZEDZIAŁU OD 1 DO 10!\n")
            elif x == 1:
                wyswietl_informacje_zwierzaka()
                print("\n=== OPERACJA ZOSTAŁA WYKONANA POMYśLNIE ===\n")
                pow_exit("Czy chcesz wyświetlić dane pacjentów ponownie?", wyswietl_informacje_zwierzaka)
            elif x == 2:
                def operacja():
                    dodanie_pacjenta("baza.json")
                    print("\n=== DODANO NOWEGO PACJENTA ===\n")
                operacja()
                pow_exit("Czy chcesz dodać kolejnego pacjenta?", operacja)
            elif x == 3:
                def operacja():
                    leczenie_wybor()
                    print("\n=== DODANO NOWE LECZENIE ===\n")
                operacja()
                pow_exit("Czy chcesz dodać kolejne leczenie?", operacja)
            elif x == 4:
                def operacja():
                    edytuj_dane()
                    print("\n=== ZAKTUALIZOWANO DANE PACJENTA ===\n")
                operacja()
                pow_exit("Czy chcesz edytować kolejnego pacjenta?", operacja)
            elif x == 5:
                wyszukanie()
                print("\n=== OPERACJA ZOSTAŁA WYKONANA POMYśLNIE ===\n")
                pow_exit("Czy chcesz wyszukać po numerze chipa lub imieniu ponownie?", wyszukanie)
            elif x == 6:
                def operacja():
                    usuwanie_wybor()
                    print("\n=== OPERACJA ZOSTAŁA WYKONANA POMYśLNIE ===\n")
                operacja()
                pow_exit("Czy chcesz usunąć kolejnego zwierzaka lub wyczyścić bazę pacjentów?", operacja)
            elif x == 7:
                wyswietl_leki()
                print("\n=== OPERACJA ZOSTAŁA WYKONANA POMYśLNIE ===\n")
                pow_exit("Czy chcesz wyświetlić bazę leków ponownie?", wyswietl_leki)
            elif x == 8:
                def operacja():
                    leki_wybor()
                    print("\n=== OPERACJA ZOSTAŁA WYKONANA POMYśLNIE ===\n")
                operacja()
                pow_exit("Czy chcesz dodać lub edytować kolejny lek?", operacja)
            elif x == 9:
                def operacja():
                    usuwanie_lekow_wybor()
                    print("\n=== OPERACJA ZOSTAŁA WYKONANA POMYśLNIE ===\n")
                operacja()
                pow_exit("Czy chcesz usunąć kolejny lek lub wyczyścić bazę leków?", operacja)
            elif x == 10:
                print("DO WIDZENIA!")
                break
        except ValueError as e:
            print(f"{e}\n")
menu()
