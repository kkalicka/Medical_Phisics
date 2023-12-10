"Using list comptahension generate a list of all odd numbers from 0 to 1000 that contain 1 one 5"
"odds numbers are numbers that are n=1+i*2"
odd_numbers_with_15 = [number for number in range(1, 1001, 2) if '1' in str(number) and '5' in str(number)]

print(odd_numbers_with_15)