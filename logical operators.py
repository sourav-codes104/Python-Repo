# logical operators = used on conditional statements.
# and = check two or more conditions if true
# or = check if at least one condition is true
# not = True if condition is false and vice versa true

temp = int(input("Enter the temperature of your room: "))
def temp_room(temp):
    if temp >= 18 and temp <= 25:
        print("you are living in a perfect environment")
    elif temp < 18 or temp >25:
        print("you need to change the environment")

temp_room(temp)

def water(temp):
    if not temp <= 100:
        print("boiling point of water my boy")
    elif not temp >= 0:
        print("freezing point of water my girl")

water(temp)