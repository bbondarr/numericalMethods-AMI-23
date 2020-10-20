from math import sqrt
import numpy as np

def CholeskyDecomposition(A):
    n = len(A)
    L = np.zeros((n, n))
    
    for i in range(n):
        for j in range(i+1):
            temp = sum(L[i][k] * L[j][k] for k in range(j))

            if (i == j):
                L[i][j] = sqrt(A[i][i] - temp)
            else:
                L[i][j] = (1.0 / L[j][j] * (A[i][j] - temp))

    return L

def calcCholesky(A, L, b):
    n = len(A)
    # Transposing L
    U = [*zip(*L)]
    resY = np.zeros((n))
    resX = np.zeros((n))

    #resY
    for i in range(n):
        temp = sum(U[j][i] * resY[j] for j in range(i))
        resY[i] = (b[i] - temp) / U[i][i]

    #resX
    for i in range(n-1, -1, -1):
        temp = sum(U[i][j] * resX[j] for j in range(i+1, n))
        resX[i] = (resY[i] - temp) / U[i][i]

    return resX


# n = int(input('Enter Matrix size: '))
#A = np.zeros((4, 4))
A = [[10, 5, 3], [3, 10, -2], [5, -7, 10]]
b = [20, 9, -9]

#print('Enter Equation Koeficiens:')
# for i in range(n):
#     for j in range(n):
#         A[i][j] = input('MATRIX[%d][%d]: ' % (i, j))

print('A:')
for row in A:
    print(row)
try:
    L = CholeskyDecomposition(A)
except ValueError as e:
    print(str(e))
print('A:')
for row in A:
    print(row)
print('L:')
for row in L:
    print(row)
print('U:')
for row in L.T:
    print(row)
print('-'*60)

print('RESULT: ', calcCholesky(A, L, b))
