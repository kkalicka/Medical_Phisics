import matplotlib.pyplot as plt
import numpy as np

x0 = 0
x = 0
y0 = 0
y = 0

data_x = [0]
data_y = [0]

for i in range(0, 10**6):
    random_number = np.random.randint(1, 101, 1)
    if random_number < 86:
        x = 0.85*x + 0.04*y
        y = -0.04*x0 + 0.85*y + 1.6 
        
    if 85 < random_number < 93:
        x = 0.2*x - 0.26*y
        y = 0.23*x0 + 0.22*y + 1.6 
        
    if 93 < random_number < 100:
        x = -0.15*x + 0.28*y
        y = 0.26*x0 + 0.24*y + 0.44 
        
    if random_number > 99:
        x = 0
        y = 0.16*y
    data_x.append(x)
    data_y.append(y)
    x0 = x
    
plt.rcParams['font.size'] = 10
plt.plot(data_x, data_y, ',', color = 'g')
plt.plot([0, 3, 3, 0, 0], [6, 6, 9, 9, 6], color = 'r')
plt.axis([-3, 3, 0, 10])
plt.savefig("lab6_ex_1.png", dpi=400)
# wyswietlenie wykresu
plt.show()
