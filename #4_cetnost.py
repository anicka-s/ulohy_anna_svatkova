# >> FUNKCE <<
def nacteni(nazev_souboru):
    # TODO: Docstring
    # TODO: Osetreni chybnych vstupu - souborove chyby...
    with open(nazev_souboru, mode='r', encoding='utf-8') as data:
        vstupni_text = str(data.read())
    return(vstupni_text)

def rozdeleni(retezec):
    # TODO: Docstring
    seznam_prvku = retezec.split()
    seznam_znaku = []
    for prvek in seznam_prvku:
        for znak in prvek:
            seznam_znaku.append(znak)
    return(seznam_znaku)

def cetnost(seznam_vsech_znaku):
    # TODO: Docstring
    slovnik_cetnost = {}
    for znak in seznam_vsech_znaku:
        if znak in slovnik_cetnost.keys():
            slovnik_cetnost[znak] = slovnik_cetnost[znak]+1
        else:
            slovnik_cetnost[znak] = 1
    return(slovnik_cetnost)


# >> PROGRAM <<
text = nacteni('vstupni_soubor.txt')
vsechny_znaky = rozdeleni(text)
cetnost = cetnost(vsechny_znaky)

# TODO: Sort output?
# TODO: Bile znaky?
# TODO: Ulozeni vystupu do .txt souboru
for znak_klic,znak_pocet in cetnost.items():
    print(f"Počet '{znak_klic}' v souboru je {znak_pocet}.")