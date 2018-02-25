from treenode import TreeNode
from collections import OrderedDict

def incrementHashTable(pathDict, key, delta):
    """Increment the dictionary for keeping running sum per node"""

    newCount = delta
    hasKey = False

    if pathDict.has_key(key):
        newCount += pathDict.get(key)
        hasKey = True

    if newCount == 0 and hasKey:
        del pathDict[key]

    pathDict[key] = newCount

def countPathWithSum(root, target):
    return countPathWithSumFromNode(root, target, 0, OrderedDict())


def countPathWithSumFromNode(node, target, runningSum, pathDict):
    """Return total path with sum equal to target"""

    if node is None:
        return 0

    print 'Before:', node.name, pathDict

    runningSum += node.name
    sum = runningSum - target
    totalPath = 0

    if pathDict.has_key(sum):
        totalPath = pathDict.get(sum)

    if runningSum == target:
        totalPath += 1
        
    incrementHashTable(pathDict, runningSum, 1)
    totalPath += countPathWithSumFromNode(node.left, target, runningSum, pathDict)
    totalPath += countPathWithSumFromNode(node.right, target, runningSum, pathDict)
    incrementHashTable(pathDict, runningSum, -1)

    print 'After:', node.name, pathDict, totalPath

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
