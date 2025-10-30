#fibonacci series : Fibonacci series ek aisi number series hoti hai jisme:

# har naya number apne pehle do numbers ka sum hota hai.

# 🔹 Formula:𝐹(𝑛)=𝐹(𝑛−1)+𝐹(𝑛−2)


first = 0
second = 1
n = 10
print(first)
print(second)
for i in range (n-2):
    third = first + second
    print(third)
    first = second
    second = third

