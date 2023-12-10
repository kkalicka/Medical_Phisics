def check_if_perfect(number):
    factor_sum = 0
    for factor in range(1, number):
        if number%factor==0:
            factor_sum = factor_sum+factor
    return factor_sum == number

Perfect_List = []
i = 1
for i in range(1,10000):
    if check_if_perfect(i):
        Perfect_List.append(i)

print(Perfect_List)
print(sum(Perfect_List))

"""
while len(Perfect_List)<4:
    if check_if_perfect(i):
        Perfect_List.append(i)
""" 
