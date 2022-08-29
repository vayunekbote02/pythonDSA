class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        tempNode = self.head
        while tempNode:
            yield tempNode
            tempNode = tempNode.next


class Queue:
    def __init__(self):
        self.ll = LinkedList()

    def __str__(self):
        values = [str(x.value) for x in self.ll]
        return ' '.join(values)

    def isEmpty(self):
        return True if self.ll.head == None else False

    def enqueue(self, value):
        newNode = Node(value)
        if self.ll.head == None:
            self.ll.head = newNode
            self.ll.tail = newNode
        else:
            self.ll.tail.next = newNode
            self.ll.tail = newNode

    def dequeue(self):
        if self.isEmpty():
            return None
        else:
            nodeValue = self.ll.head.value
            if self.ll.head == self.ll.tail:
                self.ll.head = None
                self.ll.tail = None
            else:
                self.ll.head = self.ll.head.next
            return nodeValue

    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.ll.head.value

    def delete(self):
        self.ll.head = None
        self.ll.tail = None


if __name__ == "__main__":
    q1 = Queue()
    q1.enqueue(9)
    q1.enqueue(8)
    q1.enqueue(7)
    print(q1)

    print("-" * 15)

    a = q1.dequeue()
    print(a)
    print()
    print(q1)

    print("-" * 15)

    print(q1.peek())

    print("-" * 15)

    print("Deleting entire queue:-")
    q1.delete()
    print(q1)
