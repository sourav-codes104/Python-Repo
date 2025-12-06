#what is resursion ?
#when a function class itself.

# def fun(n):
#   if n == 0:return
#   print("*")
#   n-=1
#   fun(n)
# n = 5
# fun(n)

# def fact(num):
#   if num==1 or num==1: return 1

#   return num*fact(num-1)

# c=fact(6)
# print(c)

# num=5
# fact=1
# i=1
# while i<=num:
#   fact = fact*i
#   i+=1

# print(fact)

# def fun(num):
#   if num == 0:
#     return
  
#   fun(num-1)
#   print(num)
# fun(5)


# arr=[1,2,3,4,5]
# arr[::-1]
# print(arr)
# def rev(arr,i,j):
#   if i>j:return
#   arr[i],arr[j]=arr[j],arr[i]
#   i+=1
#   j-=1
#   rev(arr,i,j)
# rev(arr,0,len(arr)-1)
# print(arr)
# def insert(arr,last):
#   if len(arr)==0:
#     arr.append(last)
#     return

# def rev(arr):
#   if len(arr)==0:
#     return 
#   last=arr[0]
#   arr.pop()
#   rev(arr)
#   insert(arr,last)

# for a in arr:
#   print(a)

# str = "nayan"
# def rev(str,i,j):
#   if i>j:return True
#   if str[i] != str[j]:
#     return False
#   i+=1
#   j-=1  
#   return rev(str,i,j)
  
  

# c=rev(str,0,len(str)-1)
# print(c)

# def fib(term):
#   if term==0: return 0
#   if term==1: return 1
#   return fib(term-1)+fib(term-2)
  

# print(fib(20))


# n=int(input())
# res=[]
# for i in range(n):
#     res.append(int(input())),end=""
# print(res)


res=[-5 ,-2 ,-9, -1]
curr_sum = 0
best_sum=0
for i in range(len(res)):
  curr_sum=curr_sum+res[i]
  if curr_sum > best_sum:
    best_sum=max(curr_sum,best_sum)
  if curr_sum < 0:
    curr_sum=0

print(best_sum)