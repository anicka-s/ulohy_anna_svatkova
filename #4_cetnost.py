# >> FUNKCE <<
def nacteni(nazev_souboru):
    # TODO: Docstring
    # TODO: Osetreni chybnych vstupu - souborove chyby...
    with open(nazev_souboru, mode='r', encoding='utf-8') as data:
        vstupni_text = str(data.read())
    return(vstupni_text)


# >> PROGRAM <<
text = nacteni('vstupni_soubor.txt')


# TODO: Ulozeni vystupu do .txt souboru
print(text)