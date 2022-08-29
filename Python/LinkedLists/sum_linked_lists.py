from linkedlistques import LinkedList


def sumList(llA, llB):
    n1 = llA.head
    n2 = llB.head
    carry = 0
    ll = LinkedList()

    while n1 or n2:
        result = carry
        if n1:
            result += n1.value
            n1 = n1.next
        if n2:
            result += n2.value
            n2 = n2.next
        ll.add(int(result % 10))
        carry = result / 10
    if carry > 0:
        ll.add(int(carry))

    return ll


llA = LinkedList()
llA.add(9)
llA.add(9)
llA.add(9)

llB = LinkedList()
llB.add(9)
llB.add(9)
llB.add(9)

print(llA)
print(llB)
print(sumList(llA, llB))
