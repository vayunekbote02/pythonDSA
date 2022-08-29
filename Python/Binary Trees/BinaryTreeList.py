# Binary Tree using Python List

class BinaryTree:
    def __init__(self, size):
        self.l = [None] * size
        self.lastUsedIndex = 0
        self.maxSize = size

    def insertNode(self, value):
        if self.lastUsedIndex + 1 == self.maxSize:
            return None
        else:
            self.l[self.lastUsedIndex+1] = value
            self.lastUsedIndex += 1

    def searchNode(self, target):
        for i, _ in enumerate(self.l):
            if self.l[i] == target:
                return i
        return None

    def preOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
        else:
            print(self.l[index])
            self.preOrderTraversal(index * 2)
            self.preOrderTraversal(index*2 + 1)

    def inOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
        else:
            self.inOrderTraversal(index * 2)
            print(self.l[index])
            self.inOrderTraversal(index*2 + 1)

    def postOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
        else:
            self.postOrderTraversal(index * 2)
            self.postOrderTraversal(index*2 + 1)
            print(self.l[index])

    def levelOrderTraversal(self, index):
        for i in range(index, self.lastUsedIndex+1):
            print(self.l[i])

    def deleteNode(self, target):
        if self.lastUsedIndex == 0:
            return None
        else:
            for i in range(1, self.lastUsedIndex+1):
                if self.l[i] == target:
                    self.l[i] = self.l[self.lastUsedIndex]
                    self.l[self.lastUsedIndex] = None
                    self.lastUsedIndex -= 1
                    break

    def deleteBT(self):
        self.l = None


if __name__ == "__main__":
    newBT = BinaryTree(12)
    newBT.insertNode("Drinks")
    newBT.insertNode("Hot")
    newBT.insertNode("Cold")
    newBT.insertNode("Tea")
    newBT.insertNode("Coffee")
    newBT.insertNode("Fanta")
    newBT.insertNode("Miranda")
    newBT.insertNode("Green Tea")
    newBT.insertNode("Black Tea")
    newBT.insertNode("Latte")
    newBT.insertNode("Cappuchino")
    # print(newBT.l)

    # searching for a node
    '''print(newBT.searchNode("Hot"))'''

    # Pre Order Traversal
    '''newBT.preOrderTraversal(1)'''

    # In Order Traversal
    '''newBT.inOrderTraversal(1)'''

    # In Order Traversal
    """newBT.postOrderTraversal(1)"""

    # Level Order Traversal
    '''newBT.levelOrderTraversal(1)'''

    # Deleting a node from tree
    '''newBT.deleteNode("Fanta")
    newBT.levelOrderTraversal(1)'''

    # Deleting entire binary tree
    print(newBT.l)
    newBT.deleteBT()
    print(newBT.l)
