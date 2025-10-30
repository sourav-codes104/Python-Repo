# conditional expression = A one line shortcut for the if-else statement (ternary operator)
#                          Print or assign one of two values based on condition
#                          X if condition else Y

num = int(input("Enter any number: "))
def pos_neg(n):
    print("Positive" if n >0 else "Negative")



def even_odd(n):
    print("Even" if n%2==0 else "Odd")

even_odd(num)
pos_neg(num)