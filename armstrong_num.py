# Armstrong Number :Sum of each digit raised to the 
#                  power of total digits = original number
# example: 153 -> 1^3+5^3+3^3 = 1+125+27=153



num = int(input("Enter any number: "))
temp = num
no_of_digit=0
while temp != 0 : 
    no_of_digit+=1 
    temp = temp//10 
temp = num
total = 0
while temp != 0:
    rem = temp%10 # 3
    total += rem**no_of_digit
    temp=temp//10

print("Armstrong number" if num == total else "Not an armstrong number")