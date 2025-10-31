class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head=None

    def add(self,data):
        newnode = Node(data)
        if self.head:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = newnode
        else:
            self.head = newnode

    def disp(self):
        temp = self.head
        while temp != None:
            print(f"{temp.data}->",end="")
            temp = temp.next
        print("None")
obj1 = LinkedList()
n=int(input("Enter total number of nodes you want to create: "))
for i in range(n):
    value=int(input(f"Data for node {i+1}: "))
    obj1.add(value)

obj1.disp()
