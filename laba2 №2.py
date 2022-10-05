import random

import numpy
import numpy as np

while True:
    func = int(input("Введите номер необходимой функции:\n"
                     "1 - Транспонирование матрицы\n"
                     "2 - Умножение матриц\n"
                     "3 - Определение ранга матрицы\n>>"))
    if (func != 1) and (func != 2) and (func != 3):
        print("Неверная функция!")
    else:
        break
dim = []
dim1 = []
dim2 = []
matrix = []
matrix1 = []
matrix2 = []
if func == 1:
    while True:
        while True:
            dim.append(int(input("Введите количество строк в матрице\n>>")))
            if (dim[0] != 1) and (dim[0] != 2) and (dim[0] != 3):
                print("Неверное количество строк!\n")
                dim.pop()
            else:
                break
        while True:
            dim.append(int(input("Введите количество столбцов в матрице\n>>")))
            if (dim[1] != 1) and (dim[1] != 2) and (dim[1] != 3):
                print("Неверное количество столбцов!\n")
                dim.pop()
            else:
                break
        if dim[0] == dim[1] == 1:
            print("Неверная размерность матрицы!")
            dim.clear()
        else:
            break
    if (dim[0] == 1) and (dim[1] == 2):
        matrix = np.array([[0, 0]])
    if (dim[0] == 2) and (dim[1] == 1):
        matrix = np.array([[0], [0]])
    if (dim[0] == 2) and (dim[1] == 2):
        matrix = np.array([[0, 0], [0, 0]])
    if (dim[0] == 1) and (dim[1] == 3):
        matrix = np.array([[0, 0, 0]])
    if (dim[0] == 3) and (dim[1] == 1):
        matrix = np.array([[0], [0], [0]])
    if (dim[0] == 3) and (dim[1] == 3):
        matrix = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
    for i in range(int(dim[0])):
        for j in range(int(dim[1])):
            matrix[i][j] = random.randint(-10, 10)
    print("Матрица:")
    print(matrix)
    tmatrix = numpy.transpose(matrix)
    print("Транспонированная матрица:")
    print(tmatrix)
if func == 2:
    while True:
        while True:
            dim1.append(int(input("Введите количество строк в первой матрице\n>>")))
            if (dim1[0] != 1) and (dim1[0] != 2) and (dim1[0] != 3):
                print("Неверное количество строк!\n")
                dim1.pop()
            else:
                break
        while True:
            dim1.append(int(input("Введите количество столбцов в первой матрице\n>>")))
            if (dim1[1] != 1) and (dim1[1] != 2) and (dim1[1] != 3):
                print("Неверное количество столбцов!\n")
                dim1.pop()
            else:
                break
        if ((dim1[0] == dim1[1]) and (dim1[0] == 1)) or ((dim1[0] == 2) and (dim1[1] == 3)) or ((dim1[0] == 3) and (dim1[1] == 2)):
            print("Неверная размерность матрицы!")
            dim1.clear()
        else:
            if (dim1[0] == 1) and (dim1[1] == 2):
                matrix1 = np.array([[0, 0]])
            if (dim1[0] == 2) and (dim1[1] == 1):
                matrix1 = np.array([[0], [0]])
            if (dim1[0] == 2) and (dim1[1] == 2):
                matrix1 = np.array([[0, 0], [0, 0]])
            if (dim1[0] == 1) and (dim1[1] == 3):
                matrix1 = np.array([[0, 0, 0]])
            if (dim1[0] == 3) and (dim1[1] == 1):
                matrix1 = np.array([[0], [0], [0]])
            if (dim1[0] == 3) and (dim1[1] == 3):
                matrix1 = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
            for i in range(int(dim1[0])):
                for j in range(int(dim1[1])):
                    matrix1[i][j] = random.randint(-10, 10)
            while True:
                dim2.append(int(input("Введите количество строк во второй матрице\n>>")))
                if (dim2[0] != 1) and (dim2[0] != 2) and (dim2[0] != 3):
                    print("Неверное количество строк!\n")
                    dim2.pop()
                else:
                    break
            while True:
                dim2.append(int(input("Введите количество столбцов во второй матрице\n>>")))
                if (dim2[1] != 1) and (dim2[1] != 2) and (dim2[1] != 3):
                    print("Неверное количество столбцов!\n")
                    dim2.pop()
                else:
                    break
            if ((dim2[0] == dim2[1]) and (dim1[0] == 1)) or ((dim2[0] == 2) and (dim2[1] == 3)) or ((dim2[0] == 3) and (dim2[1] == 2)):
                print("Неверная размерность матрицы!")
                dim2.clear()
            else:
                if (dim2[0] == 1) and (dim2[1] == 2):
                    matrix2 = np.array([[0, 0]])
                if (dim2[0] == 2) and (dim2[1] == 1):
                    matrix2 = np.array([[0], [0]])
                if (dim2[0] == 2) and (dim2[1] == 2):
                    matrix2 = np.array([[0, 0], [0, 0]])
                if (dim2[0] == 1) and (dim2[1] == 3):
                    matrix2 = np.array([[0, 0, 0]])
                if (dim2[0] == 3) and (dim2[1] == 1):
                    matrix2 = np.array([[0], [0], [0]])
                if (dim2[0] == 3) and (dim2[1] == 3):
                    matrix2 = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
                for i in range(int(dim2[0])):
                    for j in range(int(dim2[1])):
                        matrix2[i][j] = random.randint(-10, 10)
            if dim1[1] != dim2[0]:
                print("Умножение данных матриц невозможно. Количество строк первой матрицы должно быть равно количеству столбцов второй матрицы.\n")
            else:
                break
    print("Первая матрица:")
    print(matrix1)
    print("Вторая матрица:")
    print(matrix2)
    print("Результат перемножения матриц:")
    print(np.matmul(matrix1, matrix2))
if func == 3:
    while True:
        while True:
            dim.append(int(input("Введите количество строк в матрице\n>>")))
            if (dim[0] != 1) and (dim[0] != 2) and (dim[0] != 3):
                print("Неверное количество строк!\n")
                dim.pop()
            else:
                break
        while True:
            dim.append(int(input("Введите количество столбцов в матрице\n>>")))
            if (dim[1] != 1) and (dim[1] != 2) and (dim[1] != 3):
                print("Неверное количество столбцов!\n")
                dim.pop()
            else:
                break
        if ((dim[0] != 2) and (dim[1] != 2)) and ((dim[0] != 3) and (dim[1] != 3)):
            print("Неверная размерность матрицы!\n")
            dim.clear()
        else:
            break
    if (dim[0] == 2) and (dim[1] == 2):
        matrix = np.array([[0, 0], [0, 0]])
    if (dim[0] == 3) and (dim[1] == 3):
        matrix = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
    for i in range(int(dim[0])):
        for j in range(int(dim[1])):
            matrix[i][j] = random.randint(-10, 10)
    print("Матрица:")
    print(matrix)
    print("Ранг матрицы = ")
    print(np.linalg.matrix_rank(matrix))
