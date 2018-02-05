from node import Node

def sumLists(l1, l2, i=1):
    rs = 0 #var to hold result

    if l1 and l1.next:
        if l2 and l2.next:
            rs = sumLists(l1.next, l2.next, i*10)
        else:
            rs = sumLists(l1.next, None, i*10)
    elif l2 and l2.next:
        rs = sumLists(None, l2.next, i*10)

    tmp = 0 
    if l1:
        tmp += l1.d

    if l2:
        tmp += l2.d

    return rs + (tmp)*i



l1 = Node(7)
l1.add(1)
l1.add(6)

l2 = Node(5)
l2.add(9)
l2.add(2)

rs = sumLists(l1, l2)
print "Result of 617 + 295:", rs

l1 = Node(6)
l1.add(1)
l1.add(7)

l2 = Node(0)
l2.add(1)


rs = sumLists(l1, l2)
print "Result of 716 + 10:", rs
