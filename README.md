# Zwierzogrod
Przychodnia weterynaryjna online

## Uruchomienie aplikacji
Po uruchomieniu aplikacji pojawia się menu główne.

### 1. Wyświetlenie danych pacjentów (zadanie 1) ✔
- Po wybraniu tej opcji zostaje wyświetlona lista wszystkich pacjentów w formacie (id zwierzaka - imie zwierzaka).
    1. Po wybraniu numeru pacjenta z listy zostają wyświetlone jego szczegółowe dane.
        - Dane zawierają:
            - ID
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
                - Zastosowane leki
                - Cena netto

### 2. Dodanie pacjenta (zadanie 2) ✔
- Umożliwia dodanie nowego pacjenta podając wszystkie wymagane informacje, jak w przypadku wyświetlania danych pacjentów.

### 3. Podejmij leczenie (zadanie 3) ✔
- Menu z dwoma opcjami do wyboru:
    1. Wyświetlenie historii leczenia danego zwierzaka:
        - Umożliwia wyświetlenie historii leczenia dla wybranego zwierzaka.
    2. Dodanie historii leczenia dla wybranego zwierzaka:
        - Pozwala na dodanie nowego wpisu do historii leczenia wybranego zwierzaka.

### 4. Uśmiercenie zwierzaka (zadanie 5)
- Pozwala na oznaczenie zwierzaka jako zmarłego poprzez zmianę statusu z `False` na `True` oraz wyświetlenie emotki czaszki.

### 5. Edycja danych pacjenta (zadanie 6) ✔
- Umożliwia edycję danych wybranego pacjenta.
    1. Po wybraniu pacjenta wyświetlają się wszystkie dostępne informacje.
    2. Następnie można wybrać numer danych, które chcesz edytować.

Każde zadanie jest zrobione, gdy zostanie dodane do aplikacji i w pełni funkcjonalne.
