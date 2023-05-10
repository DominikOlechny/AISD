def dzies_na_2(n):
    if n == 0:
        return 0
    else:
        return (n % 2) + 10 * dzies_na_2(n // 2)
print(dzies_na_2(20))