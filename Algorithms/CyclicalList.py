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


if __name__=="__main__":
    list = CyclicalList()

    list.insert(0)
    list.insert(2)
    list.insert(3)
    list.append(-1)
