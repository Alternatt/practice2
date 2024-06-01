# Текст, который пользователь хочет ввести
text = input("Введите текст, который хотите зашифровать: ")
# Пользователь вводит ключ
k = int(input("Укажите ключ: "))
# Пользователь вводит язык текста, который будет зашифрован
language = input("На каком языке текст, который вы ввели (русский, английский): ")

# Функция шифрования с тремя параметрами: текст, ключ, язык
def caesar_cipher(user, key, lang, decrypt=False):
    # Переменная результата шифрования; переменная, определяющая верхний и нижний регистр
    res, n = [], ""
    # Если дешифровка, инвертировать ключ
    if decrypt:
        key = -key

    # Проверка пользователем выбранного языка
    if lang.lower() in ["русский", "russian"]:
        # Двум переменным присваиваются русская азбука нижнего и верхнего регистра соответственно
        dictionary, dictionary_upper = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя", "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    elif lang.lower() in ["английский", "english"]:
        # Двум переменным присваиваются английской азбука нижнего и верхнего регистра соответственно
        dictionary, dictionary_upper = "abcdefghijklmnopqrstuvwxyz", "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    else:
        return "Такого языка нет в опции"

    # Цикл проверки, где каждую итерацию будет обрабатываться один символ из текста последовательно
    for i in range(len(user)):
        # Проверка символа на верхний или нижний регистр
        if user[i] in dictionary:
            n = dictionary
        elif user[i] in dictionary_upper:
            n = dictionary_upper
        else:
            res.append(user[i])
            continue

        # Если символ есть в списке n (является буквой), то будет происходить его зашифровка
        if user[i] in n:
            j = n.index(user[i])
            res.append(n[(j + key) % len(n)])

    # Функция возвращает зашифрованный или расшифрованный текст
    return ''.join(res)

# Вывод зашифрованного текста
encrypted_text = caesar_cipher(text, k, language)
print("Зашифрованный текст:", encrypted_text)

# Расшифровка текста
decrypted_text = caesar_cipher(encrypted_text, k, language, decrypt=True)
print("Расшифрованный текст:", decrypted_text)