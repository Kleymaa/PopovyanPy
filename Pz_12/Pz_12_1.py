#В последовательности на n целых элементов в последней ее половине найти
#сумму элементов.

from functools import reduce
import random

def sum_last_half(Aboba):
    half_length = len(Aboba) // 2
    last_half = Aboba[half_length:]
    return reduce(lambda x, y: x + y, last_half)

#Запрос
n = int(input("Введите количество целых элементов в последовательности: "))

#Генерирация
Aboba = [random.randint(1, 100) for _ in range(n)]

print("Сгенерированная последовательность:", Aboba)

#Вычисляем
result = sum_last_half(Aboba)
print("Сумма элементов во второй половине последовательности:", result)
