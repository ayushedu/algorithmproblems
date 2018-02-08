from node import Node

def search(node, llist):
    """Search data in linkedlist"""

    while llist:
        if llist == node:
            return True
        llist = llist.next

    return False

def intersect(first, second):
    """Return matching nodes

    complexity O(N^2)
    """

    rs = []
    while first:
        if search(first, second):
            rs = first.getData()
            break
        first = first.next

    return rs

first = Node(1)
l1 = Node(2)
l3 = Node(3)
first.next = l1
l1.next = l3

second = Node(10)
l2 = Node(4)
second.next = l2
l2.next = l1

print 'input:', first.getData(), second.getData()
print 'intersecting nodes:', intersect(first, second)
