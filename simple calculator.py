print("Here you can perform simple operations such as + - * /")
sign = input("Enter the sign of operation you want to perform: ")
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

if sign == "+":
    print(f"Addition of {a} and {b} is : {a+b}")
elif sign == "-":
    print(f"Substraction of {a} and {b} is : {a-b}")
elif sign == "*":
    print(f"Multiplication of {a} and {b} is : {a*b}")
elif sign == "/":
    print(f"Division of {a} and {b} is : {a/b}")
else:
    print("Invalid Operation")