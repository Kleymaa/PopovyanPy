#В двумерном списке все элементы, не лежащие на главной диагонали увеличить в 2
#раза.

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

Aboba = list(map(lambda a: list(map(lambda b: matrix[a][b] * 2 if a != b else matrix[a][b], range(len(matrix[a])))), range(len(matrix))))

for row in Aboba:
    print(row)
