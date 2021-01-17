from knjige.knjiga import prikazi_knjige
from knjige.knjiga import pretrazi_knjige
from knjige.knjiga import prikazi_sve_akcije
from knjige.knjiga import pretrazi_akcije
from knjige.knjiga import registracija
from knjige.knjiga import prikazi_sve_korisnike
from knjige.knjiga import dodaj_knjige
from knjige.knjiga import izmijeni_knjige
from knjige.knjiga import logicki_brisi_knjige



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
            dodaj_knjige()
        elif stavka == 8:
            izmijeni_knjige()
        elif stavka == 9:
            logicki_brisi_knjige()
        elif stavka == 10:
            return
        else:
            print("Pogresan izbor!")
