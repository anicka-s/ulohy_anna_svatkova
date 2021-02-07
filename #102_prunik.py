# #102 - PRUNIK POSLOUPNOSTI (intersection of sequences)
# Anna Svatkova, 3.BFGG, 2021

import os
import re

# >> FUNCTIONS <<
def data_load(file_name):
    """Loads file content, removes whitespaces from both ends, resolves input file errors.
    
    In case of unusable input the program is terminated. Termination occurs in case of these errors:
    non-existent input file, too large input file (>50MB), empty input file, unable to access input file
    (read), unreadable input file.
    Structure-checking function included.

    Input: file name (with extension)

    Output: data from file (str).
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
    """Checks if the string has a structure of sequence of real numbers.
    
    Separator is one space; decimal dot must be used. Negative numbers with '-'.
    Error in structure leads to termination. Valid structure lets the program continue.
    No outputs.

    Input: string consisting of a sequence of real numbers separated by a space
    and a name of source file (str).
    """
    structure = r"^(-?\d+(\.\d+)?)( -?\d+(\.\d+)?)*$"
    if re.match(structure,string) is None:
        print(f"Vstupní soubor {soubor} nemá validní strukturu.")
        exit()

def inters(list_values1,list_values2):
    """Finds values which are in both input lists.
    
    Input: two lists of values (list, list).

    Output: list of values (list).
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
    """Creates a file with name prunik_posloupnosti.txt in source folder, containing data info
    and a list of intersecting numbers of two global input sequences.
    
    Input: list of intersecting values.

    Output: text file (.txt) into source folder. No in-program outputs.
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