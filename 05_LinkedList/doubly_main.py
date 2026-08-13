# Doubly Linked List
from doubly_linked_list import Node, DoublyLinkedList

def test_doubly_linked_list():
    L = DoublyLinkedList()

    L.push_back(9)
    L.push_back(2)
    L.push_back(5)
    L.push_back(7)
    L.print_list()

    L.splice(9, 5, 7)
    L.print_list()
    print('size:', len(L), '\n')

test_doubly_linked_list()