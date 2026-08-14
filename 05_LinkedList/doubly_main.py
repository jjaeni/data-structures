# Doubly Linked List
from doubly_linked_list_practice import Node, DoublyLinkedList

def test_doubly_linked_list():
    L = DoublyLinkedList()
    L.insert_after(None, 2)
    L.insert_after(Node(2), 5)
    L.push_front(9)
    L.insert_before(Node(5), 7)
    L.print_list()

    L.search(9)
    L.is_empty()

    L2 = DoublyLinkedList()
    L2.push_front(10)
    L2.push_front(8)
    L2.print_list()

    L.join(L2)
    L.print_list()

    L3 = L.split(L.search(7))
    L3.print_list()
    L.print_list()

    print('size: ', len(L3))

test_doubly_linked_list()