from korisnici.korisnik import prijava
from meniji.administrator import meni_administrator
from meniji.menadzer import meni_menadzer
from meniji.prodavac import meni_prodavac


def main():
    ulogovani_korisnik = prijava()


    if ulogovani_korisnik is not None:
        if ulogovani_korisnik['tip_korisnika'] == 'Administrator':
            meni_administrator(ulogovani_korisnik)
        elif ulogovani_korisnik['tip_korisnika'] == 'Menadzer':
            meni_menadzer(ulogovani_korisnik)
        elif ulogovani_korisnik['tip_korisnika'] == 'Prodavac':
            meni_prodavac(ulogovani_korisnik)
        else:
            print("Greska! Nepostojeca uloga!")


main()
