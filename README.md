# Zwierzogrod
Aplikacja przychodnia weterynaryjnej online. 

System pozwala na wykonanie następujących operacji:

- **Wyświetlić dane pacjentów**: Uzyskanie pełnych informacji na temat wszystkich zarejestrowanych pacjentów.
- **Dodać nowego pacjenta**: Możliwość dodania nowego pacjenta do systemu z kompletem danych osobowych.
- **Wyświetlić historię leczenia**: Przeglądanie pełnej historii leczenia i zabiegów poszczególnych pacjentów.
- **Dodać historię nowego zabiegu**: Wprowadzenie do systemu informacji o nowym zabiegu przeprowadzonym na pacjencie.
- **Edytować dane pacjenta**: Aktualizacja istniejących danych pacjenta, takich jak dane kontaktowe, adres, itp.


## Uruchomienie aplikacji
Żeby uruchomić aplikację należy będąc w folderze, w którym znajduje się aplikacja w terminalu wykonać komendę ``python3 menu.py``
Po uruchomieniu aplikacji pojawia się menu główne, w którym można uruchomić różne komponenty.

## Działanie poszczególnych funkcjonalności

### 1. Wyświetlenie danych pacjentów
- Po wybraniu tej opcji zostaje wyświetlona lista wszystkich pacjentów w formacie id zwierzaka - imie zwierzaka. Po wybraniu numeru pacjenta z listy zostają wyświetlone jego szczegółowe dane:
    - Id
    - Typ zwierzaka
    - Imię
    - Waga (aktualizowana przy każdej kolejnej wizycie)
    - Wiek (podawany jako data urodzenia, aplikacja oblicza wiek) 
    - Status życia (zgon: True/False)
    - Chip: True/False (czy zwierze posiada chip)
    - Id chipu (gdy zwierze nie posiada chipu - pusta wartość) 
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
- Menu z dwoma opcjami do wyboru:
    - Wyświetlenie historii leczenia danego zwierzaka:
        - Umożliwia wyświetlenie historii leczenia dla wybranego zwierzaka.
    - Dodanie historii leczenia dla wybranego zwierzaka:
        - Pozwala na dodanie nowego wpisu do historii leczenia wybranego zwierzaka.

### 4. Edycja danych pacjenta
- Umożliwia edycję danych wybranego pacjenta.
    - Po wybraniu pacjenta wyświetlają się wszystkie dostępne informacje.
    - Następnie należy wybrać, która ma zostać zmieniona.
    - W kolejnym kroku aplikacja poprosi o podanie nowej wartości.
    - Na końcu zostanie wyświetlony komunikat o poprawnym zakutalizowaniu danej metryki.

 ### 5. Wyszukanie zwierzaka po imieniu lub numerze chipa
 - Umożliwia wyświetlenie danych wyszukiwanego po numerze chipu lub imieniu zwierzaka
    - Po wybraniu tej opcji z głównego menu pojawia się pytanie o wyszukiwaniu po imieniu lub id chipa
    - Po prawidłowym wpisaniu nr chipa pokazują się dane o wybranym pacjencie
    - W przypadku wpisania imienia, na ekranie wyświetlają się wszyscy pacjenci o danym imieniu (kilka zwierzaków może mieć to samo imie)
  
### 6. Usunięcie zwierzaka z bazy lub całej bazy
 - Pozwala na usunięcie konkretnego pacjenta z bazy lub wyczyszczenie całej predefiniowanej bazy
    - Po jej wybraniu pojawia się menu z opcjami usunięcia pojedynczego rekordu lub całej bazy
    - W przypadku wybrania opcji usunięcia pojedynczego zwierzaka, wyświetlone zostaną wszystkie rekordy
    - Wpisanie numeru id zwierzaka spowoduje jego usunięcie z bazy 

### 7. Wyświetlenie bazy leków dostępnych w przychodni weterynaryjnej
 - Po wybraniu tej opcji pokazują się wszystkie leki, których używa przychodnia

### 8. Dodanie lub edytowanie bazy leków
 - Ta opcja pozwala na dodanie nowego leku używanego przez przychodnię lub edycję obecnego już w bazie
     - 1 akcja w tym komponencie wymaga wybrania przez użytkownika czy chce dodać nowy lek czy jedynie zedytować już się znajdujący
     - Po wybraniu dodania nowego leku użytkownik musi podać jego nazwę i cenę netto
     - W przypadku wybrania opcji edycji, pojawiają się wszystkie obecne leki, z których po numerze id można wybrać ten, w którym należy zaktualizować dane

### 9. Usunięcie leku lub wyczyszczenie bazy
 - Pozwala usunąć lek, którego przychodnia już nie używa lub opróżnić całą predefiniowaną bazę
     - Wyświetla menu, z którego należy wybrać czy chce się usunąć konkretny lek czy całą bazę
     - W przypadku wybrania usunięcia jednego leku, pojawiają się wszystkie obecne w bazie leki
     - Podanie id konkretnego leku usuwa go z bazy

### 10. Wyjście z programu
 - Ta opcja kończy działanie programu
