# #102 - PRUNIK POSLOUPNOSTI
# Anna Svatkova, 3.BFGG, 2021

import os
import re

# >> FUNKCE <<
def nacteni(nazev_souboru):
    """Nacte soubor, odstrani z obou koncu bile znaky, osetri souborove chyby vstupu.
    
    V pripade nepouzitelneho vstupu ukonci program. Ukonceni programu pri nasledujicich
    chybach: neexistujici vstupni soubor, prazdny vstupni soubor, nepovolen přistup k vstupnimu
    souboru (pravo cteni).
    Soucasti je i funkce pro kontrolu struktury.

    Vstup: nazev souboru (s priponou .txt).

    Vystup: data ze souboru (str).
    """
    if os.path.exists(nazev_souboru):
        if os.path.getsize(nazev_souboru) > 0:
            try:
                with open(nazev_souboru, mode='r', encoding='utf-8') as data:
                    hodnoty = str(data.read()).strip()
                    kontrola_struktury(hodnoty,nazev_souboru)
                    return(hodnoty)
            except PermissionError:
                print(f"Ke vstupnímu souboru {nazev_souboru} není povolen přístup.")
                exit()
        else:
            print(f"Vstupní soubor {nazev_souboru} je prázdný.")
            exit()
    else:
        print(f"Vstupní soubor {nazev_souboru} chybí.")
        exit()

def kontrola_struktury(retezec,soubor):
    """Proveri, zda je retezec ve formatu posloupnosti realnych cisel.
    
    Oddelovacem je jedna mezera; pro desetinna cisla musi byt pouzita desetinna tecka,
    nikoliv carka. Zapornym cislum musi predchazet '-' (minus, pomlcka).
    V pripade nalezeni chyby ve strukture vstupu se program ukonci. V pripade validni
    struktury program neni prerusen, funkce do programu nic nevraci.

    Vstup: retezec (str) posloupnosti realnych cisel oddelovanych mezerou a nazev zdrojoveho souboru (str).
    """
    struktura = r"^(-?\d+(\.\d+)?)( -?\d+(\.\d+)?)*$"
    if re.match(struktura,retezec) is None:
        print(f"Vstupní soubor {soubor} nemá validní strukturu.")
        exit()
        

def prunik(seznam_hodnot1,seznam_hodnot2):
    """Nalezne hodnoty (prvky), ktere jsou zaroven v obou dvou vstupnich seznamech.
    
    Vstup: dva seznamy hodnot (list, list).

    Vystup: seznam hodnot (list) spolecnych pro oba vstupni seznamy.
    """
    seznam_hodnot1.sort()
    seznam_hodnot2.sort()
    seznam_prunik = []
    i = 0
    j = 0
    while not seznam_hodnot1[i] == seznam_hodnot1[len(seznam_hodnot1)-1] or not seznam_hodnot2[j] == seznam_hodnot2[len(seznam_hodnot2)-1]:
        if seznam_hodnot1[i] > seznam_hodnot2[j]:
            j += 1
        elif seznam_hodnot1[i] < seznam_hodnot2[j]:
            i += 1
        elif seznam_hodnot1[i] not in seznam_prunik: # i = j
            seznam_prunik.append(seznam_hodnot1[i])
            i += 1
            j += 1
    return(seznam_prunik)

def soubor_vystup(vystupni_soubor):
    """Vytvori ve zdrojove slozce soubor prunik_posloupnosti.txt, obsahujici popis dat a
    seznam pruniku prvku dvou posloupnosti z globalnich vstupu.
    
    Vstup: seznam (list) pruniku hodnot.

    Vystup: textovy soubor (.txt) do zdrojove do složky. Do programu funkce nic nevraci.
    """
    with open('prunik_posloupnosti.txt', mode='w', encoding='utf-8') as output:
        print("Průnikem posloupností ze vstupních souborů jsou následující hodnoty:",vystupni_soubor, file=output)


# >> PROGRAM <<
hodnoty1 = nacteni('hodnoty1_cisla.txt')
hodnoty2 = nacteni('hodnoty2_cisla.txt')
# tvorba seznamu z posloupnosti
seznam1 = [float(hodnota) for hodnota in hodnoty1.split(' ')]
seznam2 = [float(hodnota) for hodnota in hodnoty2.split(' ')]
prunik_posloupnosti = prunik(seznam1,seznam2)
prunik_posloupnosti.sort()
soubor_vystup(prunik_posloupnosti)