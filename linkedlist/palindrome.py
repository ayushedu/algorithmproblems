from node import Node

def reverse_list(node):

    if node.next is None:
        return [node.d]
    else:
        rs = reverse_list(node.next)

    rs.append(node.d)
    return rs

def reverse(node):

    list_ = reverse_list(node)
    rs = None
    rs_end = None
    for val in list_:
        if rs is None:
            rs = Node(val)
        else:
           rs.add(val)
    return rs

def isPalindrome(node):

    reversed = reverse(node)

    while(True):
        if reversed:
            if node:
                if reversed.d != node.d:
                    return False
            else:
                return False  # Unequal length
        elif node:
            return False  # unequal length
        else:
            return True # all elements matched

        if reversed.next:
            if node.next:
                if reversed.next.d != node.next.d:
                    return False
            else:  # unequal length
                return False 
        elif node.next:  # Unequal lenght
            return False
        else:
            return True  # All elements matched
        reversed = reversed.next.next
        node =node.next.next

node = Node(1)
node.add(3)
node.add(3)
node.add(2)
print 'input:', node.getData()
print 'palindrome:', isPalindrome(node)

node = Node(1)
node.add(3)
node.add(3)
node.add(1)
print 'input:', node.getData()
print 'palindrome:', isPalindrome(node)
