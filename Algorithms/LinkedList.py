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


if __name__=="__main__":
    list = LinkedList()
    list.append(10)
    list.append(20)
    list.append(30)
    print(list)
    print(reversed(list))