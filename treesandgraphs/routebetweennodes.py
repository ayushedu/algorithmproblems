from node import Node

def isRoute_DFS(root, k):
    """Return true if there is a route between root node and node of name k

    using Depth first search
    """

    if root is None or k is None:
        return False

    root.visited = True

    if root.name == k:
        return True
    else:
        for child in root.children:
            if child.visited == False:
                rs = isRoute_DFS(child, k)
                if rs == True:
                    return True

    return False


root = Node(0)
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)

#root - [1,4,5]
root.children.append(n1)
root.children.append(n4)
root.children.append(n5)
#n1 - [3,4]
n1.children.append(n4)
n1.children.append(n3)
#n2 - [1]
n2.children.append(n1)
#n3 - [2,4]
n3.children.append(n2)
n3.children.append(n4)

rs = isRoute_DFS(root, 4)
print "Route from 0 to 4:", rs

print "Route from None to 4:", isRoute_DFS(None, 4)
