# if statement
# The if statement tests a condition.
# If the condition is True, the block inside runs.
# If it’s False, Python skips it

# elif (else if) statement
# Used when you have multiple conditions.
# Runs only if all previous conditions are False and the current one is True.
# You can have multiple elifs.

# else statement
# Acts as a default block.
# Executes when all previous conditions are False.
# You can only have one else at the end.

age = int(input("Enter your age: "))
if age >= 18:
    print(f"Congratulations you are eligible to vote since you are {age} years old.")
else:
    print(f"Sorry you need to wait until you are 18 or more than 18.")