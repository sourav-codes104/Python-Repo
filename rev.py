#1234 = 4321

num = int(input("Enter any number: "))
rev = 0
rem = 0
while num != 0:
    rev  = rev*10+(num%10)
   
    num//=10

print(rev)