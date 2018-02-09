from node import Node

def detectLoop(node):
    """Return the node which is looped"""

    while node:
        if node.d == node.next.next.d:
            return node.d
        else:
            print 'node', node.d, node.next.d    
        node = node.next


first = Node(1)
l1 = Node(2)
l3 = Node(3)
first.next = l1
l1.next = l3
l3.next = l1

#print 'input:', first.getData()
print 'loop:', detectLoop(first)
