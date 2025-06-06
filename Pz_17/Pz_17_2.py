# Pz_3_2
# Дано целое число. Если оно является положительным, то прибавить к нему 1; в противном случае вычесть из него 2. Вывести полученное число.

import tkinter as tk
from tkinter import ttk, messagebox


def number_processor():
    def process_number():
        try:
            num = int(entry.get())
            if num > 0:
                result = num + 1
            else:
                result = num - 2
            result_label.config(text=f"Результат: {result}")
        except ValueError:
            messagebox.showerror("Ошибка", "Пожалуйста, введите целое число")

    root = tk.Tk()
    root.title("Обработка числа")

    main_frame = ttk.Frame(root, padding="10")
    main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    label = ttk.Label(main_frame, text="Введите целое число:")
    label.grid(row=0, column=0, sticky=tk.W, pady=5)

    entry = ttk.Entry(main_frame, width=20)
    entry.grid(row=1, column=0, pady=5)

    process_btn = ttk.Button(main_frame, text="Обработать", command=process_number)
    process_btn.grid(row=2, column=0, pady=10)

    result_label = ttk.Label(main_frame, text="Результат: ")
    result_label.grid(row=3, column=0, pady=5)

    root.mainloop()


if __name__ == "__main__":
    number_processor()