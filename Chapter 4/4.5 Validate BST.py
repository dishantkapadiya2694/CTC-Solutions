"""Implement a function to validate if a binary tree is binary search tree"""

from Nodes import BinaryTreeNode


def validateBSTHelper(node, min, max):
    if node == None:
        return True

    if node.data() < min or node.data() > max:
        return False

    else:
        return validateBSTHelper(node.leftChildrens(), min, node.data()) and validateBSTHelper(node.rightChildrens(), node.data(), max)

def validateBST(tree):
    return validateBSTHelper(tree, float("-inf"), float("inf"))

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

def inorder(node, space=""):
    if node != None:
        inorder(node.rightChildrens(), space + "   ")
        print '{0} {1}'.format(space ,node.data())
        inorder(node.leftChildrens(), space + "   ")

tree = BinaryTreeNode(8,BinaryTreeNode(1, BinaryTreeNode(0), BinaryTreeNode(100)),BinaryTreeNode(10, BinaryTreeNode(1)))
tree = minimalTree([1,2,3,4,5,6,7,8,9])
tree.rightChildrens().leftChildrens().leftChildrens().setLeftChild(BinaryTreeNode(5))
inorder(tree)

print validateBST(tree)
