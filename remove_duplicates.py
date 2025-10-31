result = [1,2,2,3,4,3,2,5,1,6]

i = 0
result.sort()


for j in range(1,len(result)):
    if result[i] != result[j]:
        i+=1
        result[i] = result[j]
        

print(result[:i+1])

new_meth = set(result)

print(new_meth)

