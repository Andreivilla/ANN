import math
def euler(f, x0: float, y0: float, h: float, n: int):
    xs, ys = [], []
    
    for k in range(n):
        x = x0 + k *h
        y = y0 + h*f(x, y0)
        xs.append(x+h)
        ys.append(y)
        y0 = y
    return xs, ys

x0 = 1.04602
y0 = 2.43731
h = 0.13844

def f(x, y):
    #return y* + math.exp(-x**2) + 2
    #return y*(1-x) + x + 2
    return y*(2-x) + x + 1


r = euler(f, x0, y0, h, n=10)
k = 1
for x, y in zip(*r):
    print(f'x_{k} = {x}\ny_{k} = {y}\n')
    k+=1