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
