import os
import re

# >> FUNKCE <<
def nacteni(nazev_souboru):
    # TODO: Docstring
    if os.path.exists(nazev_souboru) and os.path.getsize(nazev_souboru) and os.access(nazev_souboru, os.R_OK) > 0:
        with open(nazev_souboru, mode='r', encoding='utf-8') as data:
            hodnoty = str(data.read()).strip()
            kontrola_struktury(hodnoty)
            return(hodnoty)
    else:
        print("Vstupní soubor chybí, je prázdný, nebo k němu není povolen přístup.")
        exit()

def kontrola_struktury(retezec):
    # TODO: Docstring
    struktura = r"^(-?\d+(\.?\d+)?)( -?\d+(\.?\d+)?)*$"
    if re.match(struktura,retezec):
        print("Struktura vstupního souboru je v pořádku.")
    else:
        print("Vstupní soubor nemá validní strukturu.")
        exit()

def prunik(seznam_hodnot1,seznam_hodnot2):
    # TODO: Docstring
    seznam_prunik = []
    for cislo in seznam_hodnot1:
        if cislo in seznam_hodnot2:
            if cislo not in seznam_prunik:
                seznam_prunik.append(cislo)
    return(seznam_prunik)


# >> PROGRAM <<
hodnoty1 = nacteni('hodnoty1.txt')
hodnoty2 = nacteni('hodnoty2.txt')
seznam1 = [float(hodnota) for hodnota in hodnoty1.split(' ')]
seznam2 = [float(hodnota) for hodnota in hodnoty2.split(' ')]

prunik_posloupnosti = prunik(seznam1,seznam2)
prunik_posloupnosti.sort()

print(prunik_posloupnosti)
with open('prunik_posloupnosti.txt', mode='w', encoding='utf-8') as output:   # w jako write >>> mode='a' -> append, tedy připojit na konec souboru
    print(prunik_posloupnosti, file=output)