for i in range(2,1000):
    nombre_premier=0
    for j in range(2,i):
        if i%j==0:
         nombre_premier=1
    if nombre_premier==0:
        print(i)    