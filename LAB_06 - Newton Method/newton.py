from math import sin, cos, tan

import numpy as np
from sympy import Symbol, diff, symbols, cos, sin

def newton(x, y, e, f1, f2):
    ITERATION_LIMIT = 100
    result = None

    _x = Symbol('x')
    _y = Symbol('y')
    f1_dx = diff(f1, _x)
    f1_dy = diff(f1, _y)
    f2_dx = diff(f2, _x)
    f2_dy = diff(f2, _y)
    # f1_dx = lambda x, y: y - (1/(cos(x-y)**2))
    # f1_dy = lambda x, y: x + (1/(cos(y-x)**2))
    # f2_dx = lambda x, y: 2*x
    # f2_dy = lambda x, y: 2*y

    for i in range(1, ITERATION_LIMIT):
        dX = f1(x, y) * f2_dy(x, y) - f2(x, y) * f1_dy(x, y)
        dY = f2(x, y) * f1_dx(x, y) - f1(x, y) * f2_dx(x, y)

        print('-'*20, f'\nIteration {i} \nX: {x} Y: {y} \nTolerance: {dX}, {dY}')
        if abs(dX) < e or abs(dY) < e:
            result = {"y": y,
                      "x": x}; break

        d = f1_dx(x, y) * f2_dy(x, y) - f1_dy(x, y) * f2_dx(x, y)
        print('Delta: ', d)
        if not d: break

        x -= dX / d
        y -= dY / d
    
    return result

f1 = lambda x, y: tan(y-x) + x*y - 0.3
f2 = lambda x, y: x**2 + y**2 - 1.5
x0 = 1.02
y0 = 0.66
e = 0.00000000001

res = newton(x0, y0, e, f1, f2)
print(f'\nResult:  X: {res["x"]}, Y: {res["y"]}')