# Zwierzogrod
Przychodnia weterynaryjna online


Uruchomienie aplikacji -> pojawia się menu:

1. Wyświetlenie danych pacjentów 
    a. Pojawia się lista wszystkich pacjentów w formacie (1. nazwisko_imiezwierzaka 2.pies2 3.kot1)
        1. Wybierasz pacjenta wpisując w input numerek
            a. Wyświetlają się dane o danym pacjencie
                Przykładowe dane:
                    - id
                    - typ zwierzaka
                    - imie
                    - waga
                    - wiek
                    - zgon: True/False
                    - imie nazwisko wlasciciela
                    - numer telefonu wlasciciela
                    - Historia leczenia:
                        - id zabiegu
                        - data
                        - [rodzaj zabiegu]
                        - [zastosowane leki]
                        - [cena netto] 
2. Dodanie pacjenta
    a. podanie wszystkich rzeczy co wyżej
3. Podejmij leczenie
    a. Pojawia się lista wszystkich pacjentów w formacie (1. nazwisko_imiezwierzaka 2.pies2 3.kot1)
        1. Wybierasz zwierzaka
            a. Generowanie krótkiego rapotu (wyswietlenie calej historii leczenia) - wygenerowany plik csv o nazwie leczenie_nazwisko_imiezwierzaka
4. Usmiercenie zwierzaka
    a. Pojawia się lista wszystkich pacjentów w formacie (1. nazwisko_imiezwierzaka 2.pies2 3.kot1)
        1. Wybierasz którego usmieracasz - zmiana zgon z False na True i wyswietlenie czaszki 
5. Edycja danych pacjenta
    a. Pojawia się lista wszystkich pacjentów w formacie (1. nazwisko_imiezwierzaka 2.pies2 3.kot1)
        1. Wybierasz którego edytujesz
            a. Edycja - wyswietlaja sie wszystkie dane 1. id 2. typ 
                1. Wybierasz numer ktory edytujesz 