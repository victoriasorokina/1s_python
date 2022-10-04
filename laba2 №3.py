A = []
for i in range(9):
    A.append(int(input("Введите элемент матрицы.\n>>")))
print("\nМатрица:")
for i in range(0, 9, 3):
    print(A[i], A[i+1], A[i+2])
    if ((i+1) % 3) == 0:
        print("\n")
det = A[0]*A[4]*A[8] + A[1]*A[5]*A[6] + A[2]*A[3]*A[7] - A[2]*A[4]*A[6] - A[1]*A[3]*A[8] - A[0]*A[5]*A[7]
if det == 0:
    print("Для данной матрицы не существует обратной матрицы.")
else:
    Aij = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    Aij[0] = (A[4]*A[8] - A[5]*A[7])
    Aij[1] = (A[3]*A[8] - A[5]*A[6]) * (-1)
    Aij[2] = (A[3]*A[7] - A[4]*A[6])
    Aij[3] = (A[1]*A[8] - A[2]*A[7]) * (-1)
    Aij[4] = (A[0]*A[8] - A[2]*A[6])
    Aij[5] = (A[0]*A[7] - A[1]*A[6]) * (-1)
    Aij[6] = (A[1]*A[5] - A[2]*A[4])
    Aij[7] = (A[0]*A[5] - A[2]*A[3]) * (-1)
    Aij[8] = (A[0]*A[4] - A[1]*A[3])
    AijT = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    AijT[0] = Aij[0]
    AijT[1] = Aij[3]
    AijT[2] = Aij[6]
    AijT[3] = Aij[1]
    AijT[4] = Aij[4]
    AijT[5] = Aij[7]
    AijT[6] = Aij[2]
    AijT[7] = Aij[5]
    AijT[8] = Aij[8]
    invA = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(9):
        invA[i] = AijT[i] / det
    print("\nОбратная матрица:")
    for i in range(0, 9, 3):
        print(invA[i], invA[i + 1], invA[i + 2])
        if ((i + 1) % 3) == 0:
            print("\n")
