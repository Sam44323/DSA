from LinkedList import LinkedList, Node

if __name__ == '__main__':
    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)

    llist.head.next = second
    second.next = third
    third.next = fourth
