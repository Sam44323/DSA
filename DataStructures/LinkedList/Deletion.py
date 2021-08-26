from Datastructures.LinkedList.LinkedListConstruct import Node, createdLinkedList

list = createdLinkedList()
list.endInsertion(4)
list.endInsertion(5)
list.printList()
print("*" * 100)
list.deleteNode(5)
list.printList()
print("*" * 100)
