n = int(input("Enter how many prime numbers you want: "))
num = 2
count = 0

import math
while count < n:
    is_prime = True
    for i in range(2,int(math.sqrt(num))+1):
        if num % i == 0:
            is_prime = False
            break
    
    if is_prime:
        print(num,end=" ")
        count +=1
    
    num+=1

