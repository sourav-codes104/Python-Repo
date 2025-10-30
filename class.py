# Class → A design or recipe.
# Object → The real thing made from that design.
# 🧁 Example:
# Class = Cake recipe
# Object = The actual cake you bake using that recipe

class Stack:
    def __init__(self):
        self.stack=[]
    
    def push(self,item):
        self.stack.append(item)
        print(f"Pushed item:{item}")

    def is_empty(self):
        if len(self.stack)==0:
            return True
        
    def pop(self):
        if self.is_empty():
            print("stack is underflowing")
        pop_item=self.stack.pop()
        print(f"Poped item:{pop_item}")

    def peek(self):
        if self.is_empty():
            print("stack is underflowing")
        print(f"The peek element of stack is:{self.stack[-1]}")

    def display(self):
        print(f"Current stack:{self.stack}")

obj1 = Stack()

obj1.push(34)
obj1.push(28)
obj1.push(67)
obj1.push(54)
obj1.display()
obj1.pop()
obj1.peek()
obj1.display()




