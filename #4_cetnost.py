# #4 - VYPOCET CETNOSTI
# Anna Svatkova, 3.BFGG, 2021

import os

# >> FUNKCE <<
def nacteni(nazev_souboru):
    """Nacte soubor, osetri souborove chyby vstupu.
    
    V pripade nepouzitelneho vstupu ukonci program. Ukonceni programu pri nasledujicich
    chybach: neexistujici vstupni soubor, prazdny vstupni soubor, nepovolen přistup k vstupnimu
    souboru (pravo cteni).

    Vstup: nazev souboru (s priponou .txt).

    Vystup: data ze souboru (str).
    """
    if os.path.exists(nazev_souboru) == True:
        if os.path.getsize(nazev_souboru) > 0:
            try:
                with open(nazev_souboru, mode='r', encoding='utf-8') as data:
                    vstupni_text = str(data.read())
                    return(vstupni_text)
            except PermissionError:
                print(f"Ke vstupnímu souboru {nazev_souboru} není povolen přístup.")
                exit()
        else:
            print(f"Vstupní soubor {nazev_souboru} je prázdný.")
            exit()
    else:
        print(f"Vstupní soubor {nazev_souboru} chybí.")
        exit()

def cetnost(vstup):
    """Spocita cetnosti polozek vstupu (str,list) a vypise je do slovniku.

    Vstup: seznam (list) jednotlivych znaku/prvku nebo řetězec (str).

    Vystup: slovnik (dict) se znaky a jejich cetnostmi. Cetnost (int) kazdeho znaku textu pod klicem tohoto znaku (napr. 'a': 12).
    """
    slovnik_cetnost = {}
    for znak in vstup:
        if znak in slovnik_cetnost.keys():
            slovnik_cetnost[znak] = slovnik_cetnost[znak]+1
        else:
            slovnik_cetnost[znak] = 1
    return(slovnik_cetnost)

def soubor_vystup(slovnik_cetnost_out):
    """Vytvori ve zdrojove slozce soubor cetnosti_znaku.txt, obsahujici vypsane cetnosti 
    znaku z globalniho vstupu.
    
    Vstup: slovnik (dict) se znaky a jejich cetnostmi. Cetnost (int) kazdeho znaku textu pod klicem tohoto znaku (napr. 'a': 12).

    Vystup: textovy soubor (.txt) do zdrojove do složky. Do programu funkce nic nevraci.
    """
    with open('cetnosti_znaku.txt', mode='w', encoding='utf-8') as output:
        for znak_klic,znak_pocet in slovnik_cetnost_out.items():
            pocet = f"Počet '{znak_klic}' v souboru je {znak_pocet}."
            print(pocet, file=output)


# >> PROGRAM <<
text = nacteni('vstupni_soubor.txt')
cetnost = cetnost(text)
soubor_vystup(cetnost)