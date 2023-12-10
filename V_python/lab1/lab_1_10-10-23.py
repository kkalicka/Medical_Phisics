def sum_elements(list):
    sum = 0
    for i in list: sum = sum + i
    return sum

List_1 = [2,2,3,4]
print(sum_elements(List_1))

# List comprehensions
x = 0
L = [x for x in range(1, 10) if x%2==0]
print(L)

# eval -> string is interprete as python code
# False in python: None, False, 0, [], ''

L1 = [1,2,3]
L2 =[3,4,5]
L3 = [6,7,8]
Lzip = zip(L1, L2, L3)
print(Lzip)
for j,k,z in Lzip: print(j+k+z)

# Recomended: [f(x) for x in L]
# filter(f1, L)