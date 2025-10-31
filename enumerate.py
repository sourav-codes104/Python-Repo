subject = ["IOt", "Network-Security", "Operating System", 
           "Minor", "ADA", "EOI"]

for i in range(len(subject)): #value as well as index both are in picture
    print(subject[i])

print("--------------------------")

for sub in subject: #value based loop; focuses only on value
    print(sub)

print("--------------------------")

for i , value in enumerate(subject):
    print(i,value)
