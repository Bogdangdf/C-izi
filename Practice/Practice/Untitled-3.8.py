import tkinter as tk
from tkinter import colorchooser, filedialog

root = tk.Tk()
root.title("Графіка")

canvas = tk.Canvas(root, width=600, height=400, bg="white")
canvas.pack()

color = "black"
mode = "line"
x0 = y0 = 0

def choose_color():
    global color
    c = colorchooser.askcolor()[1]
    if c:
        color = c

def set_line():
    global mode
    mode = "line"

def set_circle():
    global mode
    mode = "circle"

def clear():
    canvas.delete("all")

def save():
    path = filedialog.asksaveasfilename(defaultextension=".ps")
    if path:
        canvas.postscript(file=path)

def press(event):
    global x0, y0
    x0, y0 = event.x, event.y

def release(event):
    if mode == "line":
        canvas.create_line(x0, y0, event.x, event.y, fill=color, width=2)
    if mode == "circle":
        canvas.create_oval(x0, y0, event.x, event.y, outline=color, width=2)

frame = tk.Frame(root)
frame.pack()

tk.Button(frame, text="Лінія", command=set_line).pack(side="left")
tk.Button(frame, text="Коло", command=set_circle).pack(side="left")
tk.Button(frame, text="Колір", command=choose_color).pack(side="left")
tk.Button(frame, text="Очистити", command=clear).pack(side="left")
tk.Button(frame, text="Зберегти", command=save).pack(side="left")

canvas.bind("<Button-1>", press)
canvas.bind("<ButtonRelease-1>", release)

root.mainloop()
