def citire():
    global d
    global stari
    global litere
    global stariFinale
    global tranzitii
    global cuvinte
    global stareInit
    global starePlecare
    global stariFin
    d = {}
    with open("input.txt","r") as f:
        nrStari = int(f.readline())
        stari = [x for x in f.readline().split()]
        nrLitere = int(f.readline())
        litere = [x for x in f.readline().split()]
        starePlecare = f.readline().strip()
        nrStariFin = int(f.readline())
        stariFinale = [x for x in f.readline().split()]
        nrTranzitii = int(f.readline())
        for x in range (nrTranzitii):
            stareInit, litera, stareUrm = f.readline().split()
            stareInit = stareInit.strip()
            stareUrm = stareUrm.strip()
            litera = litera.strip()
            tuplu = (stareInit, litera)
            d[tuplu] = stareUrm
        nrCuv = int(f.readline())
        cuvinte = [x.strip() for x in f.readlines()]

def acceptare(cuv):
    stareCurenta = starePlecare
    for litera in cuv:
        if (stareCurenta,litera) in d:
            stareCurenta = d[(stareCurenta, litera)]
        else:
            print("NU")
            return
    if stareCurenta in stariFinale:
        print("DA")
    else:
        print("NU")

citire()

for cuvant in cuvinte:
    acceptare(cuvant)