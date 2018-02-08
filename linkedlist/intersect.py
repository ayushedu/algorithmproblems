from node import Node

def search(data, node):
    """Search data in linkedlist"""

    while node:
        if node.d == data:
            return True
        node = node.next

    return False

def intersect(first, second):
    """Return matching nodes

    complexity O(N^2)
    """

    rs = []
    while first:
        if search(first.d, second):
            rs.append(first.d)
        first = first.next

    return rs

first = Node(1)
first.add(3)
first.add(3)
first.add(2)

second = Node(1)
second.add(3)
second.add(3)
second.add(1)

print 'input:', first.getData(), second.getData()
print 'intersecting nodes:', intersect(first, second)
