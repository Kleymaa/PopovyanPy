#В двумерном списке все элементы, не лежащие на главной диагонали увеличить в 2
#раза.

import random

randomed = [[random.randint(-5, 5) for i in range(3)] for j in range(3)]

print("Исходная матрица:")
for i in randomed:
    print(i)

randomed = list(map(lambda a:
                    [x * 2 if a[0] != j else x
                    for j, x in enumerate(a[1])],
                   enumerate(randomed)))

print("Конечная матрица:")
for i in randomed:
    print(i)
