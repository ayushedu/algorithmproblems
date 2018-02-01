from node import Node

def len_(head):
    """Get lenght of linked list"""
    i = 0
    while(head):
        i += 1
        head = head.next

    return i

def return_k_to_last(head, k):
    #1-2-3-4-5
    if k < 0:
        return None

    max_iter = len_(head) - k
    if max_iter <= 0:
        return None
    
    curr_count = 0
    while(head):
        if curr_count == max_iter:
            return head.d
        elif head.next and curr_count + 1 == max_iter:
            return head.next.d
        curr_count += 2
        if head.next:
            head = head.next.next
        else:
            break #end of linkedlist

head = Node(1)
head.addToTail(2)
head.addToTail(3)
head.addToTail(4)

print "Input:", head.getData()
print "2nd to last:", return_k_to_last(head,2)
print "-1 to last:", return_k_to_last(head,-1)
print "100 to last:", return_k_to_last(head,100)
