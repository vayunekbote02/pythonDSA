class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, value):
        node = Node(value)
        node.prev = None
        node.next = None
        self.head = node
        self.tail = node

    def __iter__(self):
        tempNode = self.head
        while tempNode:
            yield tempNode
            tempNode = tempNode.next

    def insertDLL(self, value, location):
        if self.head == None:
            return None
        else:
            newNode = Node(value)
            if location == 0:
                newNode.prev = None
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode
            elif location == -1:
                newNode.next = None
                newNode.prev = self.tail
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
                nextNode.prev = newNode
                newNode.prev = tempNode

    def traverseDLL(self, forward=True):
        if self.head == None:
            return None
        else:
            if forward:
                tempNode = self.head
                while tempNode:
                    print(tempNode.value)
                    tempNode = tempNode.next
            else:
                tempNode = self.tail
                while tempNode:
                    print(tempNode.value)
                    tempNode = tempNode.prev

    def searchDLL(self, target):
        if self.head == None:
            return None
        else:
            tempNode = self.head
            index = 0
            while tempNode:
                if tempNode.value == target:
                    return index
                tempNode = tempNode.next
                index += 1
            return None

    def deleteDLL(self, target):
        if self.head == None:
            return None
        else:
            if target == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = None
            elif target == -1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = None
            else:
                tempNode = self.head
                index = 0
                while index+1 != target:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next
                nextNode.next.prev = tempNode

    def deleteEntireDLL(self):
        if self.head == None:
            return None
        else:
            tempNode = self.head.next
            while tempNode:
                tempNode.prev = None
                tempNode = tempNode.next
            self.head = None
            self.tail = None


dll = DoublyLinkedList(1)
print([node.value for node in dll])
dll.insertDLL(2, -1)
dll.insertDLL(3, -1)
dll.insertDLL(4, -1)
dll.insertDLL(0, 0)
dll.insertDLL(5, -1)
dll.insertDLL(3.4, 4)
print([node.value for node in dll])
print(dll.tail.prev.prev.next.prev.value)
print('-'*20)
# dll.traverseDLL(forward=False)
# print(dll.searchDLL(7))
dll.deleteDLL(3)
dll.deleteDLL(3)

print([node.value for node in dll])
print(dll.tail.prev.prev.prev.prev.next.next.next.next.value)
print('-'*20)

dll.deleteEntireDLL()
print([node.value for node in dll])
