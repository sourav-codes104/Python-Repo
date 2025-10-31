zeroes = [0,45,32,0,68,0,1]
#o/p = [45,32,68,1,0,0,0]

i = 0
for j in range(0,len(zeroes)):
    if zeroes[j] != 0:
        zeroes[i],zeroes[j] = zeroes[j],zeroes[i]
        i+=1
print(zeroes)