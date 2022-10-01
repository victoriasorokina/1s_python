func = input (f"Введите функцию: \n Транспонирование \n Умножение \n Определение ранга \n")
func = func.title()
mat1 = []
mat2 = [] #матрицы пользователя
mat = [] #матрица с преобразованиями
r = 0 #ранг матрицы
from math import *
#транспонирование
if func == "Транспонирование" or func == "Т":
    n = int(input("Введите количество строк:"))
    m = int(input("Введите количество столбцов:"))
    for i in range (n):
        a = []
        for j in range (m):
            a.append (int(input("Введите элемент матрицы:")))
        mat1.append (a)
    mat = [[0 for m in range (len(mat1))] for n in range (len(mat1[0]))]
    for i in range (len(mat1)):
        for j in range (len(mat1[0])):
            mat[j][i] = mat1[i][j]
    print (mat)
#умножение
if func == "Умножение" or func == "*":
    n1 = int(input("Введите количество строк первой матрицы:"))
    m1 = int(input("Введите количество столбцов первой матрицы:"))
    n2 = int(input("Введите количество строк второй матрицы:"))
    m2 = int(input("Введите количество столбцов второй матрицы:"))
    while n1 != m2 and m1 != n2:
        print ("Умножение невозможно, введите другую размерность")
        n1 = int(input("Введите количество строк первой матрицы:"))
        m1 = int(input("Введите количество столбцов первой матрицы:"))
        n2 = int(input("Введите количество строк второй матрицы:"))
        m2 = int(input("Введите количество столбцов второй матрицы:"))
    for i in range(n1):
        a = []
        for j in range(m1):
            a.append(int(input("Введите элемент первой матрицы:")))
        mat1.append(a)
    for i in range(n2):
        a = []
        for j in range(m2):
            a.append(int(input("Введите элемент второй матрицы:")))
        mat2.append(a)
    mat = [[0 for n1 in range (len(mat1))] for m2 in range (len(mat2[0]))]
    for i in range (len(mat1)):
        for j in range (len(mat2[0])):
            for k in range (len(mat2)):
                mat[i][j]+= mat1[i][k]*mat2[k][j]
    print (mat)
#определение ранга квадратной матрицы
if func == "Определение Ранга":
    n = int(input("Введите количество строк:"))
    m = int(input("Введите количество столбцов:"))
    while not (n==2 and m==2 or n==3 and m==3):
        print ("Введите размерность квадратной матрицы")
        n = int(input("Введите количество строк:"))
        m = int(input("Введите количество столбцов:"))
    for i in range (n):
        a = []
        for j in range (m):
            a.append (int(input("Введите элемент матрицы:")))
        mat1.append (a)
    if n == 2:
        for i in range(len(mat1)):
            if mat1[i] != 0:
                r += 1
                break
        det = mat1[0][0]*mat1[1][1]-mat1[0][1]*mat1[1][0]
        if det != 0:
            r += 1
        print(r)
    if n ==3:
        for i in range(len(mat1)):
            if mat1[i] != 0:
                r += 1
                break
        for i in range(len(mat1)):
            det1 = fabs(mat1[1][1]*mat1[2][2]-mat1[1][2]*mat1[2][1])
            det2 = fabs(mat1[1][0]*mat1[2][2]-mat1[1][2]*mat1[2][0])
            det3 = fabs(mat1[1][0]*mat1[2][1]-mat1[1][1]*mat1[2][0])
            det4 = fabs(mat1[0][1]*mat1[2][2]-mat1[0][2]*mat1[2][1])
            det5 = fabs(mat1[0][0]*mat1[2][2]-mat1[0][2]*mat1[2][0])
            det6 = fabs(mat1[0][0]*mat1[2][1]-mat1[0][1]*mat1[2][0])
            det7 = fabs(mat1[0][1]*mat1[1][2]-mat1[0][2]*mat1[1][1])
            det8 = fabs(mat1[0][0]*mat1[1][2]-mat1[0][2]*mat1[1][0])
            det9 = fabs(mat1[0][0]*mat1[1][1]-mat1[0][1]*mat1[1][0])
            det = max(det1, det2, det3, det4, det5, det6, det7, det8, det9)
            if det != 0:
                r += 1
                break
        det = mat1[0][0]*mat1[1][1]*mat1[2][2]+mat1[0][1]*mat1[1][2]*mat1[2][0]+mat1[0][2]*mat1[1][0]*mat1[2][1]-mat1[0][2]*mat1[1][1]*mat1[2][0]-mat1[0][1]*mat1[1][0]*mat1[2][2]-mat1[0][0]*mat1[1][2]*mat1[2][1]
        if det != 0:
            r += 1
        print(r)