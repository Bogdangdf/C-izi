import tkinter as tk

window = tk.Tk()
window.title("Калькулятор")
window.geometry("400x300")
window.resizable(False, False)

tk.Label(window, text="Число 1:").grid(row=0, column=0, padx=10, pady=5)
entry1 = tk.Entry(window)
entry1.grid(row=0, column=1, padx=10, pady=5)

tk.Label(window, text="Число 2:").grid(row=1, column=0, padx=10, pady=5)
entry2 = tk.Entry(window)
entry2.grid(row=1, column=1, padx=10, pady=5)

result_label = tk.Label(window, text="Результат:")
result_label.grid(row=2, column=0, columnspan=2, pady=10)

def calculate(operation):
    try:
        a = float(entry1.get())
        b = float(entry2.get())

        if operation == "+":
            result = a + b
        elif operation == "-":
            result = a - b
        elif operation == "*":
            result = a * b
        elif operation == "/":
            if b == 0:
                raise ZeroDivisionError
            result = a / b

        result_label.config(text=f"Результат: {result}")
    except ValueError:
        result_label.config(text="Помилка: введіть числа")
    except ZeroDivisionError:
        result_label.config(text="Помилка: ділення на нуль")

tk.Button(window, text="+", width=5, command=lambda: calculate("+")).grid(row=3, column=0, pady=5)
tk.Button(window, text="-", width=5, command=lambda: calculate("-")).grid(row=3, column=1, pady=5)
tk.Button(window, text="*", width=5, command=lambda: calculate("*")).grid(row=4, column=0, pady=5)
tk.Button(window, text="/", width=5, command=lambda: calculate("/")).grid(row=4, column=1, pady=5)

window.mainloop()
