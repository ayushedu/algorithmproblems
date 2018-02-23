from treenode import TreeNode

def countPathWithSum(root, target):
    if root is None:
        return 0

    pathFromRoot = countPathWithSumFromNode(root, target, 0)
    pathFromLeft = countPathWithSum(root.left, target)
    pathFromRight = countPathWithSum(root.right, target)

    return pathFromRoot + pathFromLeft + pathFromRight

def countPathWithSumFromNode(node, target, current):
    
    if node is None:
        return 0

    current += node.name
    totalPath = 0
    if current == target:
        totalPath += 1
        
    totalPath += countPathWithSumFromNode(node.left, target, current)
    totalPath += countPathWithSumFromNode(node.right, target, current)
    return totalPath

# Input
n3 = TreeNode(3)
n_2 = TreeNode(-2)
n1 = TreeNode(1)

n3_1 = TreeNode(3)
n3_1.left = n3
n3_1.right = n_2
n2 = TreeNode(2)
n2.right = n1
n11 = TreeNode(11)

n5 = TreeNode(5)
n5.left = n3_1
n5.right = n2
n_3 = TreeNode(-3)
n_3.right = n11

root = TreeNode(10)
root.left = n5
root.right = n_3

rs = countPathWithSum(root, 8)
print "Result:", rs
