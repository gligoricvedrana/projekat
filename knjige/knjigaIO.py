
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



def sacuvaj_akcijske_ponude():
    pass

def ucitaj_akcijske_ponude():
    f = open(datoteka)
    redovi = f.readlines()

    akcijske_ponude = []
    for red in redovi:
        akcijske_ponude_podaci = red.strip().split("|")

        akcijska_ponuda = {}
        akcijska_ponuda['sifra'] = akcijske_ponude_podaci[0]
        akcijska_ponuda['knjige i njihove nove cijene'] = akcijske_ponude_podaci[1]
        akcijska_ponuda['datum do kad vazi'] = akcijske_ponude_podaci[2]

        akcijske_ponude.append(akcijske_ponude)

    return akcijske_ponude


def sacuvaj_racun():
    pass

def ucitaj_racun():
    f = open(datoteka)
    redovi = f.readlines()

    racun = []
    for red in redovi:
        racun_podaci = red.strip().split("|")

        racuni = {}
        racuni['sifra'] = racun_podaci[0]
        racuni['knjige i njihove nove cijene'] = racun_podaci[1]
        racuni['datum do kad vazi'] = racun_podaci[2]

        racun.append(racun)

    return racun