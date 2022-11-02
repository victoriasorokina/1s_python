f = input (f"Введите нужный алгоритм: \n O(3n) \n O(nlogn) \n O(n!) \n O(n^3) \n O(3log(n)) \n")
n = int(input("Введите количество повторений:"))
import random
#O(3n)
if f == "O(3n)":
    a = 0
    k = 1
    for i in range (3):
        for j in range (n):
            a = a+k
    print (a)
#O(nlogn)
if f == "O(nlogn)":
    a = []
    for i in range (n):
        a1 = random.randint(-100, 100)
        a.append(a1)
    print(a)
    def ms(a):
        if len (a)>1:
            mid = len(a)//2
            left = a[:mid]
            right = a[mid:]
            ms(left)
            ms(right)
            l=r=k=0
            while l<len(left) and r<len(right):
                if left[l]<right[r]:
                    a[k] = left[l]
                    l = l+1
                else:
                    a[k] = right[r]
                    r = r+1
                k = k+1
            while l<len(left):
                a[k] = left[l]
                l = l+1
                k = k+1
            while r<len(right):
                a[k] = right[r]
                r = r+1
                k = k+1
    ms(a)
    print(a)
#O(n!)
if f == "O(n!)":
    a = []
    for i in range (n):
        a1 = random.randint(-100, 100)
        a.append(a1)
    print("Начальные данные:", a)
    def permutations(a, n):
        if n == 1:
            print(a)
        else:
            for i in range (n):
                permutations(a, n-1)
                if n % 2 == 0:
                    (a[i], a[n-1]) = (a[n-1], a[i])
                else:
                    (a[0], a[n-1]) = (a[n-1], a[0])
    permutations (a, len(a))
#O(n^3)
if f == "O(n^3)":
    a = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                a = a + 1
    print(a)
#O(3log(n))
if f == "O(3log(n))":
    a = []
    k = n
    while k > 0:
        a.append(int(input("Введите элемент:")))
        k = k - 1
    el1 = int(input("Введите первый элемент для поиска:"))
    el2 = int(input("Введите второй элемент для поиска:"))
    el3 = int(input("Введите третий элемент для поиска:"))

    def binary_search_iterative(array, element):
        start = 0
        end = len(array)
        step = 0
        mid = 0
        while start <= end:
            print("Массив на шаге {}: {}".format(step, str(array[start:end + 1])))
            step = step + 1
            mid = (start + end) // 2
            if element == array[mid]:
                return mid
            if element < array[mid]:
                end = mid - 1
            else:
                start = mid + 1
        return -1
    binary_search_iterative(a, el1)
    print("\n")
    binary_search_iterative(a, el2)
    print("\n")
    binary_search_iterative(a, el3)