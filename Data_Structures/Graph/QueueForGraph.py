from SingleLinkedlistForQueue import SingleLinkedList


class Queue:
    def __init__(self) -> None:
        self.sll = SingleLinkedList()

    def isEmpty(self):
        return self.sll.isEmpty()

    def peek(self):
        return self.sll.peek()

    def push(self, data):
        return self.sll.append(data)

    def remove(self):
        return self.sll.removeHead()

    def Size(self):
        return self.sll.Size()

    def __str__(self) -> str:
        return self.sll.__str__()


if __name__ == "__main__":
    q = Queue()
    print(q.isEmpty())
    print(q.remove())
    print(q.peek())
    print(q.push(22).value)
    q.push(8)
    q.peek()
    q.push(23)
    print(q.Size())
    # print(q.remove())
    print(q.peek().value)
    print(q.Size())
    print(q.peek().value)
    print(q)
    print(type(q.remove()))
    print(q.peek().value)
    print(q)
    print(q.remove().value)
    print(q.peek().value)
