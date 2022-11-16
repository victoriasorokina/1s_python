import random
func = input ("Введите метод сортировки: \nБлочная сортировка \nПирамидальная сортировка \n")
n = int(input("Введите количество символов:"))
a = []
for i in range (n):
    a1 = random.randint(0, 100)
    a.append(a1)
print (a)
# блочная сортировка
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
# пирамидальная сортировка
def heapify(nums, heap_size, root_index):
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2

    if left_child < heap_size and nums[left_child] > nums[largest]:
        largest = left_child

    if right_child < heap_size and nums[right_child] > nums[largest]:
        largest = right_child

    if largest != root_index:
        nums[root_index], nums[largest] = nums[largest], nums[root_index]

        heapify(nums, heap_size, largest)

def heap_sort(nums):
    n = len(nums)

    for i in range(n, -1, -1):
        heapify(nums, n, i)

    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)


if func == "Блочная сортировка":
    print (bucket_sort(a))
if func == "Пирамидальная сортировка":
    heap_sort(a)
    print (a)
