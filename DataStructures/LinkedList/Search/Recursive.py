from Datastructures.LinkedList.LinkedListConstruct import Node, createdLinkedList

linkedList = createdLinkedList()
data = linkedList.recursiveSearch(linkedList.head, 3)
if data:
    print("Key is present in the linkedlist!")
else:
    print("Key is not present in the linked list!")
