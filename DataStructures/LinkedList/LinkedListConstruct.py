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
    def frontpush(self, new_node):
        new_node.next = self.head
        self.head = new_node

    # between insertion
    def betweenInsertion(self, prev_node, new_data):
        if prev_node is None:
            print("The given previous node shouldn't be None")
            return

        new_data_node = Node(new_data)
        new_data_node.next = prev_node.next
        prev_node.next = new_data_node

    # function for inserting a node at the end
    def endInsertion(self, new_data):
        last = self.head
        while(last.next):
            last = last.next
        last.next = Node(new_data)

    # function for deleting a node from the list
    def deleteNode(self, key):
        temp = self.head
        # if we want to delete the first linked list node
        if(temp.data == key):
            self.head = self.head.next
            return

        while(temp is not None):
            if(temp.data == key):
                break
            prev = temp
            temp = temp.next

        prev.next = temp.next
        temp = None

    # finding the length of a linked-list
    def printLength(self):
        temp = self.head
        c = 1
        while(temp.next):
            c = c + 1
            temp = temp.next
        return c

    # iterative search for a node in linked-list
    def iterativeSearch(self, search_node):
        if(self.head.data == search_node.data):
            return 0
        temp = self.head
        c = 1
        while(temp):
            if(temp.data == search_node.data):
                return c
            temp = temp.next
            c += 1
        return -1

    def recursiveSearch(self, list, value):
        if(not list):
            return -1

        if (list.data == value):
            return True

        return self.recursiveSearch(list.next, value)

    # n-th node searcher

    def searchNthNode(self, value):
        c = 0
        temp = self.head
        while(temp):
            if(temp.data == value):
                return c
            temp = temp.next
            c += 1
        return -1

    # single traversal middle node finder
    def singleTraversalFinder(self):
        # first finding the length for the linkedlist
        lFirst = 0
        lNext = 0
        temp = self.head
        while temp is not None:
            lFirst += 1
            temp = temp.next
        # now traversing the linked list to the half the length of lFirst
        temp = self.head
        while lNext < int(lFirst/2):
            lNext += 1
            temp = temp.next
        return temp.data

    # pointer methods for linkedlist traversal
    def pointerMethodTraversal(self):
        # Initialize two pointers, one will go one step a time(slow), another twice's at a time(fast)
        slow = self.head
        fast = self.head

        # Iterating till fast next is null valued
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow.data

    # counting how many times a particular is present in the list
    def countOccurrence(self, value):
        temp = self.head
        c = 0
        while temp:
            if temp.data == value:
                c += 1
            temp = temp.next
        return c


def createdLinkedList():
    llist = LinkedList()  # creating an empty list
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    fifth = Node(5)
    llist.head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth
    return llist
