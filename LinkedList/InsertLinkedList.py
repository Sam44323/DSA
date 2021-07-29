from LinkedListConstruct import LinkedList, Node

llist = LinkedList()  # creating an empty list
llist.head = Node(1)
second = Node(2)
third = Node(3)
llist.head.next = second
second.next = third

llist.printList()
