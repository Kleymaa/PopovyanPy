#В последовательности на n целых элементов в последней ее половине найти
#сумму элементов.

from functools import reduce
import random

def sum_last_half(sequence):
    half_length = len(sequence) // 2
    last_half = sequence[half_length:]
    return reduce(lambda x, y: x + y, last_half)

user_input = input("Введите любые числа через пробел: ")
numbers = list(map(int, user_input.split()))
result = sum_last_half(numbers)
print("Сумма второй половины (введённый список):", result)

random_length = random.randint(5, 10)
random_numbers = [random.randint(1, 100) for _ in range(random_length)]
random_result = sum_last_half(random_numbers)
print("\nСлучайный список:", random_numbers)
print("Сумма второй половины (случайный список):", random_result)
