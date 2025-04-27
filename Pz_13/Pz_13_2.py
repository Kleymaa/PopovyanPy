#В двумерном списке все элементы, не лежащие на главной диагонали увеличить в 2
#раза.

def diagonal(matrix):
    # Используем map для обработки каждой строки с учётом индекса строки
    return list(map(
        lambda row: list(map(
            lambda item: item[1] * 2 if item[0] != row[0] else item[1],
            enumerate(row)
        )),
        enumerate(matrix)
    ))

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
result = diagonal(matrix)
for row in result:
    print(row)