# Задание 1
# Написать программу, которая определяет, является ли введенная скобочная
# структура правильной.
# Примеры правильных скобочных выражений: (), (())(), ()(), ((())), неправильных —
# )(, ())((), (, )))), ((().
# Найдите порядковый номер первого символа (скобки), нарушающего правильность
# расстановки скобок.

list = list(input("Введите последовательность скобок:>"))
stack = []
index = 0
count_open = 0
count_close = 0

for i in range(len(list)):
    if (len(list) == 1):
        index += 1
        break
    if count_close <= count_open:
        if (list[i] == ')'):
            index += 1
            count_close += 1
            if bool(stack) == True:
                index += 1
                stack.pop()
            elif bool(stack) == False:
                break
        elif (list[i] == '('):
            count_open += 1
            stack.append(list[i])
        if (len(list) == count_open):
            index += 1
            break;
        elif (len(list) == count_close):
            index += 1
            break;
    else:
        break
if bool(stack) == False:
    print("Последовательность правильная")
else:
    print(index)
