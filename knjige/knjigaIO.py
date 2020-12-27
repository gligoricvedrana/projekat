
datoteka = './datoteke/knjige.txt'

def sacuvaj_knjige():
    pass


def ucitaj_knjige():
    f = open(datoteka)
    redovi = f.readlines()

    knjige = []
    for red in redovi:
        knjige_podaci = red.strip().split("|")

        knjiga = {}
        knjiga['sifra'] = knjige_podaci[0]
        knjiga['naslov'] = knjige_podaci[1]
        knjiga['isbn'] = knjige_podaci[2]
        knjiga['autor'] = knjige_podaci[3]
        knjiga['izdavac'] = knjige_podaci[4]
        knjiga['broj_strana'] = knjige_podaci[5]
        knjiga['godina'] = knjige_podaci[6]
        knjiga['cijena'] = knjige_podaci[7]
        knjiga['kategorija'] = knjige_podaci[8]


        knjige.append(knjiga)

    return knjige
