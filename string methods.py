# 1 find() = it will find the first occurrence of the letter in a string if the letter is not present
#            it will return -1 otherwise its first occurred index.

n = input("Enter anything: ")
a = n.find("n")
print(a)

# 2 rfind() = it will find the last occurrence of the letter in a string if the letter is not present
#             it will return -1 otherwise its last occurred index.

b = n.rfind("n")
print(b)

# 3 capitalize() = make the first letter capital of the string

c = n.capitalize()
print(c)

# 4 upper() = convert the whole string in uppercase

d = n.upper()
print(d)

# 5 lower() = convert the whole string in lowercase

e = n.lower()
print(e)

# 6 isdigit() = return true if the string contains only numbers otherwise false

f = n.isdigit()
print(f)

# 7 isalpha() = return true if the string contains only alphabets otherwise false

g = n.isalpha()
print(g)

# 8 count() = count the total number of times a selected character occurring in a string

h = n.count("n")
print(h)

# 9 replace() = replace the old character from a new character

i  = n.replace("y","m")
print(i)