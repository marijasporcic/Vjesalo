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

while(pocetak == "DA"):
    igraci = [] 
    broj_igraca = int(input("Unesite broj igrača > "))

    
    for i in range (0, broj_igraca):
        nadimak = input("Unesi nadimak " + str(i+1) + ". igraca > ")
        igraci.append(nadimak)
        bodovi[nadimak] = 0

    
    pocetak = input("Igra je gotova!\nAko želite opet igrati upišite DA > ")
    
