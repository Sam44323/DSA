# Node Class

class Node:

    # initializing the node object
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    # initializing the linked list
    def __init__(self):
        self.head = None

    # function for printing the linked list
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next

    # front side pushing
    def frontpush(self, new_node: Node):
        new_node.next = self.head
        self.head = new_node


def createdLinkedList():
    llist = LinkedList()  # creating an empty list
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    llist.head.next = second
    second.next = third
    return llist
