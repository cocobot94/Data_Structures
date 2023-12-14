from Node import Node


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
        if not isinstance(node, Node):
            return TypeError
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
