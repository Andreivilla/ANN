from math import*
import numpy as np
from scipy.interpolate import lagrange

x = [0.309, 0.608, 1.075, 1.17, 1.683, 1.873, 2.111, 2.55, 2.865]

def f(x):
    e = 2.718281828459045235360287
    #return e**-(x**2) + cos(x) + 3
    #return sin(x)**3 - 3*sin(x)**2 + sin(x**2) + 4
    #return cos(x)**3 + 2*cos(x)**2 + 1
    #return 1 / (1+25*x**2)
    return cos(sin(np.log(x**2)))

y = [f(i) for i in x]

x = [2.356, 3.421, 5.092]
y = [3.997, 5.352, 2.993]

print("---------------------------")
x = np.array(x)
y = np.array(y)
poly = lagrange(x, y).coeffs

print(poly)
n = len(poly)-1
for coef in poly:
    print(f'a^{n} : {coef}')
    n -= 1

print("-----------soma-----------")
def lagrangeX(x, poly):
    listaN =[]
    for xtarget in x:
        soma = 0
        n = len(poly)-1
        for coef in poly:
            soma += coef*xtarget**n
            n -= 1
        listaN.append(soma)
    return listaN

values = [0, 1, 2]

print(f'y: {y}')
print(f'x: {x}')
lx = lagrangeX(values, poly)
print(lx)

""" print("----------erro absoluto------------")
for i in range(len(values)):
    print(f(values[i]) - lx[i]) """
print("------------cn-----------")

