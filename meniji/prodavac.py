def meni_prodavac(ulogovani_korisnik):
    while True:
        print()
        print("-"*20)
        print("1. Prikaz svih knjiga")
        print("2. Pretraga knjiga")
        print("3. Prikaz svih akcija")
        print("4. Pretraga akcija")
        print("5. Prodaja knjiga")
        print("6. Dodavanje knjige")
        print("7. Izmjena knjige")
        print("8. Logicko brisanje knjige")
        print("9. Kraj")
        print("-"*20)

        stavka = int(input("Izaberite stavku: "))

        if stavka == 1:
            print("PRIKAZ SVIH KNJIGA")
        elif stavka  == 2:
            print("PRETRAGA KNJIGA")
        elif stavka == 3:
            print("PRIKAZ SVIH AKCIJA")
        elif stavka == 4:
            print("PRETRAGA AKCIJA")
        elif stavka == 5:
            print("PRODAJA KNJIGA")
        elif stavka == 6:
            print("DODAVANJE KNJIGE")
        elif stavka == 7:
            print("IZMJENA KNJIGE")
        elif stavka == 8:
            print("LOGICKO BRISANJE KNJIGE")
        elif stavka == 9:
            return
        else:
            print("Pogresan izbor!")
