class Stack:

    def __init__(self): #makeEmpty
        self.elements = []

    def __len__(self):
        return len(self.elements)
    
    #Boolean function, returns true if the stack is not empty.
    #Is to be used in place of isEmpty
    def __bool__(self):
        return bool(self.elements)

    #Allows us to do this: stack += 1 and 1 is put at the top of the stack
    def __iadd__(self,other):
        self.elements.append(other)
        return self

    #Allows us to pop n times the stack using stack -= n
    def __isub__(self, other):
        for i in range(other):
            self.elements.pop()
        return self
    
    def __str__(self):
        return str(self.elements)
    
    #Removes count elements from the stack 
    #and returns them in a generator object
    def pop(self, count = 1):
        for element in range(count):
            yield self.elements.pop()
    #Get the topmost element.
    def peek(self):
        return self.elements[len(self)-1]
    
    #Empties itself by creating a new list.
    def make_empty(self):
        self.elements = []
        return self

u = Stack()
for x in range(20):
    u += x
print(u)
u -= 4
print(u)
print(u.peek())
u += 1
print(u)
print(u.peek())
for x in u.pop(5):
    print(x)
print(u)
