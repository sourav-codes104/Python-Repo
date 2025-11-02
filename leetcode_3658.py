n=int(input("enter any number: "))
odd_sum=n*n
even_sum=n*(n+1)

print(even_sum)
print(odd_sum)

gcd = 1
for i in range(1,min(odd_sum,even_sum)+1):
    if odd_sum%i==0 and even_sum%i==0:
        gcd=i
print(gcd)
        