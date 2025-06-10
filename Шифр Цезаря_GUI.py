import customtkinter as ctk

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

def encrypt_action():
    text = entry.get()
    try:
        shift = int(shift_entry.get())
        result = encrypt(text, shift)
        output.configure(text=f"Шифр: {result}")
    except:
        output.configure(text="Помилка: зсув має бути числом")

def decrypt_action():
    text = entry.get()
    try:
        shift = int(shift_entry.get())
        result = decrypt(text, shift)
        output.configure(text=f"Розшифровано: {result}")
    except:
        output.configure(text="Помилка: зсув має бути числом")

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Шифр Цезаря(салата)")
app.geometry("400x300")

label = ctk.CTkLabel(app, text="Введи текст:")
label.pack(pady=5)

entry = ctk.CTkEntry(app, width=300)
entry.pack(pady=5)

shift_label = ctk.CTkLabel(app, text="Зсув:")
shift_label.pack(pady=5)

shift_entry = ctk.CTkEntry(app, width=100)
shift_entry.pack(pady=5)

encrypt_btn = ctk.CTkButton(app, text="Зашифрувати", command=encrypt_action)
encrypt_btn.pack(pady=5)

decrypt_btn = ctk.CTkButton(app, text="Розшифрувати", command=decrypt_action)
decrypt_btn.pack(pady=5)

output = ctk.CTkLabel(app, text="", wraplength=350)
output.pack(pady=10)

app.mainloop()