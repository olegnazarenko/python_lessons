squares = []
mynumbers = list (range(1,11))
print(mynumbers)

for v in mynumbers:
   square = v**2
   squares.append(square)
print(squares)
print(sum(squares))

squares5 = [value**2 for value in range(1,11)]
print(squares5)

