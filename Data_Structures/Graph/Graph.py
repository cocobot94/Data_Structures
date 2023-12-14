from QueueForGraph import Queue
from NodeGraph import GraphNode


class Graph:
    def __init__(self) -> None:
        self.nodes = dict()

    def getOrCreateNode(self, data):
        node = self.nodes.get(data)
        if node == None:
            node = GraphNode(data)
            self.nodes[node.value] = node
        return node

    def addEdge(self, start, last):
        startNode = self.getOrCreateNode(start)
        endNode = self.getOrCreateNode(last)
        startNode.addNeighbor(endNode)


class DepthFirstSearch:
    def recursiveDfSHelper(self, currentNode: GraphNode, target):
        if currentNode.value == target:
            return True
        currentNode.visited = True

        for node in currentNode.adjacents.values():
            if node.visited != True:
                if self.recursiveDfSHelper(node, target):
                    return True
        return False

    def depthFirstSearch(self, graph: Graph, target):
        for node in graph.nodes.values():
            if self.recursiveDfSHelper(node, target):
                return True
        return False


class BreathFirstSearch:
    def recursiveBfsHelper(self, node: GraphNode, target):
        queue = Queue()
        queue.push(node)
        while queue.isEmpty() != True:
            currentNode: GraphNode = queue.remove()
            if currentNode.value == target:
                return True
            currentNode.visited == True
            for adj in currentNode.adjacents.values():
                if adj.visited != True:
                    queue.push(adj)
        return False

    def breathFirstSearch(self, graph: Graph, target):
        for node in graph.nodes.values():
            if self.recursiveBfsHelper(node, target):
                return True
        return False


class RouteBetween:
    def isRouteBetween(self, graph: Graph, start: GraphNode, end: GraphNode):
        # if start or end not in graph.nodes.values():return
        if start == end:
            return True
        queue = Queue()
        queue.push(start)
        while not queue.isEmpty():
            next: GraphNode = queue.remove()
            if next == end:
                return True
            next.visited = True
            for node in next.adjacents.values():
                if node.visited != True:
                    queue.push(node)
        return False


if __name__ == "__main__":
    # test
    grapho = Graph()

    node0 = grapho.getOrCreateNode(0)
    node1 = grapho.getOrCreateNode(1)
    node3 = grapho.getOrCreateNode(3)
    node4 = grapho.getOrCreateNode(4)
    node6 = grapho.getOrCreateNode(6)

    grapho.addEdge(0, 1)
    grapho.addEdge(1, 2)
    grapho.addEdge(2, 0)
    grapho.addEdge(2, 3)
    grapho.addEdge(3, 2)
    grapho.addEdge(4, 6)
    grapho.addEdge(5, 4)
    grapho.addEdge(6, 5)

    # route = RouteBetween()
    # print(route.isRouteBetween(grapho,node4,node6))

    bb = BreathFirstSearch()
    print(bb.breathFirstSearch(grapho, 4))
