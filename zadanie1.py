import math

a = int(input("a"))
b = int(input("b"))
c = int(input("c"))
if a != 0:
    delta = b * b - 4 * a * c
    if delta > 0:
        x1 = (-b - math.sqrt(delta)) / (2 * a)
        x2 = (-b + math.sqrt(delta)) / (2 * a)
        print(x1, x2)
    elif delta == 0:
        x1 = -b / (2 * a)
        print(x1)
    else:
        print("brak rozwiazań rzecztwistych")
else:
    print("brak rozw")
