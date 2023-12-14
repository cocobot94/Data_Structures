from NodeGraph import GraphNode as Node


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
        else:
            return self.head

    def append(self, data):
        node = Node(data)
        if self.isEmpty():
            self.head = self.last = node
        else:
            self.last.next = node
            self.last = node
        self.size += 1
        return self.peek()

    def removeHead(self):
        if self.isEmpty():
            return
        else:
            deleted = self.head
            if self.last == self.head:
                self.last == None
            self.head = self.head.next
            self.size -= 1
            return deleted

    def remove(self, data):
        deleted = None
        if self.isEmpty():
            return
        elif data == self.head.value:
            deleted = self.head
            if self.last == self.head:
                self.last == None
            self.head = self.head.next
            self.size -= 1
            return deleted
        else:
            current = self.head
            while current != None and current.next != None:
                if current.next.value == data:
                    deleted = current.next
                    if current.next == self.last:
                        self.last = current
                    current.next = current.next.next
                current = current.next

            self.size -= 1
            return deleted

    def Size(self):
        return self.size

    def __str__(self) -> str:
        string = "["
        current = self.head
        while current != None:
            string += str(current.value)
            if current.next != None:
                string += ", "
            current = current.next
        string += "]"
        return string


if __name__ == "__main__":
    l = SingleLinkedList()
    print(l.isEmpty())
    print(l.peek())
    print(l.append(2).value)
    l.append(3)
    l.append(5)
    l.append(8)
    print(l)
    print(l.removeHead().value)
    print(l)
    print(l.removeHead().value)
    print(l)
    print(l.removeHead().value)
    print(l)
    print(type(l.removeHead()))
    print(l)
    print(l.removeHead())
