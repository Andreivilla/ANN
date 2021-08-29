import numpy as np

""" Dados de Entrada """
x = [-4.2004, -3.923, -3.6421, -3.4372, -2.9392, -2.9168, -2.5148, -2.1335, -1.9437, -1.7792, -1.3967, -1.0843, -0.8347, -0.748, -0.379, -0.2479, 0.1858, 0.4905, 0.5716, 1.0078, 1.1342, 1.3961, 1.751, 1.9727, 2.2951, 2.4645, 2.7155, 3.0374, 3.1922, 3.4705, 3.8734, 4.1286]
y = [2.6239, 5.4934, 6.8441, 8.0302, 7.5328, 8.8348, 7.5559, 4.6251, 5.031, 4.3139, 4.1473, 3.7696, 4.1009, 4.0853, 4.651, 4.4119, 5.0896, 6.3432, 6.1079, 7.2978, 5.8408, 6.2011, 5.5613, 5.2277, 4.2151, 3.4789, 3.4442, 2.0588, 1.9322, 2.2446, 3.6563, 5.8458]

x = np.array(x) 
y = np.array(y) 

""" Ajuste da curva a um polinômio """
p = np.polyfit(x,y,5)#(x,y, grau do polinomio)
#printar de tras pra frente

print(p)