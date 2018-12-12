import math


def hyp(x, y):
    hypotenuse = math.sqrt((x)**2 + (y)**2)
    print(f"The hypotenuse is {hypotenuse}")


x = int(input("Choose a number for a side of a right triangle: "))
y = int(input("Choose another number for a side of a right triangle: "))
hyp(x, y)



