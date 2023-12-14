from Node import Node
from SingleLinkedList import SingleLinkedList
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

sll = SingleLinkedList()


def test_append():
    assert sll.append(node1) == node1
    assert sll.append(node2) == node1
    assert sll.append(node3) == node1
    assert sll.append(33) == TypeError


def test_insert_before():
    assert sll.insert_before(node5, 1) == node5
    assert sll.insert_before(node6, 3) == node5


def test_insert_after():
    assert sll.insert_after(node7, 1) == node5
    assert sll.insert_after(node8, 3) == node5
    assert sll.__str__() == "[5,1,7,2,6,3,8] --> 7"


def test_remove_head():
    assert sll.remove_head() == node5
    assert sll.remove_head() == node1
    assert sll.remove_head() == node7


def test_remove():
    assert sll.remove(4) == None
    assert sll.remove(3) == node3
    assert sll.remove(2) == node2
    assert sll.remove(1) == None


def test_sort():
    assert sll.sort() == None
    assert sll.__str__() == "[6,8] --> 2"
