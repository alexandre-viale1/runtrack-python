def multiple(L):
    i = 0
    for x in L:
        if ( x%3 == 0):
            i=i+1
    print(i)
L = [8, 24,48,2,16]
print(multiple(L))
