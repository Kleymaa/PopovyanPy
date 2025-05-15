#В двумерном списке все элементы, не лежащие на главной диагонали увеличить в 2
#раза.

import random

randomed = [[random.randint(-5, 5) for i in range(3)] for i in range(3)]

print("Исходная матрица")
for i in randomed:
    print(i)

#Увеличиваем, которые не на главной в 2 раза
for i in range(len(randomed)):
    for j in range(len(randomed[i])):
        if i != j:  #Элемент не на главной диагонали
            randomed[i][j] *= 2

print("Конечная матрица")
for i in randomed:
    print(i)
