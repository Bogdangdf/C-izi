import tkinter as tk
import logic

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("App")

        self.e1 = tk.Entry(root)
        self.e2 = tk.Entry(root)
        self.e1.pack()
        self.e2.pack()

        tk.Button(root, text="Add", command=self.add).pack()
        tk.Button(root, text="Sub", command=self.sub).pack()

        self.label = tk.Label(root, text="0")
        self.label.pack()

    def add(self):
        a = int(self.e1.get())
        b = int(self.e2.get())
        self.label.config(text=logic.add(a, b))

    def sub(self):
        a = int(self.e1.get())
        b = int(self.e2.get())
        self.label.config(text=logic.sub(a, b))
