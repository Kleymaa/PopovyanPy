#Из исходного текстового файла (ip_address.txt) из раздела «Зарезервированные
#адреса» перенести в первый файл строки с ненулевыми первым и вторым октетами,
#а во второй – все остальные. Посчитать количество полученных строк в каждом
#файле.

import re

# Открываем исходный файл
with open('ip_address.txt', 'r') as file:
    lines = file.readlines()
# Подготовка файлов для записи
with open('nonzero_octets.txt', 'w') as nonzero_file, \
        open('other_ips.txt', 'w') as other_file:
    nonzero_count = 0
    other_count = 0
    for line in lines:
        # Ищем IP-адреса в строке (простейший паттерн)
        ip_match = re.search(r'\b(\d{1,3})\.(\d{1,3})\.\d{1,3}\.\d{1,3}\b', line)
        if ip_match:
            first_octet = int(ip_match.group(1))
            second_octet = int(ip_match.group(2))

            # Проверяем условие для ненулевых октетов
            if first_octet != 0 and second_octet != 0:
                nonzero_file.write(line)
                nonzero_count += 1
            else:
                other_file.write(line)
                other_count += 1
        else:
            # Если строка не содержит IP, записываем в other_file
            other_file.write(line)
            other_count += 1
print(f"Количество строк в nonzero_octets.txt: {nonzero_count}")
print(f"Количество строк в other_ips.txt: {other_count}")