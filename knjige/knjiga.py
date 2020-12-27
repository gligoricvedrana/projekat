from knjige.knjigaIO import ucitaj_knjige


def prikazi_knjige():
    knjige = ucitaj_knjige()

    for knjiga in knjige:
        print(knjiga)




