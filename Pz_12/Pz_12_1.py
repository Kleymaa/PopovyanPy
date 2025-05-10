#В последовательности на n целых элементов в последней ее половине найти
#сумму элементов.

from functools import reduce
import random

def sum_last_half(sequence):
    half_length = len(sequence) // 2
    last_half = sequence[half_length:]
    return reduce(lambda x, y: x + y, last_half)

user_input = input("Введите последовательность целых чисел через пробел: ").strip()

#Генерация 
random_length = random.randint(5, 10)
random_numbers = [random.randint(1, 100) for _ in range(random_length)]
random_result = sum_last_half(random_numbers)
print("\nСлучайный список:", random_numbers)
print("Сумма второй половины (случайный список):", random_result)

#Обработка пользовательского 
if user_input == "":
    print("\nИспользуется случайный список, так как ввод пуст.")
else:
    try:
        user_numbers = list(map(int, user_input.split()))
        if len(user_numbers) == 0:
            print("Ошибка: не введено ни одного числа!")
        else:
            user_result = sum_last_half(user_numbers)
            print("\nСумма второй половины списка:", user_result)
    except ValueError:
        print("Ошибка: введите только целые числа, разделенные пробелами!")


