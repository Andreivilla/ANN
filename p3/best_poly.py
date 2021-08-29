import numpy as np

""" Dados de Entrada """
x = [-4.4581, -4.1967, -4.0744, -3.9344, -3.6704, -3.4103, -3.2963, -3.1565, -2.9236, -2.7075, -2.5554, -2.3217, -2.1371, -2.0491, -1.8358, -1.6212, -1.4872, -1.3252, -1.1095, -0.9041, -0.8386, -0.5164, -0.4595, -0.1728, 0.0098, 0.1938, 0.2546, 0.5264, 0.6402, 0.8709, 1.0325, 1.3279, 1.4636, 1.6441, 1.8865, 2.049, 2.195, 2.3404, 2.516, 2.753, 2.9296, 3.1116, 3.2705, 3.4463, 3.6099, 3.8521, 3.9867, 4.2011, 4.2861, 4.55, 4.7496, 4.9608]
y = [3.2465, 4.0738, 3.8717, 5.3375, 4.5334, 6.3388, 6.7974, 6.6615, 7.081, 6.703, 8.5353, 6.4242, 6.2324, 5.2943, 6.1225, 5.432, 5.3417, 6.5067, 5.5866, 4.965, 4.93, 4.2939, 4.8055, 4.1253, 4.5778, 4.5174, 4.6258, 4.5606, 4.7349, 4.9161, 5.0335, 5.4052, 5.6808, 5.9025, 6.1887, 6.3929, 7.0885, 6.9632, 7.7312, 7.9177, 8.2825, 6.4847, 8.4961, 8.8768, 8.9412, 8.4731, 8.7221, 8.3048, 8.0485, 7.4429, 6.4697, 5.1175]
x = np.array(x) 
y = np.array(y) 

""" Ajuste da curva a um polinômio """
#p1 = np.polyfit(x,y,1)  
p2 = np.polyfit(x,y,2)  
p3 = np.polyfit(x,y,3) 
p4 = np.polyfit(x, y, 4)
p5 = np.polyfit(x, y, 5)

""" Rotina para determinação do valor de R da equação da reta """
#from scipy import stats
#slope,intercept,r_value,p_value,std_err = stats.linregress(x,y)

""" Cálculo dos coeficientes de determinação dos polinômios de ordem 2 e 3 """
yfit2 = p2[0] * pow(x,2) + p2[1] * x + p2[2] 
yresid2 = y - yfit2 
SQresid = sum(pow(yresid2,2)) 
SQtotal = len(y) * np.var(y) 
R2_2 = 1 - SQresid/SQtotal 

yfit3 = p3[0] * pow(x,3) + p3[1] * pow(x,2) + p3[2] * x + p3[3] 
yresid3 = y - yfit3 
SQresid = sum(pow(yresid3,2))
SQtotal = len(y) * np.var(y) 
R2_3 = 1 - SQresid/SQtotal 

#yfit4 = p4[0] * pow(x,4) + p4[1] * pow(x,3) + p4[2] * pow(x,2) + p4[3] * x + p4[4]



""" Impressão dos Resultados """
#print('Equação da reta')
#print('Coeficientes',p1,'R2 =',pow(r_value,2))
#inverter a ordem do array
print('Polinomio de ordem 2')
print('Coeficientes',p2,'R2 =',R2_2) 
#a3 a2 a1 a0
print('Polinomio de ordem 3')
print('Coeficientes',p3,'R2 =',R2_3) 

print('Polinomio de ordem 4')
print('Coeficientes',p4) 

print('Polinomio de ordem 5')
print('Coeficientes',p5)