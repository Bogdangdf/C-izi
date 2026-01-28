import tkinter as tk

window = tk.Tk()
window.title("Друга програма")
window.geometry("400x300")
window.resizable(False, False)

label = tk.Label(window, text="", font=("Arial", 16))
label.pack(pady=20)

def greet():
    label.config(text="Вітаю, користувач!")

def clear():
    label.config(text="")

button_greet = tk.Button(window, text="Привітати", command=greet)
button_greet.pack(pady=5)

button_clear = tk.Button(window, text="Очистити", command=clear)
button_clear.pack(pady=5)

button_exit = tk.Button(window, text="Вийти", command=window.destroy)
button_exit.pack(pady=5)

window.mainloop()
