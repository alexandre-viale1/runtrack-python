def draw_rectangle(width, height):
  for i in range(height):
    if i == 0:
        print("-" * width)
    print("|" + " " * (height) + "|")
print(draw_rectangle(10,5))