# 1-365!/365*365 = 1-364!/365
# a^2+b^2=c^2
import numpy as np

f = open('lab_5v1.txt', 'w')
for number_a in range(1, 150):
    for number_b in range(number_a, 150):
        for number_c in range(number_b, 151):
                if number_a**2 + number_b**2 == number_c**2:
                    f.write(f"{number_a} {number_b} {number_c}\n")
f.close()

f = open('lab_5v2.txt', 'w')
for number_a in range(1, 150):
    for number_b in range(number_a, 150):
        for number_c in range(number_b, 151):
            if number_a**3 + number_b**3 == number_c**3:
                f.write(f"{number_a} {number_b} {number_c}\n")
f.close()

f = open('lab_5v3.txt', 'w')
for number_a in range(1, 150):
    for number_b in range(number_a, 150):
        for number_c in range(number_b, 150):
                if number_a**4 + number_b**4 == number_c**4:
                    f.write(f"{number_a} {number_b} {number_c}\n")
f.close()

