class BinarySearchST():
    def __init__(self):              
        self.keys = []
        self.values = []
        self.n = 0

    def size(self):
        return self.n

    def get (self, key):
        i = self.binarySearch(key)
        if i < self.n and self.keys[i] == key:
            return self.values[i]
        else:
            return None

    def put(self, key):
        i = self.binarySearch(key)
        if i < self.n and self.keys[i] == key:
            self.values[i] += 1
            return
        self.keys.append(' ')
        self.values.append(' ')
        for j in range (self.n, i, -1):
            self.keys[j] = self.keys[j-1]
            self.values[j] = self.values[j - 1]
        self.keys[i] = key
        self.values[i] = 1
        self.n += 1


    def binarySearch(self, key):
        lo = 0
        hi = self.n - 1
        while (lo <= hi):
            mid = lo + (hi - lo) // 2
            if key < self.keys[mid]:
                hi = mid - 1
            elif key > self.keys[mid]:
                lo = mid + 1
            else:
                return mid
        return lo


"""def main():
    symbolTable = BinarySearchST()
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

    for i in range(symbolTable.n-1, -1, -1):
        print (symbolTable.keys[i], "  ", symbolTable.values[i])

if __name__ == '__main__':
    main()"""