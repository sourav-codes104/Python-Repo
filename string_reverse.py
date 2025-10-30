example = input("Enter any number/string: ")
chars = list(example)

i = 0
j = len(chars)-1

while i < j:
    chars[i],chars[j]=chars[j],chars[i]
    i+=1
    j-=1

rev_string="".join(chars)

# Python shortcut version using slicing of string
#[start:stop:step] note: stop index will excluded
print(example[:4:2])

if example == rev_string:
    print("Palindrome")

else:
    print("Not-Palindrome")