class BST:
    def __init__(self):
        self.root = None
        
    class Node:
        def __init__(self, key, value, n):
            self.key = key
            self.val = value
            self.left = None
            self.right = None
            self.n = n

    def size(self):
        return self._size(self.root)

    def _size(self, x):
        if x == None:
            return 0
        else:
            return x.n

    def get(self, key):
        return self._get(self.root, key)

    def _get(self, x, key):
        if x == None:
            return None
        if key < x.key:
            return self._get(x.left, key)
        elif key > x.key:
            return self._get(x.right, key)
        else:
            return x.val

    def put(self, key):
        self.root = self._put(self.root, key)

    def _put(self, x, key):
        if x == None:
            return BST.Node(key, 1, 1)
        if key < x.key:
            x.left = self._put (x.left, key)
        elif key > x.key:
            x.right = self._put (x.right, key)
        else:
            x.val += 1
        x.n = self._size(x.left) + self._size(x.right) + 1
        return x

    def min(self):
        x = self._min(self.root)
        return x.key

    def _min(self, x):
        if x.left == None:
            return x
        return self._min(x.left)

    def max(self):
        x = self._max(self.root)
        return x.key

    def _max(self, x):
        if x.right == None:
            return x
        return self._max(x.right)


    def rank(self, key):
        return self._rank(key, self.root)

    def _rank(self, key, x):
        if x == None:
            return 0
        if key < x.key:
            return self._rank(key, x.left)
        elif key > x.key:
            return 1 + self._size(x.left) + self._rank(key, x.right)
        else:
            return self._size(x.left)

    def deleteMin(self):
        self.root = self._deleteMin(self.root)

    def _deleteMin(self, x):
        if x.left == None:
            return x.right
        x.left = self._deleteMin(x.left)
        x.n = 1 + self._size(x.left) + self._size(x.right)
        return x

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, x, key):
        if x == None:
            return None
        if key < x.key:
            x.left = self._delete(x.left, key)
        if key > x.key:
            x.right = self._delete(x.right, key)
        else:
            if x.right == None:
                return x.left
#            if x.left == None:
#                return x.right

            t = x
            x = self._min(t.right)
            x.right = self._deleteMin(t.right)
            x.left = t.left

        x.n = self._size(x.left) + self._size(x.right) + 1
        return x

    def isBST(self):
        return self._isBST(self.root)

    def _isBST(self, root):
        if root == None or root.n == 1:
            return True
        
        if root.left :
            isLeftBST = root.left.key < root.key and self._isBST(root.left)
        else:
            isLeftBST = True
        
        if root.right :
            isRightBST = root.right.key > root.key and self._isBST(root.right)
        else:
            isRightBST = True,

        return isLeftBST and isRightBST

    def successor(self, key):
        # Find the vertex that key is indexed (Accepted as exists).
        x = self.root
        while x.key != key:
            if key < x.key:
                x = x.left
            else:
                x = x.right

        # İf the right subtree of the vertex is empty, the successor is the minimum of the left subtree.
        if x.right != None:
            return self._min(x.right).key
        # Else start from the root of the BST continously moving to the left while updating the successor until the key is found.
        # If the successor is the last key in the BST, successor will be None.
        else:
            succ = None
            y = self.root
            while y != None:
                if x.key < y.key:
                    succ = y
                    y = y.left
                elif x.key > y.key:
                    y = y.right
                    succ = y.right
                else:
                    break
        
        if succ:
            return succ.key
        else:
            return None
"""
def main():

    class Node2:
        def __init__(self, key, value, n):
            self.key = key
            self.val = value
            self.left = None
            self.right = None
            self.n = n

    symbolTable = BST()
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

    root = symbolTable.root
    traverse (root)


def traverse(root): 
    print (root.key, " ", root.val)
    if root.left != None:
        traverse(root.left)
    if root.right != None:
        traverse(root.right)

if __name__ == '__main__':
    main()"""