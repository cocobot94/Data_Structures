from Node import Node


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
            return self.peek()
        elif data == self.head.value:
            node.next = self.head
            self.head = node
            self.size += 1
            return self.peek()
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
            self.size += 1
            return self.peek()
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
            popped.next = None
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
    print(sll)
