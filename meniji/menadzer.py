from knjige.knjiga import prikazi_knjige
from knjige.knjiga import pretrazi_knjige
from knjige.knjiga import prikazi_sve_akcije
from knjige.knjiga import pretrazi_akcije
from knjige.knjiga import registracija
from knjige.knjiga import prikazi_sve_korisnike
from knjige.knjiga import dodaj_akcijske_ponude
from knjige.knjiga import kreiraj_izvjestaj


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
            prikazi_knjige()
        elif stavka  == 2:
            pretrazi_knjige()
        elif stavka == 3:
            prikazi_sve_akcije()
        elif stavka == 4:
            pretrazi_akcije()
        elif stavka == 5:
            registracija()
        elif stavka == 6:
            prikazi_sve_korisnike()
        elif stavka == 7:
            dodaj_akcijske_ponude()
        elif stavka == 8:
            kreiraj_izvjestaj()
        elif stavka == 9:
            return
        else:
            print("Pogresan izbor!")


