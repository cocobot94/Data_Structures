from Node import Node


class Tree:
    def __init__(self, data) -> None:
        self.root = Node(data)

    def __add(self, node: Node, data):
        if node == None:
            return
        if data < node.value:
            if node.left == None:
                node.left = Node(data)
            else:
                self.__add(node.left, data)
        else:
            if node.rigth == None:
                node.rigth = Node(data)
            else:
                self.__add(node.rigth, data)
        return

    def add(self, data):
        return self.__add(self.root, data)

    def __inOrdentraversal(self, node: Node):
        if node == None:
            return
        self.__inOrdentraversal(node.left)
        print(node.value, end=", ")
        self.__inOrdentraversal(node.rigth)

    def __preOrdenTraversal(self, node: Node):
        if node == None:
            return
        print(node.value, end=", ")
        self.__preOrdenTraversal(node.left)
        self.__preOrdenTraversal(node.rigth)

    def __postOrdentraversal(self, node: Node):
        if node == None:
            return
        self.__postOrdentraversal(node.left)
        self.__postOrdentraversal(node.rigth)
        print(node.value, end=", ")

    def inOrden(self):
        print("In Orden: ")
        self.__inOrdentraversal(self.root)

    def preOrden(self):
        print("Pre Orden: ")
        self.__preOrdenTraversal(self.root)

    def postOrden(self):
        print("Post Orden: ")
        self.__postOrdentraversal(self.root)

    def __invertTree(self, node: Node):
        if node == None:
            return
        temp = node.left
        node.left = self.__invertTree(node.rigth)
        node.rigth = self.__invertTree(temp)
        return node

    def invertTree(self):
        self.__invertTree(self.root)

    def Root(self):
        return self.root


class Search:
    def search(self, node: Node, target):
        if node == None:
            return False
        elif node.value == target:
            return True
        elif target < node.value:
            return self.search(node.left, target)
        else:
            return self.search(node.rigth, target)


if __name__ == "__main__":
    arbol = Tree(20)
    arbol.add(15)
    arbol.add(35)
    arbol.add(22)
    arbol.add(33)
    arbol.add(8)
    arbol.add(7)
    arbol.add(6)
    arbol.add(36)
    arbol.add(3)
    arbol.inOrden()
    arbol.preOrden()
    arbol.postOrden()
    print()
    print()
    print()
    arbol.invertTree()
    print()
    arbol.inOrden()
    print()
    arbol.preOrden()
    print()
    arbol.postOrden()
    print()
    arbol.invertTree()
    arbol.inOrden()
    print()
    print()
    b = Search()
    print(b.search(arbol.Root(), 6))
    print()
    print(b.search(arbol.Root(), 3))
