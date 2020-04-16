import math

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def findClosestValueInBST(tree, target):
    return helper(tree, target, math.inf)

def helper(tree, target, closest):
    if tree is None or closest ==target:
        return closest
    if abs(target - closest) > abs(target - tree.value):
        closest = tree.value
    if tree.value > target:
        return helper(tree.left, target, closest)
    else:
        return helper(tree.right, target, closest)


if __name__ == '__main__':
    tree = Node(10)
    tree.left = Node(5)
    tree.right = Node(15)
    tree.left.left = Node(2)
    tree.left.right = Node(5)
    tree.right.left = Node(13)
    tree.right.right = Node(22)
    tree.left.left.left = Node(1)
    tree.right.left.right = Node(14)

    print(findClosestValueInBST(tree, 14))
