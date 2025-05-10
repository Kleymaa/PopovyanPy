#В двумерном списке найти максимальный положительный элемент, кратный 4.

from functools import reduce

def find_max(matrix):
    # Преобразуем матрицу в плоский список
    flattened = reduce(lambda acc, row: acc + row, matrix, [])

    # Филь. + элем. кратные 4
    filtered = filter(lambda x: x > 0 and x % 4 == 0, flattened)

    #Поиск макс. элемент
    try:
        return reduce(lambda a, b: a if a > b else b, filtered)
    except TypeError:
        return None

matrix = [
    [1, -8, 12],
    [4, 16, -3],
    [0, 5, 24]
]

result = find_max(matrix)
print(result)
