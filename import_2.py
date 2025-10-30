import random

secret = random.randint(0,100)

count=0

while True:
    num = int(input("Choose any number: ")) 
    count+=1
    if secret == num:
        print("Oh wow correct guess you won")
        break
    elif secret > num:
        print("Oh no wrong answer try a little bit higher number")
    else:
         print("Oh no wrong answer try a little bit lower number")
    
print(f"You have guessed right number after {count} chances")