import numpy as np
X = [x_value for i in range(0, 61) for x_value in [i*2*np.pi/60]]
Y = [y_value for i in range(0, 61) for y_value in [int(60*np.sin(X[i]))]]

for i in range(0, 61):
    if Y[i] > 0:
        print("+"*Y[i])
    if Y[i] < 0:
        print("-"*(-Y[i]))
    if Y[i] == 0:
        print(0)
