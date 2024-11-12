#Даны целые положительные числа N и K. Найти сумму 1K + 2К + ... + NK.



try:
    n = int(input("Введите целое число n:"))
    k = int(input("Введите целое число k:"))
    a = 0
    for i in range(1, n+1):
        a += i**k
        print(a)
except ValueError:
    print("Ошибка: введено некорректное значение.")