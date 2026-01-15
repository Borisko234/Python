class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self, value = None):
        self.left = None
        self.right = None 
        self.value = value
        # self.count = 0

    def insert(self, value):
        if self.value == None:
            self.value = value
            return
        if (value < self.value):
            if(self.left == None):
                self.left = BinarySearchTree(value)
                return
            else:
                self.left.insert(value)
        elif(value > self.value): 
            if self.right == None:
                self.right = BinarySearchTree(value)
                return
            else:
                self.right.insert(value)
            


    def fromArray(self, array):
        for value in array:
            self.insert(value)

    def search(self, value):
        if value == self.value: return True
        if value < self.value:
            if self.left == None:
                return False
            else:
                return self.left.search(value)
        elif value > self.value:
            if self.right == None: return False
            else: 
                return self.right.search(value)

    def min(self):
        while self.left != None:
            self = self.left
        return self.value
    def max(self):
        while self.right != None:
            self = self.right
        return self.value
    def depth(self, value):
        count = 0
        current = self
        while True:
            if value == current.value: return count
            if value < current.value:
                if current.left == None:
                    print("break 1")
                    break
                else:
                    current = current.left
                    count += 1
            elif value > current.value:
                if current.right == None: 
                    print("break 2")
                    break
                else: 
                    current = current.right
                    count += 1
        return count

    def inOrderTraversal(self, arr = []):
        if self.left:
            self.left.inOrderTraversal(arr)
        arr.append(self.value)
        if self.right:
            self.right.inOrderTraversal(arr)
        return arr
    def preOrderTraversal(self, arr = []):
        arr.append(self.value)
        if self.left:
            self.left.inOrderTraversal(arr)
        arr.append(self.value)
        if self.right:
            self.right.inOrderTraversal(arr)
        return arr
        
    def BFS(self):
        current = self
        arr = []
        arr.append(current)
        

bst2 = BinarySearchTree()

