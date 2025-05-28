#Из исходного текстового файла (ip_address.txt) из раздела «Зарезервированные
#адреса» перенести в первый файл строки с ненулевыми первым и вторым октетами,
#а во второй – все остальные. Посчитать количество полученных строк в каждом
#файле.

import re
from functools import reduce


def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()


def extract_reserved_blocks(text):
    pattern = r'Зарезервированные адреса.*?(Подсеть.*?Назначение.*?)(?:\n\s*\n|\Z)'
    match = re.search(pattern, text, re.DOTALL)
    if not match:
        return []
    table = match.group(1)
    rows = re.findall(r'(\d+\.\d+\.\d+\.\d+/\d+).*?([^\n]+)', table)
    return rows


def split_rows(rows):
    def has_non_zero_first_two_octets(ip):
        octets = list(map(int, ip.split('/')[0].split('.')[:2]))
        return octets[0] != 0 and octets[1] != 0

    group1 = list(filter(lambda row: has_non_zero_first_two_octets(row[0]), rows))
    group2 = list(filter(lambda row: not has_non_zero_first_two_octets(row[0]), rows))
    return group1, group2


def write_to_file(filename, rows):
    with open(filename, 'w', encoding='utf-8') as file:
        for ip, desc in rows:
            file.write(f"{ip}\t{desc}\n")


def count_rows(rows):
    return len(rows)


def main():
    content = read_file('ip_address.txt')
    reserved_blocks = extract_reserved_blocks(content)
    group1, group2 = split_rows(reserved_blocks)

    write_to_file('non_zero_octets.txt', group1)
    write_to_file('other_octets.txt', group2)

    count_group1 = count_rows(group1)
    count_group2 = count_rows(group2)

    print(f"Количество строк в non_zero_octets.txt: {count_group1}")
    print(f"Количество строк в other_octets.txt: {count_group2}")


if __name__ == "__main__":
    main()
