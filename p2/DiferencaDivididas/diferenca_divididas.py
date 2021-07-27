from math import*

def divided_differences(x, y):
    Y = [item for item in y] # vai mudando em cada iteração
    coeffs = []
    coeffs.append(y[0])
    for i in range(len(y) - 1):
        coeffs.append(0)

    n = len(y)
    for i in range(n - 1):
        for j in range(n -1 -i):
            numer = Y[j+1] - Y[j]     
            denom = x[j+1+i] - x[j] 
            Y[j] = numer / denom
        coeffs[i+1] = Y[0]
    return coeffs


def eq(x, coefss):
    n = len(x)
    equation = f'{coeffs[0]:+}'
    for i in range(n ):
        equation += f'{coeffs[i]:+}' + '*'.join([f'(x{-xj:+})' for j,xj in enumerate(x) if j <i])
    return equation

def f(x):
    #return sin(x)**3 - 3*sin(x)**2 + sin(x**2) + 4
    #return x**5 - 4*x**2 + 2*((x+1)**(1/2)) + cos(x)
    return 1/(1+25*x**2)

x = [-0.869, -0.676, -0.552, -0.305, -0.117, 0.068, 0.195, 0.404, 0.487, 0.731, 0.839]
y = [f(i) for i in x]

coeffs = divided_differences(x, y)
print (coeffs)
poly = eq(x, coeffs)
#print('p(x) =',poly)