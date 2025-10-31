word = input("Enter any word: ")
word=word.lower()
count_of_vowel = 0
count_of_consonant = 0
for char in word:
    if char in "aeiou":
        count_of_vowel +=1
    elif char.isalpha():
        count_of_consonant +=1
#total occurences
print(count_of_vowel)
print(count_of_consonant)

#unique occurences
vowel = set()
consonant = set()
for char in word:
    if char in "aeiou":
        vowel.add(char)
    elif char.isalpha():
        consonant.add(char)

print(vowel)
print(consonant)