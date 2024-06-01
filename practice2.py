import tkinter as tk
from tkinter import messagebox

# Функция шифрования и дешифровки
def caesar_cipher(user, key, decrypt=False):
    res = []
    if decrypt:
        key = -key

    dictionary_ru, dictionary_ru_upper = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя", "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    dictionary_en, dictionary_en_upper = "abcdefghijklmnopqrstuvwxyz", "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for char in user:
        if char in dictionary_ru:
            n = dictionary_ru
        elif char in dictionary_ru_upper:
            n = dictionary_ru_upper
        elif char in dictionary_en:
            n = dictionary_en
        elif char in dictionary_en_upper:
            n = dictionary_en_upper
        else:
            res.append(char)
            continue

        j = n.index(char)
        res.append(n[(j + key) % len(n)])

    return ''.join(res)

# Функция для выполнения действия шифрования или дешифрования
def execute_cipher():
    try:
        key = int(key_entry.get())
    except ValueError:
        messagebox.showerror("Ошибка", "Ключ должен быть целым числом.")
        return

    text = text_entry.get("1.0", tk.END).strip()
    if cipher_var.get() == 1:
        result = caesar_cipher(text, key)
    elif cipher_var.get() == 2:
        result = caesar_cipher(text, key, decrypt=True)
    else:
        messagebox.showerror("Ошибка", "Выберите действие (Шифрование/Дешифрование).")
        return

    result_entry.delete("1.0", tk.END)
    result_entry.insert(tk.END, result)

# Создание главного окна
root = tk.Tk()
# Изменение тайтла
root.title("Шифратор Цезаря")
# Изменение размера окна и его расположения
 #root.geometry("500x600+100+100")
# Максимальный и минимальный размер окна, который может выставить пользователь
'''root.minsize(500, 600)
root.maxsize(1000, 1100) '''
# Если выставить false, то пользователь не сможет менять размеры окна
root.resizable(False,False)
# Создание виджетов
tk.Label(root, text='Шифрование/Дешифрование русского/английского языка', font=("Arial", 20)).grid(row=0, column=0)

cipher_var = tk.IntVar()
encrypt_radio = tk.Radiobutton(root, text="Шифрование", variable=cipher_var, value=1, font=("Arial", 15))
decrypt_radio = tk.Radiobutton(root, text="Дешифрование", variable=cipher_var, value=2, font=("Arial", 15))

text_label = tk.Label(root, text="Введите текст:", font=("Arial", 15))
text_entry = tk.Text(root, height=10, width=70, font=("Arial", 11))

key_label = tk.Label(root, text="Введите ключ:", font=("Arial", 15))
key_entry = tk.Entry(root, font=("Arial", 11), width=15)

execute_button = tk.Button(root, text="Выполнить", command=execute_cipher, font=("Arial", 13))

result_label = tk.Label(root, text="Результат:", font=("Arial", 15))
result_entry = tk.Text(root, height=10, width=70, font=("Arial", 11))


# Размещение виджетов в окне
encrypt_radio.grid(row=1, column=0, stick='w', padx=100)
decrypt_radio.grid(row=1, column=0, stick='e', padx=100)

text_label.grid(row=2, column=0, stick='w')
text_entry.grid(row=2, column=0, stick='e', padx=10, pady=10)

key_label.grid(row=3, column=0, stick='w')
key_entry.grid(row=3, column=0, stick='w', padx=160)

execute_button.grid(row=3, column=0, columnspan=2, pady=10)

result_label.grid(row=4, column=0, stick='w')
result_entry.grid(row=4, column=0, stick='e', padx=10, pady=10)


# Запуск главного цикла
root.mainloop()