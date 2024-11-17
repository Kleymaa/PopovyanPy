#Постановка задачи.
#Описать функцию TrianglePS(a, P, S), вычисляющую по стороне a равностороннего треугольника его периметр P = 3*a и площадь S = a2 √3/4 (a — входной, P и S — выходные параметры; все параметры являются вещественными). С помощью этой функции найти периметры и площади трех равносторонних треугольников с данными сторонами.


#Импортируем библиотеку math.
import math
#Функция принимает на вход одну переменную a, представляющую длину стороны равностороннего треугольника.
def my_def(a):
    # Вычисляем периметр по формуле.
    P = 3 * a
    # Вычисляем площадь по формуе.
    S = (a ** 2 * math.sqrt(3)) / 4
    #Оба результата возвращаются функцией.
    return P, S

#Блок обработки ввода и проверки значения
try:
    #Запришиваем у пользователя длину треугольника и преобразовываем в плавающую точку c float.
    num1 = float(input("Введите длину стороны равностороннего треугольника: "))
    #Если значение больше 0, то оно передается в num1ю.
    if num1 > 0:
        #Результаты выводятся на экран.
        P, S = my_def(num1)
        print(f"Периметр треугольника со стороной {num1}: {P:.2f}")
        print(f"Площадь треугольника со стороной {num1}: {S:.2f}\n")
    #Если значение меньше 0, выводится ошибка
    else:
        print("Ошибка: длина стороны должна быть положительной.")
#Сообщение об ошибке, если введено некорректное значение.
except ValueError:
    print("Ошибка: введено некорректное значение")