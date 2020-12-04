def lagrange(x, y, xn):
    if len(x) != len(y):
        raise ValueError('X and Y have not equal length')

    Lxn = 0
    for i in range(len(y)):
        p1 = p2 = 1
        for j in range(len(x)):
            if i == j: continue
            else:
                p1 *= xn - x[j]
                p2 *= x[i] - x[j]

        Lxn += y[i] * p1/p2
    return {'L': Lxn, 'x': xn}


x = [1, 1.7, 2, 2.2, 2.6]
y = [0.1, 0.53, 0.79, -2.1, -3.2]
xn = 2.5

res = lagrange(x, y, xn)
print(f'\nX = {res["x"]}\nL({res["x"]}) = {res["L"]}')
