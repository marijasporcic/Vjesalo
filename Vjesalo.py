import random

baza_rijeci=["MAČKA", "PAS", "IGRAČKA", "LjEŠNjAK"] 
abeceda= "Dž - Lj - Nj - A - B - C - Č - Ć - D - Đ - E - F - G - H - I - J - K - L - M - N - O - P - R - S - Š - T - U - V - Z - Ž" 
abeceda = abeceda. split(" - ") 

bodovi={}

neiskoristena_slova = []
neiskoristena_slova.extend(abeceda) 

tocna_slova = [] 
netocna_slova = [] 
izabrana_rijec = "" 

pocetak = input("Dobro došli!\nAko želite igrati vješalo upišite DA > ")

def zamijeni_s_crticama(skrivena_rijec):
    
    skrivena_rijec = pocetna_rijec 
    
    for neiskoristeno_slovo in neiskoristena_slova:
        if neiskoristeno_slovo in izabrana_rijec:
            skrivena_rijec = skrivena_rijec.replace(neiskoristeno_slovo, "_")    
    return skrivena_rijec

while(pocetak == "DA"):
    igraci = [] 
    broj_igraca = int(input("Unesite broj igrača > "))

    
    for i in range (0, broj_igraca):
        nadimak = input("Unesi nadimak " + str(i+1) + ". igraca > ")
        igraci.append(nadimak)
        bodovi[nadimak] = 0
        
    nacin = ""
    while(nacin != "A" and nacin != "B"):
        nacin = input("Ako želiš izabrati riječ upiši: A, a ako ne znaš koju riječ želiš upiši: B i riječ će biti izabrana iz baze > ")
        if nacin == "A":
            izabrana_rijec = input("Upiši riječ (upišite riječ velikim tiskanim slovima, osim Lj, Nj, Dž. Npr. PARADAJZ, LjEŠNjAK)> ")
            izabrana_rijec.strip()
        elif nacin == "B":
            izabrana_rijec = random.choice(baza_rijeci)

    pocetna_rijec = izabrana_rijec 
    izabrana_rijec = list(izabrana_rijec)

    while("j" in izabrana_rijec): 
        index = izabrana_rijec.index("j")
        if(izabrana_rijec[index-1] == "L"):
            izabrana_rijec[index-1] = "Lj" 
        else:
            izabrana_rijec[index-1] = "Nj"
        izabrana_rijec.pop(index) 

    while("ž" in izabrana_rijec): 
        index = izabrana_rijec.index("ž")
        izabrana_rijec[index-1] = "Dž" 
        izabrana_rijec.pop(index)

    
    pocetak = input("Igra je gotova!\nAko želite opet igrati upišite DA > ")
    
