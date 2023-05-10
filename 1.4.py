tablica = [1,2,-3,4,5,6]

minimalna_wartosc = tablica[0]

for wartosc in tablica:
    if wartosc < minimalna_wartosc:
        minimalna_wartosc = wartosc

print("Minimalna wartość w tablicy to:", minimalna_wartosc)