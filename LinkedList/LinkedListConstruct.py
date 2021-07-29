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
