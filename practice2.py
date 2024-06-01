# Функция для проверки и получения целого числа от пользователя
def get_integer_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Пожалуйста, введите целое число.")

# Текст, который пользователь хочет ввести
text = input("Введите текст, который хотите зашифровать: ")
# Пользователь вводит ключ с проверкой
k = get_integer_input("Укажите ключ: ")

# Функция шифрования и дешифровки с тремя параметрами: текст, ключ, флаг дешифровки
def caesar_cipher(user, key, decrypt=False):
    # Переменная результата шифрования
    res = []
    # Если дешифровка, инвертировать ключ
    if decrypt:
        key = -key

    # Две пары переменных, содержащих русскую и английскую азбуки в нижнем и верхнем регистрах соответственно
    dictionary_ru, dictionary_ru_upper = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя", "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    dictionary_en, dictionary_en_upper = "abcdefghijklmnopqrstuvwxyz", "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # Цикл проверки, где каждую итерацию будет обрабатываться один символ из текста последовательно
    for char in user:
        # Проверка символа на принадлежность к русскому нижнему регистру
        if char in dictionary_ru:
            n = dictionary_ru
        # Проверка символа на принадлежность к русскому верхнему регистру
        elif char in dictionary_ru_upper:
            n = dictionary_ru_upper
        # Проверка символа на принадлежность к английскому нижнему регистру
        elif char in dictionary_en:
            n = dictionary_en
        # Проверка символа на принадлежность к английскому верхнему регистру
        elif char in dictionary_en_upper:
            n = dictionary_en_upper
        # Символ не принадлежит ни одной из азбук (символ не является буквой)
        else:
            res.append(char)
            continue

        # Если символ есть в списке n (является буквой), то будет происходить его зашифровка/дешифровка
        j = n.index(char)
        res.append(n[(j + key) % len(n)])

    # Функция возвращает зашифрованный или расшифрованный текст
    return ''.join(res)

# Вывод зашифрованного текста
encrypted_text = caesar_cipher(text, k)
print("Зашифрованный текст:", encrypted_text)

# Расшифровка текста
decrypted_text = caesar_cipher(encrypted_text, k, decrypt=True)
print("Расшифрованный текст:", decrypted_text)