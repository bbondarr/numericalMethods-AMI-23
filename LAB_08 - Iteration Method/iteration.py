from copy import deepcopy
from sympy import Symbol, diff, sin, cos, sqrt, log, asin, acos

def isIterable(f1, f2, x0, y0):
    f1_dx = diff(f1, x)
    f1_dy = diff(f1, y)
    f2_dx = diff(f2, x)
    f2_dy = diff(f2, y)

    if (abs(f1_dx.subs({x: x0, y: y0})) + abs(f1_dy.subs({x: x0, y: y0})) >= 1 or
        abs(f2_dx.subs({x: x0, y: y0})) + abs(f2_dy.subs({x: x0, y: y0})) >= 1):
        raise ValueError('Functions not suitable for the method')


def iteration(f1, f2, x0, y0, e):
    ITERATION_LIMIT = 100

    isIterable(f1, f2, x0, y0)

    for i in range(1, ITERATION_LIMIT):
        xi = deepcopy(x0)
        yi = deepcopy(y0)

        x0 = f1.subs({x: xi, y: yi})
        y0 = f2.subs({x: xi, y: yi})
        print(f'ITERATION {i}: X: {x0}\tY: {y0}')
        if (abs(xi -x0) <= e and abs(yi -y0) <= e):
            break

    return {'y': y0, 'x': x0}


x = Symbol('x')
y = Symbol('y')
f1 = asin(1 - cos(y))
f2 = acos(0.5*(sin(3*x) + 1))
x0 = 0.2
y0 = 0.65
e = 0.001

print(iteration(f1, f2, x0, y0, e))