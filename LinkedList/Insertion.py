from LinkedListConstruct import Node, createdLinkedList, LinkedList

# front-side insertion to linked list

list = createdLinkedList()
list.frontpush(Node(4))
list.printList()

print("*" * 100)

# between insertion

llist = LinkedList()
llist.head = Node(1)
second = Node(2)
llist.head.next = second
third = Node(3)
second.next = third
llist.betweenInsertion(second, 4)
llist.printList()
