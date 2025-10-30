# typecasting  = The process of converting a value of one data type to another
#                (string, integer, float, boolean)
#                Explicit vs Implicit
name = "Sourav Singh"
Year = 3
GPA = 7.58
student = True

print(type(name))
print(type(GPA))
print(type(student))
print(type(Year))

print("------------------")

name = bool(name)
GPA = str(GPA)
print(type(name))
print(type(GPA))
print(type(student))
print(type(Year))

print("------------------")
a = 5
b = 5.5
print(a/b)
c = type(a/b)
print(c)