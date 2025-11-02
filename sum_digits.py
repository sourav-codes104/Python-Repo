# 1234 = 4+3+2+1 = 10
# abcd % 10 = d

num = int(input("Enter any number: "))

sum = 0
while num != 0:
    sum = sum + num%10 #1234%10=4 
     
    num //= 10   #num=123

print(sum)