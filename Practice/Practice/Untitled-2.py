num = int(input("Введіть ціле число: "))

result = ""

if num == 0:
    result = "0"
else:
    is_negative = False
    if num < 0:
        is_negative = True
        num = -num

    while num > 0:
        digit = num % 10
        result = chr(ord('0') + digit) + result
        num = num // 10

    if is_negative:
        result = "-" + result

print("Рядкове представлення числа:", result)
