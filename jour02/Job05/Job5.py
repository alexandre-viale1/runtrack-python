def calcule(num1, operator, num2):
  if operator == "+":
    return num1 + num2
  elif operator == "-":
    return num1 - num2
  elif operator == "*":
    return num1 * num2
  elif operator == "/":
    return num1 / num2
  elif operator == "%":
    return num1 % num2

result = calcule(10,"+",10)
print(result)

result = calcule(8,"-",4)
print(result)

result = calcule(8,"*",4)
print(result)

result = calcule(8,"/",4)
print(result)

result = calcule(50,"%",100)
print(result)