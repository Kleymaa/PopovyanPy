import sqlite3
from datetime import datetime
from tabulate import tabulate


# Создание и подключение к базе данных
def create_database():
    conn = sqlite3.connect('car_rental.db')
    cursor = conn.cursor()

    # Создание таблицы Клиенты
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Clients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT NOT NULL,
        car_brand TEXT NOT NULL,
        rental_period INTEGER NOT NULL,
        total_amount REAL NOT NULL,
        prepayment TEXT NOT NULL,
        rental_date TEXT DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    conn.commit()
    conn.close()


# Добавление нового клиента
def add_client():
    conn = sqlite3.connect('car_rental.db')
    cursor = conn.cursor()

    print("\nДобавление нового клиента:")
    full_name = input("ФИО клиента: ")
    car_brand = input("Марка автомобиля: ")
    rental_period = int(input("Срок проката (дни): "))
    total_amount = float(input("Сумма проката: "))
    prepayment = input("Предоплата (да/нет): ").lower()

    cursor.execute('''
    INSERT INTO Clients (full_name, car_brand, rental_period, total_amount, prepayment)
    VALUES (?, ?, ?, ?, ?)
    ''', (full_name, car_brand, rental_period, total_amount, prepayment))

    conn.commit()
    conn.close()
    print("Клиент успешно добавлен!")


# Просмотр всех клиентов
def view_clients():
    conn = sqlite3.connect('car_rental.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM Clients')
    clients = cursor.fetchall()

    if not clients:
        print("\nНет данных о клиентах.")
    else:
        headers = ["ID", "ФИО", "Марка авто", "Срок проката (дни)", "Сумма", "Предоплата", "Дата проката"]
        print("\nСписок клиентов:")
        print(tabulate(clients, headers=headers, tablefmt="grid"))

    conn.close()


# Поиск клиента по ФИО
def search_client():
    conn = sqlite3.connect('car_rental.db')
    cursor = conn.cursor()

    search_name = input("\nВведите ФИО или часть ФИО для поиска: ")
    cursor.execute('SELECT * FROM Clients WHERE full_name LIKE ?', (f'%{search_name}%',))
    clients = cursor.fetchall()

    if not clients:
        print("Клиенты не найдены.")
    else:
        headers = ["ID", "ФИО", "Марка авто", "Срок проката (дни)", "Сумма", "Предоплата", "Дата проката"]
        print("\nРезультаты поиска:")
        print(tabulate(clients, headers=headers, tablefmt="grid"))

    conn.close()


# Удаление клиента
def delete_client():
    conn = sqlite3.connect('car_rental.db')
    cursor = conn.cursor()

    view_clients()
    client_id = input("\nВведите ID клиента для удаления: ")

    cursor.execute('DELETE FROM Clients WHERE id = ?', (client_id,))
    conn.commit()

    if cursor.rowcount > 0:
        print("Клиент успешно удален!")
    else:
        print("Клиент с таким ID не найден.")

    conn.close()


# Генерация отчета
def generate_report():
    conn = sqlite3.connect('car_rental.db')
    cursor = conn.cursor()

    # Общая статистика
    cursor.execute('SELECT COUNT(*) FROM Clients')
    total_clients = cursor.fetchone()[0]

    cursor.execute('SELECT SUM(total_amount) FROM Clients')
    total_revenue = cursor.fetchone()[0] or 0

    cursor.execute('SELECT COUNT(*) FROM Clients WHERE prepayment = "да"')
    prepaid_clients = cursor.fetchone()[0]

    print("\nОтчет по прокату автомобилей:")
    print(f"Общее количество клиентов: {total_clients}")
    print(f"Общая выручка: {total_revenue:.2f} руб.")
    print(f"Клиентов с предоплатой: {prepaid_clients}")

    # Популярные марки авто
    cursor.execute('''
    SELECT car_brand, COUNT(*) as count 
    FROM Clients 
    GROUP BY car_brand 
    ORDER BY count DESC
    ''')
    popular_brands = cursor.fetchall()

    print("\nПопулярные марки автомобилей:")
    for brand, count in popular_brands:
        print(f"{brand}: {count} прокатов")

    conn.close()


# Основное меню
def main_menu():
    create_database()

    while True:
        print("\n=== ПРОКАТ АВТОМОБИЛЕЙ ===")
        print("1. Добавить нового клиента")
        print("2. Просмотреть всех клиентов")
        print("3. Поиск клиента")
        print("4. Удалить клиента")
        print("5. Сформировать отчет")
        print("0. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            add_client()
        elif choice == "2":
            view_clients()
        elif choice == "3":
            search_client()
        elif choice == "4":
            delete_client()
        elif choice == "5":
            generate_report()
        elif choice == "0":
            print("Работа программы завершена.")
            break
        else:
            print("Неверный ввод. Пожалуйста, попробуйте снова.")


# Запуск программы
if __name__ == "__main__":
    main_menu()