# #102 - PRUNIK POSLOUPNOSTI (intersection of sequences)
# Anna Svatkova, 3.BFGG, 2021

import os
import re

# >> FUNCTIONS <<
def data_load(file_name):
    """Nacte soubor, odstrani z obou koncu bile znaky, osetri souborove chyby vstupu.
    
    V pripade nepouzitelneho vstupu ukonci program. Ukonceni programu pri nasledujicich
    chybach: neexistujici vstupni soubor, prilis velky vstupni soubor (>50MB), prazdny vstupni soubor,
    nepovolen pristup k vstupnimu souboru (pravo cteni), necitelny vstupni soubor.
    Soucasti je i funkce pro kontrolu struktury.

    Vstup: nazev souboru (s priponou).

    Vystup: data ze souboru (str).
    """
    if os.path.exists(file_name): # file existence
        if os.path.getsize(file_name) > 50000000: # 50 megabytes > filesize > 0
            print(f"Vstupní soubor {file_name} je příliš velký.")
            exit()
        elif os.path.getsize(file_name) > 0:
            try:
                with open(file_name, mode='r', encoding='utf-8') as data:
                    values = str(data.read()).strip()
                    structure_check(values,file_name)
                    return(values)
            except PermissionError: # file accessibility
                print(f"Ke vstupnímu souboru {file_name} není povolen přístup.")
                exit()
            except UnicodeDecodeError: # binary exception
                print(f"Vstupní soubor {file_name} není čitelný.")
                exit()
        else:
            print(f"Vstupní soubor {file_name} je prázdný.")
            exit()
    else:
        print(f"Vstupní soubor {file_name} chybí.")
        exit()

def structure_check(string,soubor):
    """Proveri, zda je string ve formatu posloupnosti realnych cisel.
    
    Oddelovacem je jedna mezera; pro desetinna cisla musi byt pouzita desetinna tecka,
    nikoliv carka. Zapornym cislum musi predchazet '-' (minus, pomlcka).
    V pripade nalezeni chyby ve strukture vstupu se program ukonci. V pripade validni
    struktury program neni prerusen, funkce do programu nic nevraci.

    Vstup: string (str) posloupnosti realnych cisel oddelovanych mezerou a nazev zdrojoveho souboru (str).
    """
    structure = r"^(-?\d+(\.\d+)?)( -?\d+(\.\d+)?)*$"
    if re.match(structure,string) is None:
        print(f"Vstupní soubor {soubor} nemá validní strukturu.")
        exit()

def inters(list_values1,list_values2):
    """Nalezne values (prvky), ktere jsou zaroven v obou dvou vstupnich seznamech.
    
    Vstup: dva seznamy hodnot (list, list).

    Vystup: seznam hodnot (list) spolecnych pro oba vstupni seznamy.
    """
    list_values1.sort()
    list_values2.sort()
    list_inters = []
    i = 0
    j = 0
    while not list_values1[i] == list_values1[len(list_values1)-1] or not list_values2[j] == list_values2[len(list_values2)-1]:
        if list_values1[i] > list_values2[j]:
            j += 1
        elif list_values1[i] < list_values2[j]:
            i += 1
        elif list_values1[i] not in list_inters: # i = j
            list_inters.append(list_values1[i])
            i += 1
            j += 1
    return(list_inters)

def file_out(output_file):
    """Vytvori ve zdrojove slozce soubor prunik_posloupnosti.txt, obsahujici popis dat a
    seznam pruniku prvku dvou posloupnosti z globalnich vstupu.
    
    Vstup: seznam (list) pruniku hodnot.

    Vystup: textovy soubor (.txt) do zdrojove do složky. Do programu funkce nic nevraci.
    """
    with open('prunik_posloupnosti.txt', mode='w', encoding='utf-8') as output:
        print("Průnikem posloupností ze vstupních souborů jsou následující values:",output_file, file=output)


# >> PROGRAM <<
values1 = data_load('hodnoty1.txt')
values2 = data_load('hodnoty2.txt')
# creates list from the sequence
seznam1 = [float(item) for item in values1.split(' ')]
seznam2 = [float(item) for item in values2.split(' ')]
inters_of_seq = inters(seznam1,seznam2)
inters_of_seq.sort()
file_out(inters_of_seq)