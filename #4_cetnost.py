# #4 - VYPOCET CETNOSTI (calculation of frequencies)
# Anna Svatkova, 3.BFGG, 2021

import os

# >> FUNCTIONS <<
def data_load():
    """Nacte soubor uzivatelem zadaneho nazvu, osetri souborove chyby vstupu.
    
    V pripade nepouzitelneho vstupu ukonci program. Ukonceni programu pri nasledujicich
    chybach: neexistujici vstupni soubor, prazdny vstupni soubor, nepovolen přistup k vstupnimu
    souboru (pravo cteni).

    Vystup: data ze souboru (str).
    """
    file_name = input('Zadejte jméno vstupního souboru včetne přípony:\n')
    if os.path.exists(file_name):
        if os.path.getsize(file_name) > 0:
            try:
                with open(file_name, mode='r', encoding='utf-8') as data:
                    input_text = str(data.read())
                    return(input_text)
            except PermissionError:
                print(f"Ke vstupnímu souboru {file_name} není povolen přístup.")
                exit()
        else:
            print(f"Vstupní soubor {file_name} je prázdný.")
            exit()
    else:
        print(f"Vstupní soubor {file_name} chybí.")
        exit()

def char_frequency(vstup):
    """Spocita cetnosti polozek vstupu (str,list) a vypise je do slovniku.

    Vstup: seznam (list) jednotlivych znaku/prvku nebo řetězec (str).

    Vystup: slovnik (dict) se znaky a jejich cetnostmi. Cetnost (int) kazdeho znaku textu pod klicem tohoto znaku (napr. 'a': 12).
    """
    frequency_dict = {}
    for char in vstup:
        if char in frequency_dict.keys():
            frequency_dict[char] = frequency_dict[char]+1
        else:
            frequency_dict[char] = 1
    return(frequency_dict)

def file_output(frequency_dict_out):
    """Vytvori ve zdrojove slozce soubor cetnosti_znaku.txt, obsahujici vypsane cetnosti 
    znaku z globalniho vstupu.
    
    Vstup: slovnik (dict) se znaky a jejich cetnostmi. Cetnost (int) kazdeho znaku textu pod klicem tohoto znaku (napr. 'a': 12).

    Vystup: textovy soubor (.txt) do zdrojove do složky. Do programu funkce nic nevraci.
    """
    with open('cetnosti_znaku.txt', mode='w', encoding='utf-8') as output:
        for char_key,char_count in frequency_dict_out.items():
            count = f"Počet '{char_key}' v souboru je {char_count}."
            print(count, file=output)


# >> PROGRAM <<
text = data_load()
char_frequency = char_frequency(text)
file_output(char_frequency)