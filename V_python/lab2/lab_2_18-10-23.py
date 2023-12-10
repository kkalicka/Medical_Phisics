import math
import numpy

def manual_calculate_pi(number):
    
    pi_result = 0
    for i in range(1, number+1):
        if i%2 == 0:
            pi_result = pi_result-1/(2*i-1)
        else:
            pi_result = pi_result+1/(2*i-1)
            
    return pi_result*4


f = open('lab_2v1.txt', 'w')

for i in range(1,101):
    f.write(str(i) + ": " + str(manual_calculate_pi(i)) + "    |||   " +str(manual_calculate_pi(i)/math.pi)+"\n")

for i in range(3,8):
    f.write("10 ^" + str(i) + ": "+ str(manual_calculate_pi(10**i))+ "    |||   " + str(manual_calculate_pi(10**i)/math.pi)+"\n")

f.close()