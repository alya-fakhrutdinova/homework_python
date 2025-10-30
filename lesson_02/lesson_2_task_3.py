import math
def square(side):
    area = side * side
    return math.ceil(area)
num_side = float(input("Введите сторону квадрата: "))
print(f"Площадь квадрата: {square(num_side)}")