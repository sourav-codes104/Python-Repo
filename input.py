name = input("Enter Your name : ") # if not described interpreter will understand the input as
print(type(name))                  # a default string input always

age = int(input("Enter your age : "))
print(type(age))

print("Program to calculate area of circle")

rad = int(input("Enter the area of radius of a circle: "))
area = rad*rad*(22/7)
print(f"The area of circle is {area}")
