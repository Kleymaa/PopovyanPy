#Постановка задачи.
#С помощью функций получить вертикальную и горизонтальную линии. Линия проводится многократной печатью символа. Заключить слово в рамку из полученных линий.


#Блок обработки ввода и проверки значения.
try: 
    #Функция h(l) выводит горизонтальную линию из символов + и -
    def h(l):
        print('+' + '-' * l + '+')
    #Функция v(s) выводит строку, обрамлённую символами |
    def v(s):
        print(f'|{s}|')
    #Получаем ввод от пользователя
    num1 = input("Введите слово: ")
    #Определяем длину слова для расчета ширины рамки
    num2 = len(num1) + 2  # Добавляем 2 пробела по бокам
    #Печатаем верхнюю границу рамки
    h(num2)
    #Печатаем середину рамки с введенным словом.
    v(num1)
    #Печатаем нижнюю границу рамки
    h(num2)
except ValueError:
    #Сообщение об ошибке, если введено некорректное значение.
    print("Ошибка: введено некорректное значение")
