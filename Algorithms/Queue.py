class Queue:

    def __init__(self): #makeEmpty
        self.elements = []

    def __len__(self):
        return len(self.elements)
    
    #Boolean function, returns true if the Queue is not empty.
    #Is to be used in place of isEmpty
    def __bool__(self):
        return bool(self.elements)

    #Allows us to do this: Queue += 1 and 1 is put at the top of the Queue
    def __iadd__(self,other):
        self.elements.insert(other)
        return self

    #Allows us to pop n times the Queue using Queue -= n
    def __isub__(self, other):
        for i in range(other):
            self.elements.pop()
        return self
    
    def __str__(self):
        return str(self.elements)
    
    #Removes count elements from the Queue 
    #and returns them in a generator object
    def pop(self, count = 1):
        for element in range(count):
            yield self.elements.pop()
    #Get the topmost element.
    def peek(self):
        return self.elements[0]
    
    #Empties itself by creating a new list.
    def make_empty(self):
        self.elements = []
        return self

u = Queue()
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
