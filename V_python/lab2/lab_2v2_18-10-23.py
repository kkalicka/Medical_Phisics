import random
import math

# circle equatuion  (x−a)2+(y−b)2=r2
# for a, b = 0, r^2 = 1: x^2+y^2=1 -> y^2 = 1 - x^2

def precision(number):
    return number/math.pi

def manual_calculate_pi(number):
    
    circle_points = 0
    
    for i in range(1, number+1):
        point_x = random.uniform(-1, 1)
        point_y = random.uniform(-1, 1)
        
        # chceck if point is in circle
        if point_y**2 + point_x**2 < 1:
            circle_points = circle_points + 1
    
    return 4*(circle_points/number)

"""
for i in range(1,101):
    print("i = ", i, " ", "%.6f"%manual_calculate_pi(i), "%.6f"%(manual_calculate_pi(i)/math.pi))
    
for i in range(3,7):
    print("i = 10 ^", i, " ", "%.6f"%manual_calculate_pi(10**i), "%.6f"%(manual_calculate_pi(10**i)/math.pi))
"""

f = open('lab_2v2.txt', 'w')

for i in range(1,101):
    manual = manual_calculate_pi(i)
    f.write(str(i) + ": " + str(manual) + "    |||   " + str(manual/math.pi)+"\n")
    
for i in range(3,7):
    manual = manual_calculate_pi(10**i)
    f.write("10 ^" + str(i) + ": "+ str(manual)+ "    |||   " + str(manual/math.pi)+"\n")

f.close()