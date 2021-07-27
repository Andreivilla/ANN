from math import*
import numpy as np

def prod(lst):
    p = 1
    for i in lst:
        p*= i
    return p


def finite_diffs(xs, ordem, x0, f):
    A = []
    B = []
    n = len(xs)
    for i in range(n):
        #para construir a matriz A
        A.append([0] * (n))
        for j in range(n):
            A[i][j] = xs[j] ** i 
        
        #para construir a matriz B
        potencias = [k +1 for k in range(i - ordem,  i)]
        fatorial = 0 if i < ordem else prod(potencias)
        termo = fatorial * x0 ** (i-ordem)
        B.append(termo)
    A = np.array(A, dtype = 'float')
    B = np.array(B, dtype = 'float')
    cs = np.linalg.solve(A,B)
    soma = 0
    for ck,xk in zip(cs, xs):
        soma += ck * f(xk)
    return soma


if __name__ == '__main__':

    def f(x):
        e = 2.718281828459045235360287
        pi = 3.1415926535897932384626
        #return (x**2)*(e**-x)*cos(x)+1
        #return cos(x)**3 + 2*cos(x)**2 + 1
        #return e**(-x**2) + cos(x) + 3
        #return (cos(x**2) + x)**(1/2)
        #return e**(cos(x)**2) + e**(-x**2) + log(x)
        #return cos(x + log(x**2)**(1/2))
        #return cos(sin(log(x**2)))
        return sin((pi+x**2)**(1/2))


    #pontos para contruir a fórmula
    ordem = 5
    x0 = 2.3516108
    x = [-1.8012243, -1.0566657, -0.4934558, 0.3113094, 0.7616207, 1.2475632, 1.832175, 2.7456502, 3.2937524, 3.6551106, 3.9560499, 4.5322, 5.5664778, 6.0629338, 6.5930397]

    r = finite_diffs(x, ordem, x0, f)
    print(f(3))
    print(f'aproximação para a derivada de ordem {ordem} de f no ponto {x0}', r)