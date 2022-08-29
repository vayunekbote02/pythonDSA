import queuell as q


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


def preOrderTraversal(rootnode):
    if not rootnode:
        return
    print(rootnode.data)
    preOrderTraversal(rootnode.leftChild)
    preOrderTraversal(rootnode.rightChild)


def inOrderTraversal(rootnode):
    if not rootnode:
        return
    inOrderTraversal(rootnode.leftChild)
    print(rootnode.data)
    inOrderTraversal(rootnode.rightChild)


def postOrderTraversal(rootnode):
    if not rootnode:
        return
    else:
        postOrderTraversal(rootnode.leftChild)
        postOrderTraversal(rootnode.rightChild)
        print(rootnode.data)


def levelOrderTraversal(rootnode):
    if not rootnode:
        return
    else:
        q1 = q.Queue()
        q1.enqueue(rootnode)
        while not q1.isEmpty():
            root = q1.dequeue()
            if root == None:
                continue
            print(root.data)
            q1.enqueue(root.leftChild)
            q1.enqueue(root.rightChild)


def searchBT(rootnode, target):
    if not rootnode:
        return None
    else:
        q1 = q.Queue()
        q1.enqueue(rootnode)
        while not q1.isEmpty():
            root = q1.dequeue()
            if root == None:
                continue
            if root.data == target:
                return "The target exists in the binary tree."

            q1.enqueue(root.leftChild)
            q1.enqueue(root.rightChild)
    return "The target does not exist in the binary tree."


def insertNodetoBT(rootnode, newNode):
    if not rootnode:
        rootnode = newNode
    else:
        q1 = q.Queue()
        q1.enqueue(rootnode)
        while not q1.isEmpty():
            root = q1.dequeue()
            if root.leftChild != None:
                q1.enqueue(root.leftChild)
            else:
                root.leftChild = newNode
                break
            if root.rightChild != None:
                q1.enqueue(root.rightChild)
            else:
                root.rightChild = newNode
                break


def getDeepestNode(rootnode):
    if not rootnode:
        return
    else:
        q1 = q.Queue()
        q1.enqueue(rootnode)
        while not q1.isEmpty():
            root = q1.dequeue()
            if root.leftChild != None:
                q1.enqueue(root.leftChild)
            if root.rightChild != None:
                q1.enqueue(root.rightChild)
        return root


def deleteDeepestNode(rootnode, dNode):
    if not rootnode:
        return
    else:
        q1 = q.Queue()
        q1.enqueue(rootnode)
        while not q1.isEmpty():
            root = q1.dequeue()
            if root == dNode:
                root = None
                return
            if root.rightChild:
                if root.rightChild == dNode:
                    root.rightChild = None
                    return
                else:
                    q1.enqueue(root.rightChild)
            if root.leftChild:
                if root.leftChild == dNode:
                    root.leftChild = None
                    return
                else:
                    q1.enqueue(root.leftChild)


def deleteNode(rootnode, node):
    if not rootnode:
        return
    else:
        q1 = q.Queue()
        q1.enqueue(rootnode)
        while not q1.isEmpty():
            root = q1.dequeue()
            if root.data == node:
                dNode = getDeepestNode(rootnode)
                root.data = dNode.data
                deleteDeepestNode(rootnode, dNode)
                return
            if root.leftChild != None:
                q1.enqueue(root.leftChild)
            if root.rightChild != None:
                q1.enqueue(root.rightChild)
        return None


def deleteBT(rootnode):
    rootnode.data = None
    rootnode.leftChild = None
    rootnode.rightChild = None


if __name__ == "__main__":
    newBT = TreeNode("Drinks")
    hot = TreeNode("Hot")
    cold = TreeNode("Cold")
    newBT.leftChild = hot
    newBT.rightChild = cold

    tea = TreeNode("Tea")
    hot.leftChild = tea
    coffee = TreeNode("Coffee")
    hot.rightChild = coffee

    #fanta = TreeNode("Fanta")
    #cold.leftChild = fanta
    fanta = TreeNode("Fanta")
    cold.leftChild = fanta

    # testing the traversal methods
    '''preOrderTraversal(newBT)
    print()
    inOrderTraversal(newBT)
    print()
    postOrderTraversal(newBT)
    print()
    levelOrderTraversal(newBT)'''

    # Searching for a node
    '''print(searchBT(newBT, "Coffee"))'''

    # Inserting a node
    newNode = TreeNode("Miranda")
    insertNodetoBT(newBT, newNode)

    newNode1 = TreeNode("Black Tea")
    insertNodetoBT(newBT, newNode1)

    newNode2 = TreeNode("Green Tea")
    insertNodetoBT(newBT, newNode2)

    newNode3 = TreeNode("Latte")
    insertNodetoBT(newBT, newNode3)

    newNode4 = TreeNode("Cappuchino")
    insertNodetoBT(newBT, newNode4)
    '''preOrderTraversal(newBT)'''

    # getting the deepest node
    '''node = getDeepestNode(newBT)
    print(node.data)'''

    # deleting the deepest node
    '''node = getDeepestNode(newBT)
    deleteDeepestNode(newBT, node)'''

    # deleting node from tree
    '''deleteNode(newBT, "Cold")'''
    '''preOrderTraversal(newBT)'''

    # Deleting entire binary tree
    deleteBT(newBT)
    preOrderTraversal(newBT)
