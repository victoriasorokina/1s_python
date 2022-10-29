#пузырьковая сортировка
import time
a1 = []
a = []
a2 = 0
n = int(input("Введите количество элементов:"))
for i in range (n):
    a1 = int(input("Введите элемент:"))
    a.append (a1)
def func():
    for i in range (n-1):
        for j in range (n-i-1):
            if a[j]>a[j+1]:
                a2 = a[j]
                a[j] = a[j+1]
                a[j+1] = a2
    print(a)
start = time.time()
func()
end = time.time()
total = end - start
print ("Затраченное время на пузырьковую сортировку:")
print (total)
def s():
    a.sort()
    print(a)
starts = time.time()
s()
ends = time.time()
totals = ends - starts
print ("Затраченное время методом sort:")
print (totals)