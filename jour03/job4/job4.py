i = 1
while i <= 100:
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
    i = i + 1



for n in range(1,1000):
   if n > 1:
       for i in range(2,n):
           if (n % i) == 0:
               break
           else:
            print(n)