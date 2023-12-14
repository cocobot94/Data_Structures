from Node import Node
from Queue import Queue
import pytest

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

queue = Queue()


def test_isEmpty():
    assert queue.isEmpty() == True


@pytest.mark.parametrize(
    "node,expected",
    [
        (node1, node1),
        (node2, node1),
        (node3, node1),
        (node4, node1),
        (node5, node1),
        (node6, node1),
        (node7, node1),
        (8, TypeError),
        (node9, node1),
    ],
)
def test_push(node, expected):
    assert queue.push(node) == expected


def test_remove():
    assert queue.remove().value == 1
    assert queue.remove().value == 2
    assert queue.remove().value == 3
    assert queue.remove().value == 4
    assert queue.remove().value == 5
    assert queue.remove().value == 6
    assert queue.remove().value == 7
    assert queue.remove().value == 9
    assert queue.remove() == None
