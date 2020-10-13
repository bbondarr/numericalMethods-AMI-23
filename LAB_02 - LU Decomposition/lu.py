import numpy as np

def LUDecomposition(A, L, U):
    U = A
    n = len(A)

    for i in range(n):
        for j in range(i, n):
            L[j][i] = U[j][i] / U[i][i]
	
    for k in range(1, n):
        for i in range(k-1, n):
            for j in range(i, n):
                L[j][i] = U[j][i] / U[i][i]

        for i in range(k, n):
            for j in range(k-1, n):
                U[i][j] = U[i][j]-L[i][k-1] * U[k-1][j]

    return (L, U)

n = int(input('Enter Matrix size: '))
A, L, U = np.zeros((n, n)), np.zeros((n, n)), np.zeros((n, n))

print('Enter Matrix Elements:')
for i in range(n):
    for j in range(n):
        A[i][j] = input('MATRIX[%d][%d]: ' % (i, j))

print('A:\n', A)
print('-'*20)
print('AFTER LU DECOMPOSITION:')
print('-'*20)
[L, U] = LUDecomposition(A, L, U)
print('A:\n', np.matmul(L, U))
print('L:\n', L.round(2))
print('U:\n', U.round(2))