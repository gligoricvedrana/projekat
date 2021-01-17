from knjige.knjiga import prikazi_knjige
from knjige.knjiga import pretrazi_knjige
from knjige.knjiga import prikazi_sve_akcije
from knjige.knjiga import pretrazi_akcije
from knjige.knjiga import prodaj_knjige
from knjige.knjiga import dodaj_knjige
from knjige.knjiga import izmijeni_knjige
from knjige.knjiga import logicki_brisi_knjige

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
            prikazi_knjige()
        elif stavka  == 2:
            pretrazi_knjige()
        elif stavka == 3:
            prikazi_sve_akcije()
        elif stavka == 4:
            pretrazi_akcije()
        elif stavka == 5:
            prodaj_knjige()
        elif stavka == 6:
            dodaj_knjige()
        elif stavka == 7:
            izmijeni_knjige()
        elif stavka == 8:
            logicki_brisi_knjige()
        elif stavka == 9:
            return
        else:
            print("Pogresan izbor!")
