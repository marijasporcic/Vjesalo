import random

baza_rijeci=["MAČKA", "PAS", "IGRAČKA", "LjEŠNjAK", "PRST", "CVIJET", "LIST", "BIOLOGIJA", "KEMIJA", "FIZIKA", "INFORMATIKA", "RIJEČ", "ZAMJENICA", "IMENICA", "PJESMA", "ŽIVOT", "IGRA", "SLOVO", "TINTA", "BRAK", "LjEPOTA", "ZEMLjA", "PRAH", "ŠLjUNAK", "BAČVA", "TULIPAN", "PANj", "TRUBA", "GITARA", "TROMBON", "KLAVIR", "MORE", "OBLAK", "NEBO", "SUTON", "BROJ", "ČESTICA", "USKLIK", "PRINTER", "ELEKTROMOTOR", "BARA", "JEZERO", "RIJEKA", "POTOK", "ŠUMA", "ŠARAN", "ŠTUKA", "SOM", "PASTRVA", "BRZACI", "BLIZANCI", "DIJETE", "MAJKA", "TULjAN", "KIT", "VESLO", "LABUD", "GALEB", "DALjINA", "PATKA", "PINGVIN", "ORHIDEJA", "SLIKA", "PRIKAZ", "FOTOGRAFIJA", "FOTOAPARAT", "MITOZA", "KARDIOLOGIJA", "KARDIOKIRURG", "KARDIOKIRURGIJA", "NEUROLOG", "NEUROLOGIJA", "REUMATOLOG", "REUMATOLOGIJA", "SIMFONIJA", "SONATA", "SAT"]  
abeceda= "Dž - Lj - Nj - A - B - C - Č - Ć - D - Đ - E - F - G - H - I - J - K - L - M - N - O - P - R - S - Š - T - U - V - Z - Ž" #postavljena je hrvatska abeceda kao varijabla abeceda
abeceda = abeceda. split(" - ") #abecedu se razdvojilo po crticama kako bi se dobila slova pojedinačno


leaderboard = {} #rječnik u koji se bilježe nadimci i rezultati igrača
f = open("scores.txt", "r", encoding = "UTF8") #otvara se postojeća datoteka "scores.txt" u koju se tijekom igre bilježe rezultati
lines = f.readlines() 
for line in lines:
    nadimak, bodovi = line.split(" ") 
    leaderboard[nadimak.strip()] = int(bodovi.strip()) 

f.close() 


bodovi={} #rječnik bodova

crtezi = ["  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========", 
              "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========",
              "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========",
              "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========",
              "  +---+\n  |   |\n  O   |\n /|\  |\n      |\n      |\n=========",
              "  +---+\n  |   |\n  O   |\n /|\  |\n /    |\n      |\n=========",
              "  +---+\n  |   |\n  O   |\n /|\  |\n / \  |\n      |\n========="] #lista crteža za vješalo


def novo_slovo(krivih): #definira se definicija za nova slova koja prima samo argument krivih slova
    slovo = "" 
    while(slovo == ""): #sljedeće se provodi dok se slovo tek treba izabrati
        slovo = input("Unesi slovo > ") 
        if(len(slovo) == 1 and slovo.upper() in abeceda): 
            slovo = slovo.upper() 
        elif(slovo == "dž" or slovo == "DŽ" or slovo == "Dž"): #provjeravaju se svi mogući unosi slova dž
            slovo = "Dž" #slovo se postavlja na način na koji nama paše
        elif(slovo == "lj" or slovo == "LJ" or slovo == "Lj"): #isto kao i za dž
            slovo = "Lj"
        elif(slovo == "nj" or slovo == "NJ" or slovo == "Nj"): #isto kao i za nj
            slovo = "Nj"
        else: 
            print("Ovo slovo ne postoji.") #ako korisnik upiše bilo što što nije slovo
            slovo = "" 
            
        if(slovo != "" and slovo not in neiskoristena_slova): #ako je upisano slovo koje je već izabrano, ispisuje se poruka koja na to upućuje
            print("Ovo slovo je već isprobano. Probaj neko drugo slovo: " + str(neiskoristena_slova)) #uz tu poruku se ispisuje lista dotad neiskorištena slova
            slovo = "" 
            
        elif(slovo in neiskoristena_slova): #ako se upiše slovo koje nije isprobano,
            neiskoristena_slova.remove(slovo) #iz liste neisorištenih slova se miče to slovo
        
    if(slovo in izabrana_rijec): #ako je slovo u izabranoj riječi,
        tocna_slova.append(slovo) #u listu točnih slova se ubacuje to slovo
        uspjesno = True 
        print("Bravo!")
    else:
        netocna_slova.append(slovo) #ako nije pogođeno, stavlja se u listu netočnih slova
        print("Nažalost to slovo nije u riječi.") 
        krivih = krivih + 1 #zbrajaju se sva netočna slova kako bi se moglo bilježiti u bodove
        uspjesno = False 
    return krivih, uspjesno 


 

