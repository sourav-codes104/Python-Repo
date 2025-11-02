arr = [4,12,9,7,3]
#o/p = [3,4,7,9,12]

for i in range(len(arr)):
    smallest = i
    for j in range(i+1,len(arr)):
        if arr[j] < arr[smallest]:
            smallest  = j
    arr[i],arr[smallest] = arr[smallest],arr[i]

print(arr)