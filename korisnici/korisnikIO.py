
datoteka = './datoteke/korisnici.txt'

def sacuvaj_korisnike():
    pass


def ucitaj_korisnike():
    f = open(datoteka)
    redovi = f.readlines()

    korisnici = []
    for red in redovi:
        korisnicki_podaci = red.strip().split("|")

        korisnik = {}
        korisnik['korisnicko_ime'] = korisnicki_podaci[0]
        korisnik['lozinka'] = korisnicki_podaci[1]
        korisnik['ime'] = korisnicki_podaci[2]
        korisnik['prezime'] = korisnicki_podaci[3]
        korisnik['tip_korisnika'] = korisnicki_podaci[4]

        korisnici.append(korisnik)

    return korisnici