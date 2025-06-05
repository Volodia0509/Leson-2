import customtkinter as ctk
key = {
    'А': '@', 'Б': '#', 'В': '$', 'Г': '%', 'Ґ': '&', 'Д': '*', 'Е': '(',
    'Є': ')', 'Ж': '!', 'З': '^', 'И': '_', 'І': '+', 'Ї': '~', 'Й': '`',
    'К': '-', 'Л': '=', 'М': '{', 'Н': '}', 'О': '[', 'П': ']', 'Р': ';',
    'С': ':', 'Т': '"', 'У': "'", 'Ф': '<', 'Х': '>', 'Ц': '/', 'Ч': '|',
    'Ш': '?', 'Щ': ',', 'Ь': '.', 'Ю': '1', 'Я': '2', ' ': ' '
}


def encrypt_ukr():
    text = input_entry.get().upper()
    result = ''
    for ch in text:
        result += key.get(ch, '?')
    output_entry.delete(0, ctk.END)
    output_entry.insert(0, result)

def decrypt_ukr():
    code = input_entry.get()
    result = ''
    for symbol in code:
        for letter, code_symbol in key.items():
            if code_symbol == symbol:
                result += letter
                break
        else:
            result += symbol
    output_entry.delete(0, ctk.END)
    output_entry.insert(0, result)

# GUI
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

window = ctk.CTk()
window.title("Український шифратор")
window.geometry("500x300")

ctk.CTkLabel(window, text="Введіть український текст:").pack(pady=10)
input_entry = ctk.CTkEntry(window, width=450)
input_entry.pack()

ctk.CTkButton(window, text="Зашифрувати", command=encrypt_ukr).pack(pady=5)
ctk.CTkButton(window, text="Розшифрувати", command=decrypt_ukr).pack(pady=5)

ctk.CTkLabel(window, text="Результат:").pack(pady=10)
output_entry = ctk.CTkEntry(window, width=450)
output_entry.pack()

window.mainloop()