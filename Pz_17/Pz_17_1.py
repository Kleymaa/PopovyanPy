#Взял с ссылки Варианта 25

import tkinter as tk
from tkinter import ttk, filedialog


def create_application_form():
    root = tk.Tk()
    root.title("Форма заявки")

    # Основные элементы формы
    header = ttk.Label(root, text="Форма заявки", font=('Arial', 14, 'bold'))
    header.grid(row=0, column=0, columnspan=2, pady=10)

    # Информация о файлах
    file_info = ttk.Label(root, text="Допустимые типы вложений: zip, rar, txt, doc, jpg, png, gif, odt, xml\n"
                                     "Макс. размер каждого файла: 1024kb.\n"
                                     "Макс. общий размер файла: 2048kb.", justify=tk.LEFT)
    file_info.grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky=tk.W)

    # Поля формы
    fields = [
        ("Ваше имя:", "*", 2),
        ("Ваш Email:", "*", 3),
        ("Тема письма:", "", 4),
    ]

    entries = []
    for label_text, required, row in fields:
        label = ttk.Label(root, text=label_text)
        label.grid(row=row, column=0, padx=10, pady=5, sticky=tk.E)

        entry = ttk.Entry(root, width=40)
        entry.grid(row=row, column=1, padx=10, pady=5, sticky=tk.W)
        entries.append(entry)

        if required:
            req_label = ttk.Label(root, text=required)
            req_label.grid(row=row, column=2, padx=5, sticky=tk.W)

    # Поля для прикрепления файлов
    file_buttons = []
    for i, row in enumerate([5, 6, 7]):
        label = ttk.Label(root, text="Прикрепить файл:")
        label.grid(row=row, column=0, padx=10, pady=5, sticky=tk.E)

        btn = ttk.Button(root, text="Обзор", command=lambda r=row: browse_file(r))
        btn.grid(row=row, column=1, padx=10, pady=5, sticky=tk.W)
        file_buttons.append(btn)

    # Поле сообщения
    msg_label = ttk.Label(root, text="Ваше сообщение: *")
    msg_label.grid(row=8, column=0, padx=10, pady=5, sticky=tk.NE)

    msg_text = tk.Text(root, width=40, height=10)
    msg_text.grid(row=8, column=1, padx=10, pady=5, sticky=tk.W)

    # Кнопки
    send_btn = ttk.Button(root, text="Отправить Email")
    send_btn.grid(row=9, column=0, columnspan=2, pady=10)

    clear_btn = ttk.Button(root, text="Отчистить")
    clear_btn.grid(row=10, column=0, columnspan=2, pady=5)

    def browse_file(row):
        file_path = filedialog.askopenfilename()
        if file_path:
            # Здесь можно добавить логику проверки файла
            print(f"Выбран файл для строки {row}: {file_path}")

    root.mainloop()


if __name__ == "__main__":
    create_application_form()