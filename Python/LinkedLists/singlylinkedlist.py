class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class SLinkedlist:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertSLL(self, value, location):
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            elif location == -1:
                tempNode = self.head
                while tempNode.next != None:
                    tempNode = tempNode.next
                tempNode.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location-1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode

    def traverseSLL(self):
        l = []
        if self.head == None:
            return None
        else:
            tempNode = self.head
            while tempNode != None:
                l.append(tempNode.value)
                tempNode = tempNode.next

        return l

    def searchSLL(self, target):
        tempNode = self.head
        index = 0
        while tempNode != None:
            if tempNode.value == target:
                return (index, tempNode.value)
            tempNode = tempNode.next
            index += 1
        return (None, None)

    def deleteSLL(self, target):
        if self.head == None:
            return None
        else:
            if target == 0:
                if self.head == self.tail:
                    self.head == None
                    self.tail == None
                else:
                    nextNode = self.head.next
                    del self.head
                    self.head = nextNode
            elif target == -1:
                if self.head == self.tail:
                    del self.tail
                    self.head = None
                    self.tail = None
                else:
                    tempNode = self.head
                    while tempNode.next.next != None:
                        tempNode = tempNode.next
                    del tempNode.next
                    self.tail = tempNode
                    tempNode.next = None
            else:
                tempNode = self.head
                index = 0
                while index < target - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next
                del nextNode

    def deleteEntireSLL(self):
        self.head = None
        self.tail = None


sll = SLinkedlist()
sll.insertSLL(1, -1)
sll.insertSLL(2, -1)
sll.insertSLL(3, -1)
sll.insertSLL(4, -1)
sll.insertSLL(0, 0)
sll.insertSLL(0, 4)

print(sll.traverseSLL())
print(sll.head.value)
print(sll.tail.value)

sll.deleteSLL(-1)

print()
print(sll.traverseSLL())
print(sll.head.value)
print(sll.tail.value)

sll.deleteEntireSLL()

print()
print(sll.traverseSLL())
