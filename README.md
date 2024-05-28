# Zwierzogrod
Aplikacja przychodnia weterynaryjnej online. 

System pozwala:
    - wyświetlić dane pacjentów
    - dodać nowego pacjenta
    - wyświetlić historię leczenia
    - dodać historię nowego zabiegu
    - edytować dane pacjenta


## Uruchomienie aplikacji
Po uruchomieniu aplikacji pojawia się menu główne, w którym można uruchomić różne komponenty.

## Działanie poszczególnych funkcjonalności

### 1. Wyświetlenie danych pacjentów
- Po wybraniu tej opcji zostaje wyświetlona lista wszystkich pacjentów w formacie <id zwierzaka - imie zwierzaka>. Po wybraniu numeru pacjenta z listy zostają wyświetlone jego szczegółowe dane:
    - Id
    - Typ zwierzaka
    - Imię
    - Waga
    - Wiek
    - Status życia (zgon: True/False)
    - Imię i nazwisko właściciela
    - Numer telefonu właściciela
    - Historia leczenia:
        - ID zabiegu
        - Data
        - Rodzaj zabiegu
        - Przypisane leki
        - Cena netto zabiegu

### 2. Dodanie pacjenta
- Umożliwia dodanie nowego pacjenta podając wszystkie wymagane informacje.

### 3. Podejmij leczenie
Menu z dwoma opcjami do wyboru:
    - Wyświetlenie historii leczenia danego zwierzaka:
        - Umożliwia wyświetlenie historii leczenia dla wybranego zwierzaka.
    - Dodanie historii leczenia dla wybranego zwierzaka:
        - Pozwala na dodanie nowego wpisu do historii leczenia wybranego zwierzaka.

### 5. Edycja danych pacjenta
Umożliwia edycję danych wybranego pacjenta.
    - Po wybraniu pacjenta wyświetlają się wszystkie dostępne informacje.
    - Następnie należy wybrać, która ma zostać zmieniona.
    - W kolejnym kroku aplikacja poprosi o podanie nowej wartości.
    - Na końcu zostanie wyświetlony komunikat o poprawnym zakutalizowaniu danej metryki.