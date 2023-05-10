n = int(input("Podaj liczbę elementów ciągu: "))
while n<=0:
    n = int(input("Podaj prawidłowa liczbe cyfr w ciagu: "))
liczba = 0

for i in range(n):
    x = int(input(f"Podaj liczbę: "))
    if x < 0:
        liczba += 1

print(f"Ilość liczb ujemnych w ciągu: {liczba}")

