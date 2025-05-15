#В двумерном списке найти максимальный положительный элемент, кратный 4.

import random

# Создаем двумерный список (матрицу) случайных чисел
randomed = [[random.randint(-20, 20) for i in range(4)] for j in range(4)]

print("Исходная матрица:")
for row in randomed:
    print(row)

elements = [num for row in randomed for num in row if num > 0 and num % 4 == 0]

if not elements:
    print("В матрице нет положительных элементов, кратных 4.")
else:
    max_element = max(elements)
    print(f"Максимальный положительный элемент, кратный 4: {max_element}")
