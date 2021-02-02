import os
import re

# >> FUNKCE <<
def nacteni(nazev_souboru):
    # TODO: Docstring
    if os.path.exists(nazev_souboru) and os.path.getsize(nazev_souboru) and os.access(nazev_souboru, os.R_OK) > 0:
        try: # mozna nebude potreba
            with open(nazev_souboru, mode='r', encoding='utf-8') as data:
                # TODO: osetreni vstupy obsahuje jen '0123456789. '; musi obsahovat cislice

                hodnoty = data.read()
                doplnek_ok_znaky = r"[^-0-9\. ]"
                cislice = r"[0-9]+"
                if '  ' in hodnoty:
                    print('Neplatné oddělení mezerami - nadbytek mezer.')
                    exit()
                elif re.match(doplnek_ok_znaky, hodnoty):
                    print('Neplatný vstup - obsahuje nepodporované znaky.\n(Podporované jsou 0-9, minus, des. tečka, mezera.)')
                    exit()
                elif not re.search(cislice, hodnoty):
                    print('Neplatný vstup - neobsahuje číselné hodnoty.')
                    exit()
                else:
                    print("zatím to prošlo, ale není ještě validován formát")
                    return(hodnoty)
                    
        except ValueError:
            print("Vstupní soubor není v platném formátu.")
            exit()
    else:
        print("Vstupní soubor chybí, je prázdný, nebo k němu není povolen přístup.")
        exit()


def prunik(seznam_hodnot1,seznam_hodnot2):
    # TODO: Docstring
    seznam_prunik = []
    for cislo in seznam_hodnot1:
        if cislo in seznam_hodnot2:
            if cislo not in seznam_prunik:
                seznam_prunik.append(cislo)
    return(seznam_prunik)

# TODO: zamezeni vstupu obsahujicich napr. '..4.' ci '.4...4..' atd. -> obecne, bude vyhozeno
# v ramci cyklu lines 39 a 40, kde to zjisti, ze format neni float ale str
# TODO: a osetreni !-' tam kde nema bejt - v cyklu struktura regex



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