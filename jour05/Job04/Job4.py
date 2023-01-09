L=['a', 'b', 'c', 'd', "e", "f", "g", "h","i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y","z" ]
for x in range(len(L)):
    L.append(L[x])
message = input("Entrez le message: ")
décalage = int(input("Entrez le décalage: "))
def chiffrage(lettre,L,décalage):
    for i in range(len(L)):
        if L[i]==lettre:
            return str(L[i+décalage])
message_chiffré = str()
for lettre in message:
    message_chiffré += chiffrage(lettre,L,décalage)
print(message_chiffré)