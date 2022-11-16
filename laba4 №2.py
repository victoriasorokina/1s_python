func = input ("Введите метод сортировки: \nБлочная сортировка \nПирамидальная сортировка \n")
import random
n = int(input("Введите количество символов:"))
a = []
for i in range (n):
    a1 = random.randint(0, 100)
    a.append(a1)
print (a)
#блочная сортировка
def insertion_sort(bucket):
    for i in range (1, len (bucket)):
        b = bucket[i]
        j = i - 1
        while (j >= 0 and b < bucket[j]):
            bucket[j + 1] = bucket[j]
            j = j - 1
        bucket[j + 1] = b
def bucket_sort(a):
    size = max(a)/len(a)
    buckets = [[] for i in range (len(a))]
    for i in range (len(a)):
        j = int(a[i]/size)
        if j != len(a):
            buckets[j].append(a[i])
        else:
            buckets[len(a)-1].append(a[i])
    for i in range (len(a)):
        insertion_sort(buckets[i])
    list = []
    for i in range (len(a)):
        list = list + buckets[i]
    return list
if func == "Блочная сортировка":
    print (bucket_sort(a))
