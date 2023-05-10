def nwd(a, b):
    while b:
        a, b = b, a%b
    return a
print(nwd(12,18))
print(nwd(28,24))