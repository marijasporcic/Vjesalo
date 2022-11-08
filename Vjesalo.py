import random

baza_rijeci=["MAČKA", "PAS", "IGRAČKA", "LjEŠNjAK", "PRST", "CVIJET", "LIST", "BIOLOGIJA", "KEMIJA", "FIZIKA", "INFORMATIKA", "RIJEČ", "ZAMJENICA", "IMENICA", "PJESMA", "ŽIVOT", "IGRA", "SLOVO", "TINTA", "BRAK", "LjEPOTA", "ZEMLJA", "PRAH", "ŠLjUNAK", "BAČVA", "TULIPAN", "PANj", "TRUBA", "GITARA", "TROMBON", "KLAVIR", "MORE", "OBLAK", "NEBO", "SUTON", "BROJ", "ČESTICA", "USKLIK", "PRINTER", "ELEKTROMOTOR", "BARA", "JEZERO", "RIJEKA", "POTOK", "ŠUMA", "ŠARAN", "ŠTUKA", "SOM", "PASTRVA", "RIJEKA", "BRZACI", "BLIZANCI", "DIJETE", "MAJKA", "TULJAN", "KIT", "VESLO", "LABUD", "GALEB", "DALJINA", "PATKA", "PINGVIN", "ORHIDEJA", "SLIKA", "PRIKAZ", "FOTOGRAFIJA", "FOTOAPARAT", "MITOZA", "KARDIOLOGIJA", "KARDIOKIRURG", "KARDIOKIRURGIJA", "NEUROLOG", "NEUROLOGIJA", "REUMATOLOG", "REUMATOLOGIJA", "SIMFONIJA", "SONATA", "SAT"] 
abeceda= "Dž - Lj - Nj - A - B - C - Č - Ć - D - Đ - E - F - G - H - I - J - K - L - M - N - O - P - R - S - Š - T - U - V - Z - Ž" 
abeceda = abeceda. split(" - ") 


leaderboard = {}
f = open("scores.txt", "r", encoding = "UTF8")
lines = f.readlines()
for line in lines:
    nadimak, bodovi = line.split(" ")
    leaderboard[nadimak.strip()] = int(bodovi.strip())

f.close()


bodovi={}

crtezi = ["  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========", 
              "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========",
              "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========",
              "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========",
              "  +---+\n  |   |\n  O   |\n /|\  |\n      |\n      |\n=========",
              "  +---+\n  |   |\n  O   |\n /|\  |\n /    |\n      |\n=========",
              "  +---+\n  |   |\n  O   |\n /|\  |\n / \  |\n      |\n========="]


def novo_slovo(krivih):
    slovo = "" 
    while(slovo == ""):
        slovo = input("Unesi slovo > ")
        if(len(slovo) == 1 and slovo.upper() in abeceda):
            slovo = slovo.upper()
        elif(slovo == "dž" or slovo == "DŽ" or slovo == "Dž"):
            slovo = "Dž"
        elif(slovo == "lj" or slovo == "LJ" or slovo == "Lj"):
            slovo = "Lj"
        elif(slovo == "nj" or slovo == "NJ" or slovo == "Nj"):
            slovo = "Nj"
        else: 
            print("Ovo slovo ne postoji.")
            slovo = ""
            
        if(slovo != "" and slovo not in neiskoristena_slova):
            print("Ovo slovo je već isprobano. Probaj neko drugo slovo: " + str(neiskoristena_slova))
            slovo = ""
            
        elif(slovo in neiskoristena_slova):
            neiskoristena_slova.remove(slovo)
        
    if(slovo in izabrana_rijec):
        tocna_slova.append(slovo)
        uspjesno = True
        print("Bravo!")
    else:
        netocna_slova.append(slovo)
        print("Nažalost to slovo nije u riječi.")
        krivih = krivih + 1
        uspjesno = False
    return krivih, uspjesno 


 

pocetak = input("Dobro došli!\nAko želite igrati vješalo upišite DA > ")
pocetak=pocetak.upper()

def zamijeni_s_crticama(skrivena_rijec):
    
    skrivena_rijec = pocetna_rijec 
    
    for neiskoristeno_slovo in neiskoristena_slova:
        if neiskoristeno_slovo in izabrana_rijec:
            skrivena_rijec = skrivena_rijec.replace(neiskoristeno_slovo, "_")    
    return skrivena_rijec

while(pocetak == "DA"):
    neiskoristena_slova = []
    neiskoristena_slova.extend(abeceda) 

    tocna_slova = [] 
    netocna_slova = [] 
    izabrana_rijec = ""
    igraci = [] 
     
    broj_igraca = int(input("Unesite broj igrača > "))

    
    for i in range (0, broj_igraca):
        nadimak = input("Unesi nadimak " + str(i+1) + ". igraca > ")
        igraci.append(nadimak)
        bodovi[nadimak] = 0
    bira=random.choice(igraci)
    if broj_igraca!=1:
        print("Riječ u ovoj igri bira "+str(bira)+".")  
         
    nacin = ""
    while(nacin != "A" and nacin != "B"):
        if broj_igraca==1:
            nacin = "B"
            print("Riječ je izabrana iz baze")
        else:
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
    if nacin=="A":
        maknuti=igraci.pop(igraci.index(bira))
    skrivena_rijec = "" 
    krivih = 0
    najvise_krivih = 6
    index_igraca = 0
    skrivena_rijec = zamijeni_s_crticama(skrivena_rijec) 

    
    while(krivih < 6):

        print(crtezi[krivih])
        print("Na redu je " + igraci[index_igraca] + ".")
        print(skrivena_rijec)

        krivih, uspjeh = novo_slovo(krivih) 
        skrivena_rijec = zamijeni_s_crticama(skrivena_rijec) 

        
        if(not uspjeh):
            
            index_igraca = index_igraca + 1
            
            if(index_igraca == len(igraci)):
                index_igraca = 0
        else:
            bodovi[igraci[index_igraca]] += 1 

        
        if(skrivena_rijec == pocetna_rijec): 
            break 

        
        print("------------------------------------------\n\n")

    if(pocetna_rijec == skrivena_rijec): 
        print("Čestitam! Pogodili ste riječ " + skrivena_rijec)
    else:
        print("Nažalost niste uspjeli pogoditi riječ.")
    
    #https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
    bodovi = {k: v for k, v in sorted(bodovi.items(), key=lambda item: item[1], reverse=True)}

    for ime in bodovi.keys():
        print(ime + " ---> " + str(bodovi[ime]))
        
        if(ime in leaderboard.keys()):
            
            stari_rezultat = leaderboard[ime]
            novi_rezultat = bodovi[ime]
            if(novi_rezultat > stari_rezultat): 
                leaderboard[ime] = novi_rezultat 
        else: 
            leaderboard[ime] = bodovi[ime] 


    print("-----------------------------------------")
    print("Bodovi [sve igre ikad]: ")

    leaderboard = {k: v for k, v in sorted(leaderboard.items(), key=lambda item: item[1], reverse=True)}

    for ime in leaderboard.keys():
        print(ime + " ---> " + str(leaderboard[ime]))

    
    pocetak = input("Igra je gotova!\nAko želite opet igrati upišite DA > ")
    pocetak=pocetak.upper()
    
    
    
zapis = ""
for ime in leaderboard.keys(): 
    zapis += ime + " " + str(leaderboard[ime]) + "\n" 
    
print(zapis.split("\n")[0:5])
if len(zapis.split("\n"))<5:
    print(zapis.split("\n")[0:len(zapis.split("\n"))])

f = open("scores.txt", "w")
f.write(zapis)
f.close()
