# one task few components
"""
write the function that calculate factorial (only for int and half)
for half calculating factorial:
(1/2)! = sqrt(pi/2)
(3/2)! = 3/2 * (1/2)!
funkcja obliczająca silnię dla połówek liczb (np. 1/2) oraz dla liczb całkowitych w pythonie
"""
import numpy as np

def factorial(number):
    if number % 1 == 0:
        return int_fac(number)
    else:
        return half_fac(number)

def half_fac(number):
    if number * 2 > 1:
        return number* half_fac(((number*2 - 2)/2))
    else:
        return np.sqrt(np.pi) / 2

def int_fac(number):
    if number > 1:
        return number * int_fac(number - 1)
    else:
        return 1

def V_math(number):
    return (np.pi**(number/2))/factorial(number/2)


h_in_circle = 0

for i in range(2, 21):
    
    random_matrix = np.random.uniform(-1, 1, size=(i, 10**6))
    sum_of_squares = np.sum(random_matrix**2, axis=0)
    h_in_circle = np.sum(sum_of_squares < 1)
    
    V_cal = (2**i)*h_in_circle/10**6
    print(f"{i}: V_cal={V_cal}; V_cal/V_math={V_cal/V_math(i)}; n_of_hits; h_in_circle={h_in_circle}")

    
    