#Постановка задачи:
#Дана строка, изображающая арифметическое выражение вида «<цифра>±<цифра>±.. .±<цифра>»,
#где на месте знака операции «±» находится символ «+» или «-» (например, «4+7-2—8»). Вывести значение данного выражения (целое число).



def evaluate(expression):
    total = 0
    current_number = ""
    last_operator = "+"

    for i, char in enumerate(expression):
        if char.isdigit() or (char == '-' and (i == 0 or expression[i - 1] in "+-")):
            current_number += char
        elif char in "+-":
            if current_number == "":
                raise ValueError("Некорректное выражение!")

            number = int(current_number)
            if last_operator == "+":
                total += number
            elif last_operator == "-":
                total -= number

            current_number = ""
            last_operator = char
        else:
            raise ValueError("Некорректное выражение!")

    if current_number != "":
        number = int(current_number)
        if last_operator == "+":
            total += number
        elif last_operator == "-":
            total -= number
    else:
        raise ValueError("Некорректное выражение!")

    return total


expression = input('Введите выражение: ')
print('Результат:', evaluate(expression))
