class GraphNode:
    def __init__(self, value) -> None:
        self.value = value
        self.adjacents = {}
        self.visited = False
        self.next = None

    def addNeighbor(self, node):
        if node != None:
            if node.value not in self.adjacents.keys():
                self.adjacents[node.value] = node
