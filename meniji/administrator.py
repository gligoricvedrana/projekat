from knjige.knjiga import prikazi_knjige

def meni_administrator(ulogovani_korisnik):
    while True:
        print()
        print("-"*20)
        print("1. Prikaz svih knjiga")
        print("2. Pretraga knjiga")
        print("3. Prikaz svih akcija")
        print("4. Pretraga akcija")
        print("5. Registracija")
        print("6. Prikaz svih korisnika")
        print("7. Dodavanje knjige")
        print("8. Izmjena knjige")
        print("9. Logicko brisanje knjige")
        print("10. Kraj")
        print("-"*20)

        stavka = int(input("Izaberite stavku: "))

        if stavka == 1:
            prikazi_knjige()
        elif stavka  == 2:
            print("PRETRAGA KNJIGA")
        elif stavka == 3:
            print("PRIKAZ SVIH AKCIJA")
        elif stavka == 4:
            print("PRETRAGA AKCIJA")
        elif stavka == 5:
            print("REGISTRACIJA")
        elif stavka == 6:
            print("PRIKAZ SVIH KORISNIKA")
        elif stavka == 7:
            print("DODAVANJE KNJIGE")
        elif stavka == 8:
            print("IZMJENA KNJIGE")
        elif stavka == 9:
            print("LOGICKO BRISANJE KNJIGE")
        elif stavka == 10:
            return
        else:
            print("Pogresan izbor!")
