class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class CircularDoublyLinkedList:
    def __init__(self, value):
        node = Node(value)
        self.head = node
        self.tail = node
        node.next = node
        node.prev = node

    def __iter__(self):
        tempNode = self.head
        while tempNode:
            yield tempNode
            if tempNode.next == self.head:
                break
            tempNode = tempNode.next

    def insertCDLL(self, value, location):
        if self.head == None:
            return None
        else:
            newNode = Node(value)
            if location == 0:
                newNode.next = self.head
                self.head.prev = newNode
                self.tail.next = newNode
                newNode.prev = self.tail
                self.head = newNode
            elif location == -1:
                self.tail.next = newNode
                newNode.prev = self.tail
                self.tail = newNode
                self.tail.next = self.head
                self.head.prev = self.tail
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.prev = tempNode
                newNode.next = nextNode
                nextNode.prev = newNode

    def traversalCDLL(self, forward=True):
        if self.head == None:
            return None
        else:
            if forward:
                tempNode = self.head
                while tempNode:
                    print(tempNode.value)
                    if tempNode == self.tail:
                        break
                    tempNode = tempNode.next
            else:
                tempNode = self.tail
                while tempNode:
                    print(tempNode.value)
                    if tempNode == self.head:
                        break
                    tempNode = tempNode.prev

    def searchCDLL(self, target):
        if self.head == None:
            return None
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

    def deleteCDLL(self, location):
        if self.head == None:
            return None
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.prev = None
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.tail.next = self.head
                    self.head.prev = self.tail
            elif location == -1:
                if self.head == self.tail:
                    self.head.prev = None
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = self.head
                    self.head.prev = self.tail
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next
                nextNode.next.prev = tempNode

    def deleteEntireCDLL(self):
        if self.head == None:
            return None
        else:
            tempNode = self.head
            while tempNode:
                tempNode.prev = None
                if tempNode == self.tail:
                    break
                tempNode = tempNode.next
            self.tail.next = None
            self.head = None
            self.tail = None


cdll = CircularDoublyLinkedList(1)
print([node.value for node in cdll])
cdll.insertCDLL(2, -1)
cdll.insertCDLL(3, -1)
cdll.insertCDLL(4, -1)
cdll.insertCDLL(5, -1)
cdll.insertCDLL(0, 0)
cdll.insertCDLL(1.5, 2)
print([node.value for node in cdll])
print(cdll.tail.next.next.next.prev.prev.prev.value)

print('-'*20)

# cdll.traversalCDLL(forward=False)
# print(cdll.searchCDLL(9))
cdll.deleteCDLL(-1)
print([node.value for node in cdll])
print(cdll.head.prev.value)
print(cdll.tail.next.value)

print('-'*20)

cdll.deleteEntireCDLL()
print([node.value for node in cdll])
print(cdll.head, cdll.tail)
