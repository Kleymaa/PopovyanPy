#Из предложенного текстового файла (text18-23.txt) вывести на экран его содержимое,
#количество знаков пунктуации в первых четырёх строках. Сформировать новый файл, в
#который поместить текст в стихотворной форме предварительно заменив символы верхнего
#регистра на нижний

import string
# Чтение исходного файла
with open('text18-23.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
# Вывод содержимого файла
print("Содержимое файла:")
print(''.join(lines))
# Подсчёт знаков пунктуации в первых 4 строках
punctuation = set(string.punctuation)  # Все знаки пунктуации
count = 0
for line in lines[:4]:
    count += sum(1 for char in line if char in punctuation)
print(f"\nКоличество знаков пунктуации в первых 4 строках: {count}")
# Создание нового файла с текстом в нижнем регистре
with open('lowercase_poem.txt', 'w', encoding='utf-8') as new_file:
    lowercase_lines = [line.lower() for line in lines]
    new_file.writelines(lowercase_lines)
print("\nФайл 'lowercase_poem.txt' создан, все буквы приведены к нижнему регистру.")
