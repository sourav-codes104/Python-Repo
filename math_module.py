import math as m
result=pow(2,5)
print(m.pi)
print(m.e)
print(result)
print(m.sqrt(9))

print("Pythagoras Theorem")
base = int(input("Enter the value of base: "))
perpendicular =  int(input("Enter the value of perpendicular: "))
hypotenuse = int(input("Enter the value of hypotenuse: "))
lhs = m.sqrt(pow(base,2)+ pow(perpendicular,2))
rhs = hypotenuse
if lhs == rhs:
    print("Right angle triangle")
else:
    print("Not right angle triangle")