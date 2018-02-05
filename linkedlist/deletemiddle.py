"""
delete the node in the middle of single linked list.
"""
from node import Node

def deleteMiddle(head):
    #Get node length
    nodeLen = 1
    tmp = head
    while(tmp.next): 
        nodeLen += 1
        if tmp.next.next:
            nodeLen += 1
            tmp = tmp.next.next
        else:
            tmp = tmp.next

    if nodeLen % 2 == 0:
        middleIdx = nodeLen / 2
    else:
        middleIdx = (nodeLen + 1) / 2
    if middleIdx > 1 and middleIdx < nodeLen:
        i = 1
        while(head.next):
            i += 1
            if middleIdx == i:
                head.next = head.next.next
                break
            elif middleIdx + 2 == i:
                i += 1
                head = head.next.next
            else:
                head = head.next
    else:
        print "Invalid input: cannot delete middle node"

head = Node('a')
head.addToTail('b')
head.addToTail('c')
head.addToTail('d')
head.addToTail('e')
head.addToTail('f')

print "Input:", head.getData() 
deleteMiddle(head)
print "Ouptut:", head.getData()

head = Node('a')
head.addToTail('b')
head.addToTail('c')
head.addToTail('d')
head.addToTail('e')

print "Input:", head.getData() 
deleteMiddle(head)
print "Ouptut:", head.getData()
