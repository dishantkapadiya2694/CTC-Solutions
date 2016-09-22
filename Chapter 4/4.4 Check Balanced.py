"""Balanced Binary Tree: a binary tree whose subtrees never differ in height by more then one
    design an algorithm to check if given tree is balanced."""


from Nodes import BinaryTreeNode

def minimalTree(arr):

    if len(arr) == 0:
        return None

    if len(arr) == 1:
        return BinaryTreeNode(arr[0])

    ind = len(arr)/2

    temp = BinaryTreeNode(arr[ind])
    arr.remove(arr[ind])

    templ = minimalTree(arr[:ind])
    if templ:
        temp.setLeftChild(templ)

    tempr = minimalTree(arr[ind:])
    if tempr:
        temp.setRightChild(tempr)
    return temp


def checkBalanced(tree):
    if tree != None:
        #val1 = checkBalance(tree)
        #val2 = checkBalanced(tree.leftChildrens())
        #val3 = checkBalanced(tree.rightChildrens())
        #return val1 and val2 and val3
        return checkBalance(tree) and checkBalanced(tree.leftChildrens()) and checkBalanced(tree.rightChildrens())
    else:
        return True

def checkBalance(node):
    return abs(height(node.leftChildrens()) - height(node.rightChildrens())) <= 1

def height(node):
    if node == None:
        return 0
    else:
        return 1 + max(height(node.leftChildrens()), height(node.rightChildrens()))

def inorder(node, space=""):
    if node != None:
        inorder(node.rightChildrens(), space + "   ")
        print '{0} {1}'.format(space ,node.data())
        inorder(node.leftChildrens(), space + "   ")


tree = minimalTree([1,2,3,4,5,6,7,8,9])

a = tree.leftChildrens()
b = a.leftChildrens()
c = b.leftChildrens()
a.rightChildrens().setLeftChild(BinaryTreeNode(10))
b.setRightChild(BinaryTreeNode(10))
c.setLeftChild(BinaryTreeNode(5, BinaryTreeNode(5)))


inorder(tree)

print checkBalanced(tree)