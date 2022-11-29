from random import randint
n = int(input("Введите количество символов:"))
a = []
for i in range (n):
    a1 = randint(0, 1)
    a.append(a1)
print (a)
for i in range(1,n+1):
    zero = 0
    for j in range(0, n - i+1):
        if sum(a[j:j+i])==0:
            zero=zero+1
    one=0
    for j in range(0, n - i+1):
        if sum(a[j:j+i])==i:
            one=one+1
    if one==zero==0:
        break
    print("Вероятность", "0"*i, ":", zero/(n-i+1))
    print("Вероятность", "1"*i, ":", one/(n-i+1))