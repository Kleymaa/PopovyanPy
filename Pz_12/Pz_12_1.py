#В последовательности на n целых элементов в последней ее половине найти
#сумму элементов.

from functools import reduce
def sum_last_half(sequence):
    half_length = len(sequence) // 2
    last_half = sequence[half_length:]
    return reduce(lambda x, y: x + y, last_half)

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
result = sum_last_half(numbers)
print(result)