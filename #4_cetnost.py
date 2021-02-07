# #4 - VYPOCET CETNOSTI (calculation of frequencies)
# Anna Svatkova, 3.BFGG, 2021

import os

# >> FUNCTIONS <<
def data_load():
    """Loads content of user defined file, resolves input file errors.
    
    In case of unusable input the program is terminated. Termination occurs in case of these errors:
    non-existent input file, too large input file (>50MB), empty input file, unable to access input file
    (read), unreadable input file.

    Output: data from file (str).
    """
    file_name = input('Zadejte jméno vstupního textového souboru včetne přípony (.txt):\n')
    if os.path.exists(file_name): # file existence
        if os.path.getsize(file_name) > 50000000: # 50 megabytes > filesize > 0
            print(f"Vstupní soubor {file_name} je příliš velký.")
            exit()
        elif os.path.getsize(file_name) > 0:
            try:
                with open(file_name, mode='r', encoding='utf-8') as data:
                    input_text = str(data.read())
                    return(input_text)
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

def char_frequency(vstup):
    """Counts the frequency of characters in input (str,list) and creates a list out of them.

    Input: list of characters/elements or a string.

    Output: dictionary with characters and their counts.
    Count (int) of each character of the text is under a key of that character (eg. 'a': 12).
    """
    frequency_dict = {}
    for char in vstup:
        if char in frequency_dict.keys():
            frequency_dict[char] = frequency_dict[char]+1
        else:
            frequency_dict[char] = 1
    return(frequency_dict)

def file_output(frequency_dict_out):
    """Creates a file with name cetnosti_znaku.txt in source folder, containing printed counts of characters of global input.
   
    Input: dictionary with characters and their counts.
    Count (int) of each character of the text is under a key of that character (eg. 'a': 12).

    Output: text file (.txt) into source folder. No in-program outputs.
    """
    with open('cetnosti_znaku.txt', mode='w', encoding='utf-8') as output:
        for char_key,char_count in frequency_dict_out.items():
            count = f"Počet '{char_key}' v souboru je {char_count}."
            print(count, file=output)


# >> PROGRAM <<
text = data_load()
char_frequency = char_frequency(text)
file_output(char_frequency)