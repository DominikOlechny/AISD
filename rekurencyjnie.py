def nwd(a, b):
    if b > 0:
        return nwd(b, a%b)
    else:
        return a
print(nwd(12,18))
print(nwd(28,24))