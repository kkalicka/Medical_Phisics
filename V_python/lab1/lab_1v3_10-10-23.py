def check_if_even(number):
    return number%2 == 0

def check_if_prime(number):
    if number < 2: return False
    if number == 2: return True
    for i in range(2, int((number+3)/2)):
        if number%i == 0:
            return False
        return True

print("Choose your number")
x = int(input())
print(f"Is your number even? {check_if_even(x)}")
print(f"Is your number odd? {check_if_even(x)==0}")
print(f"Is your number prime? {check_if_prime(x)}")