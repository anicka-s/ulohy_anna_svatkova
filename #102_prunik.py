
seznam1 = [5,3,4,8,2,2,6,5,8,5]
seznam2 = [2,1,1,1,1,5,8,9,9,9,1,2]
seznam_prunik = []

for cislo in seznam1:
    if cislo in seznam2:
        if cislo not in seznam_prunik:
            seznam_prunik.append(cislo)


print(seznam_prunik)