def multiple(L):
    pair = 0
    for x in L:
        if ( x%2 == 0):
            pair = pair + x
            print(pair)
L = [8, 24, 27, 48, 2,16, 9, 7, 84, 91]

print(multiple(L))