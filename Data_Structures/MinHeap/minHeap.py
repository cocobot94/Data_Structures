from Node import Node


class minHeap:
    def __init__(self) -> None:
        self.heap = []
        self.size = 0

    def parentIndex(self, i):
        return int((i - 1) / 2)

    def leftChildIndex(self, i):
        return int((i * 2) + 1)

    def rigthChildIndex(self, i):
        return int((i * 2) + 2)

    def swap(self, x, y):
        temp = self.heap[x]
        self.heap[x] = self.heap[y]
        self.heap[y] = temp

    def isLeaf(self, i):
        if self.leftChildIndex(i) >= self.size and self.rigthChildIndex(i) >= self.size:
            return True
        return False

    def insert(self, element):
        if element == None:
            return
        self.heap.append(element)
        current = self.size
        while self.heap[current] < self.heap[self.parentIndex(current)]:
            self.swap(current, self.parentIndex(current))
            current = self.parentIndex(current)
        self.size += 1

    def extractMin(self):
        if self.size == 0:
            return
        popped = self.heap[0]
        self.heap[0] = self.heap[self.size - 1]
        self.size -= 1
        self.minHeapfy(0)
        self.heap.pop()
        return popped

    def minHeapfy(self, i):
        if not self.isLeaf(i):
            while (
                self.heap[i] > self.heap[self.leftChildIndex(i)]
                or self.heap[i] > self.heap[self.rigthChildIndex(i)]
            ):
                if (
                    self.heap[self.leftChildIndex(i)]
                    < self.heap[self.rigthChildIndex(i)]
                ):
                    self.swap(i, self.leftChildIndex(i))
                    self.minHeapfy(self.leftChildIndex(i))
                else:
                    self.swap(i, self.rigthChildIndex(i))
                    self.minHeapfy(self.rigthChildIndex(i))

    def printHeap(self):
        rango = int((self.size / 2))
        for i in range(0, rango):
            print(f"Parent: {self.heap[i]}")
            if self.leftChildIndex(i) < self.size:
                print(f"Left: {self.heap[self.leftChildIndex(i)]}")
            if self.rigthChildIndex(i) < self.size:
                print(f"Rigth: {self.heap[self.rigthChildIndex(i)]}")

    def __str__(self) -> str:
        return str(self.heap)


if __name__ == "__main__":
    minheap = minHeap()
    minheap.insert(5)
    minheap.insert(10)
    minheap.insert(12)
    minheap.printHeap()
    print()
    minheap.insert(9)
    minheap.insert(15)
    minheap.printHeap()
    print()
    minheap.insert(1)
    minheap.insert(4)
    minheap.printHeap()
    print()
    minheap.extractMin()
    # minheap.insert(44)
    minheap.printHeap()
    print(minheap)
    print()
    minheap.extractMin()
    minheap.insert(44)
    minheap.printHeap()
    minheap.extractMin()
    minheap.extractMin()
    print()
    minheap.printHeap()
    print(minheap)

    # use this:
    """
        minheap = minHeap()
    minheap.insert(5)
    minheap.insert(10)
    minheap.insert(12)
    print(minheap)
    minheap.insert(9)
    minheap.insert(15)

    print()
    minheap.insert(1)
    minheap.insert(4)
 
    print(minheap)
    print(minheap.extractMin())
    #minheap.insert(44)

    print(minheap)
    print()
    print(minheap.extractMin())
    minheap.insert(44)
    print(minheap.extractMin())
    print(minheap.extractMin())
    print()

    print(minheap)   

    """
