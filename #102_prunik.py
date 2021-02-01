# >> FUNKCE <<
def nacteni(nazev_souboru):
    # TODO: Docstring
    # TODO: Osetreni chybnych vstupu - souborove chyby, vstupy nejsou cisla...
    with open(nazev_souboru, mode='r', encoding='utf-8') as data:
        hodnoty = data.read()
    return(hodnoty)

def prunik(seznam_hodnot1,seznam_hodnot2):
    # TODO: Docstring
    seznam_prunik = []
    for cislo in seznam_hodnot1:
        if cislo in seznam_hodnot2:
            if cislo not in seznam_prunik:
                seznam_prunik.append(cislo)
    return(seznam_prunik)

# vyjimky:
# osetreni souboru: neexistujici/prazdny/nepristupny vstupni soubor
# neoddeleno mezerami: if neobsahuje ' '
# des. carka nebo oddeleno carkami: if cislo obsahuje carku, nahradit teckou (-> rozlozi cyklus nize)
# nebo vseobecne: pokud obsahuje soubor cokoliv jineho, nez cislice, tecky nebo mezery -> ukonceni (chyba formatu)
# obecne osetreni erroru


# >> PROGRAM <<
hodnoty1 = nacteni('hodnoty1.txt')
hodnoty2 = nacteni('hodnoty2.txt')
# TODO: Vstup oddeleni carkou osetrit
seznam1 = [float(hodnota) for hodnota in hodnoty1.split(' ')]
seznam2 = [float(hodnota) for hodnota in hodnoty2.split(' ')]

prunik_posloupnosti = prunik(seznam1,seznam2)
prunik_posloupnosti.sort()

with open('prunik_posloupnosti.txt', mode='w', encoding='utf-8') as output:   # w jako write >>> mode='a' -> append, tedy připojit na konec souboru
    print(prunik_posloupnosti, file=output)