pocetak = input("Dobro došli!\nAko želite igrati vješalo upišite DA > ") 
pocetak=pocetak.upper() 

def zamijeni_s_crticama(skrivena_rijec): #definira se definicija koja će zamijeniti sva slova crticama na početku igre
    
    skrivena_rijec = pocetna_rijec 
    
    for neiskoristeno_slovo in neiskoristena_slova: 
        if neiskoristeno_slovo in izabrana_rijec: 
            skrivena_rijec = skrivena_rijec.replace(neiskoristeno_slovo, "_")    
    return skrivena_rijec #vraća nam se riječ s crticama

while(pocetak == "DA"): 
    neiskoristena_slova = []
    neiskoristena_slova.extend(abeceda) #u listi neiskorištenih slova se na početku nalazi cijela abeceda

    tocna_slova = [] 
    netocna_slova = [] 
    izabrana_rijec = "" 
    igraci = [] 
     
    broj_igraca = int(input("Unesite broj igrača > ")) 

    
    for i in range (0, broj_igraca): #u for petlji se traži nadimak igrača te se od upisanih nadimaka pravi lista igrača i bodovi se postavljaju na nula
        nadimak = input("Unesi nadimak " + str(i+1) + ". igraca > ") 
        igraci.append(nadimak) 
        bodovi[nadimak] = 0 
    bira=random.choice(igraci) #bira nasumično igrača iz liste igrača, a ako igra samo jedan igrač, onda će samo on uvijek biti izabran
    if broj_igraca!=1: #ako je više igrača od jednog, onda će se ispisati koji će nasumični igrač birati riječ
        print("Riječ u ovoj igri bira "+str(bira)+".")  
         
    nacin = "" 
    while(nacin != "A" and nacin != "B"): #pomoću while petlje se bira način igre i ako je samo jedan igrač, onda se način automatki postavlja na "B"
        if broj_igraca==1: 
            nacin = "B" 
            print("Riječ je izabrana iz baze")
        else:
            nacin = input("Ako želiš izabrati riječ upiši: A, a ako ne znaš koju riječ želiš upiši: B i riječ će biti izabrana iz baze > ")
        
        if nacin == "A": #pomoću if se postavlja izabrana riječ ako je više igrača
            izabrana_rijec = input("Upiši riječ (upišite riječ velikim tiskanim slovima, osim Lj, Nj, Dž. Npr. PARADAJZ, LjEŠNjAK)> ")
            izabrana_rijec.strip()
        elif nacin == "B":
            izabrana_rijec = random.choice(baza_rijeci)

    pocetna_rijec = izabrana_rijec 
    izabrana_rijec = list(izabrana_rijec)

    while("j" in izabrana_rijec): #ovom petljom se rješavaju problemi indeksa za lj i nj
        index = izabrana_rijec.index("j")
        if(izabrana_rijec[index-1] == "L"):
            izabrana_rijec[index-1] = "Lj" 
        else:
            izabrana_rijec[index-1] = "Nj"
        izabrana_rijec.pop(index) 

    while("ž" in izabrana_rijec): #rješava se isti problem kao za lj i nj, ali za dž
        index = izabrana_rijec.index("ž")
        izabrana_rijec[index-1] = "Dž" 
        izabrana_rijec.pop(index)
    if nacin=="A": #ako je odabrana opcija kada igrač bira svoju riječ, izbacuje ga se iz liste igrača da on ne može pogađati slova
        maknuti=igraci.pop(igraci.index(bira))
    skrivena_rijec = "" 
    krivih = 0
    najvise_krivih = 6
    index_igraca = 0
    skrivena_rijec = zamijeni_s_crticama(skrivena_rijec) 

    
    while(krivih < 6): #ovom while petljom se printaju crteži za svako pogrešno pogođeno slovo i prelazi se na sljedećeg igrača na listi, a ako igrač pogodi slovo, onda mu se dodavaju bodovi, a ako su igrači pogodili sva slova petlja se prekida

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
        print("Izabrana riječ je "+pocetna_rijec+".")
    
    #https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
    bodovi = {k: v for k, v in sorted(bodovi.items(), key=lambda item: item[1], reverse=True)}

    for ime in bodovi.keys(): #ovom se petljom dodaju bodovi i oblikuje leaderboard
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
    

if len(zapis.split("\n"))<5:
    print(zapis.split("\n")[0:len(zapis.split("\n"))])
else:
    print(zapis.split("\n")[0:5])

f = open("scores.txt", "w") #ovdje se u datoteku zapisuju rezultati igre
f.write(zapis)
f.close()
