"""Given a directed graph, design an algorithm to find out whether there is a route between two nodes."""

from Nodes import GraphNode
from Queue import Queue

five = GraphNode(5)
six = GraphNode(6)
one = GraphNode(1)
four = GraphNode(4)
fivedash = GraphNode(5)
three = GraphNode(3)
nine = GraphNode(9)

five.addNeighbour(six)
five.addNeighbour(one)
six.addNeighbour(fivedash)
fivedash.addNeighbour(three)
one.addNeighbour(four)
four.addNeighbour(six)
three.addNeighbour(four)

def searchPath(source, dest):
    assert isinstance(source, GraphNode)
    assert isinstance(dest, GraphNode)

    q = Queue()
    source.setMark(True)
    q.enqueue(source)

    while not q.isEmpty():
        temp = q.dequeue()
        assert isinstance(temp, GraphNode)
        if temp == dest:
            return True
        for child in temp.neighbours():
            assert isinstance(child, GraphNode)
            if not child.marked():
                child.setMark(True)
                q.enqueue(child)

    return False

print searchPath(nine, five)



