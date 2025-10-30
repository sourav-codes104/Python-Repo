# Decorator = A function that extends the behavior of another function
#             w/o modifying the base function
#             Pass the base function as an argument to the decorator

def decorator(cunc):
    def wrapper():
        print("Butterfly phase")
        cunc()
        print("Breakup phase")
    return wrapper

@decorator
def love():
    print("I love you")

love()
print("---------------")
@decorator
def hate():

    print("I hate you")

hate()




