from Datastructures.LinkedList.LinkedListConstruct import LinkedList, Node

common = Node(6)

listFirst = LinkedList()  # creating an empty list
listFirst.head = Node(3)
listFirst.next = Node(6)
listFirst.next.next = Node(9)
listFirst.next.next.next = common
listFirst.next.next.next.next = Node(30)

listSecond = Node(10)
listSecond.next = common
listSecond.next.next = Node(30)
