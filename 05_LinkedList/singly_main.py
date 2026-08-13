# SinglyL inked List
from singly_linked_list import Node, SinglyLinkedList

def test_singly_linked_list():
    L = SinglyLinkedList()

    L.push_front(10)
    L.push_back(20)
    L.push_front(30)
    L.print_list()

    L.pop_back()
    L.print_list()

    print('list has', len(L), 'nodes.')

test_singly_linked_list()