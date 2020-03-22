import math
import matplotlib.pyplot as plt
from random import *
import time
import numpy as np

n = 8 # число гармонік в сигналі
Wmax = 1000 # гранична частота
N = 256 # число дискретних відліків

x = [0 for i in range(N)] # масив сигналів

# Генерація сигналів
start = time.time()
for i in range(n):
    A = uniform(0, 1)
    F = uniform(0, 1)
    for j in range(0, N):
        x[j] += A * math.sin(Wmax / n * j * i + F)

end = time.time()
print("Час генерації сигналів",end - start)

#Таблиця коефіцієнтів
w= np.zeros((int(N/2), int(N/2)))
for i in range(int(N/2)):
    for k in range(int(N/2)):
        w[i][k] = math.cos(4*math.pi/N * i * k ) + math.sin(4 * math.pi/N * i * k)

#Нові коефіцієнти для швидкої збірки
w_new = [0 for i in range(N)]
for i in range(N):
    w_new[i] = math.cos(2*math.pi/N * i ) + math.sin(2 * math.pi/N * i)

start = time.time()
F_I = [0 for i in range(int(N/2))]
F_II = [0 for i in range(int(N/2))]
F = [0 for i in range(int(N))]          #Функція після швидкої збірки

for p in range(int(N/2)):
    for k in range(int(N/2)):
        #Для парних
        F_II[p] += x[2 * k] * w[p][k]
        #Для  непарних
        F_I[p] += x[2 * k + 1] * w[p][k]


for p in range(N):
    if p < (N/2):
        F[p] += F_II[p] + w_new[p] * F_I[p]
    else:
        F[p] += F_II[p - int(N/2)] - w_new[p] * F_I[p - int(N/2)]

end = time.time()
print("Час ШПФ", end - start)

plt.plot(range(0, N), F)
plt.show()



