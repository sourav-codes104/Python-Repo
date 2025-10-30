import math
num = int(input("Enter any number: "))
is_prime = True
for i in range(2,int(math.sqrt(num))+1):
    if num % i == 0:
        is_prime  = False
        break

if is_prime:
    print("Prime number")

else:
    print("Non-Prime number")
