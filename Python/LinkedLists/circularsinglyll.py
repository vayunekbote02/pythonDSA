from operator import ne


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class CircularSinglyLinkedList:
    def __init__(self, value):
        node = Node(value)
        node.next = node
        self.head = node
        self.tail = node

    def __iter__(self):
        tempNode = self.head
        while tempNode:
            yield tempNode
            if tempNode.next == self.head:
                break
            tempNode = tempNode.next

    def insertCSLL(self, value, location):
        if self.head == None:
            return None
        else:
            newNode = Node(value)
            if location == 0:
                newNode.next = self.head
                self.head = newNode
                self.tail.next = newNode
            elif location == -1:
                self.tail.next = newNode
                self.tail = newNode
                newNode.next = self.head
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode

    def traverseCSLL(self):
        tempNode = self.head
        while tempNode:
            print(tempNode.value)
            if tempNode == self.tail:
                break
            tempNode = tempNode.next

    def searchCSLL(self, target):
        if self.head == None:
            return self.head
        else:
            tempNode = self.head
            index = 0
            while tempNode:
                if tempNode.value == target:
                    return index
                if tempNode == self.tail:
                    break
                tempNode = tempNode.next
                index += 1
            return None

    def deleteCSLL(self, location):
        if self.head == None:
            return None
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.tail.next = self.head
            elif location == -1:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    tempNode = self.head
                    while tempNode.next != self.tail:
                        tempNode = tempNode.next
                    self.tail = tempNode
                    self.tail.next = self.head
            else:
                tempNode = self.head
                index = 0
                while index+1 != location:
                    tempNode = tempNode.next
                    index += 1
                tempNode.next = tempNode.next.next

    def deleteEntireCSLL(self):
        self.head = None
        self.tail.next = None
        self.tail = None


csll = CircularSinglyLinkedList(1)
print([node.value for node in csll])

csll.insertCSLL(2, -1)
csll.insertCSLL(3, -1)
csll.insertCSLL(4, -1)
csll.insertCSLL(5, -1)
csll.insertCSLL(0, 0)
csll.insertCSLL(2.3, 3)
print([node.value for node in csll])
'''print("Head ->", csll.head.value)
print("Head.next ->", csll.head.next.value)
print("Tail ->", csll.tail.value)
print("Tail.next ->", csll.tail.next.value)'''
# csll.traverseCSLL()
print(csll.searchCSLL(8))
csll.deleteCSLL(0)
print([node.value for node in csll])
csll.deleteEntireCSLL()
print([node.value for node in csll])
