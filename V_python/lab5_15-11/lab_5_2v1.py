import numpy as np
import random


# chciałabym, żeby ten kod w obliczał prawdopodobieństwo, że w pokoju w którym znajduje się n osób przynajmniej 2 znich mają urodziny. chcę użyć wyrażenia podobnego do:

a = np.array([1,2,3,4])
b = np.array([10,20,30])
b = b[:, np.newaxis]
print(a+b)
print(a>b)
print(a==b)

n_people = 27
room_b = np.array(np.random.randint(0, 365, size = n_people, ))
b = room_b[:, np.newaxis]
print(b)

for n_people in range(2, 27):
    probability = 0
    for _ in range(2000): 
        room_b = np.array(np.random.randint(0, 365, size = n_people, ))
        b = room_b[:, np.newaxis]

        if n_people > len(np.unique(b)):
            probability += 1

    print(f"{n_people}) probability: {probability/2000}")
    
    
"""
for n_people in range(2, 27):
    probability = 0
    for _ in range(1000): 
        room = np.random.randint(0, 365, size = n_people, )
        room_b = np.random.randint(0, 365, size = n_people, )
        if n_people > len(np.unique(room)):
            probability += 1

    print(f"{n_people}) probability: {probability/1000}")
"""


"""
for n in range (2, 365):
    probability = 0
    for j in range(1, 2000):
        for i in range(1, n): a.append(random.randint(1,365))
        b = a[:, np.newaxis]
        if(a==b): probability = probability + 1
    print(print(f"{n}) probability: {probability/2000}"))
"""
