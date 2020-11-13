import numpy as np

def printSystem(A, b):
    for i in range(A.shape[0]):
        row = ["{}x{}" .format(A[i, j], j + 1) for j in range(A.shape[1])]
        print(" + ".join(row), "=", b[i])

def seidel(A, b, e):
    ITERATION_LIMIT = 100
    n  = len(A)
    x0 = [0] * n 
    x1 = x0[:]

    for i in range(ITERATION_LIMIT):
        print('Iteration '+str(i+1)+': ')

        # Calculating X(i)
        for k in range(n):
            s = sum(-A[k][j] * x1[j] for j in range(n) if k != j) 

            x1[k] = (b[k] + s) / A[k][k]

        # Checkinh the tolerance
        if all(abs(x1[j]-x0[j]) < e for j in range(n)):
            return x1 

        x0 = x1[:]    
        print(x0)

A = np.array([[1, 0.47, -0.11, 0.55],
                [0.42, 1, 0.35, 0.17],
                [-0.25, 0.67, 1, 0.36],
                [0.54, -0.32, -0.74, 1]])

b = np.array([1.33, 1.29, 2.11, 0.1])
e = 0.001

printSystem(A, b)
x = seidel(A, b, e)
print('-'*50, "\nSolution:" )
print(x)