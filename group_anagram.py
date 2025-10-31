#anagram = Do words jinke characters same ho, bas order alag ho.
#"eat", "tea", "ate" → ek group
#"bat" → alag group

words = ["eat", "tea", "tan", "ate", "nat", "bat"]
#o/p = [["eat","teat","ate"],["tan","nat"],["bat"]]

anagram = {}

for word in words:
    key = "".join(sorted(word))  #aet

    if key in anagram:
        anagram[key].append(word)

    else:
        anagram[key] = [word]

print(anagram.values())
print(anagram)

#valid anagram 
#if two strings are equal
def valid_anagram():
    spell1 = "tea"
    spell2 = "eat"

    spell1=sorted(spell1)
    spell2=sorted(spell2)
    
    return True if spell1 == spell2 else False

print(valid_anagram())

