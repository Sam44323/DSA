from Datastructures.LinkedList.LinkedListConstruct import createdLinkedList

list = createdLinkedList()
list.head.next.next.next = list.head
print(list.hashingCheckLoop())
