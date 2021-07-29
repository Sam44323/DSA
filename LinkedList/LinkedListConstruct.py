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

    # between insertion
    def betweenInsertion(self, prev_node: Node, new_data):
        if prev_node is None:
            print("The given previous node shouldn't be None")
            return

        new_data_node = Node(new_data)
        new_data_node.next = prev_node.next
        prev_node.next = new_data_node

    def endInsertion(self, new_data: int):
        last: Node = self.head
        while(last.next):
            last = last.next
        last.next = Node(new_data)


def createdLinkedList():
    llist = LinkedList()  # creating an empty list
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    llist.head.next = second
    second.next = third
    return llist
