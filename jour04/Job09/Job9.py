def minmax(L):
    L.sort()
    print(L[0],L[-1])
L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]
print(minmax(L))