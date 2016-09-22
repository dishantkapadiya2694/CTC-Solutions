"""Class for Node of graphs"""

class GraphNode():
    def __init__(self, val = None, children = [], marked = None):
        self.__val = val
        self.__children = children
        self.__marked = marked

    def data(self):
        return self.__val

    def neighbours(self):
        return self.__children

    def marked(self):
        return self.__marked

    def setData(self, newValue):
        self.__val = newValue

    def setMark(self, mark):
        self.__marked = mark

    def addNeighbour(self, node):
        assert isinstance(node, GraphNode)
        self.__children.append(node)

    def removeNeighbour(self, node):
        assert isinstance(node, GraphNode)
        self.__children.remove(node)



class BinaryTreeNode():
    def __init__(self, val = None, leftChildren = None, rightChildren = None, marked = None):
        self.__val = val
        self.__left = leftChildren
        self.__right = rightChildren
        self.__marked = marked

    def data(self):
        return self.__val

    def leftChildrens(self):
        return self.__left

    def rightChildrens(self):
        return self.__right

    def marked(self):
        return self.__marked

    def setData(self, newValue):
        self.__val = newValue

    def setMark(self, mark):
        self.__marked = mark

    def setLeftChild(self, node):
        assert isinstance(node, BinaryTreeNode)
        self.__left = node

    def removeLeftChild(self):
        self.__left = None

    def setRightChild(self, node):
        assert isinstance(node, BinaryTreeNode)
        self.__right = node

    def removeRightChild(self):
        self.__right = None