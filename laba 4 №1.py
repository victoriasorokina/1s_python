import module
import timeit
func = input ("Введите метод сортировки: \nБыстрая сортировка \nСортировка расчёской \n")
import random
n = int(input("Введите количество символов:"))
a = []
for i in range (n):
    a1 = random.randint(-100, 100)
    a.append(a1)
print (a)
if func == "Быстрая сортировка":
    print (module.quick_sort(a))
    print (timeit.timeit())
if func == "Сортировка расчёской":
    print (module.comb_sort(a))
    print(timeit.timeit())