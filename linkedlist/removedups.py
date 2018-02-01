# Code to remove duplicates from unsorted LinkedList
from node import Node

def removeDups(head):
    """
    Remove duplicates from list
    """
    while(head): # compare each element of linked list from the next two elements
        prev = head
        while(prev.next):
            if prev.next.d == head.d: #compare next
                prev.next = prev.next.next
            elif prev.next.next and prev.next.next.d == head.d: #compare next.next
                if prev.next.next.next:
                    prev.next.next = prev.next.next.next
                    prev = prev.next
                else:
                    prev.next = None
                continue #prev is already set, hence continue

            prev = prev.next
        head = head.next
        


print "==== Removing duplicates from LinkedList ===="        
# Prepare input
head = Node(1)
head.addToTail(20)
head.addToTail(3)
head.addToTail(4)
head.addToTail(3)
head.addToTail(20)        
print "Input:", head.getData() 
removeDups(head)
print "Result:", head.getData()

removeDups(None)
