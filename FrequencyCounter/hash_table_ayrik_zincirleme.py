class seperateChainingHashST():
    def __init__(self, M):
        self.M = M
        self.st = []
        for i in range(M):
            self.st.append(None)

    class Node:
        def __init__(self, key, value, next):
            self.key = key
            self.val = value
            self.next = next

    def hash(self, key):
        return (hash(key) & 0x7fffffff) % self.M
                              
    def get(self, key):
        i = self.hash(key)
        x = self.st[i]
        while x != None:
            if key == x.key:
                return x.val
            x = x.next
        return None

    def put (self, key):
        i = self.hash(key)
        x = self.st[i]
        while x != None:
            if key == x.key:
                x.val += 1
                return i,self.length(self.st[i])
            x = x.next
        self.st[i] = seperateChainingHashST.Node(key, 1, self.st[i])
        return i,self.length(self.st[i])

    def length(self, lst):
        r = 0
        while lst:
            lst = lst.next
            r += 1
        return r