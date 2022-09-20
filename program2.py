# калькулятор
import math
func = input(f"Введите необходимую функцию:\nСложение\nВычитание\nУмножение\nДеление\nВозведение в степень\nЛогарифм\nОкругление\n")
func = func.title()
res = 0
while True:
    a = input("Введите первый элемент:\n>>")
    try:
        a = float(a)
    except ValueError:
        print("Введенный элемент не является числом")
    if isinstance(a, float):
        break
while True:
    b = input("Введите второй элемент:\n>>")
    try:
        b = float(b)
    except ValueError:
        print("Введенный элемент не является числом")
    if isinstance(b, float):
        break
while True:
    if func == "Сложение" or func == "+":
        res = a + b
    elif func == "Вычитание" or func == "-":
        res = a - b
    elif func == "Умножение" or func == "*":
        res = a * b
    elif func == "Деление" or func == "/":
        if b != 0:
            res = a / b
        else:
            print("Деление на ноль!")
            break
    elif func == "Возведение в степень" or func == "**" or func == "^":
        res = a ** b
    elif func == "Логарифм" or func == "log":
        if (b != 1) & (b > 0) & (a > 0):
            res = math.log(a, b)
        else:
            print("Значение введённых элементов не удовлетворяет ОДЗ!")
            break
    elif func == "Округление":
        b = int(b)
        res = round(a, b)
    else:
        print("Введена неверная функция")
        break
    print(f"Результат:", res)
    break
