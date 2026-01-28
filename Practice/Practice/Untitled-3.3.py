import tkinter as tk

window = tk.Tk()
window.title("Анкета користувача")
window.geometry("500x300")
window.resizable(False, False)

tk.Label(window, text="Ім'я:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
name_entry = tk.Entry(window)
name_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(window, text="Стать:").grid(row=1, column=0, padx=10, pady=5, sticky="w")

gender = tk.StringVar(value="Чоловіча")
tk.Radiobutton(window, text="Чоловіча", variable=gender, value="Чоловіча").grid(row=1, column=1, sticky="w")
tk.Radiobutton(window, text="Жіноча", variable=gender, value="Жіноча").grid(row=2, column=1, sticky="w")

agree = tk.BooleanVar()
tk.Checkbutton(window, text="Погоджуюсь із умовами", variable=agree).grid(row=3, column=1, pady=5, sticky="w")

result = tk.Label(window, text="", justify="left")
result.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky="w")

def save():
    text = f"Ім'я: {name_entry.get()}\nСтать: {gender.get()}\nПогодився з умовами: {'Так' if agree.get() else 'Ні'}"
    result.config(text=text)

tk.Button(window, text="Зберегти", command=save).grid(row=4, column=1, pady=10, sticky="e")

window.mainloop()
