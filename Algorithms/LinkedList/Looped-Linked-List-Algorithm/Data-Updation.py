from Datastructures.LinkedList.LinkedListConstruct import createdLinkedList

list = createdLinkedList()
list.head.next.next = list.head
print(list.listDataUpdationLoopFinder())
