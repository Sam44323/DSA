# Node Class


from typing import Any


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

    # checking for loop in a linkedlist using hashing
    def hashingCheckLoop(self):
        temp = self.head
        values = set()
        while temp:
            if(temp.data in values):
                return "This is a looped linked list"
            values.add(temp.data)
            temp = temp.next
        return "This ain't a looped linked list"

    # checking for loop in a linkedlist using floyd-cycle-algorithm
    def floydCycleAlgorithmLoop(self):
        slow = self.head
        fast = self.head
        while fast and fast.next and slow:
            slow = slow.next
            fast = fast.next.next
            if(slow == fast):
                return "This linked list has a loop"
        return "This is not a looped linked list"

    # checking for loop in a linkedlist using list data updation
    def listDataUpdationLoopFinder(self):
        if(self.head is None):
            return "This is en empty list"
        self = self.head
        while self:
            if(self.data == -1):
                return "This is a loop"
            self.data = -1
            self = self.next
        return "This is not a loop"

    # palindrome check using list
    def listPopperPalindrome(self):
        values = list()
        fCount = 0
        sCount = 0
        temp = self.head
        while temp:
            values.append(temp.data)
            fCount += 1
            temp = temp.next
        temp = self.head
        while temp:
            if(values):
                if(temp.data == values.pop()):
                    sCount += 1
            temp = temp.next
        return fCount == sCount

    # remove duplicates using traversal
    def traversalRemoveDuplicates(self):
        self = self.head
        if self is None:
            return
        while self and self.next is not None:
            if(self.data == self.next.data):
                self.next = self.next.next
            else:
                self = self.next  # we'll be moving to the next node only when we are sure there is not duplicates for the current node value

    # remove duplicates using recursion
    def recursionRemoveDuplicates(self):
        if(self.head is None):
            return
        # creating a function for recursion

        def mainFunction(value):
            if(value.next is not None):
                if (value.data == value.next.data):
                    value.next = value.next.next
                    mainFunction(value)
                else:
                    mainFunction(value.next)
        mainFunction(self.head)

    # swapping nodes x and y in the linked list by chaning the links
    def swapNodesByLinks(self, x, y):

        # if x and y are same
        if x == y:
            return

        prevX = None
        currX = self.head
        # search for x (storing the track for prev node and the current node)

        while currX != None and currX.data != x:
            prevX = currX
            currX = currX.next

        prevY = None
        currY = self.head
        # search for y(storing the track for prev node and the current node)

        while currY != None and currY.data != y:
            prevY = currY
            currY = currY.next

        # if either x, y or none of them are present in the linked list
        if currX == None or currY == None:
            return

        # if x is not the head
        if prevX != None:
            prevX.next = currY
        else:
            # else make y the head
            self.head = currY

        # if y is not the head
        if prevY != None:
            prevY.next = currX
        else:
            # else make x the head
            self.head = currX

        # swapping the next pointer
        temp = currX.next
        currX.next = currY.next
        currY.next = temp

    # pair swapping standard method
    def pairwiseSwappingStandard(self):
        temp = self.head
        if temp is None:
            return

        # start swapping only if list has more than two nodes
        while temp and temp.next:
            # when both the current and next nodes are different
            if temp.data != temp.next.data:
                temp.data, temp.next.data = temp.next.data, temp.data

            temp = temp.next.next

    # pair swapping recursive method
    def pairwiseSwappingRecursive(self):
        temp = self.head
        if temp is None:
            return

        def recursiveFunction(node):
            if node.next is None or node.next.next is None:
                return
            if node.data != node.next.data:
                node.data, node.next.data = node.next.data, node.data

            recursiveFunction(node.next.next)

        recursiveFunction(temp)

    def firstLastTransfer(self):
        temp = self.head
        secondLast = None

        # if the linked list has only one node
        if temp is None or temp.next is None:
            return

        # traversing the list to store the second last node and last node
        while temp and temp.next:
            secondLast = temp
            temp = temp.next

        # shifting the last node to the front
        secondLast.next = None
        temp.next = self.head
        self.head = temp

    # function for sorting a linked list using quick sort mechanism
    def quickSortLinkedList(self, end: LinkedList):
        start = self.head
        if(start == None or start == end or start == end.next):
            return


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

# traversal common list intersection checker


def commonListIntersectionTraversal(a: LinkedList or Any, b: LinkedList or Any):
    temp = LinkedList()
    new_list = temp
    temp.head = Node(None)
    temp = temp.head
    (a, b) = (a.head, b.head)

    if a == None or b == None:
        return

    while a != None and b != None:
        if (a.data == b.data):
            temp.next = Node(a.data)
            temp = temp.next
            a = a.next
            b = b.next

        elif (a.data < b.data):
            a = a.next
        else:
            b = b.next
    return new_list

# looping method for finding the intersection point for two linked-list


def intersectionPointLoopMethod(a: LinkedList, b: LinkedList):
    tempFirst = a.head
    c = 0
    while tempFirst != None:
        tempSecond = b.head
        while tempSecond != None:
            if(tempFirst.data == tempSecond.data):
                c = tempFirst.data
                return c
            tempSecond = tempSecond.next
        tempFirst = tempFirst.next
    return 'No intersection found'

# node count difference method for finding the intersection point for two linked-list


def intersectionPointNodeCountDifferenceMethod(a: LinkedList, b: LinkedList):
    # finding the difference between the length of lists
    d = abs(a.printLength() - b.printLength())

    def traverseListMethodAndFind(longer: LinkedList, shorter: LinkedList, limit: int):
        c = 1
        while c <= limit:
            longer = longer.next
            c += 1

        c = 0
        while longer != None and shorter != None:
            if (longer.data == shorter.data):
                return longer.data
            longer = longer.next
            shorter = shorter.next
        return 'No intersection found'

    # traversing the bigger list till d point and finding the intersection point
    if a.printLength() > b.printLength():
        data = traverseListMethodAndFind(a.head, b.head,  d)
    else:
        data = traverseListMethodAndFind(b.head, a.head, d)
    print(data)


def intersectionFinderUsingHashing(a: LinkedList, b: LinkedList):
    dataSet = set()
    temp = a.head
    while temp != None:
        dataSet.add(temp.data)
        temp = temp.next

    temp = b.head
    while temp != None:
        if temp.data in dataSet:
            return temp.data

        temp = temp.next

    return 'No intersection found'
