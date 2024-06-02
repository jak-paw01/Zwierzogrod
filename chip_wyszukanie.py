from pacjenci import odczyt, odczyt_danych_zwierzak

def szukaj_chip():
    while True:
        chip_id = input("Podaj numer chipu: " ).upper()
        if len(chip_id) != 5:
            print("Nieprawidłowa długość ID chipu. ID powinno mieć 5 znaków.")
        else:
            break
    
    data = odczyt()

    for zwierze in data['zwierzeta']:
        if zwierze['chip'] == True:
            if zwierze['id_chip'] == chip_id:
                odczyt_danych_zwierzak(zwierze)