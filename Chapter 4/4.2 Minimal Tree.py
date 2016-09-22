"""Given a sorted(increasing) array, find a way to create a binary search tree with minimal height"""

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


def inorder(node, space):
    if node != None:
        inorder(node.rightChildrens(), space + "   ")
        print '{0} {1}'.format(space ,node.data())
        inorder(node.leftChildrens(), space + "   ")


temp = minimalTree([1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 9])

inorder(temp, "")
