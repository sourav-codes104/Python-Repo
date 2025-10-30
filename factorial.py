# x = int(input("Enter any number: "))

# def fact(num):
#     if num == 1 or num  == 0:
#         return 1
#     return num*fact(num-1)

# c=fact(x)
# print(c)

x = int(input("Enter any number: "))
fact = 1
for i in range(1, x + 1):
    fact *= i
print(fact)
