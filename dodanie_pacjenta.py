import csv

def dodanie_pacjenta(plik_csv: str) -> None:
    typ_zwierzaka = input("Typ zwierzaka: ")
    imie = input("Imie zwierzaka: ")
    try:
        waga = float(input("Waga: "))
    except ValueError:
        print("Waga musi być liczbą.")
        return
    try:
        wiek = int(input("Wiek: "))
    except ValueError:
        print("Wiek musi być liczbą całkowitą.")
        return
    wlasciciel = input("Imie i nazwisko wlasciciela: ")
    nr_tel = input("Numer telefonu: ")

    with open(plik_csv, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([typ_zwierzaka, imie, waga, wiek, wlasciciel, nr_tel])

plik_csv = 'zwierzaki.csv'
dodanie_pacjenta(plik_csv)
