# Code to remove duplicates from unsorted LinkedList

class Node:
    """
    LinkedList implementation
    """
    def __init__(self, d):
        self.d = d
        self.next = None

    def addToTail(self, d):
        """
        Add element to tail of the list
        """
        head = self.next
        
        while(head and head.next):
            head = head.next

        if head == None:
            head = self
        head.next = Node(d)

def getData(head):
    """
    Collect linkedlist values in a list and return
    """
    data = []
    while(head):
        data.append(head.d)
        head = head.next
    return data

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
print "Input:", getData(head) 
removeDups(head)
print "Result:", getData(head)

removeDups(None)
