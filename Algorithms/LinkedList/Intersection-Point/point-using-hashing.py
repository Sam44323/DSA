from Datastructures.LinkedList.LinkedListConstruct import LinkedList, Node, intersectionFinderUsingHashing

common = Node(8)

listFirst = LinkedList()
listFirst.head = Node(3)
listFirst.head.next = Node(6)
listFirst.head.next.next = Node(9)
listFirst.head.next.next.next = common
listFirst.head.next.next.next.next = Node(30)
listSecond = LinkedList()
listSecond.head = Node(10)
listSecond.head.next = common
listSecond.head.next.next = Node(100)
print(intersectionFinderUsingHashing(listFirst, listSecond))
