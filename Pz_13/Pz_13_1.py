#В двумерном списке найти максимальный положительный элемент, кратный 4.

from itertools import chain
def find_4(matrix):
    # Преобразуем матрицу в плоский список
    flattened = chain.from_iterable(matrix)
    # Фильтруем элементы: положительные и кратные 4
    filtered = filter(lambda x: x > 0 and x % 4 == 0, flattened)
    # Находим максимальный элемент (если таких нет, вернётся None)
    return max(filtered, default=None)

matrix = [
    [1, -8, 12],
    [5, 16, 0],
    [9, -4, 8]
]
result = find_4(matrix)
print(result)