
def meni_menadzer(ulogovani_korisnik):
    while True:
        print()
        print("-"*20)
        print("1. Prikaz svih knjiga")
        print("2. Pretraga knjiga")
        print("3. Prikaz svih akcija")
        print("4. Pretraga akcija")
        print("5. Registracija")
        print("6. Prikaz svih korisnika")
        print("7. Dodavanje akcijske ponude")
        print("8. Kreiranje izvještaja")
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
            print("REGISTRACIJA")
        elif stavka == 6:
            print("PRIKAZ SVIH KORISNIKA")
        elif stavka == 7:
            print("DODAVANJE AKCIJSKE PONUDE")
        elif stavka == 8:
            print("KREIRANJE IZVJESTAJA")
        elif stavka == 9:
            return
        else:
            print("Pogresan izbor!")


