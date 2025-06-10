# alphabet = 'АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ'
#
# def encrypt(text, shift):
#     result = ''
#     for char in text.upper():
#         if char in alphabet:
#             index = alphabet.index(char)
#             result += alphabet[(index + shift) % len(alphabet)]
#         else:
#             result += char
#     return result
#
# def decrypt(text, shift):
#     result = ''
#     for char in text.upper():
#         if char in alphabet:
#             index = alphabet.index(char)
#             result += alphabet[(index - shift) % len(alphabet)]
#         else:
#             result += char
#     return result
#
# mode = input("Вибери режим (1 - шифрувати, 2 - розшифрувати): ")
# message = input("Введи речення: ")
# shift = int(input("Введи зсув: "))
#
# if mode == '1':
#     result = encrypt(message, shift)
#     print("Зашифровано:", result)
# elif mode == '2':
#     result = decrypt(message, shift)
#     print("Розшифровано:", result)
# else:
#     print("Невірний вибір режиму")


def encrypt(text, shift):
    result = ''
    for char in text:
        result += chr(ord(char) + shift)
    return result

def decrypt(text, shift):
    result = ''
    for char in text:
        result += chr(ord(char) - shift)
    return result

mode = input("Вибери режим (1 - шифрувати, 2 - розшифрувати): ")
text = input("Введи текст: ")
shift = int(input("Введи зсув: "))

if mode == '1':
    print("Зашифровано:", encrypt(text, shift))
elif mode == '2':
    print("Розшифровано:", decrypt(text, shift))
else:
    print("Невірний режим")