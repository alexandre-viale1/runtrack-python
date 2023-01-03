def triangle_type(a, b, c):
  if a + b > c and a + c > b and b + c > a:
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        print("triangle rectangle") 
    elif a == b and b == c:
        print("triangle equilatéral") 
    else:
        if a == b or a == c or b == c:
            print("triangle isosèle") 
        else:
            print("triangle quelconque") 
  else:
    print("pas un triangle") 


print(triangle_type(10,20,2))