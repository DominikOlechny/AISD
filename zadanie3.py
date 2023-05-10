liczby = [1, 2, 3, 11, 21, 111, 231]
liczby = [str(x) for x in liczby]
for i in range(len(liczby)):
    for j in range(i+1, len(liczby)):
        if liczby[j] < liczby[i]:
            liczby[i], liczby[j] = liczby[j], liczby[i]
liczby = [int(x) for x in liczby]
print(liczby)