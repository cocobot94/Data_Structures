class Node:
    def __init__(self) -> None:
        self.value = None
        self.next = None
        self.left = None
        self.rigth = None
        self.adjacents = {}
        self.visited = False
        self.before = None

    def addNeighbor(self, node):
        if node not in self.adjacents.values():
            self.adjacents[node.value] = node
        return


class Stack:
    def __init__(self) -> None:
        self.top = None
        self.size = 0

    def isEmpty(self):
        return self.top == None

    def peek(self):
        if self.isEmpty():
            return
        return self.top

    def push(self, node):
        if self.isEmpty():
            self.top = node
        else:
            node.next = self.top
            self.top = node
        self.size += 1
        return self.peek()

    def pop(self):
        if self.isEmpty():
            return
        else:
            popped = self.top
            self.top = self.top.next
            self.size -= 1
            return popped

    def __str__(self) -> str:
        string = "["
        current = self.top
        while current != None:
            string += str(current.value)
            if current.next != None:
                string += ","
            current = current.next
        string += "]"
        return f"{string} --> {self.size}"


class Queue:
    def __init__(self) -> None:
        self.first = None
        self.last = None
        self.size = 0

    def isEmpty(self):
        return self.first == None

    def peek(self):
        if self.isEmpty():
            return
        return self.first

    def push(self, node: Node):
        if self.isEmpty():
            self.first = self.last = node
        else:
            self.last.next = node
            self.last = node
        self.size += 1
        return self.peek()

    def remove(self):
        if self.isEmpty():
            return
        else:
            popped = self.first
            if self.last == self.first:
                self.last = None
            self.first = self.first.next
            self.size -= 1
            popped.next = None
            return popped

    def __str__(self) -> str:
        string = "["
        current = self.first
        while current != None:
            string += str(current.value)
            if current.next != None:
                string += ","
            current = current.next
        string += "]"
        return f"{string} --> {self.size}"


class SingleLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.last = None
        self.size = 0

    def isEmpty(self):
        return self.head == None

    def peek(self):
        if self.isEmpty():
            return
        return self.head

    def append(self, node: Node):
        if not isinstance(node, Node):
            return TypeError
        if self.isEmpty():
            self.head = self.last = node
        else:
            self.last.next = node
            self.last = node
        self.size += 1
        return self.peek()

    def insert_before(self, node: Node, data):
        if not isinstance(node, Node):
            return TypeError
        if self.isEmpty():
            self.head = self.last = node
        elif data == self.head.value:
            node.next = self.head
            self.head = node
        else:
            current = self.head
            while current.next != None:
                if current.next.value == data:
                    node.next = current.next
                    current.next = node
                    self.size += 1
                    return self.peek()
                current = current.next
            self.last.next = node
            self.last = node
        self.size += 1
        return self.peek()

    def insert_after(self, node: Node, data):
        if not isinstance(node, Node):
            return TypeError
        if self.isEmpty():
            self.head = self.last = node
        else:
            current = self.head
            while current != None:
                if current.value == data:
                    if current == self.last:
                        self.last = node
                    node.next = current.next
                    current.next = node
                    self.size += 1
                    return self.peek()
                current = current.next
            self.last.next = node
            self.last = node
        self.size += 1
        return self.peek()

    def remove_head(self):
        if self.isEmpty():
            return
        else:
            popped = self.head
            if self.last == self.head:
                self.last = None
            self.head = self.head.next
            self.size -= 1
            popped.next = None
            return popped

    def remove(self, data):
        if self.isEmpty():
            return
        elif self.head.value == data:
            return self.remove_head()
        else:
            current = self.head
            while current != None and current.next != None:
                if current.next.value == data:
                    popped = current.next
                    if current.next == self.last:
                        self.last = current
                    current.next = current.next.next
                    self.size -= 1
                    popped.next = None
                    return popped
                current = current.next
            return

    def __quicksort(self, arr: list):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return self.__quicksort(left) + middle + self.__quicksort(right)

    def __get_dict_and_clean_list(self):
        nodes = {}
        while self.head is not None:
            popped = self.remove_head()
            # popped.next = None
            nodes[popped.value] = popped
        return nodes

    def sort(self):
        nodes = self.__get_dict_and_clean_list()
        arr = [item for item in nodes.keys()]
        array_values = self.__quicksort(arr)
        for value in array_values:
            self.append(nodes.get(value))
        return

    def __str__(self) -> str:
        string = "["
        current = self.head
        while current != None:
            string += str(current.value)
            if current.next != None:
                string += ","
            current = current.next
        string += "]"
        return f"{string} --> {self.size}"


