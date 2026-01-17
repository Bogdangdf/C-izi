import this

print("\n--- Оголошення змінних ---")

a = 10
b = 3
x = 2.5
y = 4.0
text = "Python"

print("a =", a)
print("b =", b)
print("x =", x)
print("y =", y)
print("text =", text)

print("\n--- Арифметичні операції ---")

print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)

print("x + y =", x + y)
print("x - y =", x - y)
print("x * y =", x * y)
print("x / y =", x / y)

print("\n--- Робота з рядками ---")

print(text + " language")
print(text * 3)

print("\n--- Ввід даних користувачем ---")

user_int = int(input("Введіть ціле число: "))
user_float = float(input("Введіть дійсне число: "))

print("Сума:", user_int + user_float)
print("Різниця:", user_int - user_float)
print("Добуток:", user_int * user_float)
print("Частка:", user_int / user_float)

"""
Порівняння Bash та Python

Bash:
a=5
b=3
echo $((a + b))

Python:
a = 5
b = 3
print(a + b)

У Bash усі змінні є рядками, арифметика обмежена.
У Python є строгі типи даних і зручна вбудована арифметика.
"""

print("\n--- Завдання виконано успішно ---")
