#быстрая сортировка
def quick_sort(a):
    if len(a)<=1:
        return a
    else:
        middle = len(a) // 2
        mid = a[middle] #опорный
        left = []
        m = []
        right = []
        for n in a:
            if n<mid:
                left.append(n)
            elif n>mid:
                right.append(n)
            else:
                m.append(n)
    return quick_sort(left) + m + quick_sort(right)
#сортировка расчёской
def comb_sort(a):
    s = int(len(a)/1.247) #длина шага
    p = 1 #для завершения сортировки с помощью пузырьковой
    while s>1 or p>1:
        i = 0
        p = 0
        while i+s<len(a):
            if a[i]>a[i+s]:
                (a[i], a[i+s]) = (a[i+s], a[i])
                p = p+1
            i = i+1
        if s>1:
            s=int(s/1.247)
    return a