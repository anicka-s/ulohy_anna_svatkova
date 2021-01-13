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


# >> PROGRAM <<
hodnoty1 = nacteni('hodnoty1.txt')
hodnoty2 = nacteni('hodnoty2.txt')
seznam1 = [float(hodnota) for hodnota in hodnoty1.split(' ')]
seznam2 = [float(hodnota) for hodnota in hodnoty2.split(' ')]

prunik = prunik(seznam1,seznam2)

# TODO: Sort output?
# TODO: Ulozeni vystupu do .txt souboru
print(prunik)
