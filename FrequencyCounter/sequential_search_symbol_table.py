class SequentialST:
    def __init__(self):
        self.first = None
        self.n = 0

    class Node:
        def __init__(self, key, value, next):
            self.key = key
            self.value = value
            self.next = next

    def size(self):
        return self.n

    def get (self, key):
        x = self.first
        while x != None:
            if x.key == key:
                return x.value
            x = x.next
        return None

    def put(self, key):
        x = self.first
        while x != None:
            if x.key == key:
                x.value += 1
                return
            x = x.next
        self.first = SequentialST.Node(key, 1, self.first)
        self.n += 1

    def  delete (self, key):
        x = self.first
        if x.key == key:
            self.first = x.next
            return
        prev = x
        x = x.next
        while x != None:
            if x.key == key:
                prev.next = x.next
                self.n -= 1
                return
            prev = x
            x = x.next

    def keys(self):
        ll = []
        x = self.first
        while x != None:
            ll.append(x.key)
            x = x.next
        return ll

# Test code
"""def main():
    symbolTable = SequentialST()
    symbolTable.put('S')
    symbolTable.put('E')
    symbolTable.put('A')
    symbolTable.put('R')
    symbolTable.put('C')
    symbolTable.put('H')
    symbolTable.put('E')
    symbolTable.put('X')
    symbolTable.put('A')
    symbolTable.put('M')
    symbolTable.put('P')
    symbolTable.put('L')
    symbolTable.put('E')
    symbolTable.put('X')

    head = symbolTable.first
    while head != None:
        print (head.key, "  ", head.value)
        head = head.next

if __name__ == '__main__':
    main()"""