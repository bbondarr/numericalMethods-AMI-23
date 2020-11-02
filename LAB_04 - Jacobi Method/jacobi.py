import numpy as np

def printSystem(A, b):
    for i in range(A.shape[0]):
        row = ["{}x{}" .format(A[i, j], j + 1) for j in range(A.shape[1])]
        print(" + ".join(row), "=", b[i])

def jacobi(A, b, e):    
    ITERATION_LIMIT = 1000

    n = len(A)
    x = np.zeros(n)
    for i in range(ITERATION_LIMIT):
        print(i+1, ". Current solution:" , x)
        newX = np.zeros(n)

        for i in range(A.shape[0]):
            s1 = np.dot(A[i, :i], x[:i])
            s2 = np.dot(A[i, i + 1:], x[i + 1:])
            newX[i] = (b[i] - s1 - s2) / A[i, i]

        # Check if x == newX with error = e to stop iteration
        print("Difference: ", x-newX)
        if np.allclose(x, newX, atol=0.00001):
            x = newX; break

        x = newX
    
    return x


A = np.array([
    [2, 3, 1],
    [1, 1, 1],
    [3, 2, 2]])

b = [13, 6, 15]

A = np.array([
    [10, 1, -1],
    [1, 10, -1],
    [-1, 1, 10]])

b = [11, 10, 10]

e = 0.001

printSystem(A, b)
x = jacobi(A, b, e)

print("Solution:" )
print(x)
