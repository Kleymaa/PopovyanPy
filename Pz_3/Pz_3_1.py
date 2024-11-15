#Постановка задачи:
#Дано трехзначное число. Проверить истинность высказывания: «Цифры данного числа образуют возрастающую или убывающую


# Блок обработки ввода и проверки значения.
try:
    # Вводим число и сохраняем его в переменной x
    x = int(input("Введите число: "))

    # Проверка условий для арифметической прогрессии
    print('Цифры данного числа образуют арифметическую прогрессию.'
          #x2 - x1
          if (x // 100 - (x // 10) % 10) *
          #x3 - x2
             ((x // 10) % 10 - x % 10) >= 0
             #Проверяет, что первая и последняя цифры не равны друг другу.
             and x // 100 != x % 10
          else 'Цифры данного числа не образуют арифметическую прогрессию.')
# Обработка ошибки, если пользователь ввёл некорректное значение.
except ValueError:
    # Сообщение об ошибке, если введено некорректное значение
    print("Ошибка: введено некорректное значение. Пожалуйста, введите целое число.")
