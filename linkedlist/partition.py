from node import Node

def partition(head, x):
    if head is None:
        return

    before = None
    after = None
    while(head):
        if head.d < x:
            if before:
                before.add(head.d)
                
            else:
                before = Node(head.d)
        else:
            if after:
                after.add(head.d)
            else:
                after = Node(head.d)
                
        head = head.next

    while(after):
        before.add(after.d)
        after = after.next

    return before

head = Node(3)
head.add(5)
head.add(8)
head.add(5)
head.add(10)
head.add(2)
head.add(1)

print "----"
print "input:", head.getData()
rs1 = partition(head,5)
print "output:", rs1.getData()
