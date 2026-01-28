import tkinter as tk

window = tk.Tk()
window.title("Перша програма")
window.geometry("1024x768")
window.resizable(False, False)

label = tk.Label(window, text="Hello, world!", font=("Arial", 24))
label.pack(pady=50)

button = tk.Button(window, text="Закрити", command=window.destroy)
button.pack()

window.mainloop()
