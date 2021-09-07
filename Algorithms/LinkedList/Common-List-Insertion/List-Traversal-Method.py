from Datastructures.LinkedList.LinkedListConstruct import LinkedList, Node, commonListIntersectionTraversal

listFirst = LinkedList()  # creating an empty list
listFirst.head = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)
fifth = Node(5)
listFirst.head.next = second
second.next = third
third.next = fourth
fourth.next = fifth
listSecond = LinkedList()  # creating an empty list
listSecond.head = Node(1)
second = Node(2)
third = Node(3)
listSecond.head.next = second
second.next = third
list = commonListIntersectionTraversal(
    listFirst, listSecond)
