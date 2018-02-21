from treenode import TreeNode

def createMinimal(arr):
    return createMinimalBst(arr, 0, len(arr)-1)

def createMinimalBst(arr, start, end):
    if end < start:
        return None

    mid = (start+end)/2
    print "Mid:", mid, arr[mid]

    n = TreeNode(arr[mid])
    n.left = createMinimalBst(arr, start, mid-1)
    n.right = createMinimalBst(arr, mid+1, end)
    print "left, mid, right", n.left, n, n.right
    return n

def print_(n):
    if not n:
        return
    print n
    print_(n.left)
    print_(n.right)

input = [2,4,6,8,10,20]
n = createMinimal(input)
print_(n)
