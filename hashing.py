# # n = [5,3,2,2,1,5,5,7,5,10]
# # hash = [0]*13

# # for i in range(0,len(n)):
# #   hash[n[i]] += 1

# # query = int(input("Enter number of queries: "))

# # while(query):
# #   num = int(input("Enter the number: "))
# #   print(num,":",hash[num])
# #   query-=1


# #hashing of characters

# str = "mississippi"

# hash=[0]*26

# for char in str:
#   ascii_value=ord(char)
#   index=ascii_value-97
#   hash[index]+=1

# query = 5

# while(query):
#   ch = input("Enter any character: ")
#   index = ord(ch)-97
#   print(ch,":",hash[index])
#   query-=1

n = int(input())
A = []
for i in range(n):
    A.append(int(input()))


def chest(A):
    j = 0
    for i in range(len(A)):
        if A[i] != 0:
            A[i], A[j] = A[j], A[i]
            j += 1
    return A

print(chest(A))