class TrieNode:
    def __init__(self) -> None:
        self.value = None
        self.adjacents = {}
        self.isEndofWord = False


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str):
        if not isinstance(word, str):
            return TypeError
        lowerCaseWord = word.lower()
        currentNode = self.root
        for c in lowerCaseWord:
            node = currentNode.adjacents.get(c)
            if node is None:
                node = TrieNode()
                node.value = c
                currentNode.adjacents[node.value] = node
            currentNode = node

    def search(self, word: str):
        if not isinstance(word, str):
            return TypeError
        lowerCaseWord = word.lower()
        currentNode = self.root
        for c in lowerCaseWord:
            currentNode = currentNode.adjacents.get(c)
            if currentNode is None:
                return False
        return True


class Graph:
    def __init__(self) -> None:
        self.nodes = {}

    def addNode(self, node: Node):
        if not isinstance(node, Node):
            return TypeError
        if node not in self.nodes.values():
            self.nodes[node.value] = node
        return

    def addEdge(self, startNode: Node, endNode: Node):
        if not isinstance((startNode, endNode), Node):
            return TypeError
        startNode.addNeighbor(endNode)
        endNode.addNeighbor(startNode)


class BreathFirstSearch:
    def recursiveBfsHelper(self, currentNode: Node, target):
        pass

    def breathFirstSearch(self, graph: Graph, target):
        pass


class DepthFirstSearch:
    def recursiveDfsHelper(self, node: Node, target):
        pass

    def depthFirstSearch(self, graph: Graph, target):
        pass


if __name__ == "__main__":
    node1 = Node()
    node1.value = 1
    node2 = Node()
    node2.value = 2
    node3 = Node()
    node3.value = 3
    node4 = Node()
    node4.value = 4
    node5 = Node()
    node5.value = 5
    node6 = Node()
    node6.value = 6
    node7 = Node()
    node7.value = 7
    lista_nodes = [node1, node2, node3, node4, node5]
    node9 = Node()
    node9.value = 9
    node8 = Node()
    node8.value = 8

    """
    # Trie 
    t = Trie()
    t.insert("Coco")
    t.insert("MacaCo")
    t.insert("esthillita")

    print(t.search("coc"))
    print(t.search("miaca"))
    print(t.search("Esthi"))
    print(t.search("Estud"))

    print()"""

    """
    # Lista ENlazada
    sll = SingleLinkedList()
    for node in lista_nodes:
        sll.append(node)
    print(sll)
    sll.insert_before(node7, 3)
    sll.insert_after(node8, 4)
    print(sll)
    sll.insert_before(node9, 1)
    print(sll)

    sll.insert_after(node6, 5)
    print(sll)
    print("#########")
    sll.sort()
    print(sll)"""

    """
    # Cola
    queue = Queue()
    for node in lista_nodes:
        queue.push(node)
    print(queue)
    queue.remove()
    print(queue.remove().value)
    print(queue.remove().value)
    print(queue)
    queue.push(node7)
    print(queue.remove().value)
    print(queue)"""

    """ 
    # STACK
    print(lista_nodes)
    stack = Stack()
    for node in lista_nodes:
        stack.push(node)
    print(stack)
    print(stack.pop().value)
    stack.push(node7)
    print(stack)
    print(stack.pop().value)
    print(stack.pop().value)
    print(stack.pop().value)
    print(stack)"""

    g = Graph()
    g.addNode(node1)
    g.addNode(node2)
    g.addNode(node3)
    g.addNode(node4)
    g.addNode(node5)
    g.addNode(node6)
    g.addNode(node7)
    g.addNode(node8)
    g.addNode(node9)

    g.addEdge(node1, node2)
    g.addEdge(node1, node3)
    g.addEdge(node1, node7)
    g.addEdge(node2, node4)
    g.addEdge(node3, node2)
    g.addEdge(node2, node5)
    g.addEdge(node7, node6)
    g.addEdge(node2, node4)
    g.addEdge(node7, node5)
    g.addEdge(node7, node9)
    g.addEdge(node9, node8)

    """s = ShortestWay()

    print(s.shortestWay(g,node5,node3))
    print()
    print(s.shortestWay(g,node1,node6))
    print()
    print(s.shortestWay(g,node3,node6))


    bfs = BreathFirstSearch()
    print(bfs.breathFirstSearch(g,9))
    print(bfs.breathFirstSearch(g,3))
    print(bfs.breathFirstSearch(g,6))

    print()

    dfs = DepthFirstSearch()
    print(dfs.depthFirstSearch(g,6))
    print(dfs.depthFirstSearch(g,4))"""
