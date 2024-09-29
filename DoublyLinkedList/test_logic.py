# import the DoublyLinkedList class from logic.py
from logic import DoublyLinkedList



def test_delete_by_value():
    # Create a DoublyLinkedList object
    dll = DoublyLinkedList()

    # Test case 1: Deleting from an empty list
    dll.delete_by_value(5)  # Expected output: Linked List is empty

    # Test case 2: Deleting from a list with only one node
    dll.add_end(5)  # Add a node with value 5
    dll.delete_by_value(10)  # Expected output: x is not present in the LL
    dll.delete_by_value(5)  # Expected output: Linked List is empty

    # Test case 3: Deleting the first node
    dll.add_end(10)  # Add a node with value 10
    dll.add_end(20)  # Add a node with value 20
    dll.delete_by_value(10)  # Expected output: Linked List is empty

    # Test case 4: Deleting a node in the middle
    dll.add_end(10)  # Add a node with value 10
    dll.add_end(20)  # Add a node with value 20
    dll.add_end(30)  # Add a node with value 30
    dll.delete_by_value(20)  # Expected output: 10 <-> 30

    # Test case 5: Deleting the last node
    dll.add_end(40)  # Add a node with value 40
    dll.delete_by_value(40)  # Expected output: 10 <-> 30

    # Test case 6: Deleting a non-existent value
    dll.delete_by_value(50)  # Expected output: x is not present in the LL

test_delete_by_value()