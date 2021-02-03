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

def soubor_vystup(slovnik_cetnost_out):
    # TODO: Aktualizovat docstring
    """Vytvori ve zdrojove slozce soubor prunik_posloupnosti.txt, obsahujici seznam pruniku realnych
    cisel globalnich vstupu.
    
    Vstup: seznam (list) pruniku hodnot.

    Vystup: textovy soubor (.txt) do zdrojove do složky. Do programu funkce nic nevraci.
    """
    with open('cetnosti_znaku.txt', mode='w', encoding='utf-8') as output:
        for znak_klic,znak_pocet in slovnik_cetnost_out.items():
            pocet = f"Počet '{znak_klic}' v souboru je {znak_pocet}."
            print(pocet, file=output)


# >> PROGRAM <<
text = nacteni('vstupni_soubor.txt')
vsechny_znaky = rozdeleni(text)
cetnost = cetnost(vsechny_znaky)
soubor_vystup(cetnost)

# TODO: Sort output?
# TODO: Bile znaky?
