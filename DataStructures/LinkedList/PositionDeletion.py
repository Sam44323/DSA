from Datastructures.LinkedList.LinkedListConstruct import LinkedList, Node

llist = LinkedList()
llist.head = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)

llist.head.next = second
second.next = third
third.next = fourth

llist.printList()
print("*" * 30)
print(' ')

llist.deletePosNode(2)
llist.printList()
print("*" * 30)
print(' ')
