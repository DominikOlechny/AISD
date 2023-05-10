def odwroc_tablice(tablica):
    if len(tablica) < 2:
        return tablica
    reszta_tablicy_odwrocona = odwroc_tablice(tablica[1:])
    reszta_tablicy_odwrocona.append(tablica[0])
    return reszta_tablicy_odwrocona
tablica = [1,2,3,4,5]
print(odwroc_tablice(tablica))