#Средствами языка Python сформировать два текстовых файла (.txt), содержащих по одной
#последовательности из целых положительных и отрицательных чисел. Сформировать
#новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
#обработку элементов:
#Содержимое первого файла:
#Четные элементы:
#Произведение четных элементов:
#Минимальный элемент:
#Содержимое второго файла:
#Нечетные элементы:
#Количество нечетных элементов:
#Сумма нечетных элементов:

import random
def create_file(filename, numbers):
    with open(filename, 'w', encoding='utf-8') as file:  # Явно указываем UTF-8
        file.write(' '.join(map(str, numbers)))
def read_numbers(filename):
    with open(filename, 'r', encoding='utf-8') as file:  # Читаем в UTF-8
        content = file.read()
        return list(map(int, content.split()))
# Создаем первый файл со случайными числами
numbers1 = [random.randint(-100, 100) for _ in range(10)]
create_file('file1.txt', numbers1)
# Создаем второй файл со случайными числами
numbers2 = [random.randint(-100, 100) for _ in range(10)]
create_file('file2.txt', numbers2)
# Читаем числа из файлов
nums1 = read_numbers('file1.txt')
nums2 = read_numbers('file2.txt')
# Обработка первого файла
even_elements = [num for num in nums1 if num % 2 == 0]
product_even = 1
for num in even_elements:
    product_even *= num
min_element = min(nums1)
# Обработка второго файла
odd_elements = [num for num in nums2 if num % 2 != 0]
count_odd = len(odd_elements)
sum_odd = sum(odd_elements)
# Создаем итоговый файл с результатами
with open('result.txt', 'w', encoding='utf-8') as result_file:
    result_file.write("Содержимое первого файла:\n")
    result_file.write(f"Четные элементы: {', '.join(map(str, even_elements))}\n")
    result_file.write(f"Произведение четных элементов: {product_even}\n")
    result_file.write(f"Минимальный элемент: {min_element}\n\n")
    result_file.write("Содержимое второго файла:\n")
    result_file.write(f"Нечетные элементы: {', '.join(map(str, odd_elements))}\n")
    result_file.write(f"Количество нечетных элементов: {count_odd}\n")
    result_file.write(f"Сумма нечетных элементов: {sum_odd}\n")
