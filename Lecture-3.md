# Abstract Data types
  
___
# Table of Contents:
  
1. [Basic Datatypes](#basic-datatypes )
2. [Examples](#examples )
3. [Integers](#integers )
4. [Priority Queue](#priority-queue-adt )
5. [List](#lists )
6. [Stack](#stack-adt )
    1. [Stack in Python using lists](#stack-in-python )
7. [LinkedLists](#linkedlists )
   1. [Singly LinkedList](#singly-linkedlists )
      1. [Sindly LinkedList in Python](#singly-linkedlist-in-python )
   2. [Cyclical List](#cyclical-list )
      1. [Cyclical List in Python](#cyclicallist-in-python )
  
## Basic Datatypes
  
  
* Integers
  * Boolean
  * Char
  * Short
* Double
* Float
  
## Abstract Datatypes
  
  
An abstract Datatype is a mathematical model that consists of 1 or more fields, a set of operations to manipulatethe fields. In abstract Datatypes, we only care about the definition of the ADT and not the underlying implementation.
  
### Examples
  
  
#### Integers
  
  
Integers along with these functions <img src="https://latex.codecogs.com/gif.latex?&#x2F;"/>,<img src="https://latex.codecogs.com/gif.latex?*"/>,<img src="https://latex.codecogs.com/gif.latex?+"/>,<img src="https://latex.codecogs.com/gif.latex?-"/> consist a datatype. In order to use it, we need to know all of the available operations. We don't need,however to know how an integer is represented by a language or a computer.
  
The same principle is applied to floats and doubles.
  
#### Priority Queue ADT
  
  
A priority queue is an abstract datatype that uses a set of elements, representiing a key, ex. ```key=int```, ```key=char```, ```key=(int,int)```.
  
A priority queue implements the following operations:
  
* Create an empty priority queue
* Check if the queue is empty
* Enqueue element k
* Dequeue smallest element.
  
An ADT can be implementent using other Datatypes, for example, a priority queue can be implemented using Lists, Trees, etc.
  
#### Lists
  
  
A list is a sequence of elements.$$\Lambda = a_1,a_2,a_3,...,a_n$$
  
* Every element in the list is called a Node. 
* Using $\Lambda[i]$ we denote the $i_{th}$ node in the list.
* Length of $\Lambda$ is the number of elements in the list and is presented as$|\Lambda|$.
* When $|\Lambda| = 0$ then we talk about an empty list that is denoted using $\langle\rangle$.
  
A list contains the following operations:
  
* Create a new list
* Add a new element
* Remove an element
* Find a specific element
* Sort on a condition
  
The most important operations in a list, are the insertion and removal of the first and last element as they take constant time = $O(1)$
  
Two common list types are:
  
* Stacks
* Queues
  
#### Stack ADT
  
  
A stack has the following set of operations.
|Operation|Description|
|-|-|
|makeEmpty()| Create an empty stack
|isEmpty() | Return ```True``` if the stack is empty otherwise, ```False```
|push(x) | Add X to the top of the stack
|pop() | Remove the element at the top of the stack and return it.
|top() | Peek the element at the top of the stack
|size()| Return how many elements are in the stack.
  
Stack operations are bound by the following rules:
  
|Operation|Result|
|-|-|
|```isEmpty(makeEmpty)``` |  ```True``` |
|```isEmpty(push(x))``` |```False```|
|```pop(makeEmpty)```| Error|
|```pop(push(x))```|x|
|```top(makeEmpty())```| Error|
|```top(push(x))```|x|
  
##### Stack In Python
  
```Python
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
  
```
  
A simple stack implementation in Python using the builtin list ADT. Code [here](./Algorithms/Stack.py ).
  
A stack can also be implemented using arrays. Depending on the implementation however, a stack using arrays may have <img src="https://latex.codecogs.com/gif.latex?O(n)"/> insertion and removal when the initial capacity of the array is reached and all elements will have to be migrated in a new array. 
  
An easy workaround is using *lazy migration*. When the initial capacity is reached, instead of migrating all elements, we can migrate another element when a new operation is done to the stack.
  
#### Queue ADT
  
  
A queue has the following set of operations.
|Operation|Description|
|-|-|
|makeEmpty()| Create an empty queue
|isEmpty() | Return ```True``` if the queue is empty otherwise, ```False```
|enQueue(x) | Add X to the top of the queue
|deQueue | Remove the element at the top of the queue and return it.
|top() | Peek the element at the front of the queue
|size()| Return how many elements are in the queue.
  
Queue operations are bound by the following rules:
  
|Operation|Result|
|-|-|
|```isEmpty(makeEmpty)``` |  ```True``` |
|```isEmpty(enQueue(x))``` |```False```|
|```deQueue(makeEmpty)```| Error|
|```deQueue(enQueue(x))```| ```y``` if queue has more than 1 element else ```x```.
|```top(makeEmpty())```| Error |
|```top(push(x))```| ```y``` if queue has more than 1 element else ```x```|
  
  
##### Queue in Python
  
```Python
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
  
```
  
Code [here](./Algorithms/Queue.py ).
  
#### LinkedLists
  
  
LinkedLists use dynamic memory allocation where they use memory when a new element is added into the list.
  
##### Singly LinkedLists
  
In a SLL a node contains a single pointer to the next element and is unaware of the previous elements.
  
##### Singly LinkedList in Python
  
```Python
class Node:
    def __init__(self, content=None, next=None):
        self.content, self.next = content, next
  
    def has_next(self):
        return bool(self.next)
  
    def search(self, content):
        if self == content:
            return content
  
        if bool(self.next):
            return self.next.search(content)
  
        return None
  
    def remove_next(self):
        if bool(self.next):
            self.next = self.next.next
  
    def __delitem__(self, content):
  
        if self.next == content:
            self.remove_next()
            return
  
        del self.next[content]
        return
  
    def __repr__(self):
        return str(self.content)
  
    def __eq__(self, content):
        return self.content == content
  
    def __bool__(self):
        return self.content is not None
  
    def __reversed__(self):
        print("trying to reverse")
        if bool(self.next):
            self.next.reversed()
            print("trying to reverse")
        print("trying to reverse")
        yield self
class LinkedList:
    def __init__(self):
        self.root = Node()
        self.bottom = self.root
  
    def __len__(self):
        func = lambda x, node: x if node.content is None else func(x + 1, node.next)
        return func(0, self.root)
  
    def __repr__(self):
        return str([x for x in self])
  
    def __sub__(self, other):
        l = LinkedList()
  
        temp_list = []
  
        for x in self:
            if x not in other:
                temp_list.append(x)
  
        for x in temp_list:
            l.append(x)
  
        return l
  
    def __eq__(self, other):
        if len(self) != len(other):
            return False
        for x in range(len(self)):
            if self[x] != other[x]:
                return False
        return True
  
    def __add__(self, other):
        l = LinkedList()
  
        for x in self:
            l.insert(content=x)
        for x in other:
            l.insert(content=x)
  
        return l
  
    def __contains__(self, item):
        return item == self.root.search(item)
  
    def __iter__(self):
        yield self.root.content
        current = self.root.next
        while current:
            yield  current.content
            current = current.next
  
    def __getitem__(self, index):
        current = self.root
        for x in range(index):
            if bool(current):
                current = current.next
            else:
                return None
  
        return current
  
    def __reversed__(self):
        l = LinkedList()
        for x in self:
            l.insert(x)
        return l
  
    def insert(self, content):
        self.root = Node(content, self.root)
  
    def append(self, content):
        self.bottom.content = content
        self.bottom.next = Node()
        self.bottom = self.bottom.next
  
    def pop_top(self):
        temp = self.root
        self.root = self.root.next
        temp.next = None
        return temp
  
    def peek_top(self):
        return Node(content=self.root.content)
  
    def __delitem__(self, content):
        if content == self.root.content:
            self.root = self.root.next
        else:
            del self.root[content]
  
    def __bool__(self):
        return bool(self.root)
```
  
#### Cyclical List
  
  
Cyclical lists are used when there are memory constraints. In cyclical lists, our list doesn't end in a[n-1] but instead continues to a[0]. There is very litle reason to write a cyclical list in Python as there are no static arrays and One can always use a linkedlist implementation to achieve practically the same result. 
  
Regardless, here is a Cyclical List implementation in Python built atop of a singly LinkedList.
  
##### CyclicalList in Python
  
  
```Python
class Node:
    def __init__(self, content=None, nextN=None, previous=None):
        self.content = content
        self.next = nextN
        self.previous = previous
  
    def has_next(self):
        return self != self.next
  
    def search(self, content):
        if self == content:
            return content
  
        if self.has_next():
            return self.next.search(content)
  
        return None
  
    def remove_next(self):
        if bool(self.next):
            self.next = self.next.next
            self.next.previous = self
  
    def __delitem__(self, content):
  
        if self.next == content:
            self.remove_next()
            return
  
        del self.next[content]
        return
  
    def __repr__(self):
        return str(self.content)
  
    def __eq__(self, content):
        return self.content == content
  
    def __bool__(self):
        return self.content is not None
  
    def __reversed__(self):
        if self.has_next():
            self.next.reversed()
        yield self
  
class CyclicalList:
  
    def __init__(self):
        self.root = Node()
        self.root.next = self.root
        self.root.previous = self.root
        self.bottom = self.root
  
    def __len__(self):
        func = lambda x, node: x if node.content is None else func(x + 1, node.next)
        return func(0, self.root)
  
    def __repr__(self):
        return str([x for x in self])
  
    def __sub__(self, other):
        l = CyclicalList()
  
        temp_list = []
  
        for x in self:
            if x not in other:
                temp_list.append(x)
  
        for x in temp_list:
            l.append(x)
  
        return l
  
    def __eq__(self, other):
        if len(self) != len(other):
            return False
        for x in range(len(self)):
            if self[x] != other[x]:
                return False
        return True
  
    def __add__(self, other):
        l = CyclicalList()
  
        for x in self:
            l.insert(content=x)
        for x in other:
            l.insert(content=x)
  
        return l
  
    def __contains__(self, item):
        return item == self.root.search(item)
  
    def __iter__(self):
        yield self.root.content
        current = self.root.next
        while current != self.root:
            yield  current.content
            current = current.next
  
    def __getitem__(self, index):
        current = self.root
        for x in range(index):
            if bool(current):
                current = current.next
            else:
                return None
  
        return current
  
    def __reversed__(self):
        l = CyclicalList()
        for x in self:
            l.insert(x)
        return l
  
    def insert(self, content):
        if self.root.content is None:
            self.root.content = content
            return
        else:
            self.root = Node(content, nextN=self.root, previous=self.bottom)
            self.root.previous = self.root
            self.bottom.next = self.root
  
  
    def append(self, content):
        self.bottom.next = Node(content=content, previous=self.bottom, nextN=self.root)
  
        self.bottom = self.bottom.next
        self.root.previous = self.bottom
  
    def __delitem__(self, content):
        if content == self.root.content:
            del self.bottom[content]
            self.root = self.bottom.next
            return
        if content == self.bottom.content:
            self.bottom = self.bottom.previous
            self.bottom.remove_next()
            return
        else:
            del self.root[content]
            return
  
    def __next__(self):
        self.bottom = self.root
        self.root = self.root.next
        return self.bottom
  
    def __bool__(self):
        return bool(self.root)
```
  