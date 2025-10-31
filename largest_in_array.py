rank = [1,2,4,8,3,4,5]

largest = rank[0]

for j in range(len(rank)):
    if rank[j] > largest:
        largest = rank[j]

print(largest)

