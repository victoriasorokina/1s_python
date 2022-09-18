#калькулятор
func = input(f"Введите функцию: \n Сложение \n Вычитание \n Умножение \n Деление \n Возведение в степень \n Логарифм \n Округление \n")
func = func.title()
res = 0
import math
a = input("Введите первое число:")
try:
    a = float (a)
except ValueError:
    print ("Введенный элемент не является числом")
    a = input("Введите первый элемент:")
b = input("Введите второе число:")
try:
    b = float(b)
except ValueError:
    print ("Введенный элемент не является числом")
    b = input("Введите второй элемент:")
if func == "Сложение" or func == "+":
    res = a + b
if func == "Вычитание" or func == "-":
    res = a - b
if func == "Умножение" or func == "*":
    res = a * b
if func == "Деление" or func == "/":
    res = a / b
if func == "Возведение в степень" or func == "**" or func == "^":
    res = a ** b
if func == "Логарифм" or func == "log":
    res = math.log (a, b)
if func == "Округление":
    res = round (a, b)
print (f"Результат:", res)