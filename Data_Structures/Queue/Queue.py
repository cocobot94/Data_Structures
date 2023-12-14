from Node import Node


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
        if not isinstance(node, Node):
            return TypeError
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
