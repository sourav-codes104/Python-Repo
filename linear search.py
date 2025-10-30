# line = [1,2,3,4,5,6]
# target = int(input("Enter the target: "))
# for num in line:
#     if target == num:
#         print(f"Target found")
#         break
# else:
#     print("target not found")
line = [1,2,3,4,5]
target = int(input("Enter the target: "))
def lin_search(arr,target):
    for num in arr:
        if target == num:
            return True

    return False

if lin_search(line,target):
    print(f"Target found")
else:
    print("Target not found")