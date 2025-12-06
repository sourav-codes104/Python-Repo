# nums = [1,4,5,5,2,1,8,9,1,8]

# seen = {}

# for num in nums:
#   if num in seen:
#     seen[num]+=1
#   else:
#     seen[num]=1

# print(seen)

#hashing of characters:

str = "mississippi"
seen={}
for s in str:
  if s in seen:
    seen[s]+=1
  else:
    seen[s]=1

print(seen)