from node import Node

def reverse(node):
    """ Return reversed linked list """

    list_ = node.getData()
    print "list", list_
    rs = None

    try:
        if rs is None:
            rs = Node(list_.pop())
        else:
            rs.add(list_.pop())
    except IndexError:
        pass  # List is now empty
    return rs

def isPalindrome(node):
    """ Return whether palindrome or not """

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
