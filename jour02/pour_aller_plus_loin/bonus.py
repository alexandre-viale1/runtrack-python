def triangle_type(a, b, c):
  if a + b > c and a + c > b and b + c > a:
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        return "triangle rectangle"
    elif a == b and b == c:
        return "triangle equilatéral"
    else:
        if a == b or a == c or b == c:
            return "triangle isosèle"
        else:
            return "triangle quelconque"
  else:
    return "pas un triangle"


print(triangle_type(10,20,31))